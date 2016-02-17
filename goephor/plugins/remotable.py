'''
Created on Jan 29, 2016

@author: iitow
'''
import os
import re
import sys

sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "../modules"))
from remote import Run


def _has_keys(str):
    """ Collect all environment variables
    @param str: command string
    """
    matches = re.findall(r'(?<={)[^}]*', str)
    return matches


def _sanitize(str):
    """ Replace all environment variables into command
    @param str: command string
    """
    for match in _has_keys(str):
        old = '${%s}' % match
        new = os.environ.get(match)
        if new:
            str = str.replace(old, new)
    return str


def cmd(server,
        cmd_str,
        rsa_private='/root/.ssh/id_rsa.default',
        user='root',
        password='a',
        strict=True,
        verbose=True,
        show_cmd=True):
    """ Initializes a Remote ssh session
    @param server: server address
    @param cmd: string shell command
    @param rsa_private: path to the private key file
    @param user: Username used to log into system
    @param password: Password used to log into system
    @param strict: boolean fail on error
    @param verbose: print out all debug messaging
    @param show_cmd: show the command given to remote server
    @return: session info
    @note: environment variables but be as follows ${var} to pass over to ssh
    """
    if '$' in server:
        server = server.replace('$', '')
        server = os.environ.get(server)
    santized_str = _sanitize(cmd_str)
    remote = Run(server,
                 rsa_private=rsa_private,
                 user=user,
                 password=password,
                 strict=strict,
                 verbose=verbose,
                 show_cmd=show_cmd)
    session = remote.cmd(santized_str)
    return session
