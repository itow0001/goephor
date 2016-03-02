'''
Created on Jan 9, 2016
@author: iitow

* definitions can not be deleted
* definitions can always be added or modified
* definitions must always be generic
* try to group definitions of similar functionality together
* The goal is to always maintain backwards compatibility
'''
import os
import platform
import re
import sys

from modules.terminal import shell, rsync


#####
# System Definitions
##
def md5_file(path, strict=True):
    """ create an md5 file
    @param src: file path
    @param dest: new file path
    @return: shell session dictionary
    @example:{
    "core.actionable":{"md5_file":{"args":["/path/example.txt","/path/example.txt.md5"]}}
    }
    """
    system_type = platform.system().lower()
    if system_type == 'freebsd':
        session = shell("md5 %s > %s.md5" % (path, path), strict=strict, shell=True)
    else:
        session = shell("md5sum %s > %s.md5" % (path, path), strict=strict, shell=True)
    return session


def gzip(src, strict=True):
    """ gzip a file
    @param src: file path
    @param clean: make a previous gzip does not exist on src & dest
    @return: shell session dictionary
    @example: {"core.actionable":{"gzip":{"args":["/path/example.txt"]}}}
    """
    session = shell("file %s" % (src), strict=strict, shell=True)
    if 'gzip' in session.get('stdout'):
        print "[Warning] file is already gzip format skipping gzip"
        return session
    else:
        session = shell("gzip -k %s" % (src), strict=strict, shell=True)
    return session


def symlink(src, dest, strict=True):
    """ Performs a symlink
    @param src: file path
    @param dest: new file path
    @return: shell session dictionary
    @example:{
    "core.actionable":{"symlink":{"args":["/path/example","/path2/example"]}}
    }
    """
    session = shell("ln -s %s %s" % (src, dest), strict=strict, shell=True)
    return session


def mkdir(path, clean=True, strict=True):
    """ make a directory
    @param path: string, system path
    @param clean: remove path if it exists
    @return: shell session dictionary
    """
    if clean:
        remove(path)
    session = shell("mkdir -p %s" % (path), strict=strict, shell=True)
    has_dir(path)
    return session


def remove(path, strict=True):
    """ Removes a directory using rm -rf
    @param path: string, system path
    @return: shell session dictionary
    """
    session = shell("rm -rf %s" % (path), strict=strict, shell=True)
    return session


def copy(src, dest, is_dir=False, strict=True):
    """ copies a file or dir
    @param src: file path
    @param dest: new file path
    @param is_dir: adds a -R option
    @return: shell session dictionary
    """
    if is_dir:
        session = shell("cp -R %s %s" % (src, dest), strict=strict, shell=True)
        has_dir(dest)
    else:
        session = shell("cp %s %s" % (src, dest), strict=strict, shell=True)
        has_file(dest)
    return session


def move(src, dest, strict=True):
    """ Perform a directory or file move
    @param path: string, system path
    @param clean: remove path if it exists
    @return: shell session dictionary
    """
    session = shell("mv %s %s" % (src, dest), strict=strict, shell=True)
    return session


def has_dir(path, negate=False, strict=True):
    """ detect if a directory exists
    @param path: string, system path
    @param negate: boolean, fail on non existence
    @return: shell session dictionary
    """
    if negate:
        session = shell("[ ! -d %s ]" % (path), strict=strict, shell=True)
    else:
        session = shell("[ -d %s ]" % (path), strict=strict, shell=True)
    return session


def has_file(path, negate=False, strict=True):
    """ detect if a file exists
    @param path: string, system path
    @param negate: boolean, fail on non existence
    @return: shell session dictionary
    """
    if negate:
        session = shell("[ ! -f %s ]" % (path), strict=strict, shell=True)
    else:
        session = shell("[ -f %s ]" % (path), strict=strict, shell=True)
    return session


