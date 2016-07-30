##User Tutorial
TBD
##Plugin Development Tutorial
1. Create a module in [src/goephor/core/plugins](../src/goephor/core/plugins)
  * Mind the naming of the module as it will be used later.
2. Lets use [src/goephor/core/plugins/example.py](../src/goephor/core/plugins/example.py) to explore how to create a plugin
  * Plugins are called using a resolution path as follows ***[module].[class].[def]*** to call the example.py plugin a user will add this to his manifest.yaml file:
  * Use lowercase for module, class and def name.
  ```
  - example.example.runme:
     - "hello"
     - "world"
     - arbitrary: "value"
  ```
3. Here is the example plugin.
  * [self.action_manager](../src/goephor/core/plugins/modules/action.py) gives you access to goephors state for example:
    * All plugins are encapsulated in an action object and stored in action_manager`s chain array. This allows a plugin to modify, add, delete, itself or other actions objects dynamcially.
    * The action_manager can also modify environment variables and set global states.
    * The ***runme()*** accepts as 2 parameters which are order dependent
    * The 3rd parameter *** defaults *** allows you to pass ***arbitrary*** key:value pairs which can be processed in the definition
    * [message](../src/goephor/core/plugins/modules/log.py) allows you to set coloring of output.
    * All modules in [src/goephor/core/plugins/modules](../src/goephor/core/plugins/modules) can be freely used in your plugin.
    * ***def runme return*** will pass the contents back to the action object and process by [Chain.Run](../src/goephor/core/Chain.py).
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

##Call Graph
![Alt text](goephor_ex_system.png?raw=true "goephorcall")
###Generating a Call Graph
* pip install pycallgraph
```
pycallgraph -e argparse* -e gettext* -e posixpath* -e importlib* -e os* -e re* -e UserDict* -e yaml* -e pickle* -e subprocess* -e sre_parse* -e encodings* -e sre_compile* -e codecs* -e atexit* -e shlex* -e pty* -e statement* -e genericpath* -e stat* -e tty* -e locale* graphviz --output-file=../docs/goephor_ex_system.png -- goephor.py -f ./examples/ex_system.yaml -e
```
## Docs ##
