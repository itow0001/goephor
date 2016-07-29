![Alt text](docs/goephorit.jpg?raw=true "goephorit")

###Package Create/Install###
    python setup.py sdist
    cd ../dist
    pip install goephor-1.0.1.tar.gz

### Usage ###

```
usage: goephor [-h] [-f FILE] [-e] [-E ENVS] [-s] [--version]

A yaml friendly build management tool

optional arguments:
  -h, --help  show this help message and exit
  -f FILE     json file containing build instructions
  -e          execute all values in the chain
  -E ENVS     Add env vars delimiter:"," example.
              "BASE_PATH=/tmp,WORKPATH=/${BASE_PATH}/addon"
  -s          do not print any additional info
  --version   show program's version number and exit

example: 
   goephor -f <path>/manifest.yaml -e
```
### Basic Example Manifest ###
```
  name: "Project Name"
  description: "Project Description"
  globals:
    - VAR1: "HELLO WORLD"
  actions:
     - system.terminal.shell:
        - 'echo "${VAR1}"'
     
```
### More Example Manifests ###
Located at [src/examples](More Examples)

### Source Code Documentation ###




**********************************************
**********************************************
 File @ ***/goephor.py***

Created on Jan 9, 2016


**:author:** iitow

**:note:** Look to __main__.py for menu logic

**********************************************
**********************************************
**********************************************
 File @ ***/__init__.py***

None

**********************************************
**********************************************
**********************************************
 File @ ***/tests.py***

Created on May 4, 2016

**:author:** iitow

**:note:** All integration tests go here.


***def menu***: 

argparse menu here

***def test_condition***: 

test of core/plugins/condition.py

***def test_defaults***: 

test of core/plugins/pluginable.py

***def test_environment***: 

test of core/plugins/environment.py

***def test_freebsd***: 

test of core/plugins/freebsd.py

***def test_http***: 

test of core/plugins/http.py

***def test_receipt***: 

test of core/plugins/receipt.py

***def test_remote***: 

test of core/plugins/remote.py

***def test_scm***: 

test of core/plugins/scm.py

***def test_system***: 

test of core/plugins/system.py

***def test_release***: 

test of core/plugins/release.py

***def test_string***: 

test of core/plugins/string.py

***def test_on_exit***: 

test of core/Chain.py

***def test_include***: 

test of core/plugins/system.py

***def test_fail***: 

test of core/plugins/system.py

***def test_handler***: 

test of core/plugins/system.py

***def tests***: 

calls all the tests here & collects results
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/__init__.py***

goephor __init__.py

**********************************************
**********************************************
**********************************************
 File @ ***/goephor/_version.py***

None

**********************************************
**********************************************
**********************************************
 File @ ***/goephor/__main__.py***

Main entry for goephor to menu here


***def menu***: 

argparse menu here

***def parse_envs***: 

Parse environment variables from menu comma delimiter

***def main***: 

This is the entry point for the package cli
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/__init__.py***

Core __init__.py

**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/Chain.py***

Contained in this file is the main loops

**:author:** iitow


***class Run***: 

This is the entry point from the cli and drives components

***def __init__***: 

Run Constructor


**:param config_file:** path to yaml manifest

**:param verbose:** print general run info

**:param debug:** print debug info

***def __enter__***: 

Entry point for Run obj
        

***def __exit__***: 

performs actions on exit of obj
        

***def read_config***: 

Allows for reading .yaml or .json files


**:param config_file:** defines all actions in a build

**:return:** dict

***def _read_yaml***: 

Reads in the yaml config


**:param config_file:** defines all actions in a build

**:return:** dict

***def _read_json***: 

Reads in the json config


**:param config_file:** defines all actions in a build

**:return:** dict

***def add_envs***: 

Overrides environment variables from cli


**:param **envs:** dictionary of environment variables

***def set_envs***: 

sets environment variables inside of manifest

**:params reset:** Boolean, If param exists reset it

***def load_actions***: 

loads actions in to chain resolves yaml/json to a object

***def load_on_exit***: 

loads on_exit actions in to chain resolves yaml/json to a object

