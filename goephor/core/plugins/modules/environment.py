'''
Created on Apr 26, 2016

@author: iitow
'''
import os
import re

class Env(object):
    ''' Management of environment variables
    '''
    def __init__(self,debug=True):
        self.debug = debug
    
    def set(self,key,value):
        if self.debug:
            print '[set] %s=%s' % (key,value)
        os.environ[key]=str(value)
    
    def get(self,key):
        env = os.environ.get(key,None)
        if self.debug:
            print '[get] %s=%s' % (key,env)
    
    def sanitize(self,values):
        ''' sanitizes environment variables independent of array or dict
        '''
        if isinstance(values,dict):
            dfts = {}
            for key,value in values.iteritems():
                if isinstance(value,list):
                    dfts[key] = value
                else:
                    dfts[key] = self._sanitize(value)
            return dfts
            return defaults
        else:
            params = []
            for param in values:
                params.append(self._sanitize(param))
            return params

    def _sanitize(self,str):
        """ Replace all environment variables into command
        @param str: command string
        """
        matches = re.findall(r'(?<={)[^}]*', str)
        for match in matches:
            old = '${%s}' % match
            new = os.environ.get(match)
            if new:
                str = str.replace(old, new)
        return str