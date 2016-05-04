'''
Created on May 4, 2016

@author: iitow
'''
from goephor.core.plugins.modules import terminal

import inspect

def test_condition():
    funct = inspect.stack()[0][3]
    output = shell("python goephor.py -f ./examples/condition.yaml -e").get('stdout')
    if not '(THEN 1)' in output:
        return {funct:False}
    return {funct:True}
        

def test_defaults():
    pass

def test_environment():
    pass

def test_example():
    pass

def test_freebsd():
    pass

def test_http():
    pass

def test_receipt():
    pass

def test_scm():
    pass

def test_system():
    pass

def tests():
    tests = []
    tests.append(test_condition())
    
    print "\n\nTest Results:"
    for test in tests:
        print "%s : %s" % (test.keys()[0],test.get(test.keys()[0]))


if __name__ == '__main__':
    pass