'''
Created on May 4, 2016
:author: iitow
:note: All integration tests go here.
'''
from goephor.core.plugins.modules.terminal import shell
import inspect
import sys
import argparse
import platform


def menu():
    '''
    argparse menu here
    '''
    parser = argparse.ArgumentParser(
        description='Testing of goephor')
    parser.add_argument('-E',
                        action="store",
                        dest="envs",
                        default="",
                        help='Add env vars delimiter:"," '
                        'example.'
                        ' "BASE_PATH=/tmp,WORKPATH=/${BASE_PATH}/addon"')
    parser.add_argument('--version',
                        action='version',
                        version='goephor-test')
    return parser.parse_args()


def test_condition(options):
    '''
    test of core/plugins/condition.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    output = shell("python -u goephor.py -f "
                   "./examples/ex_condition.yaml -e -E %s" % options.envs).get('stdout')
    if '(THEN 1)' not in output:
        return {funct: False}
    output = shell("python -u goephor.py -f "
                   "./examples/ex_condition.yaml -e "
                   "-E 'var1=1'").get('stdout')
    if '(IF NEST 1)' not in output:
        return {funct: False}
    return {funct: True}


def test_defaults(options):
    '''
    test of core/plugins/pluginable.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    output = shell("python -u goephor.py -f "
                   "./examples/ex_defaults.yaml -e -E %s" % options.envs).get('stdout')
    if '(PASS)' not in output:
        return {funct: False}
    output = shell("python -u goephor.py -f "
                   "./examples/ex_defaults.yaml -e "
                   "-E 'SWITCH=1'").get('stdout')
    if '(PASS)' not in output:
        return {funct: False}
    return {funct: True}


def test_environment(options):
    '''
    test of core/plugins/environment.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    output = shell("python -u goephor.py -f "
                   "./examples/ex_environment.yaml -e -E %s" % options.envs).get('stdout')
    if '(FAIL)' in output:
        return {funct: False}
    return {funct: True}


def test_freebsd(options):
    '''
    test of core/plugins/freebsd.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    if platform.system() == 'FreeBSD':
        session = shell("python -u goephor.py -f ./examples/ex_freebsd.yaml -e -E %s" % options.envs)
        if not session.get('code') == 0:
            return {funct: False}
    return {funct: True}


def test_http(options):
    '''
    test of core/plugins/http.py
    '''
    funct = inspect.stack()[0][3]
    print "\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_http.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_receipt(options):
    '''
    test of core/plugins/receipt.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_receipt.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_remote(options):
    '''
    test of core/plugins/remote.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_remote.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_scm(options):
    '''
    test of core/plugins/scm.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_scm.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_system(options):
    '''
    test of core/plugins/system.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_system.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}


def test_release(options):
    '''
    test of core/plugins/release.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_release.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}

def test_string(options):
    '''
    test of core/plugins/string.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_string.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}

def test_on_exit(options):
    '''
    test of core/Chain.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    session = shell("python -u goephor.py -f ./examples/ex_on_exit.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}

def test_include(options):
    '''
    test of core/plugins/system.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    sys.stdout.flush()
    session = shell("python -u goephor.py -f ./examples/ex_include.yaml -e -E %s" % options.envs)
    if not session.get('code') == 0:
        return {funct: False}
    return {funct: True}

def test_fail(options):
    '''
    test of core/plugins/system.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    sys.stdout.flush()
    session = shell("python -u goephor.py -f ./examples/ex_fail.yaml -e -E %s" % options.envs)
    if not session.get('code') > 0:
        return {funct: False}
    return {funct: True}

def test_handler(options):
    '''
    test of core/plugins/system.py
    '''
    funct = inspect.stack()[0][3]
    print "\n\n[%s]\n" % (funct)
    sys.stdout.flush()
    session = shell("python -u goephor.py -f ./examples/ex_handler.yaml -e -E %s" % options.envs)
    if session.get('code') > 0:
        return {funct: False}
    return {funct: True}

def tests(options):
    '''
    calls all the tests here & collects results
    '''
    tests = []
    tests.append(test_condition(options))
    tests.append(test_defaults(options))
    tests.append(test_environment(options))
    tests.append(test_freebsd(options))
    tests.append(test_http(options))
    tests.append(test_receipt(options))
    tests.append(test_remote(options))
    tests.append(test_scm(options))
    tests.append(test_system(options))
    tests.append(test_string(options))
    tests.append(test_on_exit(options))
    tests.append(test_fail(options))
    tests.append(test_include(options))
    tests.append(test_handler(options))
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
    options = menu()
    tests(options)