def scm_checkout(src_path,
                 repo_url,
                 branch,
                 clean=True,
                 user="build",
                 passwd="a",
                 strict=True):
    """ performs scm source code checkout support for git & svn
    @param src_path: local path where src will go
    @param repo_url: url associated to repo
    @param branch: branch name
    @param clean: remove previous src from local file system
    @param user: username associated with scm server
    @param passwd: password
    @return: shell session dictionary
    """
    if clean:
        remove("%s/%s" % (src_path, branch))
        mkdir(src_path)
    if "git" in repo_url:
        session = shell("cd %s; git clone %s -b %s" %
                        (src_path, repo_url, branch), strict=strict, shell=True)
    else:
        print "[Error] unable to perform scm checkout"
    return session


def rsyncable(server,
              src,
              dest,
              option='pull',
              remote=True,
              excludes=[],
              rsa_private='/root/.ssh/id_rsa.default',
              user='root',
              verbose=False):
    """ perform a rsync
    @param server: server address or dns name
    @param src: source path
    @param dest: destination path
    @param option: pull,push
    @param remote: boolean, toggles local versus remote syncs
    @param exclude: list of directorys to ignore
    @param rsa_private: path to rsa private key
    @param user: username associated to sync
    @param verbose: prints all available info
    @return: shell session dictionary
    """
    session = rsync(server,
                    src,
                    dest,
                    option=option,
                    remote=remote,
                    excludes=excludes,
                    rsa_private=rsa_private,
                    user=user,
                    verbose=verbose)
    return session


def jexec(jail_name, env, cmd, strict=True, shell_on=True):
    """ Calls Jexec for running commands from within a jail
    @param jail_name: name of jail, or part of name
    @param env: shell environment example. sh, csh,
    @param cmd: string of command to be used
    @return: session
    """
    session = shell("/usr/sbin/jls | grep %s | awk '{print $1}' | tr -d '\n'" % jail_name, strict=True, shell=True)
    JID = session.get("stdout")
    jexec_cmd = 'sudo -E /usr/sbin/jexec %s %s -c "%s"' % (JID, env, cmd)
    session = shell(jexec_cmd, strict=strict, shell=shell_on)
    return session


def jls(key, search, return_type='path', strict=True):
    """ Get jail info and place it into environment variable
    @param search: string to search for
    @param key: environment key to set
    @param return_type: can only be, jid, ip, hostname, path
    @return: value
    """
    session = shell("/usr/sbin/jls", strict=strict, shell=True)
    output = session.get("stdout").split("\n")
    for line in output:
        if search in line:
            jail_line = re.split('\s+', line)
            print jail_line
            if return_type == 'path':
                os.environ[key] = jail_line[4]
                return session
            elif return_type == 'hostname':
                os.environ[key] = jail_line[3]
                return session
            elif return_type == 'ip':
                os.environ[key] = jail_line[2]
                return session
            elif return_type == 'jid':
                os.environ[key] = jail_line[1]
                return session
            else:
                print "[Error] unable to find value %s" % (return_type)
                sys.exit(1)
    env = os.environ.get(key)
    if not env:
        print "[Error] setting environment variable %s" % (key)
    print "environment set %s=%s" % (key, env)
    return session


def mount(opts, src, dest, strict=True):
    """ system mount call
    @param opts: optional variables to add
    @param src: src directory
    @param dest: destination directory
    @return: session
    """
    session = shell("/sbin/mount %s %s %s" % (opts, src, dest), strict=strict, shell=True)
    if not src and dest in session.get('stdout'):
        print "[mount] mounting %s %s" % (src, dest)
        session = shell("/sbin/mount %s %s %s" %
                        (opts, src, dest), strict=strict, shell=True)
    return session


def umount(opts, dest, strict=True):
    """ system un-mount call
    @param opts: optional variables to add
    @param dest: destination directory
    @return: session
    """
    session = shell("/sbin/umount %s %s" % (opts, dest), strict=strict, shell=True)
    if dest in session.get('stdout'):
        print "[umount] unmounting %s %s" % (dest)
        session = shell("/sbin/umount %s %s" %
                        (opts, dest), strict=strict, shell=True)
    return session


def shell_cmd(cmd,
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
    session = shell(cmd,
                    verbose=verbose,
                    strict=strict,
                    shell=shell_on,
                    buffer_size=1048576,
                    show_cmd=show_cmd)
    return session
