'''
Created on Apr 29, 2016

:author: iitow
'''
from pluginable import Plugin
from modules.terminal import shell
from modules.log import message
import re


class terminal(Plugin):
    '''
    Freebsd specific commands go here
    '''
    def __init__(self, action_manager):
        '''
        terminal Constructor

        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def jls(self,
            hostname,
            return_type,
            **defaults):
        '''
        Runs the jls command

        :param hostname: String
        :param return_type: String options: path,ip,jid
        :return: String of return_type
        :example:
        ```
        - freebsd.terminal.jls
            - "eng-sea-build10"
            - "jid"
        ```
        '''
        session = shell('/usr/sbin/jls')
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        output = session.get("stdout").split("\n")
        for line in output:
            if hostname in line:
                jail_line = re.split('\s+', line)
                print message('info',str(jail_line),debug=self.debug)
                try:
                    return_type = int(return_type)
                    print message('info',jail_line[return_type],debug=self.debug)
                    return jail_line[return_type]
                except:
                    error = "invalid return_type %s" % (str(return_type))
                    raise Exception(error)
        error = "jls command failure"
        raise Exception(error)

    def jexec(self,
              cmd,
              jid):
        '''
        Runs a command within a jail

        :param cmd: String
        :param jid: String jail id
        :return: command output
        :example:
        ```
        - freebsd.terminal.jexec
            - "echo 'running within jail'"
            - "2"
        ```
        '''
        jexec_cmd = "set -e; sudo -E /usr/sbin/jexec %s %s -c '%s'" % (jid,
                                                               '/bin/sh',
                                                               cmd)
        if self.verbose:
            print message('info',"[jexec] %s" % jexec_cmd,debug=self.debug)
            print ""
        session = shell(jexec_cmd)
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')

    def fetch(self,
              path,
              url):
        '''
        Use fetch to get things from url path

        :param path: String, current working dir
        :param url: String
        :return: String output
        :example:
        ```
        - freebsd.terminal.fetch
            - "/tmp"
            - "http://SomeUrl/to/file"
        ```
        '''
        session = shell("cd %s; fetch %s" % (path, url))
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')


class pkg(Plugin):
    '''
    Freebsd package commands go here
    '''
    def __init__(self, action_manager):
        '''
        pkg Constructor

        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def install(self,
                name,
                **defaults):
        '''
        Install a package
        :param name: String
        :return: output
        :example:
        ```
        - freebsd.pkg.install
            - "texinfo"
        ```
        '''
        session = shell("/usr/sbin/pkg install -y %s" % (name))
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')


class jails(Plugin):
    '''
    Freebsd jail management commands go here
    '''
    def __init__(self, action_manager):
        '''
        jails Constructor

        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
