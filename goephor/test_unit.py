'''
Created on Feb 17, 2016

@author: iitow
'''
import os
import platform
import shutil
import sys
import unittest

from core import actionable


class TestActionable(unittest.TestCase):
    def setUp(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_file = '%s/test.txt' % (test_dir)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
            open(test_file, 'w').close() 
        
    def tearDown(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        dest = '%s/tmp_actionable' % (this_dir)
        shutil.rmtree(dest)

    def test_md5_file(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_file = "%s/test.txt" % (test_dir)
        test_md5 = "%s/test.txt.md5" % (test_dir)
        output = actionable.md5_file(test_file)
        self.assertEqual(output.get('code'),0)
        self.assertTrue(os.path.exists(test_md5))
        
    def test_gzip(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_file = "%s/test.txt" % (test_dir)
        test_gzip = "%s/test.txt.gz" % (test_dir)
        output = actionable.gzip(test_file)
        self.assertEqual(output.get('code'),0)
        self.assertTrue(os.path.exists(test_gzip))
    
    def test_symlink(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_file = "%s/test.txt" % (test_dir)
        test_ln = "%s/test_ln" % (test_dir)
        output = actionable.symlink(test_file,test_ln)
        self.assertEqual(output.get('code'),0)
        self.assertTrue(os.path.exists(test_ln))
        
    def test_mkdir(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_mkdir = "%s/test2" % (test_dir)
        output = actionable.mkdir(test_mkdir)
        self.assertEqual(output.get('code'),0)
        self.assertTrue(os.path.exists(test_mkdir))

    def test_remove(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_mkdir = "%s/test2" % (test_dir)
        os.mkdir(test_mkdir)
        output = actionable.remove(test_mkdir)
        self.assertEqual(output.get('code'),0)
        self.assertFalse(os.path.exists(test_mkdir))

    def test_copy(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_file = "%s/test.txt" % (test_dir)
        test_copy = "%s/test_copy.txt" % (test_dir)
        output = actionable.copy(test_file,test_copy)
        self.assertEqual(output.get('code'),0)
        self.assertTrue(os.path.exists(test_copy))
        
    def test_move(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_file = "%s/test.txt" % (test_dir)
        test_mv = "%s/test_mv.txt" % (test_dir)
        output = actionable.copy(test_file,test_mv)
        self.assertEqual(output.get('code'),0)
        self.assertTrue(os.path.exists(test_mv))
    
    def test_has_dir(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        output = actionable.has_dir(test_dir)
        self.assertEqual(output.get('code'),0)
        self.assertTrue(os.path.exists(test_dir))

    def test_has_file(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '%s/tmp_actionable' % (this_dir)
        test_file = "%s/test.txt" % (test_dir)
        output = actionable.has_file(test_file)
        self.assertEqual(output.get('code'),0)
        self.assertTrue(os.path.exists(test_file))
    
    def test_shell_cmd(self):
        output = actionable.shell_cmd("ls")
        print output
        #self.assertEqual(output.get('code'),0)


if __name__ == "__main__":
    unittest.main()