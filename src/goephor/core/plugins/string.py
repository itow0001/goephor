'''
Created on May 13, 2016

@author: iitow
'''
import json
import re
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
                text,
                old,
                new,
                **defaults):
        '''
        String replace on environment variable
        :param text: String
        :param old: substring
        :param new: replaced value
        ```
        string.utils.replace:
           - "variable"
           - "old substring"
           - "new substring"
        ```
        '''
        new_str = text.replace(old, new)
        if self.verbose:
            print "[replace] %s -> %s" % (text, new_str)
        return new_str

    def substring(self,text,regex,**defaults):
        '''
        Allows you to parse strings using regex
        :param text: String
        :param regex: String
        :return: String
        :example:
        ```
        - string.utils.substring:
            - "SOME_STRING"
            - "S(.+?)G"
            - set_env: SOMEVAL
        ```
        '''
        sub = re.search(regex, text)
        substr=None
        if sub:
            substr = sub.group(1)
            if self.verbose:
                print "[substring] is %s" % (substr)
        return substr

    def is_json(self,data,**defaults):
        '''
        Is string json?
        
        :param data: String
        :return: Boolean
        :example:
        ```
        - string.utils.is_json:
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
        - string.utils.get_key:
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
