'''
Created on May 12, 2016

@author: iitow
'''
from pluginable import Plugin
import datetime
import yaml
import json


class utils(Plugin):
    ''' Helper plugin for obtaining release info
    '''
    def __init__(self, action_manager):
        '''
        utils Constructor
        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def date(self,
             prefix,
             **defaults):
        '''
        get the current date

        :param prefix: %m/%d/%y"
        :example:
        ```
        release.utils.date:
           - '%m/%d/%y'
        ```
        '''
        date = datetime.datetime.now().strftime(prefix)
        if self.verbose:
            print "[date] %s" % (str(date))
        return date

    def compare(self,
                new,
                old):
        '''
        Private, compare release numbers
        :param new: String, new release
        :param old: String, old release
        :note: Assume the last digit is build number
        so we split it off
        :example:
        '''
        old = old.rsplit('.', 1)[0]
        if new == old:
            return True
        return False

    def next(self,
             path,
             new_release):
        '''
        Get the next available release from Release.json
        for a given build
        :param path: String, path to Releases.json
        :param new_release: String, release name 7.1.1
        :note: will only use first three positions
        :example:
        ```
        release.utils.next:
           - './Release.json'
           - '7.1.1'
           - set_env: "NEXT_REL"
        ```
        '''
        if len(new_release.split('.')) > 3:
            new_split = new_release.rsplit('.', 1)
            new_release = new_split[0]
            print "[info] compare using %s" % new_release
        file_type = path.rsplit(".", 1)[1]
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
            if self.compare(new_release, name):
                print "[match] %s" % name
                old_minor = int(name.rsplit('.', 1)[1])
                if minor < old_minor:
                    minor = old_minor
        if minor > 0:
            next = "%s.%s" % (new_release, str(minor+1))
        else:
            next = "%s.%s" % (new_release, str(minor))
        print "[next] %s" % (next)
        return next
