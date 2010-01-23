#!/usr/bin/env python

"""
This file is part of DeepToad
Copyright (C) 2009, Joxean Koret

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""

import os
import sys

from kfuzzy import CKoretFuzzyHashing

MAX_EDIT_DISTANCE = 16
PROGRAM = "DeepToad"
VERSION = "1.0"

class CDeepToad:
    groups = {}
    ingroups = {}
    kfd = None
    extensions = []
    ignore_extensions = []
    edit_distance = MAX_EDIT_DISTANCE
    maximum = 0
    aggresive = True
    just_print = False
    just_compare = False

    def __init__(self):
        self.kfd = CKoretFuzzyHashing()
        self.kfd.bsize = 512
        self.kfd.output_size = 32
        self.kfd.ignore_range = 2
        self.kfd.big_file_size = 1024*1024*32

    def cluster(self, hashes, filename):
        if self.just_print or self.just_compare:
            self.groups[filename] = hashes
            return
        
        for hash in hashes:
            hashed = False
            for key in self.groups:
                # Check for maximum edit distance
                if self.kfd.edit_distance(key, hash) <= self.edit_distance:
                    self.groups[key].append(filename)
                    hashed = True
                    break
            
            if hashed:
                continue
            
            if not self.groups.has_key(hash):
                self.groups[hash] = []
            
            self.groups[hash].append(filename)

    def hashFile(self, filename):
        try:
            s1, s2, s3 = self.kfd.hash_file(filename, self.aggresive).split(";")
            if self.just_print:
                print "%s;%s;%s;%s" % (s1, s2, s3, filename)
            else:
                self.cluster((s1, s2, s3), filename)
        except KeyboardInterrupt:
            raise
        except:
            sys.stderr.write(" -> %s\n" % str(sys.exc_info()[1]))
            sys.stderr.flush()
            raise

    def printReportHeader(self):
        print "Signature;Simple Signature;Reverse Signature;Filename"
    
    def clusterDirectory(self, path, output_dir):
        last_size = 0
        total = 0
        if self.just_print:
            self.printReportHeader()
        
        for root, dirs, files in os.walk(path):
            for name in files:
                if self.maximum != 0 and total >= self.maximum:
                    break
                total += 1
                
                basename, extension = os.path.splitext(name)
                if extension in self.ignore_extensions:
                    continue
                elif len(self.extensions) != 0:
                    if extension not in self.extensions:
                        continue
                
                if not self.just_print:
                    sys.stderr.write("\b"*last_size + " "*last_size + "\b"*last_size)
                    sys.stderr.flush()
                    sys.stderr.write("Processing file %s ..." % os.path.join(root, name))
                    last_size = len("Processing file %s ..." % os.path.join(root, name))
                    sys.stderr.flush()
                
                self.hashFile(os.path.join(root, name))
            
            if self.maximum != 0 and total >= self.maximum:
                break
        
        if total > 0:
            sys.stderr.write("\n")
            sys.stderr.flush()

    def sortByCount(self):
        # First, sort by count of elements
        newGrp = {}
        for x in self.groups:
            if x == "":
                continue
            
            newGrp[x] = len(self.groups[x])
        
        # Now sort the dict by values
        outgrp = {}
        alist = sorted(newGrp.iteritems(), key=lambda (k,v): (v,k), reverse=True)
        dones = []
        
        # Create the new dict with only non empty groups
        for x in alist:
            val = x[0]
            outgrp[val] = []
            for element in self.groups[val]:
                if element not in dones:
                    outgrp[val].append(element)
                    dones.append(element)
            
            if len(outgrp[val]) == 0:
                del outgrp[val]
        
        return outgrp

    def printHashes(self):
        self.printReportHeader()
        for x in self.groups:
            hashes = self.groups[x]
            print "%s;%s;%s;%s" % (hashes[0], hashes[1], hashes[2], x)

    def compareAndReportHashes(self, x, y, hashesx, hashesy, dones):
        finished = False
        
        for hx in hashesx:
            if hx == "":
                continue
            elif finished:
                break
            
            #if hx not in hashesy:
            #    continue
            
            for hy in hashesy:
                if hy == "":
                    continue
                
                dis = self.kfd.edit_distance(hx, hy)
                dis = len(hx) - dis
                percent = dis*100.00/len(hx)
                
                if percent > 33:
                    print "File '%s' matches '%s' (%0.2f%%)" % (x, y, percent)
                    dones[y] = x
                    finished = True
                    break
        
        return dones

    def compareHashes(self):
        dones = {}
        
        for x in self.groups:
            for y in self.groups:
                if x == y:
                    continue
                elif dones.has_key(x):
                    if dones[x] == y:
                        #print "Ignored"
                        continue
                
                hashesx = self.groups[x]
                hashesy = self.groups[y]
                
                dones = self.compareAndReportHashes(x, y, hashesx, hashesy, dones)

    def printReport(self):
        if self.just_print:
            #self.printHashes()
            return
        
        if self.just_compare:
            self.compareHashes()
            return
        
        grp = self.sortByCount()
        already = []
        for x in grp:
            for element in self.groups[x]:
                if element not in already:
                    print "%s;%s" % (x, element)
                    already.append(element)

def main(args):
    output_dir = None
    kfdCluster = CDeepToad()

    for arg in args:
        if os.path.exists(arg):
            if os.path.isdir(arg):
                try:
                    kfdCluster.groups = {}
                    kfdCluster.clusterDirectory(arg, output_dir)
                except KeyboardInterrupt:
                    print "Aborted..."
                
                kfdCluster.printReport()
            else:
                try:
                    ret = kfdCluster.kfd.hash_file(arg)
                    print "%s;%s" % (ret, arg)
                except KeyboardInterrupt:
                    print "Aborted..."
        elif arg.startswith("-o"):
            output_dir = arg[3:]
        elif arg.startswith("-e="):
            extensions = arg[3:].split(",")
            kfdCluster.ignore_extensions = extensions
        elif arg.startswith("-i="):
            extensions = arg[3:].split(",")
            kfdCluster.extensions = extensions
        elif arg.startswith("-m="):
            value = int(arg[3:])
            kfdCluster.maximum = value
        elif arg.startswith("-d="):
            value = int(arg[3:])
            kfdCluster.edit_distance = value
        elif arg.startswith("-b="):
            value = int(arg[3:])
            kfdCluster.kfd.bsize = value
        elif arg.startswith("-r="):
            value = int(arg[3:])
            kfdCluster.kfd.ignore_range = value
        elif arg.startswith("-s="):
            value = int(arg[3:])
            kfdCluster.kfd.output_size = value
        elif arg == "-c":
            kfdCluster.just_compare = True
        elif arg == "-f":
            kfdCluster.kfd.algorithm = kfdCluster.kfd._fast_hash
        elif arg == "-x":
            kfdCluster.kfd.algorithm = kfdCluster.kfd._experimental_hash
        elif arg == "-na":
            kfdCluster.aggresive = False
        elif arg == "-ag":
            kfdCluster.aggresive = True
        elif arg == "-nb":
            kfdCluster.kfd.reduce_errors = True
        elif arg == "-cb":
            kfdCluster.kfd.reduce_errors = False
        elif arg == "-simple":
            kfdCluster.kfd.algorithm = kfdCluster.kfd.simplified
        elif arg == "-p":
            kfdCluster.just_print = True
        elif arg == "-ida":
            kfdCluster.ignore_extensions = [".idb", ".id0", ".id1", ".til", ".nam"]
        elif arg == "-spam":
            kfdCluster.kfd.remove_spaces = True
        elif arg == "-dspam":
            kfdCluster.kfd.remove_spaces = True
        elif arg.startswith("-echo"):
            print arg[6:]
            print "="*len(arg[6:])
        else:
            sys.stderr.write("Unknown argument '%s' ignored\n" % arg)

def usage():
    print "%s v%s, Copyright (c) 2009, 2010 Joxean Koret <admin@joxeankoret.com>" % (PROGRAM, VERSION)
    print "Usage:", sys.argv[0], "[parameters] <directory>"
    print
    print "Common parameters:"
    print "   -o=<directory>    Not yet implemented"
    print "   -e=<extensions>   Exclude extensions (separated by comma)"
    print "   -i=<extensions>   Clusterize only specified extensions (separated by comma)"
    print "   -m=<value>        Clusterize a maximum of <value> file(s)"
    print "   -d=<distance>     Specify the maximum edit distance (by default, 16 or 33%)"
    print "   -ida              Ignore files created by IDA"
    print "   -spam             Enable spam mode (remove space characters)"
    print "   -dspam            Disable spam mode"
    print "   -p                Just print the generated hashes"
    print "   -c                Compare the files"
    print "   -echo=<msg>       Print a message (usefull to generate reports)"
    print
    print "Advanced parameters:"
    print "   -b=<block size>   Specify the block size (by default, 512)"
    print "   -r=<ignore range> Specify the range of bytes to be ignored (by default, 2)"
    print "   -s=<output size>  Specify the signature's size (by default, 32)"
    print "   -f                Use faster (but weaker) algorithm"
    print "   -x                Use eXperimental algorithm"
    print "   -simple           Use the simplified algorithm"
    print "   -na               Use non aggresive method (only applicable to default algorithm)"
    print "   -ag               Use aggresive method (default)"
    print "   -nb               Ignore null blocks (default)"
    print "   -cb               Consider null blocks"
    print
    print "Example:"
    print
    print "Analyze a maximum of 25 files excluding zip and rar files:"
    print "%s -e=.zip,.rar -m=25 /home/luser/samples" % sys.argv[0]
    print

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        sys.exit(main(sys.argv[1:]))