***def execute_actions***: 

Executes all action objects
        

***def execute_on_exit***: 

Executes all on exit action objects
        
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/receipt.py***

Created on Apr 27, 2016


**:author:** iitow


***class maker***: 

Receipt creator tasks go here
    

***def __init__***: 

maker Constructor

**:param action_manager:** Obj, from action_manager class

***def is_json***: 

Is string json?


**:param data:** String

**:return:** Boolean

**:example:**
```
- string.utils.is_json:
    - data
    - set_env: SOMEVAL
```

***def on_actions***: 

This creates a receipt of all actions in the chain


**:param path:** String, system path to put receipt

**:param defaults:** additional params

**:example:**
```
- receipt.maker.on_actions:
    - "./receipt.yaml"
```

***def custom***: 

Create a custom receipt from key/value pairs in defaults


**:param path:** String, system path to put receipt

**:param defaults:** additional params

**:example:**
```
- receipt.maker.custom:
    - "./receipt.yaml"
    - var1: "SOMEVALUE1"
    - var2: "SOMEVALUE2"
    - var3: "SOMEVALUE3"
```

***def custom_json***: 

produces output file from json data

**:param path:** String

**:param data:** String

**:example:**
```
- receipt.maker.custom_json:
    - path/put/file
    - somejsonhere
```

***def read***: 

Reads in a custom receipt and generates environment variables

**:param defaults:** additional params

**:note:** Consumes only files from a custom receipt

**:example:**
```
- receipt.maker.read:
   - "receipt.yaml"
```

***def add***: 

 Add to an existing receipt
 
**:param path:** String, path to existing file
 
**:param json_str:** String, using json syntax add to receipt
 
**:param to_json:** Boolean, write file out as json
 
**:note:** json syntax, {hello:{world}}
 
**:example:**
 ```
- receipt.maker.add:
                 - "./custom.yaml"
                 - '{"HELLO":["WORLD","05/10/14"]}'
 ```
 

***def _to_dict***: 

Private, Load a file in and output a dict


**:param path:** String

**:param is_string:** String path is a string do not load file

**:return:** Dictionary

***def _str_to_dict***: 

Convert json string to dict

**:param data:** String

**:return:** Dictionary

***def _to_file***: 

Private, convert dict to file


**:param path:** String
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/__init__.py***

modules __init__.py

**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/release.py***

Created on May 12, 2016

@author: iitow


***class utils***: 

Helper plugin for obtaining release info
    

***def __init__***: 

utils Constructor

**:param action_manager:** Obj, from action_manager class

***def date***: 

get the current date


**:param prefix:** %m/%d/%y"

**:example:**
```
release.utils.date:
   - '%m/%d/%y'
```

***def pad***: 

Provides generic padding to numbers and strings


**:param text:** String

**:param fill:** Char

**:param amount:** Int

**:return:** String

**:example:**
```
- release.utils.pad:
   - '9'
   - '0'
   - 3
   - set_env: "PAD"
```

***def compare***: 

Private, compare release numbers

**:param new:** String, new release

**:param old:** String, old release

**:note:** Assume the last digit is build number
so we split it off

**:example:**

***def next***: 

Get the next available release from Release.json
for a given build

**:param path:** String, path to Releases.json

**:param new_release:** String, release name 7.1.1

**:note:** will only use first three positions

**:example:**
```
release.utils.next:
   - './Release.json'
   - '7.1.1'
   - set_env: "NEXT_REL"
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/string.py***

Created on May 13, 2016

@author: iitow


***class utils***: 

Utils class for parsing strings

***def __init__***: 

utils Constructor

**:param action_manager:** Obj, from action_manager class

***def println***: 

Generic print line

**:param msg_type:** String: header, info, success, warning, fail, error

**:param text:** String
```
string.utils.println:
   - 'info'
   - "HELLO WORLD"
```

***def replace***: 

String replace on environment variable

**:param text:** String

**:param old:** substring

**:param new:** replaced value
```
string.utils.replace:
   - "variable"
   - "old substring"
   - "new substring"
