'''
Created on Apr 27, 2016

:author: iitow
'''
from pluginable import Plugin
import yaml
import json


class maker(Plugin):
    ''' Receipt creator tasks go here
    '''
    def __init__(self, action_manager):
        '''
        maker Constructor
        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def on_actions(self, path, **defaults):
        '''
        This creates a receipt of all actions in the chain
        
        :param path: String, system path to put receipt
        :param defaults: additional params
        :example:
        ```
        - receipt.maker.on_actions:
            - "./receipt.yaml"
        ```
        '''
        receipt = {}
        receipt["results"] = []
        receipt['globals'] = []
        for key, value in self.envs.iteritems():
            receipt.get('globals').append({key: value})
        for action in self.action_manager.chain:
            result = action.get_receipt()
            receipt.get("results").append(result)
        with open(path, 'w') as file:
            if defaults.get('type') == 'json':
                file.write(json.dumps(receipt,
                                      indent=4,
                                      sort_keys=True))
            else:
                file.write(yaml.dump(receipt,
                                     default_flow_style=False,
                                     allow_unicode=True))
    
    def custom(self, path, **defaults):
        '''
        Create a custom receipt from key/value pairs in defaults
        
        :param path: String, system path to put receipt
        :param defaults: additional params
        :example:
        ```
        - receipt.maker.custom:
            - "./receipt.yaml"
            - var1: "SOMEVALUE1"
            - var2: "SOMEVALUE2"
            - var3: "SOMEVALUE3"
        ```
        '''
        with open(path, 'w') as file:
            if defaults.get('type') == 'json':
                file.write(json.dumps(defaults,
                                      indent=4,
                                      sort_keys=True))
            else:
                file.write(yaml.dump(defaults,
                                     default_flow_style=False,
                                     allow_unicode=True))
