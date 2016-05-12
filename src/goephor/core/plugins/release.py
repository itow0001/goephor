'''
Created on May 12, 2016

@author: iitow
'''
import datetime

class utils(object):
    ''' Helper plugin for obtaining release info
    '''
    def __init__(self, action_manager):
        '''
        utils Constructor
        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
    
    def date(self,prefix,**defaults):
        '''
        get the current date
        
        :param prefix: %m/%d/%y"
        
        ```
        release.utils.date:
           - '%m/%d/%y'
        ```
        '''
        date = datetime.datetime.now().strftime(prefix)
        return date
    
    def compare(self,new,old):
        '''
        Private, compare release numbers
        :param new: String, new release 3 digits
        :param old: String, old release 4 digits
        '''
        new = new.split('.')
        old = old.split('.')
        if not len(old) == 3:
            return False
        if not len(new) == 2:
            return False
        if new[0] == old[0] and new[1] == old[1] and new[2] == old[2]:
            return True
        return False

    def next(self,path,new_release):
        '''
        Get the next available release from Release.json
        for a given build
        :param path: String, path to Releases.json
        :param new_release: String, release name 7.1.1
        :example:
        ```
        release.utils.next:
           - './Release.json'
           - '7.1.1'
           - set_env: "NEXT_REL"
        ```
        '''
        file_type = path.rsplit(".",1)[1]
        releases_dict = {}
        try:
            with open(path) as file:
                if 'json' in file_type:
                    releases = json.loads(file.read())
                else:
                    releases = yaml.load(file)
        except Exception:
            error = "unable to read %s" % (path)
            raise Exception(error)
        minor = 0
        for name, values in releases.iteritems():
            if compare(new_release,name):
                name = name.split('.')
                if minor < int(name[len(name)]):
                    minor = int(name[len(name)])
        next = "%s.%s" % (new_release,str(minor+1))
        print "[next] %s" % (next)
        return next
                
                
                
                
            
            
                
                 
        
        

        
                
                
                
        
        
        
        
                    
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        