```

***def substring***: 

Allows you to parse strings using regex

**:param text:** String

**:param regex:** String

**:return:** String

**:example:**
```
- string.utils.substring:
    - "SOME_STRING"
    - "S(.+?)G"
    - set_env: SOMEVAL
```

***def is_json***: 

Is string json?


**:param data:** String

**:return:** Boolean

**:example:**
```
- string.utils.is_json:
    - data
    - set_env: SOMEVAL
```

***def get_key***: 

Get a key from json string

**:param data:** String

**:param key:** String 

**:return:** String, value

**:note:** Can add future support for different data formats

**:example:**
```
- string.utils.get_key:
    - Somejsonhere
    - somekey
    - set_env: SOMEVAL
```

***def traverse***: 

Private recursively traverse nested json data

**:param data:** Nested dict/list

**:param key:** String

**:return:** value
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/scm.py***

Created on Apr 28, 2016

@author: iitow


***class git***: 

This class Represents a call to git
    

***def __init__***: 

git Constructor


**:param action_manager:** Obj, from action_manager class

***def latest_commit***: 

get the latest commit info from a branch

**:param user:** String, username

**:param local_path:** String, full path and desired dir name

**:param branch:** String

**:param info_type:** String, sha1, message, author

**:return:** String

**:example:**
```
        - scm.git.latest_commit:
              - "root"
              - "/tmp/goephor"
              - "refactor"
              - "sha1"
```

***def clone***: 

Clone a git repo


**:param user:** String, username

**:param new_local_path:** String, full path and desired dir name

**:param remote:** String, git repo

**:param branch:** define the branch to checkout

**:param depth:** to perform a shallow clone

**:example:**
```
       - scm.git.clone:
              - "root"
              - "/tmp/goephor"
              - "git@github.west.isilon.com:eng-tools/goephor"
```

***def checkout***: 

checkout a local branch

**:param user:** String, username

**:param local_path:** String, full path and desired dir name

**:param branch:** String
```
        - scm.git.checkout:
              - "root"
              - "/tmp/goephor"
              - "refactor"
```

***def delete***: 

Delete a local repo

**:param local_path:** String

**:example:**
```
    - scm.git.delete:
        - "/tmp/goephor"
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/handler.py***

Created on Jul 1, 2016

@author: iitow


***class file***: 

General class can read configuration files

***def __init__***: 

terminal Constructor


**:param action_manager:** Obj, from action_manager class

***def readconfig***: 

General read configs into environment currently only supports ConfigParser

**:param path:** String, full path to file

**:return:** key value pairs become environment variables

**:example:**
```
- handler.file.readconfig:
   - "${CFG}"
```

***def _configparser***: 

Private, adds configparser values to environment 
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/freebsd.py***

Created on Apr 29, 2016


**:author:** iitow


***class terminal***: 

Freebsd specific commands go here

***class pkg***: 

Freebsd package commands go here

***class jails***: 

Freebsd jail management commands go here

***def __init__***: 

terminal Constructor


**:param action_manager:** Obj, from action_manager class

***def jls***: 

Runs the jls command


**:param hostname:** String

**:param return_type:** String options: path,ip,jid

**:return:** String of return_type

**:example:**
```
- freebsd.terminal.jls
    - "eng-sea-build10"
    - "jid"
```

***def jexec***: 

Runs a command within a jail


**:param cmd:** String

**:param jid:** String jail id

**:return:** command output

**:example:**
```
- freebsd.terminal.jexec
    - "echo 'running within jail'"
    - "2"
```

***def fetch***: 

Use fetch to get things from url path


**:param path:** String, current working dir

**:param url:** String

**:return:** String output

**:example:**
```
- freebsd.terminal.fetch
    - "/tmp"
    - "http://SomeUrl/to/file"
```

***def __init__***: 

pkg Constructor


**:param action_manager:** Obj, from action_manager class

***def install***: 

Install a package

**:param name:** String

**:return:** output

**:example:**
```
- freebsd.pkg.install
    - "texinfo"
```

***def __init__***: 

jails Constructor


