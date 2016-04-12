'''
Created on Jan 9, 2016
@author: iitow

* definitions can not be deleted
* definitions can always be added or modified
* definitions must always be generic
* try to group definitions of similar functionality together
* The goal is to always maintain backwards compatibility
'''
import json
import os
import platform
import random
import re
import sys
import tempfile

from modules.terminal import shell, rsync


def create_flash(key, mnt, disk_size, disk_file='/tmp', strict=True, noop=False):
    """ Create a flash disk for internal onefs reimaging installer
    @param key: environment variable name  
    @param disk_file: Path to disk file
    @param disk_size: size you wish to apply to disk as bytes
    """
    if noop:
        print "[noop] destroy_memdisks"
        return
    mnt = _sanitize(mnt)
    print "mnt:%s" % (mnt)
    disk_size_small = int(disk_size)
    disk_size_small = str(disk_size_small)
    ### if disk file does not exist create it
    disk_file = "%s/%s.disk" % (disk_file,random.randint(1111,9999))
    #if os.path.exists(disk_file):
    #    # unlink it if it does exist
    #    os.unlink(disk_file)
    # Zero things out in the file
    shell("dd if=/dev/zero of=%s bs=1M count=%s" % (disk_file,disk_size_small))
    # Create the new device
    md = shell("mdconfig -a -t vnode -f %s -s %sm" % (disk_file,disk_size_small)).get('stdout')
    md = md[:-1]
    mainpart = "%sa" % md
    print "MAINPART: %s" % (mainpart)
    print "      MD: %s" % (md)
    # add our own label
    disklabel="""
#        size   offset    fstype   [fsize bsize bps/cpg]
  a:   %s        0    4.2BSD        0     0     0
  c:   %s        0    unused        0     0         # "raw" part, don't edit
""" % (disk_size_small,disk_size_small)
    labelfd,labelfilepath = tempfile.mkstemp()
    print labelfd
    print labelfilepath
    print disklabel
    os.write(labelfd,disklabel)
    os.close(labelfd)
    # Partition the device
    shell("disklabel -B -w -r /dev/%s auto" % md,shell=True)
    # Apply our custom label for a disk with complete a partition
    shell("cat %s | disklabel -B -R /dev/%s /dev/fd/0" % (labelfilepath, md),shell=True)
    # Format partition
    shell("newfs -O1 /dev/%s" % mainpart,shell=True)
    os.unlink(labelfilepath)
    if not os.path.exists(mnt):
        os.mkdir(mnt)
    mount('', '/dev/%s' % (mainpart),mnt)
    os.environ[key] = mnt
    env = os.environ.get(key)
    if not env:
        print "[Error] setting environment variable %s" % (key)
    print "environment set %s=%s" % (key, env)

def destroy_memdisks(strict=False, noop=False):
    """ Destroy all memory disks
    """
    if noop:
        print "[noop] destroy_memdisks"
        return
    stdout = shell("mdconfig -l",strict=strict).get('stdout')
    mds = stdout.split(' ')
    for md in mds:
        if md:
            shell('mdconfig -d -u %s' % (md),strict=strict)
   

def md5_file(path, strict=True, noop=False):
    """ create an md5 file
    @param src: file path
    @param dest: new file path
    @param noop: pass on running the command
    
    @return: shell session dictionary
    @example:{
    "core.actionable":{"md5_file":{"args":["/path/example.txt","/path/example.txt.md5"]}}
    }
    """
    if noop:
        print "[noop] md5_file"
        return
    system_type = platform.system().lower()
    if system_type == 'freebsd':
        session = shell("md5 %s > %s.md5" % (path, path), strict=strict, shell=True)
    else:
        session = shell("md5sum %s > %s.md5" % (path, path), strict=strict, shell=True)
    return session


def gzip(src, strict=True, noop=False):
    """ gzip a file
    @param src: file path
    @param clean: make a previous gzip does not exist on src & dest
    @return: shell session dictionary
    @example: {"core.actionable":{"gzip":{"args":["/path/example.txt"]}}}
    """
    if noop:
        print "[noop] gzip"
        return
    session = shell("file %s" % (src), strict=strict, shell=True)
    if 'gzip' in session.get('stdout'):
        print "[Warning] file is already gzip format skipping gzip"
        return session
    else:
        session = shell("gzip -k %s" % (src), strict=strict, shell=True)
    return session


def symlink(src, dest, strict=True, noop=False):
    """ Performs a symlink
    @param src: file path
    @param dest: new file path
    @return: shell session dictionary
    @example:{
    "core.actionable":{"symlink":{"args":["/path/example","/path2/example"]}}
    }
    """
    if noop:
        print "[noop] symlink"
        return
    session = shell("ln -s %s %s" % (src, dest), strict=strict, shell=True)
    return session


def mkdir(path, clean=True, strict=True, noop=False):
    """ make a directory
    @param path: string, system path
    @param clean: remove path if it exists
    @return: shell session dictionary
    """
    if noop:
        print "[noop] mkdir"
        return
    if clean:
        remove(path)
    session = shell("mkdir -p %s" % (path), strict=strict, shell=True)
    has_dir(path)
    return session


def remove(path, strict=True, noop=False):
    """ Removes a directory using rm -rf
    @param path: string, system path
    @return: shell session dictionary
    """
    if noop:
        print "[noop] remove"
        return
    session = shell("rm -rf %s" % (path), strict=strict, shell=True)
    return session


