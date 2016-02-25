'''
Created on Feb 24, 2016

@author: iitow
'''
import json
import os
import yaml

from modules.terminal import shell

this_dir = os.path.dirname(os.path.realpath(__file__))

def write_config(data,type='yaml'):
    if type is 'yaml':
        config = '%s/%s' % (this_dir,'integ_test.yaml')
    elif type is 'json':
        config = '%s/%s' % (this_dir,'integ_test.json')
    else:
        print "[Error] Un supported type %s" % (type)
    with open(config,'w') as file:
        if type is 'yaml':
            file.write(yaml.dump(data, default_flow_style=False))
        if type is 'json':
            file.write(json.dumps(data, indent=4, sort_keys=True))
    return config
            
    

if __name__ == '__main__':
    t1 = {"globals":[{"BRANCH_NAME":"master"},{"BASE_PATH":this_dir}],
          "actions":[
                     {"actionable":{"scm_checkout":{"args":["$BASE_PATH/repo","git@github.west.isilon.com:eng-tools/goephor.git","$BRANCH_NAME"],"kwargs":{"clean":"True"}}}}
                    ]
         }
    config = write_config(t1,type='json')
    shell("python goephor.py -f %s -e" % (config))
    shell("python goephor.py -f ./receipt.json -e")
    config = write_config(t1,type='yaml')
    shell("python goephor.py -f %s -e" % (config))
    shell("python goephor.py -f ./receipt.yaml -e")
    shell('rm -f %s/receipt.json' % (this_dir))
    shell('rm -f %s/receipt.yaml' % (this_dir))
    shell('rm -f %s/integ_test.json' % (this_dir))
    shell('rm -f %s/integ_test.yaml' % (this_dir))
    shell('rm -rf %s/repo' % (this_dir))
    
    
    