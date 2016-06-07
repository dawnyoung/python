# -*- coding: utf-8 -*-


###############################################################################
#   unit test
###############################################################################
        
# unit test
import unittest

from mydict import Dict

class TestDict(unittest.TestCase): # base class: unittest.TestCase
    def test_init(self): # test starts with test
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            
    def setUp(self): # excute before each unit
        print('before excuting the unit')
    def tearDown(self): # excute after each unit
        print('after excuting the unit')
    # For example, we can use setUp to open a database, and use tearDown to close
    # a database. The setUp and tearDown will be excuted before or after each unit.
    # It makes it unnecessary to write the open and close code in each unit.

if __name__ == '__main__':
    unittest.main()