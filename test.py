#!/usr/bin/python
# -*- Mode: Python; py-indent-offset: 4 -*-

import unittest
from kfuzzy import CKoretFuzzyHashing

class TestKFuzzy(unittest.TestCase):

    kfd = None
    buf = ""

    def setUp(self):
        self.kfd = CKoretFuzzyHashing()
        buf = ""
        for c in xrange(0, 255):
            buf += chr(c)*512
        self.buf = buf

    def testDHA(self):
        """ Default hashing algorithm (DHA) """
        key = "AgL7+wQE+fkGBvf3CAj19QoK8/MMDPHx;BAQGBggICgoMDA4OEBASEhQUFhYYGBoa;+/v5+ff39fXz8/Hx7+/t7evr6enn5+Xl"
        hash = self.kfd.hash_bytes(self.buf)
        self.assert_(key == hash)

    def testFHA(self):
        key = "AgQGCAoMDhASFBYYGhweIN/h4+Xn6evt;AgQGCAoMDhASFBYYGhweICIkJigqLC4w;vb/Bw8XHycvNz9HT1dfZ293f4ePl5+nr"
        self.kfd.algorithm = self.kfd._fast_hash
        hash = self.kfd.hash_bytes(self.buf)
        self.assert_(key == hash)

    def testSimplified(self):
        key = "/v4DA/39Bgb8/AkJ+/sMDPr6Dw/5+RIS;AYB//n/+fv1+/X38ffx8+3z7e/p7+nr5;+3z8ff19/X7+fv5/f4ABgAGBAoECggOC"
        buf = self.buf * 16
        self.kfd.algorithm = self.kfd.simplified
        hash = self.kfd.hash_bytes(buf)
        self.assert_(key == hash)

    def testOutputSize(self):
        self.kfd.algorithm = None
        l = len(self.kfd.hash_bytes(self.buf))
        size = self.kfd.output_size * 3
        size += 2
        self.assertEqual(l, size)

    def testNullBlocks(self):
        buf  = "\x00"*8192
        buf += self.buf
        self.kfd.algorithm = None
        self.kfd.reduce_errors = True
        h = self.kfd.hash_bytes(buf)
        self.failUnless(h.find("AA") == -1)

    def testSimplified(self):
        self.kfd.algorithm = self.kfd.simplified
        h = self.kfd.hash_bytes(self.buf + self.buf)
        self.kfd.algorithm = self.kfd._fast_hash
        h2 = self.kfd.hash_bytes(self.buf + self.buf)
        self.failUnless(((self.kfd.output_size*3)+2) - self.kfd.edit_distance(h, h2) < 16)

if __name__ == '__main__':
    unittest.main()