**:param action_manager:** Obj, from action_manager class
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/pluginable.py***

Created on Apr 25, 2016


**:author:** iitow


***class DecoMeta***: 

This is a meta class for decorating all classes

***class Plugin***: 

This is the base class for a plugin
    

***def __new__***: 

Allows for grabbing class info for parsing

***def deco***: 

We use this to append defaults actions here

***def __init__***: 

Plugin constructor

***def wrapper***: 

This is a decorator for adding global key,value pairs
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/environment.py***

Created on Apr 27, 2016


**:author:** iitow


***class env***: 

Environment specific tasks go here
    

***class utils***: 

Environment utilities
    

***def __init__***: 

env Constructor


**:param action_manager:** Obj, from action_manager class

***def set***: 

Set an environment variable


**:param key:** String

**:param value:** String

**:example:**
```
- environment.env.set:
   - "VAR1"
   - "some value"
```

***def unset***: 

Unset an environment variable


**:param key:** String

**:param value:** String

**:example:**
```
- environment.env.unset:
   - "VAR1"
```

***def __init__***: 

env Constructor


**:param action_manager:** Obj, from action_manager class

***def has_path***: 

Checks if a pth exists


**:param path_str:** String

**:return:** boolean

**:example:**
```
- environment.utils.has_path:
   - "/some/path"
   - set_env: "VAR1"
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/system.py***

Created on Apr 25, 2016


**:author:** iitow


***class include***: 

General class to include other files

***class terminal***: 

General nix system commands go here

***def __init__***: 

terminal Constructor


**:param action_manager:** Obj, from action_manager class

***def manifest***: 

This allows you to link a external manifests into your script

**:param file:** String, path to file

**:param silent:** Boolean

**:param debug:** Boolean
```
- system.include.manifest:
    - '/path/to/manifest.yaml'
    - False
    - False
    - VAR1: "SOMEVALUE"
```

***def __init__***: 

terminal Constructor


**:param action_manager:** Obj, from action_manager class

***def shell***: 

Run a shell command


**:param cmd:** String

**:example:**
```
- system.terminal.shell:
    - 'echo " THIS IS IT"'
```

***def rsync***: 

Perform an rsync

**:param user:** String

**:param rsa_private_path:** String

**:param server:** String

**:param src:** String, source dir

**:param dest:** String, dest dir

**:param options:** String, push,pull

**:example:**
```
- system.terminal.rsync:
      - "root"
      - "~/.ssh/id_rsa"
      - "Some.Server.Name"
      - "/tmp/remote"
      - "/tmp/local"
      - "pull"
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/remote.py***

Created on Apr 28, 2016


**:author:** iitow


***class ssh***: 

This class can perform ssh commands

***def __init__***: 

ssh Constructor


**:param action_manager:** Obj, from action_manager class

***def cmd***: 

Run a command remotely via ssh

**:param cmdstr:** String

**:param server:** String

**:param user:** String

**:param rsa_private_path:** String

**:example:**
```
       - remote.ssh.cmd:
            - "uname -a"
            - "some.server.com"
            - "root"
            - "~/.ssh/id_rsa"
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/example.py***

Created on Apr 27, 2016


**:author:** iitow


***class example***: 

This class Represents an example
    

***def __init__***: 

example Constructor


**:param action_manager:** Obj, from action_manager class

***def runme***: 

This is an example of setting up an action

**:param var1:** String

**:param var2:** String

**:return:** runme_output

**:example:**
```
- example.example.runme:
    - "hello"
    - "world"
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/http.py***

Created on Apr 29, 2016


**:author:** iitow


***class rest***: 

This class handles all rest actions

***def __init__***: 

rest Constructor


**:param action_manager:** Obj, from action_manager class

***def send***: 

Performs a http restful call


**:param type:** String, PUT,GET

**:param base_url:** String

**:param url_ext:** String

**:param params:** json string

**:param data:** json string

**:param silent:** boolean

