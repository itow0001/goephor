'''
Created on May 4, 2016

@author: iitow
'''
from goephor.core.plugins.modules.terminal import shell

import inspect
import sys


def test_condition():
    funct = inspect.stack()[0][3]
    print "\n[%s]\n" % (funct)
    output = shell("python goephor.py -f ./examples/ex_condition.yaml -e").get('stdout')
    if not '(THEN 1)' in output:
        return {funct:False}
    output = shell("python goephor.py -f ./examples/ex_condition.yaml -e -E 'var1=1'").get('stdout')
    if not '(IF NEST 1)' in output:
        return {funct:False}
    return {funct:True}
        

def test_defaults():
    funct = inspect.stack()[0][3]
    print "\n[%s]\n" % (funct)
    output = shell("python goephor.py -f ./examples/ex_defaults.yaml -e").get('stdout')
    if not '(PASS)' in output:
        return {funct:False}
    output = shell("python goephor.py -f ./examples/ex_defaults.yaml -e -E 'SWITCH=1'").get('stdout')
    if not '(PASS)' in output:
        return {funct:False}
    return {funct:True}


def test_environment():
    funct = inspect.stack()[0][3]
    print "\n[%s]\n" % (funct)
    output = shell("python goephor.py -f ./examples/ex_environment.yaml -e").get('stdout')
    if '(FAIL)' in output:
        return {funct:False}
    return {funct:True}


def test_freebsd():
    funct = inspect.stack()[0][3]
    print "\n[%s]\n" % (funct)
    session = shell("python goephor.py -f ./examples/ex_freebsd.yaml -e")
    if not session.get('code') == 0:
        return {funct:False} 
    return {funct:True}
    

def test_http():
    funct = inspect.stack()[0][3]
    print "\n[%s]\n" % (funct)
    session = shell("python goephor.py -f ./examples/ex_http.yaml -e")
    if not session.get('code') == 0:
        return {funct:False} 
    return {funct:True}

def test_receipt():
    funct = inspect.stack()[0][3]
    print "\n[%s]\n" % (funct)
    session = shell("python goephor.py -f ./examples/ex_receipt.yaml -e")
    if not session.get('code') == 0:
        return {funct:False} 
    return {funct:True}

def test_scm():
    pass

def test_system():
    pass

def tests():
    tests = []
    tests.append(test_condition())
    tests.append(test_defaults())
    tests.append(test_environment())
    tests.append(test_freebsd())
    tests.append(test_http())
    tests.append(test_receipt())
    #tests.append(test_scm())
    #tests.append(test_system())
    
    print "\n\n[Test Results]:"
    for test in tests:
        key = test.keys()[0]
        value = test.get(test.keys()[0])
        print "%s : %s" % (key.rjust(20),value)
    print ""
    for test in tests:
        key = test.keys()[0]
        value = test.get(test.keys()[0])
        if not value:
            print "[Failure] %s : %s" % (key,value)
            sys.exit(1)
            


if __name__ == '__main__':
    tests()