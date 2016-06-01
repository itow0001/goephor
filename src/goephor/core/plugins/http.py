'''
Created on Apr 29, 2016

:author: iitow
'''
from modules.http import Restful
from pluginable import Plugin


class rest(Plugin):
    '''
    This class handles all rest actions
    '''
    def __init__(self, action_manager):
        '''
        rest Constructor

        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def send(self,
             req_type,
             base_url,
             url_ext,
             **defaults):
        '''
        Performs a http restful call

        :param type: String, PUT,GET
        :param base_url: String
        :param url_ext: String
        :example:
        ```
               - http.rest.send:
                     - "GET"
                     - "http://www.google.com"
                     - ""
        ```
        '''
        if self.verbose:
            for key,value in defaults.iteritems():
                print "%s: %s" % (key,value)
        session = Restful(base_url)
        output = session.send(req_type, url_ext,data=defaults)
        if self.verbose:
            print output
        return output.get('response')