**:example:**
```
       - http.rest.send:
             - "GET"
             - "https://build.west.isilon.com"
             - "api/branch"
             - params
**
**: '{"name":****"${BRANCH_NAME}"}'
             - data
**
**: '{"name":****"${BRANCH_NAME}"}'
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/condition.py***

Created on Apr 26, 2016


**:author:** iitow


***class statement***: 

Conditional statements go here

***def __init__***: 

statement Constructor


**:param action_manager:** Obj, from action_manager class

***def add_obj***: 

Private def to add action out of band

**:param clause:** dict, if statement

***def IF***: 

Represents an if statement

**:param arg1:** int,str

**:param operator:** String, follows python rules
:param arg12 int,str

**:param THEN:** List, several other actions

**:param ELSE:** List, several other actions

**:example:**
```
   - condition.statement.IF:
                        - "${var1}"
                        - "=="
                        - "${var2}"
                        - THEN:
                          - system.terminal.shell:
                            - "echo 'THEN IS HAPPENING'"
                        - ELSE:
                          - system.terminal.shell:
                            - "echo 'ELSE IS HAPPENING'"
```

***def HAS_TOKEN***: 

Check if a string exists in some output

**:param token:** String

**:param output:** String

**:return:** Boolean
```
    - condition.statement.HAS_TOKEN:
                            - ${token}
                            - ${output}
                            -set_env: VAR1
