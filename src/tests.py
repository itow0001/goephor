'''
Created on May 4, 2016
:author: iitow
:note: All integration tests go here.
'''
from goephor.core.plugins.modules.terminal import shell
import inspect
import sys


def test_condition():
    '''
    test of core/plugins/condition.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    output = shell("python -u goephor.py -f "
                   "./examples/ex_condition.yaml -e").get('stdout')
    if '(THEN 1)' not in output:
        return {funct: False}
    output = shell("python -u goephor.py -f "
                   "./examples/ex_condition.yaml -e "
                   "-E 'var1=1'").get('stdout')
    if '(IF NEST 1)' not in output:
        return {funct: False}
    return {funct: True}


def test_defaults():
    '''
    test of core/plugins/pluginable.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    output = shell("python -u goephor.py -f "
                   "./examples/ex_defaults.yaml -e").get('stdout')
    if '(PASS)' not in output:
        return {funct: False}
    output = shell("python -u goephor.py -f "
                   "./examples/ex_defaults.yaml -e "
                   "-E 'SWITCH=1'").get('stdout')
    if '(PASS)' not in output:
        return {funct: False}
    return {funct: True}


def test_environment():
    '''
    test of core/plugins/environment.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    output = shell("python -u goephor.py -f "
                   "./examples/ex_environment.yaml -e").get('stdout')
    if '(FAIL)' in output:
        return {funct: False}
    return {funct: True}


def test_freebsd():
    '''
    test of core/plugins/freebsd.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_freebsd.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_http():
    '''
    test of core/plugins/http.py
    '''
    funct = inspect.stack()[0][3]
    print "\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_http.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_receipt():
    '''
    test of core/plugins/receipt.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_receipt.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_remote():
    '''
    test of core/plugins/remote.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_remote.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_scm():
    '''
    test of core/plugins/scm.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_scm.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_system():
    '''
    test of core/plugins/system.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_system.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_release():
    '''
    test of core/plugins/release.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_release.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}

def test_string():
    '''
    test of core/plugins/string.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_string.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}

def test_on_exit():
    '''
    test of core/Chain.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_on_exit.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}

def test_include():
    '''
    test of core/plugins/system.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    sys.stdout.flush()
    session = shell("python -u goephor.py -f ./examples/ex_include.yaml -e")
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def tests():
    '''
    calls all the tests here & collects results
    '''
    tests = []
    tests.append(test_condition())
    tests.append(test_defaults())
    tests.append(test_environment())
    tests.append(test_freebsd())
    tests.append(test_http())
    tests.append(test_receipt())
    tests.append(test_remote())
    tests.append(test_scm())
    tests.append(test_system())
    tests.append(test_release())
    tests.append(test_string())
    tests.append(test_on_exit())
    tests.append(test_include())
    print "\n\n[Test Results]:"
    for test in tests:
        key = test.keys()[0]
        value = test.get(test.keys()[0])
        print "%s : %s" % (key.rjust(20), value)
    print ""
    for test in tests:
        key = test.keys()[0]
        value = test.get(test.keys()[0])
        if not value:
            print "[Failure] %s : %s" % (key, value)
            sys.exit(1)


if __name__ == '__main__':
    tests()
