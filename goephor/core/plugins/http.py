'''
Created on Apr 29, 2016

@author: iitow
'''
from modules.http import Restful
from pluginable import Plugin

class rest(Plugin):
    '''
    This class handles all rest actions
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
    
    def send(self,type,base_url,url_ext,**defaults):
        session = Restful(base_url)
        session.send(type,url_ext)
        
        