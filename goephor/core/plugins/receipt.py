'''
Created on Apr 27, 2016

@author: iitow
'''
from pluginable import Plugin
import yaml
import json


class maker(Plugin):
    ''' This class represents a receipt maker class
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def on_actions(self, path, **defaults):
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
