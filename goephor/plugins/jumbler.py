'''
Created on Feb 29, 2016

@author: sdouglas2
'''
import os
import platform
import re
import sys

from modules.terminal import shell

def jexec(cmd,
              verbose=True,
              strict=True,
              shell_on=True,
              buffer_size=1048576,
              show_cmd=True):
    """ Run Shell commands  [Non Blocking, no Buffer, print live, log it]
    @param cmd: String command
    @param verbose:bool
    @param strict:bool will exit based on code if enabled
    @return:  {command, stdout, code} as dict
    """

    cmd="env JAIL_OP=EXEC jumbler %s" % cmd

    session = shell(cmd,
                    verbose=verbose,
                    strict=strict,
                    shell=shell_on,
                    buffer_size=1048576,
                    show_cmd=show_cmd)
    return session

def jdestroy( verbose=True,
              strict=True,
              shell_on=True,
              buffer_size=1048576,
              show_cmd=True):
    """ Run Shell commands  [Non Blocking, no Buffer, print live, log it]
    @param cmd: String command
    @param verbose:bool
    @param strict:bool will exit based on code if enabled
    @return:  {command, stdout, code} as dict
    """

    cmd="env JAIL_OP=DESTROY jumbler" 

    session = shell(cmd,
                    verbose=verbose,
                    strict=strict,
                    shell=shell_on,
                    buffer_size=1048576,
                    show_cmd=show_cmd)
    return session