```

***def FAIL***: 

Cause a failure generally used with a IF

**:param text:** String
    ```
        - condition.statement.FAIL:
           - "Failed because of some issue"
    ```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/action.py***

Created on Apr 26, 2016


**:author:** iitow


***class Manager***: 

This class manages state of action objects


**:note:** This is passed into each of the plugins and can be used to manage
Serveral states.

***class Action***: 

Object containing instructions to create and execute actions

***def __init__***: 

Constructor


**:param config:** nest dict from manifest

**:param EnvManager:** Holds the state of the Environment

**:param verbose:** set verbosity

**:param debug:** set debug

***def to_obj***: 

Converts action dictionary to action obj


**:param action:** base action dict

**:param action_manager:** from chain.Run pass in Action_manager

**:note:** We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

***def add***: 

Append an action obj to chain


**:param action_obj:** Obj

***def insert***: 

Insert action object at a given index in the chain


**:param index:** Int of chain

**:param action_obj:** Obj

***def get_index***: 

Get the index number of an action object in the chain


**:param memory_address:** String, of object.__repr__(self)

**:note:** See plugins.condition for usage

***def __init__***: 

Constructor


**:param name:** String, full resolve path

**:param IMP:** String, import name

**:param CLASS:** String, class name

**:param DEF:** String, definition name

**:param parameters:** list

**:param defaults:** Dict

**:param action_manager:** Obj

***def __repr__***: 

Override container name so we can match the array in the chain


**:note:** This is how we match chain to current
plugin using object.__repr__(self)

***def set_ignore***: 

catch the ignore parameter and delete it in defaults

***def get_receipt***: 

return a dictionary of all Action info

***def pprint***: 

print state about the object pretty


**:param title:** String

**:param footer:** String

***def _init_instance***: 

Initializes the class

**:note:** we initialize the plugin class so we
can pass info into action Obj before run.

***def execute***: 

execute the instruction
        
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/git_kit.py***

Created on Oct 8, 2015


**:author:** iitow


***class Repo_actions***: 

None

***class Commit_actions***: 

This class handles all commit type actions
    

***class Branch_actions***: 

This class handles all branch related actions


**:requires:** Repo obj

***class Remote_actions***: 

This class handles all remote actions
    

***def __init__***: 

Initialize Repo actions

***def _set_ssh_config***: 

This turns off host verification


**:param ssh_config:** path to <user>/.ssh/config

**:param git_host:** example. github.west.isilon.com

***def _set_dirs***: 

None

***def attach***: 

attach to a git repo on your local system


**:param repo_path:** system path to repo

**:return:** boolean, success/failure

***def _initial_commit***: 

To fully init an empty rep

***def init***: 

Initialize a new repo on your local system


**:param set_bare:** boolean, default is False, creates a 'bare repo',
to run like a src repo

**:return:** boolean, success/failure

**:note:** Shared repositories should always be created with the set_bare
flag and should be stored in a directory called <projectname>.git

***def clone***: 

Clone a repository from a remote location


**:param remote_ssh:** provide the ssh full info
example. git@github.west.isilon.com:iitow/scm-tools.git

**:return:** boolean, success/failure

***def untracked_files***: 

list all untracked files


**:return:** list of untracked files

***def __init__***: 

None

***def commit***: 

Commits changes


**:param msg:** string, the commit message

**:return:** boolean, success/failure

***def cherry_pick***: 

Cherry picks a commit


**:param sha1_str:** sha1 string of commit

**:return:** boolean True/False

***def diff_tree***: 

Performs a diff tree against current and sha1


**:param sha1_str:** String

***def search_log***: 

Search logs for a given token


**:param search:** String token

***def latest***: 

None

***def add***: 

adds files to git index


**:param file_name:** name of the file to commit

**:return:** boolean, success/failure

***def __init__***: 

None

***def branch***: 

Creates a new local branch


**:param branch_name:** string, name of the new branch to create it

**:return:** boolean, success/failure

***def branch_from***: 

Create a branch from existing branch


**:param src_branch:** original branch name

**:param dest_branch:** new branch name

***def branch_is***: 

provides the current branch


**:return:** the current branch

***def branch_list***: 

provides a list of all branches


**:param verbose:** boolean, prints branches out

**:return:** list of git.branch objects

***def has_reference***: 

Search for reference


**:param branch_name:** string of branch name

**:return:** reference obj

***def has_head***: 

Search for branch head


**:param branch_name:** string of branch name

**:return:** head obj

***def checkout***: 

checks out a specific branch


**:param branch_name:** string, branch you wish to checkout

**:param remote:** remote name default is origin

**:return:** boolean, success/failure

***def push***: 

Push branch to remote


**:param branch_name:** string branch name

**:param remote:** remote reference

**:return:** boolean

***def remote_delete***: 

Deletes branch from github remote


**:param branch_name:** string branch name

**:param remote:** remote reference

**:return:** boolean

***def delete***: 

Delete local branch


**:param branch_name:** string branch name

**:param remote:** remote reference

**:return:** boolean

***def __init__***: 

Remote_actions Constructor

***def list***: 

None

***def has_remote***: 

None

***def add***: 

add a remote to repo


**:param remote:** remote url string

**:param name:** reference to the remote example. upstream

**:return:** boolean True/False

***def fork_sync***: 

Syncs a fork of repo with another repository


**:param remote:** remote url string
example. git@github.west.isilon.com:iitow/onefs.git

**:param name:** reference to the remote example. upstream

**:return:** boolean True/False

***def fetch***: 

Fetch remote branches


**:param remote:** repo url
example. git@github.west.isilon.com:isilon/onefs.git

**:param name:** name of the remote
:param branch; branch to switch to when fetching

**:param add_remote:** boolean add a remote

**:return:** boolean
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/__init__.py***

None

**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/log.py***

Created on Jun 3, 2016


**:author:** iitow


***def colors***: 

Types of colors to display

***def message***: 

Display a colorized message

**:param message_type:** String, header, info, success, warning, fail, error

**:param output:** String

**:return:** colorized string
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/environment.py***

Created on Apr 26, 2016


**:author:** iitow


***class EnvManager***: 

Management of runtime environment


**:note:** This is passed to each of the plugins
when the action obj is initialized
Its contained within the action_manager.

***def __init__***: 

Constructor


**:param debug:** Bool

***def set***: 

set an environment variable


**:param key:** String

**:param value:** String

**:param reset:** Bool, if false it will not override an existing env value

***def unset***: 

unset environment variable


**:param value:** String

***def get***: 

get an environment variable


**:param key:** String

***def sanitize***: 

sanitizes environment variables in a given values


**:param values:** List

***def _sanitize***: 

Replace all environment variables into command


**:param stri:** String,Bool,Int

**:note:** when nested environment variables are used
in a string convert all
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/remote.py***

Created on Nov 18, 2015


**:author:** iitow


***class Run***: 

This class represents a remote machine
using SSH to perform all needed actions

***def __init__***: 

Initializes a Remote session

**:param server:** server address

**:param rsa_private:** path to the private key file

**:param user:** Username used to log into system

**:param password:** Password used to log into system

**:param strict:** boolean fail on error

**:param verbose:** print out all debug messaging

**:param show_cmd:** show the command given to remote server

***def is_alive***: 

Pings the remote to make sure its a valid address

**:return:** boolean

***def is_alive_poll***: 

Polls for a ping

**:param timeout:** default 30 seconds

**:return:** boolean

***def is_writable***: 

Check to make sure the file system is writable

**:return:** boolean

***def is_writable_poll***: 

Check to make sure file system is writable poll

**:param timeout:** default 30 seconds

**:return:** boolean

***def has_access***: 

Does a key already exist on the remote?

**:return:** boolean

***def has_file***: 

Does a file exist on the remote?

**:param path:** path where file should exist

**:param file:** name of the file

***def has_dir***: 

Does a file exist on the remote?

**:param path:** path where file should exist

**:param file:** name of the file
:return boolean

***def remove***: 

Remove a file or directory on remote

**:param path:**path to file/dir to remove

**:param recursive:** adds a -r to the rm command

**:return:** boolean

***def move***: 

Perform a move operation

**:param src:** String

**:param dest:** String

***def copy***: 

Perform a copy operation

**:param src:** String

**:param dest:** String

***def set_rsa***: 

Put a rsa key on the remote

**:return:** None

***def cmd***: 

Runs a shell command on the remote

**:return:** session info

***def find***: 

Finds a file on the remote system returns a list of values

**:param path:** path where file should exist

**:param file:** name of the file

**:return:** output from the session

***def os_type***: 

Gets the os type of the system

**:return:** returns os string

***def onefs_version***: 

Get onefs os version

***def get_MD5***: 

gets the md5sum of a file
Supports Freebsd and Linux

**:return:** md5 string

***def _clean_MD5***: 

private Cleans the md5 string produced

**:param os_type:** type of operating system

**:param output:** string from get_MD5
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/terminal.py***

Created on Nov 18, 2015


**:author:** iitow


***def waitfor***: 

poll the child for input


**:param fd:** forked process

***def event***: 

find all output and inspect it for searches dict key & value


**:param fd:** forked process

**:param searches:** dictionary key value pair

***def set_rsa***: 

logs into system via ssh
and appends to authorized_keys using username password


**:param     host:** name over the server

**:param  rsa_pub:** absolute path to your id_rsa.pub

**:param     user:** host login creds

**:param password:** host login creds

**:param home_dir:** home directory for user

***def create_rsa_public***: 

generate a public key from the private key


**:param rsa_private:** path to private key

***def ssh***: 

Run a single ssh command on a remote server


**:param server:** username@servername

**:param cmd:** single command you wish to run

***def rsync***: 

Performs an rsync of files; requires ssh keys setup.


**:param   server:** username@server

**:param      src:** full path of src directory/file

**:param     dest:** full path to dest directory

**:param   option:** [pull] get file from a remote,
[push] put a file from your server into a remote

**:param   remote:** [True] assumes we are working with
a remote system, [False] assumes we are copying files locally

**:param excludes:** exclude directory, or file from array

**:note:** --delete will delete files on dest if it does not match src

***def sig_exception***: 

None

***def shell***: 

Run Shell commands  [Non Blocking, no Buffer, print live, log it]


**:param cmd:** String command

**:param verbose:**bool

**:param strict:**bool will exit based on code if enabled

**:return:**  {command, stdout, code} as dict

***def _exit_clean***: 

cleans .tmp_shell files before exit
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/http.py***

Created on Jun 2, 2015


**:author:** iitow


***class Restful***: 

Perform restful calls with this class
    

***def __init__***: 

Generic class to handle All types of
Restful requests

***def send***: 

send http restful requests

**:param type:** String, GET,PUT,POST,PATCH

**:param ext:** String, url extention

**:return:** Dictionary
**********************************************