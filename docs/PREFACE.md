##User Tutorial
TBD
##Plugin Development Tutorial
1. Create a module in [src/goephor/core/plugins](../src/goephor/core/plugins)
  * Mind the naming of the module as it will be used later.
2. Lets use [src/goephor/core/plugins/example.py](../src/goephor/core/plugins/example.py) to explore how to create a plugin
  * Please use lowercase for your module, class and def naming as this is how your users will resolve the path to your plugin.
  * Plugins are called using a resolution path as follows ***[module].[class].[def]*** to call the example.py plugin a user will add this to his manifest.yaml file:
  ```
  - example.example.runme:
     - "hello"
     - "world"
     - arbitrary: "value"
  ```
3. Here is the example plugin.
  * [self.action_manager](../src/goephor/core/plugins/modules/action.py) gives you access to goephors state for example:
    * All plugins are encapsulated in an action object and stored in action_manager`s chain array. This allows a plugin to modify, add, delete, objects dynamcially.
    * The action_manager can also modify environment variables and set global states.
    * the definition ***runme()*** accepts as 2 parameters which are order dependent
    * The 3rd parameter ***defaults*** allows you to pass ***arbitrary*** key:value pairs [shown above] which can be processed in the definition at your discretion.
    * [message](../src/goephor/core/plugins/modules/log.py) allows you to set coloring of output.
    * All modules in [src/goephor/core/plugins/modules](../src/goephor/core/plugins/modules) can be freely used in your plugin.
    * When ***def runme*** returns it passes the contents back to the action object in variable self.session.
  ```
	from pluginable import Plugin
	from modules.log import message
	class example(Plugin):
	    def __init__(self, action_manager):
	        self.action_manager = action_manager
	        Plugin.__init__(self, self.action_manager)
	
	    def runme(self,
	              var1,
	              var2,
	              **defaults):
	        print message('info',"This var [%s] was passed in " % var1,debug=self.debug)
	        print message('info',"This var [%s] was passed in " % var2,debug=self.debug)
	        print "\nhere are the defaults:"
	        for key, value in defaults.iteritems():
	            print message('info' "%s : %s" % (key, value),debug=self.debug)
	        return "runme_output"
  ```
4. When your plugin is complete hook it into the testing framework.
  * First you need to create ex_[module].yaml file in [src/examples](../src/examples) its generic yaml manifest.
  * Then run your ex_[module].yaml using [test.py](../src/test.py)
  * Create a definition for example.
  ```
  def test_fail(options):
    funct = inspect.stack()[0][3]      << This just gets the currently running def name 
    print "\n\n[%s]\n" % (funct)
    sys.stdout.flush()          
    session = shell("python -u goephor.py -f ./examples/ex_fail.yaml -e -E %s" % options.envs) << call your ex_plugin.yaml here
    if not session.get('code') > 0:    << perform your fail case
        return {funct: False}          << return a dict like this
    return {funct: True}
  ```
  * Then add it to the tests definition
  ```
    tests = []
    tests.append(test_condition(options))
    tests.append(test_defaults(options))
    tests.append(test_environment(options))
    tests.append(test_freebsd(options))
    tests.append(test_http(options))
    tests.append(test_receipt(options))
    tests.append(test_remote(options))
    tests.append(test_scm(options))
    tests.append(test_system(options))
    tests.append(test_string(options))
    tests.append(test_on_exit(options))
    tests.append(test_fail(options))
    tests.append(test_include(options))
    tests.append(test_handler(options))
  ```

##Runtime Call Graph
![Alt text](goephor_ex_system.png?raw=true "goephorcall")
###Generating a Call Graph
* pip install pycallgraph
```
pycallgraph -e argparse* -e gettext* -e posixpath* -e importlib* -e os* -e re* -e UserDict* -e yaml* -e pickle* -e subprocess* -e sre_parse* -e encodings* -e sre_compile* -e codecs* -e atexit* -e shlex* -e pty* -e statement* -e genericpath* -e stat* -e tty* -e locale* graphviz --output-file=../docs/goephor_ex_system.png -- goephor.py -f ./examples/ex_system.yaml -e
```
##Source References##
