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
        for key, value in self.action_manager.config.iteritems():
            receipt.get('globals').append({key: value})
        for action in self.action_manager.chain:
            result = action.get_receipt()
            receipt.get("results").append(result)
        
        self._to_file(receipt,path)
    
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
        print "[custom] %s" % (path)
        for key,value in defaults.iteritems():
            print "%s: %s" % (key,value)
        self._to_file(defaults, path)

    def read(self,path,**defaults):
        '''
        Reads in a custom receipt and generates environment variables
        :param defaults: additional params
        :note: Consumes only files from a custom receipt
        :example:
        ```
        - receipt.maker.read:
           - "receipt.yaml"
        ```
        '''
        print "[read] %s" % path

        data = self._to_dict(path)
        for key,value in data.iteritems():
            self.EnvManager.set(key, value)
            if self.verbose:
                print "[set] %s=%s" % (key,value)
    
    def add(self,path,**defaults):
        '''
        Add to an existing receipt
        :param path: String, path to existing file
        :param set: values to add to file
        :example:
        ```
       - receipt.maker.add:
                        - "./custom.yaml"
                        - set:
        ```
        '''
        if defaults.get('set'): 
            set = defaults.get('set')            
            data = None
            print "[add] %s" % path
            data = self._to_dict(path)
            data.update(set)
            self._to_file(data, path)
        else:
            raise Exception('[set] default required')

    def _to_dict(self,path):
        '''
        Private, Load a file in and output a dict
        
        :param path: String
        :param is_string: String path is a string do not load file
        :return: Dictionary
        '''
        file_type = path.rsplit(".",1)[1]
        with open(path) as file:
            if 'json' in file_type:
                if self.verbose:
                    print "[_to_dict] json"
                data = json.loads(file.read())
                return data
            else:
                if self.verbose:
                    print "[_to_dict] yaml"
                data = yaml.load(file)
                return data
        print "[None]"
        return None

    def _to_file(self,data,path):
        '''
        Private, convert dict to file
        
        :param path: String
        '''
        file_type = path.rsplit(".",1)[1]
        with open(path, 'w') as file:
            if 'json' in file_type:
                if self.verbose:
                    print "[_to_file] json"
                file.write(json.dumps(data,
                                      indent=4,
                                      sort_keys=True))
            elif 'txt' in file_type:
                if self.verbose:
                    print "[_to_file] txt"
                for key,value in data.iteritems():
                    pair = "%s=%s" % (key,value)
                    file.write(pair)
            else:
                if self.verbose:
                    print "[_to_file] yaml"
                file.write(yaml.dump(data,
                                     default_flow_style=False,
                                     allow_unicode=True))
        
        
        
        




























