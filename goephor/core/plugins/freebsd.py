'''
Created on Apr 29, 2016

@author: iitow
'''
from pluginable import Plugin
from modules.terminal import shell

import re

class terminal(Plugin):
    '''
    Freebsd specific commands go here
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
    
    def jls(self,hostname,return_type,**defaults):
        session = shell('/usr/sbin/jls')
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        output = session.get("stdout").split("\n")
        for line in output:
            if hostname in line:
                jail_line = re.split('\s+', line)
                print jail_line
                if return_type == 'path':
                    return jail_line[4]
                elif return_type == 'hostname':
                    return jail_line[3]
                elif return_type == 'ip':
                    return jail_line[2]
                elif return_type == 'jid':
                    return jail_line[1]
                else:
                    error = "invalid return_type %s" % (return_type)
                    raise Exception(error)
        error = "jls command failure"
        raise Exception(error)

    def jexec(self, cmd, jid):
        jexec_cmd = "sudo -E /usr/sbin/jexec %s %s -c '%s'" % (jid, '/bin/sh', cmd)
        session = shell(jexec_cmd)
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')
    
    def fetch(self,path,url):
        session = shell("cd %s; fetch %s" % (path,url))
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')
        

class pkg(Plugin):
    '''
    Freebsd package commands go here
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
    
    def install(name,**defaults):
        session = shell("/usr/sbin/pkg install -y %s" % (name))
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')


class jails(Plugin):
    '''
    Freebsd jail management commands go here
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

        
        
        
    
        
    
    
    
    
    
    
    
    
    
    
        