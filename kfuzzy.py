#!/usr/bin/env python

"""
Fuzzy hashing algorithms
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
import base64

from itertools import imap

try:
    import psyco
    psyco.full()
except ImportError:
    pass

class CKoretFuzzyHashing:
    """ Generate partial hashes of files or bytes """
    bsize = 512
    output_size = 32
    ignore_range = 2
    algorithm = None
    reduce_errors = True

    def edit_distance(self, sign1, sign2):
        if sign1 == sign2:
            return 0
        
        m = max(len(sign1), len(sign2))
        distance = 0
        
        for c in xrange(0, m):
            if sign1[c:c+1] != sign2[c:c+1]:
                distance += 1
        
        return distance

    def simplified(self, bytes, aggresive = False):
        output_size = self.output_size
        ignore_range = self.ignore_range
        bsize = self.bsize
        total_size = len(bytes)
        size = (total_size/bsize) / output_size
        buf = []
        reduce_errors = self.reduce_errors
        # Adjust the output to the desired output size
        for c in xrange(0, output_size):
            tmp = bytes[c*size:(c*size+1)+bsize]
            ret = sum(imap(ord, tmp)) % 255
            if reduce_errors:
                if ret != 255 and ret != 0:
                    buf.append(chr(ret))
            else:
                buf.append(chr(ret))
        
        buf = "".join(buf)
        return base64.b64encode(buf).strip("=")[:output_size]

    def _hash(self, bytes, aggresive = False):
        idx = 0
        ret = []
        
        output_size = self.output_size
        ignore_range = self.ignore_range
        bsize = self.bsize
        total_size = len(bytes)
        rappend = ret.append
        chunk_size = idx*bsize
        reduce_errors = self.reduce_errors
        # Calculate the sum of every block
        while 1:
            chunk_size = idx*bsize
            buf = bytes[chunk_size:chunk_size+bsize]
            char = sum(imap(ord, buf)) % 255
            
            if reduce_errors:
                if char != 255 and char != 0:
                    rappend(chr(char))
            else:
                rappend(chr(char))
            
            idx += 1
            
            if chunk_size+bsize > total_size:
                break
        
        ret = "".join(ret)
        size = len(ret) / output_size
        buf = []
        
        # Adjust the output to the desired output size
        for c in xrange(0, output_size):
            if aggresive:
                buf.append(ret[c:c+size+1][ignore_range:ignore_range+1])
            else:
                buf.append(ret[c:c+size+1][1:2])
            
            i = 0
            for x in ret[c:c+size+1]:
                i += 1
                if i != ignore_range:
                    continue
                i = 0
                buf += x
                break
            
        ret = "".join(buf)
        
        return base64.b64encode(ret).strip("=")[:output_size]

    def _fast_hash(self, bytes, aggresive = False):
        i = -1
        ret = set()
        
        output_size = self.output_size
        size = len(bytes) *1.00 / output_size
        bsize = self.bsize
        radd = ret.add
        
        while i < output_size:
            i += 1
            buf = bytes[i*bsize:(i+1)*bsize]
            char = sum(imap(ord, buf)) % 255
            if self.reduce_errors:
                if char != 255 and char != 0:
                    radd(chr(char))
            else:
                radd(chr(char))
        
        ret = "".join(ret)
        return base64.b64encode(ret).strip("=")[:output_size]

    def _experimental_hash(self, bytes, aggresive = False):
        idx = 0
        ret = []
        bsize = self.bsize
        output_size = self.output_size
        size = len(bytes)
        ignore_range = self.ignore_range
        chunk_size = idx*self.bsize
        byte = None
        
        while size > chunk_size + (bsize/output_size):
            chunk_size = idx*self.bsize
            if byte is None:
                val = bsize
            elif ord(byte) > 0:
                val = ord(byte)
            else:
                val = output_size
            
            buf = bytes[chunk_size:chunk_size+val]
            byte = chr(sum(imap(ord, buf)) % 255)
            ret.append(byte)
            idx += 1
        
        ret = "".join(ret)
        buf = ""
        size = len(ret)/output_size
        for n in xrange(0, output_size):
            buf += ret[n*size:(n*size)+1]
        
        return base64.b64encode(buf).strip("=")[:output_size]

    def mix_blocks(self, bytes):
        idx = 0
        buf = bytes
        fub = buf[::1]
        ret = ""
        size1 = 0
        size2 = 0
        total_size = len(bytes)
        
        while 1:
            size1 = idx*self.bsize
            size2 = (idx+1)*self.bsize
            
            tmp = buf[size1:size2]
            pmt = fub[size1:size2]
            ret += tmp
            ret += pmt
            
            idx += 1
            
            if len(tmp) < self.bsize:
                break
        
        return ret

    def hash_bytes(self, bytes, aggresive = False):
        mix = self.mix_blocks(bytes)
        if self.algorithm is None:
            func = self._hash
        else:
            func = self.algorithm
        
        hash1 = func(mix, aggresive)
        hash2 = func(bytes, aggresive)
        hash3 = func(bytes[::-1], aggresive)
        
        return hash1 + ";" + hash2 + ";" + hash3

    def hash_file(self, filename, aggresive = False):
        buf = file(filename, "rb").read()
        return self.hash_bytes(buf, aggresive)

def usage():
    print "Usage:", sys.argv[0], "<filename>"

def main(path):
    hash = CKoretFuzzyHashing()
    #hash.algorithm = hash._fast_hash
    
    if os.path.isdir(path):
        print "Signature;Simple Signature;Reverse Signature;Filename"
        for root, dirs, files in os.walk(path):
            for name in files:
                tmp = os.path.join(root, name)
                try:
                    ret = hash.hash_file(tmp, True)
                    print "%s;%s" % (ret, tmp)
                except:
                    print "***ERROR with file %s" % tmp
                    print sys.exc_info()[1]
    else:
        hash = CKoretFuzzyHashing()
        ret = hash.hash_file(path, True)
        print "%s;%s" % (path, ret)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        main(sys.argv[1])
