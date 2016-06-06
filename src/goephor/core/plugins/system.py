'''
Created on Apr 25, 2016

:author: iitow
'''
from pluginable import Plugin
from modules.terminal import shell, rsync
from modules.log import message

class terminal(Plugin):
    '''
    General nix system commands go here
    '''
    def __init__(self, action_manager):
        '''
        terminal Constructor

        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def shell(self,
              cmd,
              **defaults):
        '''
        Run a shell command

        :param cmd: String
        :example:
        ```
        - system.terminal.shell:
            - 'echo " THIS IS IT"'
        ```
        '''
        if self.verbose:
            print "[cmd] %s\n" % (cmd)
        session = shell(cmd)
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')

    def rsync(self,
              user,
              rsa_private_path,
              server,
              src,
              dest,
              option,
              **defaults):
        '''
        Perform an rsync
        :param user: String
        :param rsa_private_path: String
        :param server: String
        :param src: String, source dir
        :param dest: String, dest dir
        :param options: String, push,pull
        :example:
        ```
        - system.terminal.rsync:
              - "root"
              - "~/.ssh/id_rsa"
              - "Some.Server.Name"
              - "/tmp/remote"
              - "/tmp/local"
              - "pull"
        ```
        '''
        if self.verbose:
            print message('info',"[rsync] %s [%s] -> [%s]" % (option,
                                               src,
                                               dest))
        session = rsync(server,
                        src,
                        dest,
                        user=user,
                        rsa_private=rsa_private_path,
                        option=option)
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')
