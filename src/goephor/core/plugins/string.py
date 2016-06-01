'''
Created on May 13, 2016

@author: iitow
'''
import json
from pluginable import Plugin


class utils(Plugin):
    '''
    Utils class for parsing strings
    '''
    def __init__(self, action_manager):
        '''
        utils Constructor
        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def replace(self,
                name,
                old,
                new,
                **defaults):
        '''
        String replace on environment variable
        :param name: String, environment variable to use
        :param old: substring
        :param new: replaced value
        ```
        string.utils.replace:
           - "env variable"
           - "old substring"
           - "new substring"
        ```
        '''
        env = self.EnvManager.get(name)
        if not env:
            error = "env not found %s" % (name)
            raise Exception(error)
        new_env = env.replace(old, new)
        self.EnvManager.set(name, new_env)
        if self.verbose:
            print "[replace] %s=%s" % (name, new_env)
    
    def is_json(self,data,**defaults):
        '''
        Is string json?
        
        :param data: String
        :return: Boolean
        :example:
        ```
        string.utils.is_json:
           - data
           - set_env: SOMEVAL
        ```
        '''
        try:
            json_object = json.loads(data)
        except ValueError:
            return False
        return True  
    
    def get_key(self,data, key,**defaults):
        '''
        Get a key from json string
        :param data: String
        :param key: String 
        :return: String, value
        :note: Can add future support for different data formats
        :example:
        ```
        string.utils.get_key:
           - Somejsonhere
           - somekey
           - set_env: SOMEVAL
        ```
        '''
        if self.is_json(data):
            data = json.loads(data)
            value = self.traverse(data,key)
            if self.verbose:
                print "[value] is [%s]" % (str(value))
            if not value:
                return None
            return value
        else:
            raise Exception('Must be well formed json string')

    def traverse(self,data, key):
        '''
        Private recursively traverse nested json data
        :param data: Nested dict/list
        :param key: String
        :return: value
        '''
        values=[]
        if isinstance(data, list):
            for items in data:
                value = self.traverse(items, key)
                values.append(''.join(value))
            return ''.join(values)

        elif isinstance(data, dict):
            for k, v in data.iteritems():
                if self.verbose:
                    print "%s: %s" % (k,v)
                if k == key:
                    return str(v)
                if isinstance(v, list) or isinstance(v, dict):
                    value = self.traverse(v, key)
                    values.append(''.join(value))
            return ''.join(values)  
        else:
            if values:
                return values