def copy(src, dest, is_dir=False, strict=True, noop=False):
    """ copies a file or dir
    @param src: file path
    @param dest: new file path
    @param is_dir: adds a -R option
    @return: shell session dictionary
    """
    if noop:
        print "[noop] copy"
        return
    if is_dir:
        session = shell("cp -R %s %s" % (src, dest), strict=strict, shell=True)
        has_dir(dest)
    else:
        session = shell("cp %s %s" % (src, dest), strict=strict, shell=True)
        has_file(dest)
    return session


def move(src, dest, strict=True, noop=False):
    """ Perform a directory or file move
    @param path: string, system path
    @param clean: remove path if it exists
    @return: shell session dictionary
    """
    if noop:
        print "[noop] move"
        return
    session = shell("mv %s %s" % (src, dest), strict=strict, shell=True)
    return session


def has_dir(path, negate=False, strict=True, noop=False):
    """ detect if a directory exists
    @param path: string, system path
    @param negate: boolean, fail on non existence
    @return: shell session dictionary
    """
    if noop:
        print "[noop] has_dir"
        return
    if negate:
        session = shell("[ ! -d %s ]" % (path), strict=strict, shell=True)
    else:
        session = shell("[ -d %s ]" % (path), strict=strict, shell=True)
    return session


def has_file(path, negate=False, strict=True, noop=False):
    """ detect if a file exists
    @param path: string, system path
    @param negate: boolean, fail on non existence
    @return: shell session dictionary
    """
    if noop:
        print "[noop] has_file"
        return
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
                 strict=True,
                 noop=False,
                 ssh_config='/root/.ssh/config'):
    """ performs scm source code checkout support for git & svn
    @param src_path: local path where src will go
    @param repo_url: url associated to repo
    @param branch: branch name
    @param clean: remove previous src from local file system
    @param user: username associated with scm server
    @param passwd: password
    @return: shell session dictionary
    """
    if noop:
        print "[noop] scm_checkout"
        return
    if clean:
        remove("%s/%s" % (src_path, branch))
        mkdir(src_path)
    if "git" in repo_url:
        git_url = repo_url.rsplit('@',1)[1].rsplit(':',1)[0]
        print "[Info] Creating ssh config @ %s" % (ssh_config)
        shell("sudo printf 'Host %s\\n\\tStrictHostKeyChecking no\\n' > %s" % (git_url,ssh_config),shell=True)
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
              verbose=False,
              noop=False):
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
    if noop:
        print "[noop] rsyncable"
        return
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


def jexec(jail_name, env, cmd, strict=True, shell_on=True, noop=False):
    """ Calls Jexec for running commands from within a jail
    @param jail_name: name of jail, or part of name
    @param env: shell environment example. sh, csh,
    @param cmd: string of command to be used
    @return: session
    """
    if noop:
        print "[noop] jexec"
        return
    session = shell("/usr/sbin/jls | grep %s | awk '{print $1}' | tr -d '\n'" % jail_name, strict=True, shell=True)
    JID = session.get("stdout")
    jexec_cmd = "sudo -E /usr/sbin/jexec %s %s -c '%s'" % (JID, env, cmd)
    session = shell(jexec_cmd, strict=strict, shell=shell_on)
    return session


def jls(key, search, return_type='path', strict=True, noop=False):
    """ Get jail info and place it into environment variable
    @param search: string to search for
    @param key: environment key to set
    @param return_type: can only be, jid, ip, hostname, path
    @return: value
    """
    if noop:
        print "[noop] jls"
        return
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


def mount(opts, src, dest, strict=True, noop=False):
    """ system mount call
    @param opts: optional variables to add
    @param src: src directory
    @param dest: destination directory
    @return: session
    """
    if noop:
        print "[noop] mount"
        return
    session = shell("/sbin/mount %s %s %s" % (opts, src, dest), strict=strict, shell=True)
    if not src and dest in session.get('stdout'):
        print "[mount] mounting %s %s" % (src, dest)
        session = shell("/sbin/mount %s %s %s" %
                        (opts, src, dest), strict=strict, shell=True)
    return session


def umount(opts, dest, strict=True, noop=False):
    """ system un-mount call
    @param opts: optional variables to add
    @param dest: destination directory
    @return: session
    """
    if noop:
        print "[noop] umount"
        return
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
              show_cmd=True,
              noop=False):
    """ Run Shell commands  [Non Blocking, no Buffer, print live, log it]
    @param cmd: String command
    @param verbose:bool
    @param strict:bool will exit based on code if enabled
    @return:  {command, stdout, code} as dict
    """
    if noop:
        print "[noop] shell_cmd"
        return
    session = shell(cmd,
                    verbose=verbose,
                    strict=strict,
                    shell=shell_on,
                    buffer_size=1048576,
                    show_cmd=show_cmd)
    return session


def custom_receipt(path,type='json',**kwargs):
    """ Creates a custom receipt in either json or yaml
    @param path:full path and name to produce a receipt
    @param type: json or yaml
    @param kwargs: all dictionary values in the receipt
    @return: receipt file   
    """
    for key,value in kwargs.iteritems():
        kwargs[key] = _sanitize(value)
    with open(path,'w') as file:
        if type == 'yaml':
            import yaml
            file.write(yaml.dump(kwargs, default_flow_style=False))
        elif type == 'json':
            file.write(json.dumps(kwargs, indent=4, sort_keys=True))
        else:
            print "[Error] Unable to write receipt @ %s" % path
            sys.exit(1)


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
        
