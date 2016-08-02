##User Quick start Tutorial
###Installation
1 install goephor
  ```
  $ git clone git@github.west.isilon.com:eng-tools/goephor.git
  $ cd goephor
  $ python setup.py install
  ```
2. Create a goephor manifest in your home directory.
  ```
  $ cd ~
  $ touch manifest.yaml 
  ```
3. Add the following lines into your manifest:
  ```
  name: "Project Name"
  description: "Project Description"
  globals:
  actions:
  on_exit:
  
  ```
### Manifest and Global Variables
4. Goephor follows yaml convention; 5 tags are needed to run a manifest.
  * ***name*** which is the manifest name.
  * ***description*** which provides a short description of what it does.
  * ***globals*** All variables go here.
  * ***actions*** which provides a method for using the available actions. which can be found at [src/README.md](../src/README.md) under API LIST *** use the examples ***
  * ***on_exit*** which provides a method for using the available action regardless of failures.

5. How to pass global variables into actions.
  * ***global*** global variables can be passed around the manifest freely as with the case of ***VAR1***.
  * ***system.terminal.shell*** is considered an ***action*** many actions exist you can look to the examples directory for more info [src/examples](../src/examples)
  * run goephor with command: goephor -f ./manifest.yaml -e
  ```
  name: "Project Name"
  description: "Project Description"
  globals:
  - VAR1: "WORLD"
  actions:
     - system.terminal.shell:
        - 'echo "${VAR1}"'
  on_exit:
  ```
6. You can nest global variables to create new variables
  * run goephor with command: goephor -f ./manifest.yaml -e
  ```
  name: "Project Name"
  description: "Project Description"
  globals:
  - VAR1: "WORLD"
  - VAR2: "HELLO ${VAR1}"
  actions:
     - system.terminal.shell:
        - 'echo "${VAR2}"'
  on_exit:
  ```
7. You can set new global variables from actions using ***set_env:[variable]***
  * ***set_env*** can be used on all available actions.
  * run goephor with command: goephor -f ./manifest.yaml -e
```
name: "Project Name"
description: "Project Description"
globals:
  - VAR1: "WORLD"
  - VAR2: "HELLO ${VAR1}"
actions:
  - system.terminal.shell:
     - 'echo "WALDO SAYS ${VAR2}"'
     - set_env: "VAR3"
  - system.terminal.shell:
     - 'echo "${VAR3}"'
 on_exit:
```

### on_exit functionality and including manifests

8. ***on_exit*** allows you to run actions regardless of the scripts failure.
  * run goephor with command: goephor -f ./manifest.yaml -e
```
name: "Project Name"
description: "Project Description"
globals:
  - VAR1: "WORLD"
  - VAR2: "HELLO ${VAR1}"
actions:
  - system.terminal.shell:
     - 'echo "WALDO SAYS ${VAR2}"'
     - set_env: "VAR3"
  - system.terminal.shell:
     - 'echo "${VAR3}' #<<< This will fail
on_exit:
   - system.terminal.shell:
      - 'echo "This is an on_exit example"'  
```
9. ***on_exit*** runs just like anything contained in ***actions***
  * You can pass ***globals*** to things in on_exit
  * You can use ***set_env**
  * run goephor with command: goephor -f ./manifest.yaml -e
```
name: "Project Name"
description: "Project Description"
globals:
  - VAR1: "WORLD"
  - VAR2: "HELLO ${VAR1}"
actions:
  - system.terminal.shell:
     - 'echo "WALDO SAYS ${VAR2}"'
     - set_env: "VAR3"
  - system.terminal.shell:
     - 'echo "${VAR3}' #<<< This will fail
on_exit:
   - system.terminal.shell:
      - 'echo "This is an on_exit example"'
      - set_env: "VAR4"
   - system.terminal.shell:
      - 'echo "WALDO SAYS ${VAR4}"'
```
10. Goephor can link manifests
  * create a file called tests.yaml next to manifest.yaml
  * copy this text into the file tests.yaml
  * run goephor with command: goephor -f ./manifest.yaml -e
```
name: "Tests"
description: "Testing goephor functionality"
globals:
  - VAR6: "APPLES"
actions:
  - system.terminal.shell:
     - 'echo "WALDO SAYS ${VAR6}"'
```
    * Update manifest.yaml as follows:
    * the action is ***system.include.manifest***
```
name: "Project Name"
description: "Project Description"
globals:
  - VAR1: "WORLD"
  - VAR2: "HELLO ${VAR1}"
actions:
  - system.terminal.shell:
     - 'echo "WALDO SAYS ${VAR2}"'
     - set_env: "VAR3"
  - system.include.manifest: #<<< include a manifest
     - "./tests.yaml"
     - True
     - False
on_exit:
   - system.terminal.shell:
      - 'echo "This is an on_exit example"'
      - set_env: "VAR4"
   - system.terminal.shell:
      - 'echo "WALDO SAYS ${VAR4}"'
```

### How conditional statements work

11. Goephor has the ability to perform basic if statements.
  * The action is called ***condition.statement.IF***
  * run goephor with command: goephor -f ./manifest.yaml -e
```
name: "Project Name"
description: "Project Description"
globals:
  - VAR1: "WORLD"
  - VAR2: "HELLO ${VAR1}"
actions:
  - system.terminal.shell:
     - 'echo "WALDO SAYS ${VAR2}"'
     - set_env: "VAR3"
  - system.include.manifest: 
     - "./tests.yaml"
     - True
     - False
  - condition.statement.IF: #<<< IF statement here
     - "${VAR1}"
     - "=="
     - "WORLD"
     - THEN:
        - system.terminal.shell:
           - 'echo "WALDO FOUND THE ${VAR1}"'
     - ELSE:
        - system.terminal.shell:
           - 'echo "WALDO FOUND NOTHING"'
on_exit:
   - system.terminal.shell:
      - 'echo "This is an on_exit example"'
      - set_env: "VAR4"
   - system.terminal.shell:
      - 'echo "WALDO SAYS ${VAR4}"'
```
12 Passing variables into manifest at runtime
  * variables can be passed in at runtime using ***-E***
  * The above tag ***condition.statement.IF*** will now follow the ***ELSE*** path
```
goephor -f ./manifest.yaml -e -E "VAR1=WIZARD,VAR2=NOTWALDO"
```

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
def tests(options):
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
  * you can run tests.py like so:
  ```
  sudo python tests.py -E "SERVER_BB=some.servername,PATH_INSTALL=/path/to/an/installer,GITHUB_REPO=git@github.com/<name>/<repo>.git,WORKSPACE=${WORKSPACE},USER=<name>,ID_RSA_PATH=~/.ssh/id_rsa,CFG=/some/random/build.cfg"
  
  ```
  * Your plugin is now ready to be tested and it can be hooked into a CI system such as Jenkins.
5. Your all Finished! Drink a beer.

##Runtime Call Graph
![Alt text](goephor_ex_system.png?raw=true "goephorcall")
###Generating a Call Graph
* pip install pycallgraph
```
pycallgraph -e argparse* -e gettext* -e posixpath* -e importlib* -e os* -e re* -e UserDict* -e yaml* -e pickle* -e subprocess* -e sre_parse* -e encodings* -e sre_compile* -e codecs* -e atexit* -e shlex* -e pty* -e statement* -e genericpath* -e stat* -e tty* -e locale* graphviz --output-file=../docs/goephor_ex_system.png -- goephor.py -f ./examples/ex_system.yaml -e
```
##Source References##
