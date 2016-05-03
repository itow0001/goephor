

file @ **/goephor.py**


file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

__def menu__
None
__def parse_envs__
None
__def main__
None

file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**
####class Run####

This is the entry point from the cli and runs drives componentsdef __init__
Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
__def read_config__
Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
__def _read_yaml__
Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
__def _read_json__
Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
__def add_envs__
Overrides environment variables from cli

__param **envs__  dictionary of environment variables
__def set_envs__
sets environment variables inside of manifest
__def load_actions__
loads actions in to chain resolves yaml/json to a object
__def execute_actions__
Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**
####class maker####

This class represents a receipt maker class
    def __init__
None
__def on_actions__
None
__def custom__
None

file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**
####class git####

This class Represents a call to git
    def __init__
None
__def clone__
None
__def delete__
None

file @ **/goephor/core/plugins/freebsd.py**
####class terminal####

Freebsd specific commands go here####class pkg####

Freebsd package commands go here####class jails####

Freebsd jail management commands go heredef __init__
None
__def jls__
None
__def jexec__
None
__def fetch__
Nonedef __init__
None
__def install__
Nonedef __init__
None

file @ **/goephor/core/plugins/pluginable.py**
####class DecoMeta####

None####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    
__def __new____
None
__def deco__
Nonedef __init__
None
__def wrapper__
None

file @ **/goephor/core/plugins/environment.py**
####class env####

This class Represents an example
    def __init__
None
__def set__
None

file @ **/goephor/core/plugins/system.py**
####class terminal####

General nix system commands go heredef __init__
None
__def shell__
None
__def rsync__
None

file @ **/goephor/core/plugins/remote.py**
####class ssh####

This class can perform ssh commandsdef __init__
None
__def cmd__
None

file @ **/goephor/core/plugins/example.py**
####class example####

This class Represents an example
    def __init__
None
__def runme__
None

file @ **/goephor/core/plugins/jumbler.py**

__def jexec__
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
__def jdestroy__
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

file @ **/goephor/core/plugins/http.py**
####class rest####

This class handles all rest actionsdef __init__
None
__def send__
None

file @ **/goephor/core/plugins/condition.py**
####class statement####

Nonedef __init__
None
__def add_obj__
None
__def IF__
None

file @ **/goephor/core/plugins/remotable.py**

__def _has_keys__
Collect all environment variables
@param str: command string
__def _sanitize__
Replace all environment variables into command
@param str: command string
__def cmd__
Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**
####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####

Object containing instructions to create and execute actionsdef __init__
Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
__def to_obj__
Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
__def add__
Append an action obj to chain

__param action_obj__  Obj
__def insert__
Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
__def get_index__
Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usagedef __init__
Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
__def __repr____
Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
__def set_ignore__
catch the ignore parameter and delete it in defaults
__def get_receipt__
return a dictionary of all Action info
__def pprint__
print state about the object pretty

__param title__  String
__param footer__  String
__def _init_instance__
Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
__def execute__
execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**
####class Repo_actions####

None####class Commit_actions####

This class handles all commit type actions
    ####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj####class Remote_actions####

This class handles all remote actions
    def __init__
Initialize Repo actions
        
__def _set_ssh_config__
This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
__def _set_dirs__
None
__def attach__
attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
__def _initial_commit__
To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
__def init__
Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
__def clone__
Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
__def untracked_files__
list all untracked files
@return: list of untracked filesdef __init__
None
__def commit__
Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
__def cherry_pick__
Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
__def diff_tree__
None
__def search_log__
None
__def add__
adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failuredef __init__
None
__def branch__
Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
__def branch_from__
Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
__def branch_is__
provides the current branch
@return: the current branch
__def branch_list__
provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
__def has_reference__
Search for reference
@param branch_name__ string of branch name
@return__  reference obj
__def has_head__
Search for branch head
@param branch_name__ string of branch name
@return__  head obj
__def checkout__
checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
__def push__
Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
__def remote_delete__
Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
__def delete__
Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: booleandef __init__
None
__def list__
None
__def has_remote__
None
__def add__
add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
__def fork_sync__
Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
__def fetch__
Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**
####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.def __init__
Constructor

__param debug__  Bool
__def set__
set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
__def get__
get an environment variable

__param key__  String
__def sanitize__
sanitizes environment variables in a given values

__param values__  List
__def _sanitize__
Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**
####class Run####

This class represents a remote machine
using SSH to perform all needed actionsdef __init__
Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
__def is_alive__
Pings the remote to make sure its a valid address
@return: boolean
__def is_alive_poll__
Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
__def is_writable__
Check to make sure the file system is writable
@return: boolean
__def is_writable_poll__
Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
__def has_access__
Does a key already exist on the remote?
@return: boolean
__def has_file__
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
__def has_dir__
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
__def remove__
Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
__def move__
Perform a move operation
        
__def copy__
Perform a copy operation
        
__def set_rsa__
Put a rsa key on the remote
@return: None
__def cmd__
Runs a shell command on the remote
@return: session info
__def find__
Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
__def os_type__
Gets the os type of the system
@return: returns os string
__def onefs_version__
None
__def get_MD5__
gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
__def _clean_MD5__
private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

__def waitfor__
poll the child for input

__param fd__  forked process
__def event__
find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
__def set_rsa__
logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
__def create_rsa_public__
generate a public key from the private key

__param rsa_private__  path to private key
__def ssh__
Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
__def rsync__
Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
__def shell__
Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
__def _exit_clean__
cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**
####class Restful####

Nonedef __init__
Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
__def send__
Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
__def post_multipart__
None

file @ **/goephor.py**


file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

__def menu__
None
__def parse_envs__
None
__def main__
None

file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**
####class Run####

This is the entry point from the cli and runs drives componentsdef __init__
Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
__def read_config__
Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
__def _read_yaml__
Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
__def _read_json__
Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
__def add_envs__
Overrides environment variables from cli

__param **envs__  dictionary of environment variables
__def set_envs__
sets environment variables inside of manifest
__def load_actions__
loads actions in to chain resolves yaml/json to a object
__def execute_actions__
Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**
####class maker####

This class represents a receipt maker class
    def __init__
None
__def on_actions__
None
__def custom__
None

file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**
####class git####

This class Represents a call to git
    def __init__
None
__def clone__
None
__def delete__
None

file @ **/goephor/core/plugins/freebsd.py**
####class terminal####

Freebsd specific commands go here####class pkg####

Freebsd package commands go here####class jails####

Freebsd jail management commands go heredef __init__
None
__def jls__
None
__def jexec__
None
__def fetch__
Nonedef __init__
None
__def install__
Nonedef __init__
None

file @ **/goephor/core/plugins/pluginable.py**
####class DecoMeta####

None####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    
__def __new____
None
__def deco__
Nonedef __init__
None
__def wrapper__
None

file @ **/goephor/core/plugins/environment.py**
####class env####

This class Represents an example
    def __init__
None
__def set__
None

file @ **/goephor/core/plugins/system.py**
####class terminal####

General nix system commands go heredef __init__
None
__def shell__
None
__def rsync__
None

file @ **/goephor/core/plugins/remote.py**
####class ssh####

This class can perform ssh commandsdef __init__
None
__def cmd__
None

file @ **/goephor/core/plugins/example.py**
####class example####

This class Represents an example
    def __init__
None
__def runme__
None

file @ **/goephor/core/plugins/jumbler.py**

__def jexec__
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
__def jdestroy__
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

file @ **/goephor/core/plugins/http.py**
####class rest####

This class handles all rest actionsdef __init__
None
__def send__
None

file @ **/goephor/core/plugins/condition.py**
####class statement####

Nonedef __init__
None
__def add_obj__
None
__def IF__
None

file @ **/goephor/core/plugins/remotable.py**

__def _has_keys__
Collect all environment variables
@param str: command string
__def _sanitize__
Replace all environment variables into command
@param str: command string
__def cmd__
Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**
####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####

Object containing instructions to create and execute actionsdef __init__
Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
__def to_obj__
Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
__def add__
Append an action obj to chain

__param action_obj__  Obj
__def insert__
Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
__def get_index__
Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usagedef __init__
Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
__def __repr____
Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
__def set_ignore__
catch the ignore parameter and delete it in defaults
__def get_receipt__
return a dictionary of all Action info
__def pprint__
print state about the object pretty

__param title__  String
__param footer__  String
__def _init_instance__
Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
__def execute__
execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**
####class Repo_actions####

None####class Commit_actions####

This class handles all commit type actions
    ####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj####class Remote_actions####

This class handles all remote actions
    def __init__
Initialize Repo actions
        
__def _set_ssh_config__
This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
__def _set_dirs__
None
__def attach__
attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
__def _initial_commit__
To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
__def init__
Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
__def clone__
Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
__def untracked_files__
list all untracked files
@return: list of untracked filesdef __init__
None
__def commit__
Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
__def cherry_pick__
Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
__def diff_tree__
None
__def search_log__
None
__def add__
adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failuredef __init__
None
__def branch__
Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
__def branch_from__
Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
__def branch_is__
provides the current branch
@return: the current branch
__def branch_list__
provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
__def has_reference__
Search for reference
@param branch_name__ string of branch name
@return__  reference obj
__def has_head__
Search for branch head
@param branch_name__ string of branch name
@return__  head obj
__def checkout__
checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
__def push__
Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
__def remote_delete__
Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
__def delete__
Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: booleandef __init__
None
__def list__
None
__def has_remote__
None
__def add__
add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
__def fork_sync__
Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
__def fetch__
Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**
####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.def __init__
Constructor

__param debug__  Bool
__def set__
set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
__def get__
get an environment variable

__param key__  String
__def sanitize__
sanitizes environment variables in a given values

__param values__  List
__def _sanitize__
Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**
####class Run####

This class represents a remote machine
using SSH to perform all needed actionsdef __init__
Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
__def is_alive__
Pings the remote to make sure its a valid address
@return: boolean
__def is_alive_poll__
Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
__def is_writable__
Check to make sure the file system is writable
@return: boolean
__def is_writable_poll__
Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
__def has_access__
Does a key already exist on the remote?
@return: boolean
__def has_file__
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
__def has_dir__
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
__def remove__
Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
__def move__
Perform a move operation
        
__def copy__
Perform a copy operation
        
__def set_rsa__
Put a rsa key on the remote
@return: None
__def cmd__
Runs a shell command on the remote
@return: session info
__def find__
Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
__def os_type__
Gets the os type of the system
@return: returns os string
__def onefs_version__
None
__def get_MD5__
gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
__def _clean_MD5__
private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

__def waitfor__
poll the child for input

__param fd__  forked process
__def event__
find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
__def set_rsa__
logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
__def create_rsa_public__
generate a public key from the private key

__param rsa_private__  path to private key
__def ssh__
Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
__def rsync__
Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
__def shell__
Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
__def _exit_clean__
cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**
####class Restful####

Nonedef __init__
Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
__def send__
Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
__def post_multipart__
None

file @ **/goephor.py**


file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**
def menu
Nonedef parse_envs
Nonedef main
None

file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**
####class Run####

This is the entry point from the cli and runs drives componentsdef __init__
Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug infodef read_config
Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dictdef _read_yaml
Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dictdef _read_json
Reads in the json config

__param config_file__  defines all actions in a build
__return__  dictdef add_envs
Overrides environment variables from cli

__param **envs__  dictionary of environment variablesdef set_envs
sets environment variables inside of manifestdef load_actions
loads actions in to chain resolves yaml/json to a objectdef execute_actions
Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**
####class maker####

This class represents a receipt maker class
    def __init__
Nonedef on_actions
Nonedef custom
None

file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**
####class git####

This class Represents a call to git
    def __init__
Nonedef clone
Nonedef delete
None

file @ **/goephor/core/plugins/freebsd.py**
####class terminal####

Freebsd specific commands go here####class pkg####

Freebsd package commands go here####class jails####

Freebsd jail management commands go heredef __init__
Nonedef jls
Nonedef jexec
Nonedef fetch
Nonedef __init__
Nonedef install
Nonedef __init__
None

file @ **/goephor/core/plugins/pluginable.py**
####class DecoMeta####

None####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    def __new__
Nonedef deco
Nonedef __init__
Nonedef wrapper
None

file @ **/goephor/core/plugins/environment.py**
####class env####

This class Represents an example
    def __init__
Nonedef set
None

file @ **/goephor/core/plugins/system.py**
####class terminal####

General nix system commands go heredef __init__
Nonedef shell
Nonedef rsync
None

file @ **/goephor/core/plugins/remote.py**
####class ssh####

This class can perform ssh commandsdef __init__
Nonedef cmd
None

file @ **/goephor/core/plugins/example.py**
####class example####

This class Represents an example
    def __init__
Nonedef runme
None

file @ **/goephor/core/plugins/jumbler.py**
def jexec
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dictdef jdestroy
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

file @ **/goephor/core/plugins/http.py**
####class rest####

This class handles all rest actionsdef __init__
Nonedef send
None

file @ **/goephor/core/plugins/condition.py**
####class statement####

Nonedef __init__
Nonedef add_obj
Nonedef IF
None

file @ **/goephor/core/plugins/remotable.py**
def _has_keys
Collect all environment variables
@param str: command stringdef _sanitize
Replace all environment variables into command
@param str: command stringdef cmd
Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**
####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####

Object containing instructions to create and execute actionsdef __init__
Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debugdef to_obj
Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.def add
Append an action obj to chain

__param action_obj__  Objdef insert
Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Objdef get_index
Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usagedef __init__
Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Objdef __repr__
Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)def set_ignore
catch the ignore parameter and delete it in defaultsdef get_receipt
return a dictionary of all Action infodef pprint
print state about the object pretty

__param title__  String
__param footer__  Stringdef _init_instance
Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.def execute
execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**
####class Repo_actions####

None####class Commit_actions####

This class handles all commit type actions
    ####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj####class Remote_actions####

This class handles all remote actions
    def __init__
Initialize Repo actions
        def _set_ssh_config
This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com def _set_dirs
Nonedef attach
attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure def _initial_commit
To fully init an empty repo you need an initial commit, which in this case
is an empty README.mddef init
Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.gitdef clone
Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure def untracked_files
list all untracked files
@return: list of untracked filesdef __init__
Nonedef commit
Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failuredef cherry_pick
Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False def diff_tree
Nonedef search_log
Nonedef add
adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failuredef __init__
Nonedef branch
Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  def branch_from
Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch namedef branch_is
provides the current branch
@return: the current branchdef branch_list
provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects def has_reference
Search for reference
@param branch_name__ string of branch name
@return__  reference objdef has_head
Search for branch head
@param branch_name__ string of branch name
@return__  head objdef checkout
checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  def push
Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: booleandef remote_delete
Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: booleandef delete
Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: booleandef __init__
Nonedef list
Nonedef has_remote
Nonedef add
add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False def fork_sync
Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False def fetch
Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**
####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.def __init__
Constructor

__param debug__  Booldef set
set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env valuedef get
get an environment variable

__param key__  Stringdef sanitize
sanitizes environment variables in a given values

__param values__  Listdef _sanitize
Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**
####class Run####

This class represents a remote machine
using SSH to perform all needed actionsdef __init__
Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote serverdef is_alive
Pings the remote to make sure its a valid address
@return: booleandef is_alive_poll
Polls for a ping
@param timeout__ default 30 seconds
@return__  booleandef is_writable
Check to make sure the file system is writable
@return: booleandef is_writable_poll
Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  booleandef has_access
Does a key already exist on the remote?
@return: booleandef has_file
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the filedef has_dir
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return booleandef remove
Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: booleandef move
Perform a move operation
        def copy
Perform a copy operation
        def set_rsa
Put a rsa key on the remote
@return: Nonedef cmd
Runs a shell command on the remote
@return: session infodef find
Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the sessiondef os_type
Gets the os type of the system
@return: returns os stringdef onefs_version
Nonedef get_MD5
gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 stringdef _clean_MD5
private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**
def waitfor
poll the child for input

__param fd__  forked processdef event
find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pairdef set_rsa
logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for userdef create_rsa_public
generate a public key from the private key

__param rsa_private__  path to private keydef ssh
Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to rundef rsync
Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match srcdef shell
Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dictdef _exit_clean
cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**
####class Restful####

Nonedef __init__
Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>def send
Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit codedef post_multipart
None

file @ **/goephor.py**


file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**
def menu
Nonedef parse_envs
Nonedef main
None

file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**
####class Run####

This is the entry point from the cli and runs drives componentsdef __init__
Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug infodef read_config
Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dictdef _read_yaml
Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dictdef _read_json
Reads in the json config

__param config_file__  defines all actions in a build
__return__  dictdef add_envs
Overrides environment variables from cli

__param **envs__  dictionary of environment variablesdef set_envs
sets environment variables inside of manifestdef load_actions
loads actions in to chain resolves yaml/json to a objectdef execute_actions
Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**
####class maker####

This class represents a receipt maker class
    def __init__
Nonedef on_actions
Nonedef custom
None

file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**
####class git####

This class Represents a call to git
    def __init__
Nonedef clone
Nonedef delete
None

file @ **/goephor/core/plugins/freebsd.py**
####class terminal####

Freebsd specific commands go here####class pkg####

Freebsd package commands go here####class jails####

Freebsd jail management commands go heredef __init__
Nonedef jls
Nonedef jexec
Nonedef fetch
Nonedef __init__
Nonedef install
Nonedef __init__
None

file @ **/goephor/core/plugins/pluginable.py**
####class DecoMeta####

None####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    def __new__
Nonedef deco
Nonedef __init__
Nonedef wrapper
None

file @ **/goephor/core/plugins/environment.py**
####class env####

This class Represents an example
    def __init__
Nonedef set
None

file @ **/goephor/core/plugins/system.py**
####class terminal####

General nix system commands go heredef __init__
Nonedef shell
Nonedef rsync
None

file @ **/goephor/core/plugins/remote.py**
####class ssh####

This class can perform ssh commandsdef __init__
Nonedef cmd
None

file @ **/goephor/core/plugins/example.py**
####class example####

This class Represents an example
    def __init__
Nonedef runme
None

file @ **/goephor/core/plugins/jumbler.py**
def jexec
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dictdef jdestroy
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

file @ **/goephor/core/plugins/http.py**
####class rest####

This class handles all rest actionsdef __init__
Nonedef send
None

file @ **/goephor/core/plugins/condition.py**
####class statement####

Nonedef __init__
Nonedef add_obj
Nonedef IF
None

file @ **/goephor/core/plugins/remotable.py**
def _has_keys
Collect all environment variables
@param str: command stringdef _sanitize
Replace all environment variables into command
@param str: command stringdef cmd
Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**
####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####

Object containing instructions to create and execute actionsdef __init__
Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debugdef to_obj
Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.def add
Append an action obj to chain

__param action_obj__  Objdef insert
Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Objdef get_index
Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usagedef __init__
Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Objdef __repr__
Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)def set_ignore
catch the ignore parameter and delete it in defaultsdef get_receipt
return a dictionary of all Action infodef pprint
print state about the object pretty

__param title__  String
__param footer__  Stringdef _init_instance
Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.def execute
execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**
####class Repo_actions####

None####class Commit_actions####

This class handles all commit type actions
    ####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj####class Remote_actions####

This class handles all remote actions
    def __init__
Initialize Repo actions
        def _set_ssh_config
This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com def _set_dirs
Nonedef attach
attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure def _initial_commit
To fully init an empty repo you need an initial commit, which in this case
is an empty README.mddef init
Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.gitdef clone
Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure def untracked_files
list all untracked files
@return: list of untracked filesdef __init__
Nonedef commit
Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failuredef cherry_pick
Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False def diff_tree
Nonedef search_log
Nonedef add
adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failuredef __init__
Nonedef branch
Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  def branch_from
Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch namedef branch_is
provides the current branch
@return: the current branchdef branch_list
provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects def has_reference
Search for reference
@param branch_name__ string of branch name
@return__  reference objdef has_head
Search for branch head
@param branch_name__ string of branch name
@return__  head objdef checkout
checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  def push
Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: booleandef remote_delete
Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: booleandef delete
Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: booleandef __init__
Nonedef list
Nonedef has_remote
Nonedef add
add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False def fork_sync
Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False def fetch
Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**
####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.def __init__
Constructor

__param debug__  Booldef set
set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env valuedef get
get an environment variable

__param key__  Stringdef sanitize
sanitizes environment variables in a given values

__param values__  Listdef _sanitize
Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**
####class Run####

This class represents a remote machine
using SSH to perform all needed actionsdef __init__
Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote serverdef is_alive
Pings the remote to make sure its a valid address
@return: booleandef is_alive_poll
Polls for a ping
@param timeout__ default 30 seconds
@return__  booleandef is_writable
Check to make sure the file system is writable
@return: booleandef is_writable_poll
Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  booleandef has_access
Does a key already exist on the remote?
@return: booleandef has_file
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the filedef has_dir
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return booleandef remove
Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: booleandef move
Perform a move operation
        def copy
Perform a copy operation
        def set_rsa
Put a rsa key on the remote
@return: Nonedef cmd
Runs a shell command on the remote
@return: session infodef find
Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the sessiondef os_type
Gets the os type of the system
@return: returns os stringdef onefs_version
Nonedef get_MD5
gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 stringdef _clean_MD5
private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**
def waitfor
poll the child for input

__param fd__  forked processdef event
find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pairdef set_rsa
logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for userdef create_rsa_public
generate a public key from the private key

__param rsa_private__  path to private keydef ssh
Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to rundef rsync
Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match srcdef shell
Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dictdef _exit_clean
cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**
####class Restful####

Nonedef __init__
Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>def send
Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit codedef post_multipart
None

file @ **/goephor.py**


file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

def menu
None
def parse_envs
None
def main
None

file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**
####class Run####

This is the entry point from the cli and runs drives components
def __init__
Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
def read_config
Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
def _read_yaml
Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
def _read_json
Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
def add_envs
Overrides environment variables from cli

__param **envs__  dictionary of environment variables
def set_envs
sets environment variables inside of manifest
def load_actions
loads actions in to chain resolves yaml/json to a object
def execute_actions
Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**
####class maker####

This class represents a receipt maker class
    
def __init__
None
def on_actions
None
def custom
None

file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**
####class git####

This class Represents a call to git
    
def __init__
None
def clone
None
def delete
None

file @ **/goephor/core/plugins/freebsd.py**
####class terminal####

Freebsd specific commands go here####class pkg####

Freebsd package commands go here####class jails####

Freebsd jail management commands go here
def __init__
None
def jls
None
def jexec
None
def fetch
None
def __init__
None
def install
None
def __init__
None

file @ **/goephor/core/plugins/pluginable.py**
####class DecoMeta####

None####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    
def __new__
None
def deco
None
def __init__
None
def wrapper
None

file @ **/goephor/core/plugins/environment.py**
####class env####

This class Represents an example
    
def __init__
None
def set
None

file @ **/goephor/core/plugins/system.py**
####class terminal####

General nix system commands go here
def __init__
None
def shell
None
def rsync
None

file @ **/goephor/core/plugins/remote.py**
####class ssh####

This class can perform ssh commands
def __init__
None
def cmd
None

file @ **/goephor/core/plugins/example.py**
####class example####

This class Represents an example
    
def __init__
None
def runme
None

file @ **/goephor/core/plugins/jumbler.py**

def jexec
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
def jdestroy
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

file @ **/goephor/core/plugins/http.py**
####class rest####

This class handles all rest actions
def __init__
None
def send
None

file @ **/goephor/core/plugins/condition.py**
####class statement####

None
def __init__
None
def add_obj
None
def IF
None

file @ **/goephor/core/plugins/remotable.py**

def _has_keys
Collect all environment variables
@param str: command string
def _sanitize
Replace all environment variables into command
@param str: command string
def cmd
Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**
####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####

Object containing instructions to create and execute actions
def __init__
Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
def to_obj
Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
def add
Append an action obj to chain

__param action_obj__  Obj
def insert
Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
def get_index
Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage
def __init__
Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
def __repr__
Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
def set_ignore
catch the ignore parameter and delete it in defaults
def get_receipt
return a dictionary of all Action info
def pprint
print state about the object pretty

__param title__  String
__param footer__  String
def _init_instance
Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
def execute
execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**
####class Repo_actions####

None####class Commit_actions####

This class handles all commit type actions
    ####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj####class Remote_actions####

This class handles all remote actions
    
def __init__
Initialize Repo actions
        
def _set_ssh_config
This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
def _set_dirs
None
def attach
attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
def _initial_commit
To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
def init
Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
def clone
Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
def untracked_files
list all untracked files
@return: list of untracked files
def __init__
None
def commit
Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
def cherry_pick
Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
def diff_tree
None
def search_log
None
def add
adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure
def __init__
None
def branch
Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
def branch_from
Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
def branch_is
provides the current branch
@return: the current branch
def branch_list
provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
def has_reference
Search for reference
@param branch_name__ string of branch name
@return__  reference obj
def has_head
Search for branch head
@param branch_name__ string of branch name
@return__  head obj
def checkout
checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
def push
Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def remote_delete
Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def delete
Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def __init__
None
def list
None
def has_remote
None
def add
add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
def fork_sync
Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
def fetch
Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**
####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.
def __init__
Constructor

__param debug__  Bool
def set
set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
def get
get an environment variable

__param key__  String
def sanitize
sanitizes environment variables in a given values

__param values__  List
def _sanitize
Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**
####class Run####

This class represents a remote machine
using SSH to perform all needed actions
def __init__
Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
def is_alive
Pings the remote to make sure its a valid address
@return: boolean
def is_alive_poll
Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
def is_writable
Check to make sure the file system is writable
@return: boolean
def is_writable_poll
Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
def has_access
Does a key already exist on the remote?
@return: boolean
def has_file
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
def has_dir
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
def remove
Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
def move
Perform a move operation
        
def copy
Perform a copy operation
        
def set_rsa
Put a rsa key on the remote
@return: None
def cmd
Runs a shell command on the remote
@return: session info
def find
Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
def os_type
Gets the os type of the system
@return: returns os string
def onefs_version
None
def get_MD5
gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
def _clean_MD5
private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

def waitfor
poll the child for input

__param fd__  forked process
def event
find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
def set_rsa
logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
def create_rsa_public
generate a public key from the private key

__param rsa_private__  path to private key
def ssh
Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
def rsync
Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
def shell
Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
def _exit_clean
cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**
####class Restful####

None
def __init__
Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
def send
Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
def post_multipart
None

file @ **/goephor.py**


file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

def menu
None
def parse_envs
None
def main
None

file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**
####class Run####

This is the entry point from the cli and runs drives components
def __init__
Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
def read_config
Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
def _read_yaml
Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
def _read_json
Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
def add_envs
Overrides environment variables from cli

__param **envs__  dictionary of environment variables
def set_envs
sets environment variables inside of manifest
def load_actions
loads actions in to chain resolves yaml/json to a object
def execute_actions
Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**
####class maker####

This class represents a receipt maker class
    
def __init__
None
def on_actions
None
def custom
None

file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**
####class git####

This class Represents a call to git
    
def __init__
None
def clone
None
def delete
None

file @ **/goephor/core/plugins/freebsd.py**
####class terminal####

Freebsd specific commands go here####class pkg####

Freebsd package commands go here####class jails####

Freebsd jail management commands go here
def __init__
None
def jls
None
def jexec
None
def fetch
None
def __init__
None
def install
None
def __init__
None

file @ **/goephor/core/plugins/pluginable.py**
####class DecoMeta####

None####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    
def __new__
None
def deco
None
def __init__
None
def wrapper
None

file @ **/goephor/core/plugins/environment.py**
####class env####

This class Represents an example
    
def __init__
None
def set
None

file @ **/goephor/core/plugins/system.py**
####class terminal####

General nix system commands go here
def __init__
None
def shell
None
def rsync
None

file @ **/goephor/core/plugins/remote.py**
####class ssh####

This class can perform ssh commands
def __init__
None
def cmd
None

file @ **/goephor/core/plugins/example.py**
####class example####

This class Represents an example
    
def __init__
None
def runme
None

file @ **/goephor/core/plugins/jumbler.py**

def jexec
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
def jdestroy
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

file @ **/goephor/core/plugins/http.py**
####class rest####

This class handles all rest actions
def __init__
None
def send
None

file @ **/goephor/core/plugins/condition.py**
####class statement####

None
def __init__
None
def add_obj
None
def IF
None

file @ **/goephor/core/plugins/remotable.py**

def _has_keys
Collect all environment variables
@param str: command string
def _sanitize
Replace all environment variables into command
@param str: command string
def cmd
Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**
####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####

Object containing instructions to create and execute actions
def __init__
Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
def to_obj
Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
def add
Append an action obj to chain

__param action_obj__  Obj
def insert
Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
def get_index
Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage
def __init__
Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
def __repr__
Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
def set_ignore
catch the ignore parameter and delete it in defaults
def get_receipt
return a dictionary of all Action info
def pprint
print state about the object pretty

__param title__  String
__param footer__  String
def _init_instance
Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
def execute
execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**
####class Repo_actions####

None####class Commit_actions####

This class handles all commit type actions
    ####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj####class Remote_actions####

This class handles all remote actions
    
def __init__
Initialize Repo actions
        
def _set_ssh_config
This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
def _set_dirs
None
def attach
attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
def _initial_commit
To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
def init
Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
def clone
Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
def untracked_files
list all untracked files
@return: list of untracked files
def __init__
None
def commit
Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
def cherry_pick
Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
def diff_tree
None
def search_log
None
def add
adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure
def __init__
None
def branch
Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
def branch_from
Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
def branch_is
provides the current branch
@return: the current branch
def branch_list
provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
def has_reference
Search for reference
@param branch_name__ string of branch name
@return__  reference obj
def has_head
Search for branch head
@param branch_name__ string of branch name
@return__  head obj
def checkout
checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
def push
Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def remote_delete
Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def delete
Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def __init__
None
def list
None
def has_remote
None
def add
add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
def fork_sync
Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
def fetch
Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**
####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.
def __init__
Constructor

__param debug__  Bool
def set
set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
def get
get an environment variable

__param key__  String
def sanitize
sanitizes environment variables in a given values

__param values__  List
def _sanitize
Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**
####class Run####

This class represents a remote machine
using SSH to perform all needed actions
def __init__
Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
def is_alive
Pings the remote to make sure its a valid address
@return: boolean
def is_alive_poll
Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
def is_writable
Check to make sure the file system is writable
@return: boolean
def is_writable_poll
Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
def has_access
Does a key already exist on the remote?
@return: boolean
def has_file
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
def has_dir
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
def remove
Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
def move
Perform a move operation
        
def copy
Perform a copy operation
        
def set_rsa
Put a rsa key on the remote
@return: None
def cmd
Runs a shell command on the remote
@return: session info
def find
Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
def os_type
Gets the os type of the system
@return: returns os string
def onefs_version
None
def get_MD5
gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
def _clean_MD5
private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

def waitfor
poll the child for input

__param fd__  forked process
def event
find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
def set_rsa
logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
def create_rsa_public
generate a public key from the private key

__param rsa_private__  path to private key
def ssh
Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
def rsync
Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
def shell
Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
def _exit_clean
cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**
####class Restful####

None
def __init__
Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
def send
Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
def post_multipart
None
def menu
None
def parse_envs
None
def main
None####class Run####
file @ **/goephor/core/Chain.py**


This is the entry point from the cli and runs drives components
def __init__
Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
def read_config
Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
def _read_yaml
Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
def _read_json
Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
def add_envs
Overrides environment variables from cli

__param **envs__  dictionary of environment variables
def set_envs
sets environment variables inside of manifest
def load_actions
loads actions in to chain resolves yaml/json to a object
def execute_actions
Executes all action objects
        ####class maker####
file @ **/goephor/core/plugins/receipt.py**


This class represents a receipt maker class
    
def __init__
None
def on_actions
None
def custom
None####class git####
file @ **/goephor/core/plugins/scm.py**


This class Represents a call to git
    
def __init__
None
def clone
None
def delete
None####class terminal####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd specific commands go here####class pkg####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd package commands go here####class jails####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd jail management commands go here
def __init__
None
def jls
None
def jexec
None
def fetch
None
def __init__
None
def install
None
def __init__
None####class DecoMeta####
file @ **/goephor/core/plugins/pluginable.py**


None####class Plugin####
file @ **/goephor/core/plugins/pluginable.py**


This is the base class for plugin which all plugins must inherit from.
    
def __new__
None
def deco
None
def __init__
None
def wrapper
None####class env####
file @ **/goephor/core/plugins/environment.py**


This class Represents an example
    
def __init__
None
def set
None####class terminal####
file @ **/goephor/core/plugins/system.py**


General nix system commands go here
def __init__
None
def shell
None
def rsync
None####class ssh####
file @ **/goephor/core/plugins/remote.py**


This class can perform ssh commands
def __init__
None
def cmd
None####class example####
file @ **/goephor/core/plugins/example.py**


This class Represents an example
    
def __init__
None
def runme
None
def jexec
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
def jdestroy
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict####class rest####
file @ **/goephor/core/plugins/http.py**


This class handles all rest actions
def __init__
None
def send
None####class statement####
file @ **/goephor/core/plugins/condition.py**


None
def __init__
None
def add_obj
None
def IF
None
def _has_keys
Collect all environment variables
@param str: command string
def _sanitize
Replace all environment variables into command
@param str: command string
def cmd
Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh####class Manager####
file @ **/goephor/core/plugins/modules/action.py**


This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####
file @ **/goephor/core/plugins/modules/action.py**


Object containing instructions to create and execute actions
def __init__
Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
def to_obj
Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
def add
Append an action obj to chain

__param action_obj__  Obj
def insert
Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
def get_index
Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage
def __init__
Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
def __repr__
Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
def set_ignore
catch the ignore parameter and delete it in defaults
def get_receipt
return a dictionary of all Action info
def pprint
print state about the object pretty

__param title__  String
__param footer__  String
def _init_instance
Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
def execute
execute the instruction
        ####class Repo_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


None####class Commit_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all commit type actions
    ####class Branch_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all branch related actions
@requires: Repo obj####class Remote_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all remote actions
    
def __init__
Initialize Repo actions
        
def _set_ssh_config
This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
def _set_dirs
None
def attach
attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
def _initial_commit
To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
def init
Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
def clone
Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
def untracked_files
list all untracked files
@return: list of untracked files
def __init__
None
def commit
Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
def cherry_pick
Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
def diff_tree
None
def search_log
None
def add
adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure
def __init__
None
def branch
Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
def branch_from
Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
def branch_is
provides the current branch
@return: the current branch
def branch_list
provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
def has_reference
Search for reference
@param branch_name__ string of branch name
@return__  reference obj
def has_head
Search for branch head
@param branch_name__ string of branch name
@return__  head obj
def checkout
checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
def push
Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def remote_delete
Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def delete
Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def __init__
None
def list
None
def has_remote
None
def add
add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
def fork_sync
Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
def fetch
Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  ####class EnvManager####
file @ **/goephor/core/plugins/modules/environment.py**


Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.
def __init__
Constructor

__param debug__  Bool
def set
set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
def get
get an environment variable

__param key__  String
def sanitize
sanitizes environment variables in a given values

__param values__  List
def _sanitize
Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all####class Run####
file @ **/goephor/core/plugins/modules/remote.py**


This class represents a remote machine
using SSH to perform all needed actions
def __init__
Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
def is_alive
Pings the remote to make sure its a valid address
@return: boolean
def is_alive_poll
Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
def is_writable
Check to make sure the file system is writable
@return: boolean
def is_writable_poll
Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
def has_access
Does a key already exist on the remote?
@return: boolean
def has_file
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
def has_dir
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
def remove
Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
def move
Perform a move operation
        
def copy
Perform a copy operation
        
def set_rsa
Put a rsa key on the remote
@return: None
def cmd
Runs a shell command on the remote
@return: session info
def find
Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
def os_type
Gets the os type of the system
@return: returns os string
def onefs_version
None
def get_MD5
gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
def _clean_MD5
private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5
def waitfor
poll the child for input

__param fd__  forked process
def event
find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
def set_rsa
logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
def create_rsa_public
generate a public key from the private key

__param rsa_private__  path to private key
def ssh
Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
def rsync
Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
def shell
Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
def _exit_clean
cleans .tmp_shell files before exit####class Restful####
file @ **/goephor/core/plugins/modules/http.py**


None
def __init__
Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
def send
Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
def post_multipart
None
def menu
None
def parse_envs
None
def main
None####class Run####
file @ **/goephor/core/Chain.py**


This is the entry point from the cli and runs drives components
def __init__
Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
def read_config
Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
def _read_yaml
Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
def _read_json
Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
def add_envs
Overrides environment variables from cli

__param **envs__  dictionary of environment variables
def set_envs
sets environment variables inside of manifest
def load_actions
loads actions in to chain resolves yaml/json to a object
def execute_actions
Executes all action objects
        ####class maker####
file @ **/goephor/core/plugins/receipt.py**


This class represents a receipt maker class
    
def __init__
None
def on_actions
None
def custom
None####class git####
file @ **/goephor/core/plugins/scm.py**


This class Represents a call to git
    
def __init__
None
def clone
None
def delete
None####class terminal####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd specific commands go here####class pkg####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd package commands go here####class jails####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd jail management commands go here
def __init__
None
def jls
None
def jexec
None
def fetch
None
def __init__
None
def install
None
def __init__
None####class DecoMeta####
file @ **/goephor/core/plugins/pluginable.py**


None####class Plugin####
file @ **/goephor/core/plugins/pluginable.py**


This is the base class for plugin which all plugins must inherit from.
    
def __new__
None
def deco
None
def __init__
None
def wrapper
None####class env####
file @ **/goephor/core/plugins/environment.py**


This class Represents an example
    
def __init__
None
def set
None####class terminal####
file @ **/goephor/core/plugins/system.py**


General nix system commands go here
def __init__
None
def shell
None
def rsync
None####class ssh####
file @ **/goephor/core/plugins/remote.py**


This class can perform ssh commands
def __init__
None
def cmd
None####class example####
file @ **/goephor/core/plugins/example.py**


This class Represents an example
    
def __init__
None
def runme
None
def jexec
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
def jdestroy
Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict####class rest####
file @ **/goephor/core/plugins/http.py**


This class handles all rest actions
def __init__
None
def send
None####class statement####
file @ **/goephor/core/plugins/condition.py**


None
def __init__
None
def add_obj
None
def IF
None
def _has_keys
Collect all environment variables
@param str: command string
def _sanitize
Replace all environment variables into command
@param str: command string
def cmd
Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh####class Manager####
file @ **/goephor/core/plugins/modules/action.py**


This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####
file @ **/goephor/core/plugins/modules/action.py**


Object containing instructions to create and execute actions
def __init__
Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
def to_obj
Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
def add
Append an action obj to chain

__param action_obj__  Obj
def insert
Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
def get_index
Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage
def __init__
Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
def __repr__
Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
def set_ignore
catch the ignore parameter and delete it in defaults
def get_receipt
return a dictionary of all Action info
def pprint
print state about the object pretty

__param title__  String
__param footer__  String
def _init_instance
Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
def execute
execute the instruction
        ####class Repo_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


None####class Commit_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all commit type actions
    ####class Branch_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all branch related actions
@requires: Repo obj####class Remote_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all remote actions
    
def __init__
Initialize Repo actions
        
def _set_ssh_config
This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
def _set_dirs
None
def attach
attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
def _initial_commit
To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
def init
Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
def clone
Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
def untracked_files
list all untracked files
@return: list of untracked files
def __init__
None
def commit
Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
def cherry_pick
Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
def diff_tree
None
def search_log
None
def add
adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure
def __init__
None
def branch
Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
def branch_from
Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
def branch_is
provides the current branch
@return: the current branch
def branch_list
provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
def has_reference
Search for reference
@param branch_name__ string of branch name
@return__  reference obj
def has_head
Search for branch head
@param branch_name__ string of branch name
@return__  head obj
def checkout
checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
def push
Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def remote_delete
Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def delete
Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
def __init__
None
def list
None
def has_remote
None
def add
add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
def fork_sync
Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
def fetch
Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  ####class EnvManager####
file @ **/goephor/core/plugins/modules/environment.py**


Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.
def __init__
Constructor

__param debug__  Bool
def set
set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
def get
get an environment variable

__param key__  String
def sanitize
sanitizes environment variables in a given values

__param values__  List
def _sanitize
Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all####class Run####
file @ **/goephor/core/plugins/modules/remote.py**


This class represents a remote machine
using SSH to perform all needed actions
def __init__
Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
def is_alive
Pings the remote to make sure its a valid address
@return: boolean
def is_alive_poll
Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
def is_writable
Check to make sure the file system is writable
@return: boolean
def is_writable_poll
Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
def has_access
Does a key already exist on the remote?
@return: boolean
def has_file
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
def has_dir
Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
def remove
Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
def move
Perform a move operation
        
def copy
Perform a copy operation
        
def set_rsa
Put a rsa key on the remote
@return: None
def cmd
Runs a shell command on the remote
@return: session info
def find
Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
def os_type
Gets the os type of the system
@return: returns os string
def onefs_version
None
def get_MD5
gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
def _clean_MD5
private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5
def waitfor
poll the child for input

__param fd__  forked process
def event
find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
def set_rsa
logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
def create_rsa_public
generate a public key from the private key

__param rsa_private__  path to private key
def ssh
Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
def rsync
Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
def shell
Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
def _exit_clean
cleans .tmp_shell files before exit####class Restful####
file @ **/goephor/core/plugins/modules/http.py**


None
def __init__
Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
def send
Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
def post_multipart
None
   def menu
      None
   def parse_envs
      None
   def main
      None####class Run####
file @ **/goephor/core/Chain.py**


This is the entry point from the cli and runs drives components
   def __init__
      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
   def read_config
      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
   def _read_yaml
      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
   def _read_json
      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
   def add_envs
      Overrides environment variables from cli

__param **envs__  dictionary of environment variables
   def set_envs
      sets environment variables inside of manifest
   def load_actions
      loads actions in to chain resolves yaml/json to a object
   def execute_actions
      Executes all action objects
        ####class maker####
file @ **/goephor/core/plugins/receipt.py**


This class represents a receipt maker class
    
   def __init__
      None
   def on_actions
      None
   def custom
      None####class git####
file @ **/goephor/core/plugins/scm.py**


This class Represents a call to git
    
   def __init__
      None
   def clone
      None
   def delete
      None####class terminal####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd specific commands go here####class pkg####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd package commands go here####class jails####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd jail management commands go here
   def __init__
      None
   def jls
      None
   def jexec
      None
   def fetch
      None
   def __init__
      None
   def install
      None
   def __init__
      None####class DecoMeta####
file @ **/goephor/core/plugins/pluginable.py**


None####class Plugin####
file @ **/goephor/core/plugins/pluginable.py**


This is the base class for plugin which all plugins must inherit from.
    
   def __new__
      None
   def deco
      None
   def __init__
      None
   def wrapper
      None####class env####
file @ **/goephor/core/plugins/environment.py**


This class Represents an example
    
   def __init__
      None
   def set
      None####class terminal####
file @ **/goephor/core/plugins/system.py**


General nix system commands go here
   def __init__
      None
   def shell
      None
   def rsync
      None####class ssh####
file @ **/goephor/core/plugins/remote.py**


This class can perform ssh commands
   def __init__
      None
   def cmd
      None####class example####
file @ **/goephor/core/plugins/example.py**


This class Represents an example
    
   def __init__
      None
   def runme
      None
   def jexec
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
   def jdestroy
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict####class rest####
file @ **/goephor/core/plugins/http.py**


This class handles all rest actions
   def __init__
      None
   def send
      None####class statement####
file @ **/goephor/core/plugins/condition.py**


None
   def __init__
      None
   def add_obj
      None
   def IF
      None
   def _has_keys
      Collect all environment variables
@param str: command string
   def _sanitize
      Replace all environment variables into command
@param str: command string
   def cmd
      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh####class Manager####
file @ **/goephor/core/plugins/modules/action.py**


This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####
file @ **/goephor/core/plugins/modules/action.py**


Object containing instructions to create and execute actions
   def __init__
      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
   def to_obj
      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
   def add
      Append an action obj to chain

__param action_obj__  Obj
   def insert
      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
   def get_index
      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage
   def __init__
      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
   def __repr__
      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
   def set_ignore
      catch the ignore parameter and delete it in defaults
   def get_receipt
      return a dictionary of all Action info
   def pprint
      print state about the object pretty

__param title__  String
__param footer__  String
   def _init_instance
      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
   def execute
      execute the instruction
        ####class Repo_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


None####class Commit_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all commit type actions
    ####class Branch_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all branch related actions
@requires: Repo obj####class Remote_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all remote actions
    
   def __init__
      Initialize Repo actions
        
   def _set_ssh_config
      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
   def _set_dirs
      None
   def attach
      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
   def _initial_commit
      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
   def init
      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
   def clone
      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
   def untracked_files
      list all untracked files
@return: list of untracked files
   def __init__
      None
   def commit
      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
   def cherry_pick
      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
   def diff_tree
      None
   def search_log
      None
   def add
      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure
   def __init__
      None
   def branch
      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
   def branch_from
      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
   def branch_is
      provides the current branch
@return: the current branch
   def branch_list
      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
   def has_reference
      Search for reference
@param branch_name__ string of branch name
@return__  reference obj
   def has_head
      Search for branch head
@param branch_name__ string of branch name
@return__  head obj
   def checkout
      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
   def push
      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def remote_delete
      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def delete
      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def __init__
      None
   def list
      None
   def has_remote
      None
   def add
      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
   def fork_sync
      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
   def fetch
      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  ####class EnvManager####
file @ **/goephor/core/plugins/modules/environment.py**


Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.
   def __init__
      Constructor

__param debug__  Bool
   def set
      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
   def get
      get an environment variable

__param key__  String
   def sanitize
      sanitizes environment variables in a given values

__param values__  List
   def _sanitize
      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all####class Run####
file @ **/goephor/core/plugins/modules/remote.py**


This class represents a remote machine
using SSH to perform all needed actions
   def __init__
      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
   def is_alive
      Pings the remote to make sure its a valid address
@return: boolean
   def is_alive_poll
      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
   def is_writable
      Check to make sure the file system is writable
@return: boolean
   def is_writable_poll
      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
   def has_access
      Does a key already exist on the remote?
@return: boolean
   def has_file
      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
   def has_dir
      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
   def remove
      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
   def move
      Perform a move operation
        
   def copy
      Perform a copy operation
        
   def set_rsa
      Put a rsa key on the remote
@return: None
   def cmd
      Runs a shell command on the remote
@return: session info
   def find
      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
   def os_type
      Gets the os type of the system
@return: returns os string
   def onefs_version
      None
   def get_MD5
      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
   def _clean_MD5
      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5
   def waitfor
      poll the child for input

__param fd__  forked process
   def event
      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
   def set_rsa
      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
   def create_rsa_public
      generate a public key from the private key

__param rsa_private__  path to private key
   def ssh
      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
   def rsync
      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
   def shell
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
   def _exit_clean
      cleans .tmp_shell files before exit####class Restful####
file @ **/goephor/core/plugins/modules/http.py**


None
   def __init__
      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
   def send
      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
   def post_multipart
      None
   def menu
      None
   def parse_envs
      None
   def main
      None####class Run####
file @ **/goephor/core/Chain.py**


This is the entry point from the cli and runs drives components
   def __init__
      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
   def read_config
      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
   def _read_yaml
      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
   def _read_json
      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
   def add_envs
      Overrides environment variables from cli

__param **envs__  dictionary of environment variables
   def set_envs
      sets environment variables inside of manifest
   def load_actions
      loads actions in to chain resolves yaml/json to a object
   def execute_actions
      Executes all action objects
        ####class maker####
file @ **/goephor/core/plugins/receipt.py**


This class represents a receipt maker class
    
   def __init__
      None
   def on_actions
      None
   def custom
      None####class git####
file @ **/goephor/core/plugins/scm.py**


This class Represents a call to git
    
   def __init__
      None
   def clone
      None
   def delete
      None####class terminal####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd specific commands go here####class pkg####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd package commands go here####class jails####
file @ **/goephor/core/plugins/freebsd.py**


Freebsd jail management commands go here
   def __init__
      None
   def jls
      None
   def jexec
      None
   def fetch
      None
   def __init__
      None
   def install
      None
   def __init__
      None####class DecoMeta####
file @ **/goephor/core/plugins/pluginable.py**


None####class Plugin####
file @ **/goephor/core/plugins/pluginable.py**


This is the base class for plugin which all plugins must inherit from.
    
   def __new__
      None
   def deco
      None
   def __init__
      None
   def wrapper
      None####class env####
file @ **/goephor/core/plugins/environment.py**


This class Represents an example
    
   def __init__
      None
   def set
      None####class terminal####
file @ **/goephor/core/plugins/system.py**


General nix system commands go here
   def __init__
      None
   def shell
      None
   def rsync
      None####class ssh####
file @ **/goephor/core/plugins/remote.py**


This class can perform ssh commands
   def __init__
      None
   def cmd
      None####class example####
file @ **/goephor/core/plugins/example.py**


This class Represents an example
    
   def __init__
      None
   def runme
      None
   def jexec
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
   def jdestroy
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict####class rest####
file @ **/goephor/core/plugins/http.py**


This class handles all rest actions
   def __init__
      None
   def send
      None####class statement####
file @ **/goephor/core/plugins/condition.py**


None
   def __init__
      None
   def add_obj
      None
   def IF
      None
   def _has_keys
      Collect all environment variables
@param str: command string
   def _sanitize
      Replace all environment variables into command
@param str: command string
   def cmd
      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh####class Manager####
file @ **/goephor/core/plugins/modules/action.py**


This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.####class Action####
file @ **/goephor/core/plugins/modules/action.py**


Object containing instructions to create and execute actions
   def __init__
      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
   def to_obj
      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
   def add
      Append an action obj to chain

__param action_obj__  Obj
   def insert
      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
   def get_index
      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage
   def __init__
      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
   def __repr__
      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
   def set_ignore
      catch the ignore parameter and delete it in defaults
   def get_receipt
      return a dictionary of all Action info
   def pprint
      print state about the object pretty

__param title__  String
__param footer__  String
   def _init_instance
      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
   def execute
      execute the instruction
        ####class Repo_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


None####class Commit_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all commit type actions
    ####class Branch_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all branch related actions
@requires: Repo obj####class Remote_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**


This class handles all remote actions
    
   def __init__
      Initialize Repo actions
        
   def _set_ssh_config
      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
   def _set_dirs
      None
   def attach
      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
   def _initial_commit
      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
   def init
      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
   def clone
      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
   def untracked_files
      list all untracked files
@return: list of untracked files
   def __init__
      None
   def commit
      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
   def cherry_pick
      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
   def diff_tree
      None
   def search_log
      None
   def add
      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure
   def __init__
      None
   def branch
      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
   def branch_from
      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
   def branch_is
      provides the current branch
@return: the current branch
   def branch_list
      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
   def has_reference
      Search for reference
@param branch_name__ string of branch name
@return__  reference obj
   def has_head
      Search for branch head
@param branch_name__ string of branch name
@return__  head obj
   def checkout
      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
   def push
      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def remote_delete
      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def delete
      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def __init__
      None
   def list
      None
   def has_remote
      None
   def add
      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
   def fork_sync
      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
   def fetch
      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  ####class EnvManager####
file @ **/goephor/core/plugins/modules/environment.py**


Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.
   def __init__
      Constructor

__param debug__  Bool
   def set
      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
   def get
      get an environment variable

__param key__  String
   def sanitize
      sanitizes environment variables in a given values

__param values__  List
   def _sanitize
      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all####class Run####
file @ **/goephor/core/plugins/modules/remote.py**


This class represents a remote machine
using SSH to perform all needed actions
   def __init__
      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
   def is_alive
      Pings the remote to make sure its a valid address
@return: boolean
   def is_alive_poll
      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
   def is_writable
      Check to make sure the file system is writable
@return: boolean
   def is_writable_poll
      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
   def has_access
      Does a key already exist on the remote?
@return: boolean
   def has_file
      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
   def has_dir
      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
   def remove
      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
   def move
      Perform a move operation
        
   def copy
      Perform a copy operation
        
   def set_rsa
      Put a rsa key on the remote
@return: None
   def cmd
      Runs a shell command on the remote
@return: session info
   def find
      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
   def os_type
      Gets the os type of the system
@return: returns os string
   def onefs_version
      None
   def get_MD5
      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
   def _clean_MD5
      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5
   def waitfor
      poll the child for input

__param fd__  forked process
   def event
      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
   def set_rsa
      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
   def create_rsa_public
      generate a public key from the private key

__param rsa_private__  path to private key
   def ssh
      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
   def rsync
      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
   def shell
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
   def _exit_clean
      cleans .tmp_shell files before exit####class Restful####
file @ **/goephor/core/plugins/modules/http.py**


None
   def __init__
      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
   def send
      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
   def post_multipart
      None
   def menu
      None
   def parse_envs
      None
   def main
      None
####class Run####
file @ **/goephor/core/Chain.py**

This is the entry point from the cli and runs drives components
   def __init__
      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
   def read_config
      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
   def _read_yaml
      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
   def _read_json
      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
   def add_envs
      Overrides environment variables from cli

__param **envs__  dictionary of environment variables
   def set_envs
      sets environment variables inside of manifest
   def load_actions
      loads actions in to chain resolves yaml/json to a object
   def execute_actions
      Executes all action objects
        
####class maker####
file @ **/goephor/core/plugins/receipt.py**

This class represents a receipt maker class
    
   def __init__
      None
   def on_actions
      None
   def custom
      None
####class git####
file @ **/goephor/core/plugins/scm.py**

This class Represents a call to git
    
   def __init__
      None
   def clone
      None
   def delete
      None
####class terminal####
file @ **/goephor/core/plugins/freebsd.py**

Freebsd specific commands go here
####class pkg####
file @ **/goephor/core/plugins/freebsd.py**

Freebsd package commands go here
####class jails####
file @ **/goephor/core/plugins/freebsd.py**

Freebsd jail management commands go here
   def __init__
      None
   def jls
      None
   def jexec
      None
   def fetch
      None
   def __init__
      None
   def install
      None
   def __init__
      None
####class DecoMeta####
file @ **/goephor/core/plugins/pluginable.py**

None
####class Plugin####
file @ **/goephor/core/plugins/pluginable.py**

This is the base class for plugin which all plugins must inherit from.
    
   def __new__
      None
   def deco
      None
   def __init__
      None
   def wrapper
      None
####class env####
file @ **/goephor/core/plugins/environment.py**

This class Represents an example
    
   def __init__
      None
   def set
      None
####class terminal####
file @ **/goephor/core/plugins/system.py**

General nix system commands go here
   def __init__
      None
   def shell
      None
   def rsync
      None
####class ssh####
file @ **/goephor/core/plugins/remote.py**

This class can perform ssh commands
   def __init__
      None
   def cmd
      None
####class example####
file @ **/goephor/core/plugins/example.py**

This class Represents an example
    
   def __init__
      None
   def runme
      None
   def jexec
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
   def jdestroy
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
####class rest####
file @ **/goephor/core/plugins/http.py**

This class handles all rest actions
   def __init__
      None
   def send
      None
####class statement####
file @ **/goephor/core/plugins/condition.py**

None
   def __init__
      None
   def add_obj
      None
   def IF
      None
   def _has_keys
      Collect all environment variables
@param str: command string
   def _sanitize
      Replace all environment variables into command
@param str: command string
   def cmd
      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh
####class Manager####
file @ **/goephor/core/plugins/modules/action.py**

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.
####class Action####
file @ **/goephor/core/plugins/modules/action.py**

Object containing instructions to create and execute actions
   def __init__
      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
   def to_obj
      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
   def add
      Append an action obj to chain

__param action_obj__  Obj
   def insert
      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
   def get_index
      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage
   def __init__
      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
   def __repr__
      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
   def set_ignore
      catch the ignore parameter and delete it in defaults
   def get_receipt
      return a dictionary of all Action info
   def pprint
      print state about the object pretty

__param title__  String
__param footer__  String
   def _init_instance
      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
   def execute
      execute the instruction
        
####class Repo_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**

None
####class Commit_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all commit type actions
    
####class Branch_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all branch related actions
@requires: Repo obj
####class Remote_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all remote actions
    
   def __init__
      Initialize Repo actions
        
   def _set_ssh_config
      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
   def _set_dirs
      None
   def attach
      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
   def _initial_commit
      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
   def init
      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
   def clone
      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
   def untracked_files
      list all untracked files
@return: list of untracked files
   def __init__
      None
   def commit
      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
   def cherry_pick
      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
   def diff_tree
      None
   def search_log
      None
   def add
      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure
   def __init__
      None
   def branch
      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
   def branch_from
      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
   def branch_is
      provides the current branch
@return: the current branch
   def branch_list
      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
   def has_reference
      Search for reference
@param branch_name__ string of branch name
@return__  reference obj
   def has_head
      Search for branch head
@param branch_name__ string of branch name
@return__  head obj
   def checkout
      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
   def push
      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def remote_delete
      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def delete
      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def __init__
      None
   def list
      None
   def has_remote
      None
   def add
      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
   def fork_sync
      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
   def fetch
      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  
####class EnvManager####
file @ **/goephor/core/plugins/modules/environment.py**

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.
   def __init__
      Constructor

__param debug__  Bool
   def set
      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
   def get
      get an environment variable

__param key__  String
   def sanitize
      sanitizes environment variables in a given values

__param values__  List
   def _sanitize
      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all
####class Run####
file @ **/goephor/core/plugins/modules/remote.py**

This class represents a remote machine
using SSH to perform all needed actions
   def __init__
      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
   def is_alive
      Pings the remote to make sure its a valid address
@return: boolean
   def is_alive_poll
      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
   def is_writable
      Check to make sure the file system is writable
@return: boolean
   def is_writable_poll
      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
   def has_access
      Does a key already exist on the remote?
@return: boolean
   def has_file
      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
   def has_dir
      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
   def remove
      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
   def move
      Perform a move operation
        
   def copy
      Perform a copy operation
        
   def set_rsa
      Put a rsa key on the remote
@return: None
   def cmd
      Runs a shell command on the remote
@return: session info
   def find
      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
   def os_type
      Gets the os type of the system
@return: returns os string
   def onefs_version
      None
   def get_MD5
      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
   def _clean_MD5
      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5
   def waitfor
      poll the child for input

__param fd__  forked process
   def event
      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
   def set_rsa
      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
   def create_rsa_public
      generate a public key from the private key

__param rsa_private__  path to private key
   def ssh
      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
   def rsync
      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
   def shell
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
   def _exit_clean
      cleans .tmp_shell files before exit
####class Restful####
file @ **/goephor/core/plugins/modules/http.py**

None
   def __init__
      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
   def send
      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
   def post_multipart
      None
   def menu
      None
   def parse_envs
      None
   def main
      None
####class Run####
file @ **/goephor/core/Chain.py**

This is the entry point from the cli and runs drives components
   def __init__
      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info
   def read_config
      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict
   def _read_yaml
      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict
   def _read_json
      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict
   def add_envs
      Overrides environment variables from cli

__param **envs__  dictionary of environment variables
   def set_envs
      sets environment variables inside of manifest
   def load_actions
      loads actions in to chain resolves yaml/json to a object
   def execute_actions
      Executes all action objects
        
####class maker####
file @ **/goephor/core/plugins/receipt.py**

This class represents a receipt maker class
    
   def __init__
      None
   def on_actions
      None
   def custom
      None
####class git####
file @ **/goephor/core/plugins/scm.py**

This class Represents a call to git
    
   def __init__
      None
   def clone
      None
   def delete
      None
####class terminal####
file @ **/goephor/core/plugins/freebsd.py**

Freebsd specific commands go here
####class pkg####
file @ **/goephor/core/plugins/freebsd.py**

Freebsd package commands go here
####class jails####
file @ **/goephor/core/plugins/freebsd.py**

Freebsd jail management commands go here
   def __init__
      None
   def jls
      None
   def jexec
      None
   def fetch
      None
   def __init__
      None
   def install
      None
   def __init__
      None
####class DecoMeta####
file @ **/goephor/core/plugins/pluginable.py**

None
####class Plugin####
file @ **/goephor/core/plugins/pluginable.py**

This is the base class for plugin which all plugins must inherit from.
    
   def __new__
      None
   def deco
      None
   def __init__
      None
   def wrapper
      None
####class env####
file @ **/goephor/core/plugins/environment.py**

This class Represents an example
    
   def __init__
      None
   def set
      None
####class terminal####
file @ **/goephor/core/plugins/system.py**

General nix system commands go here
   def __init__
      None
   def shell
      None
   def rsync
      None
####class ssh####
file @ **/goephor/core/plugins/remote.py**

This class can perform ssh commands
   def __init__
      None
   def cmd
      None
####class example####
file @ **/goephor/core/plugins/example.py**

This class Represents an example
    
   def __init__
      None
   def runme
      None
   def jexec
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
   def jdestroy
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict
####class rest####
file @ **/goephor/core/plugins/http.py**

This class handles all rest actions
   def __init__
      None
   def send
      None
####class statement####
file @ **/goephor/core/plugins/condition.py**

None
   def __init__
      None
   def add_obj
      None
   def IF
      None
   def _has_keys
      Collect all environment variables
@param str: command string
   def _sanitize
      Replace all environment variables into command
@param str: command string
   def cmd
      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh
####class Manager####
file @ **/goephor/core/plugins/modules/action.py**

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.
####class Action####
file @ **/goephor/core/plugins/modules/action.py**

Object containing instructions to create and execute actions
   def __init__
      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug
   def to_obj
      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.
   def add
      Append an action obj to chain

__param action_obj__  Obj
   def insert
      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj
   def get_index
      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage
   def __init__
      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj
   def __repr__
      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)
   def set_ignore
      catch the ignore parameter and delete it in defaults
   def get_receipt
      return a dictionary of all Action info
   def pprint
      print state about the object pretty

__param title__  String
__param footer__  String
   def _init_instance
      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.
   def execute
      execute the instruction
        
####class Repo_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**

None
####class Commit_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all commit type actions
    
####class Branch_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all branch related actions
@requires: Repo obj
####class Remote_actions####
file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all remote actions
    
   def __init__
      Initialize Repo actions
        
   def _set_ssh_config
      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 
   def _set_dirs
      None
   def attach
      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 
   def _initial_commit
      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md
   def init
      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git
   def clone
      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 
   def untracked_files
      list all untracked files
@return: list of untracked files
   def __init__
      None
   def commit
      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure
   def cherry_pick
      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 
   def diff_tree
      None
   def search_log
      None
   def add
      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure
   def __init__
      None
   def branch
      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  
   def branch_from
      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name
   def branch_is
      provides the current branch
@return: the current branch
   def branch_list
      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 
   def has_reference
      Search for reference
@param branch_name__ string of branch name
@return__  reference obj
   def has_head
      Search for branch head
@param branch_name__ string of branch name
@return__  head obj
   def checkout
      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  
   def push
      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def remote_delete
      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def delete
      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean
   def __init__
      None
   def list
      None
   def has_remote
      None
   def add
      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
   def fork_sync
      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 
   def fetch
      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  
####class EnvManager####
file @ **/goephor/core/plugins/modules/environment.py**

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.
   def __init__
      Constructor

__param debug__  Bool
   def set
      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value
   def get
      get an environment variable

__param key__  String
   def sanitize
      sanitizes environment variables in a given values

__param values__  List
   def _sanitize
      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all
####class Run####
file @ **/goephor/core/plugins/modules/remote.py**

This class represents a remote machine
using SSH to perform all needed actions
   def __init__
      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server
   def is_alive
      Pings the remote to make sure its a valid address
@return: boolean
   def is_alive_poll
      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean
   def is_writable
      Check to make sure the file system is writable
@return: boolean
   def is_writable_poll
      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean
   def has_access
      Does a key already exist on the remote?
@return: boolean
   def has_file
      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
   def has_dir
      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean
   def remove
      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean
   def move
      Perform a move operation
        
   def copy
      Perform a copy operation
        
   def set_rsa
      Put a rsa key on the remote
@return: None
   def cmd
      Runs a shell command on the remote
@return: session info
   def find
      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session
   def os_type
      Gets the os type of the system
@return: returns os string
   def onefs_version
      None
   def get_MD5
      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string
   def _clean_MD5
      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5
   def waitfor
      poll the child for input

__param fd__  forked process
   def event
      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair
   def set_rsa
      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user
   def create_rsa_public
      generate a public key from the private key

__param rsa_private__  path to private key
   def ssh
      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run
   def rsync
      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src
   def shell
      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict
   def _exit_clean
      cleans .tmp_shell files before exit
####class Restful####
file @ **/goephor/core/plugins/modules/http.py**

None
   def __init__
      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>
   def send
      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code
   def post_multipart
      None
   def menu

      None

   def parse_envs

      None

   def main

      None

####class Run####

file @ **/goephor/core/Chain.py**

This is the entry point from the cli and runs drives components

   def __init__

      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info

   def read_config

      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict

   def _read_yaml

      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict

   def _read_json

      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict

   def add_envs

      Overrides environment variables from cli

__param **envs__  dictionary of environment variables

   def set_envs

      sets environment variables inside of manifest

   def load_actions

      loads actions in to chain resolves yaml/json to a object

   def execute_actions

      Executes all action objects
        

####class maker####

file @ **/goephor/core/plugins/receipt.py**

This class represents a receipt maker class
    

   def __init__

      None

   def on_actions

      None

   def custom

      None

####class git####

file @ **/goephor/core/plugins/scm.py**

This class Represents a call to git
    

   def __init__

      None

   def clone

      None

   def delete

      None

####class terminal####

file @ **/goephor/core/plugins/freebsd.py**

Freebsd specific commands go here

####class pkg####

file @ **/goephor/core/plugins/freebsd.py**

Freebsd package commands go here

####class jails####

file @ **/goephor/core/plugins/freebsd.py**

Freebsd jail management commands go here

   def __init__

      None

   def jls

      None

   def jexec

      None

   def fetch

      None

   def __init__

      None

   def install

      None

   def __init__

      None

####class DecoMeta####

file @ **/goephor/core/plugins/pluginable.py**

None

####class Plugin####

file @ **/goephor/core/plugins/pluginable.py**

This is the base class for plugin which all plugins must inherit from.
    

   def __new__

      None

   def deco

      None

   def __init__

      None

   def wrapper

      None

####class env####

file @ **/goephor/core/plugins/environment.py**

This class Represents an example
    

   def __init__

      None

   def set

      None

####class terminal####

file @ **/goephor/core/plugins/system.py**

General nix system commands go here

   def __init__

      None

   def shell

      None

   def rsync

      None

####class ssh####

file @ **/goephor/core/plugins/remote.py**

This class can perform ssh commands

   def __init__

      None

   def cmd

      None

####class example####

file @ **/goephor/core/plugins/example.py**

This class Represents an example
    

   def __init__

      None

   def runme

      None

   def jexec

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

   def jdestroy

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

####class rest####

file @ **/goephor/core/plugins/http.py**

This class handles all rest actions

   def __init__

      None

   def send

      None

####class statement####

file @ **/goephor/core/plugins/condition.py**

None

   def __init__

      None

   def add_obj

      None

   def IF

      None

   def _has_keys

      Collect all environment variables
@param str: command string

   def _sanitize

      Replace all environment variables into command
@param str: command string

   def cmd

      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

####class Manager####

file @ **/goephor/core/plugins/modules/action.py**

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.

####class Action####

file @ **/goephor/core/plugins/modules/action.py**

Object containing instructions to create and execute actions

   def __init__

      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug

   def to_obj

      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

   def add

      Append an action obj to chain

__param action_obj__  Obj

   def insert

      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj

   def get_index

      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage

   def __init__

      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj

   def __repr__

      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)

   def set_ignore

      catch the ignore parameter and delete it in defaults

   def get_receipt

      return a dictionary of all Action info

   def pprint

      print state about the object pretty

__param title__  String
__param footer__  String

   def _init_instance

      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.

   def execute

      execute the instruction
        

####class Repo_actions####

file @ **/goephor/core/plugins/modules/git_kit.py**

None

####class Commit_actions####

file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all commit type actions
    

####class Branch_actions####

file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all branch related actions
@requires: Repo obj

####class Remote_actions####

file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all remote actions
    

   def __init__

      Initialize Repo actions
        

   def _set_ssh_config

      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 

   def _set_dirs

      None

   def attach

      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 

   def _initial_commit

      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md

   def init

      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git

   def clone

      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 

   def untracked_files

      list all untracked files
@return: list of untracked files

   def __init__

      None

   def commit

      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure

   def cherry_pick

      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 

   def diff_tree

      None

   def search_log

      None

   def add

      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure

   def __init__

      None

   def branch

      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  

   def branch_from

      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name

   def branch_is

      provides the current branch
@return: the current branch

   def branch_list

      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 

   def has_reference

      Search for reference
@param branch_name__ string of branch name
@return__  reference obj

   def has_head

      Search for branch head
@param branch_name__ string of branch name
@return__  head obj

   def checkout

      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  

   def push

      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def remote_delete

      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def delete

      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def __init__

      None

   def list

      None

   def has_remote

      None

   def add

      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fork_sync

      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fetch

      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

####class EnvManager####

file @ **/goephor/core/plugins/modules/environment.py**

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.

   def __init__

      Constructor

__param debug__  Bool

   def set

      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value

   def get

      get an environment variable

__param key__  String

   def sanitize

      sanitizes environment variables in a given values

__param values__  List

   def _sanitize

      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

####class Run####

file @ **/goephor/core/plugins/modules/remote.py**

This class represents a remote machine
using SSH to perform all needed actions

   def __init__

      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server

   def is_alive

      Pings the remote to make sure its a valid address
@return: boolean

   def is_alive_poll

      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean

   def is_writable

      Check to make sure the file system is writable
@return: boolean

   def is_writable_poll

      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean

   def has_access

      Does a key already exist on the remote?
@return: boolean

   def has_file

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file

   def has_dir

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean

   def remove

      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean

   def move

      Perform a move operation
        

   def copy

      Perform a copy operation
        

   def set_rsa

      Put a rsa key on the remote
@return: None

   def cmd

      Runs a shell command on the remote
@return: session info

   def find

      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session

   def os_type

      Gets the os type of the system
@return: returns os string

   def onefs_version

      None

   def get_MD5

      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string

   def _clean_MD5

      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

   def waitfor

      poll the child for input

__param fd__  forked process

   def event

      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair

   def set_rsa

      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user

   def create_rsa_public

      generate a public key from the private key

__param rsa_private__  path to private key

   def ssh

      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run

   def rsync

      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src

   def shell

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict

   def _exit_clean

      cleans .tmp_shell files before exit

####class Restful####

file @ **/goephor/core/plugins/modules/http.py**

None

   def __init__

      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>

   def send

      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code

   def post_multipart

      None

   def menu

      None

   def parse_envs

      None

   def main

      None

####class Run####

file @ **/goephor/core/Chain.py**

This is the entry point from the cli and runs drives components

   def __init__

      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info

   def read_config

      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict

   def _read_yaml

      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict

   def _read_json

      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict

   def add_envs

      Overrides environment variables from cli

__param **envs__  dictionary of environment variables

   def set_envs

      sets environment variables inside of manifest

   def load_actions

      loads actions in to chain resolves yaml/json to a object

   def execute_actions

      Executes all action objects
        

####class maker####

file @ **/goephor/core/plugins/receipt.py**

This class represents a receipt maker class
    

   def __init__

      None

   def on_actions

      None

   def custom

      None

####class git####

file @ **/goephor/core/plugins/scm.py**

This class Represents a call to git
    

   def __init__

      None

   def clone

      None

   def delete

      None

####class terminal####

file @ **/goephor/core/plugins/freebsd.py**

Freebsd specific commands go here

####class pkg####

file @ **/goephor/core/plugins/freebsd.py**

Freebsd package commands go here

####class jails####

file @ **/goephor/core/plugins/freebsd.py**

Freebsd jail management commands go here

   def __init__

      None

   def jls

      None

   def jexec

      None

   def fetch

      None

   def __init__

      None

   def install

      None

   def __init__

      None

####class DecoMeta####

file @ **/goephor/core/plugins/pluginable.py**

None

####class Plugin####

file @ **/goephor/core/plugins/pluginable.py**

This is the base class for plugin which all plugins must inherit from.
    

   def __new__

      None

   def deco

      None

   def __init__

      None

   def wrapper

      None

####class env####

file @ **/goephor/core/plugins/environment.py**

This class Represents an example
    

   def __init__

      None

   def set

      None

####class terminal####

file @ **/goephor/core/plugins/system.py**

General nix system commands go here

   def __init__

      None

   def shell

      None

   def rsync

      None

####class ssh####

file @ **/goephor/core/plugins/remote.py**

This class can perform ssh commands

   def __init__

      None

   def cmd

      None

####class example####

file @ **/goephor/core/plugins/example.py**

This class Represents an example
    

   def __init__

      None

   def runme

      None

   def jexec

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

   def jdestroy

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

####class rest####

file @ **/goephor/core/plugins/http.py**

This class handles all rest actions

   def __init__

      None

   def send

      None

####class statement####

file @ **/goephor/core/plugins/condition.py**

None

   def __init__

      None

   def add_obj

      None

   def IF

      None

   def _has_keys

      Collect all environment variables
@param str: command string

   def _sanitize

      Replace all environment variables into command
@param str: command string

   def cmd

      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

####class Manager####

file @ **/goephor/core/plugins/modules/action.py**

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.

####class Action####

file @ **/goephor/core/plugins/modules/action.py**

Object containing instructions to create and execute actions

   def __init__

      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug

   def to_obj

      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

   def add

      Append an action obj to chain

__param action_obj__  Obj

   def insert

      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj

   def get_index

      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage

   def __init__

      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj

   def __repr__

      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)

   def set_ignore

      catch the ignore parameter and delete it in defaults

   def get_receipt

      return a dictionary of all Action info

   def pprint

      print state about the object pretty

__param title__  String
__param footer__  String

   def _init_instance

      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.

   def execute

      execute the instruction
        

####class Repo_actions####

file @ **/goephor/core/plugins/modules/git_kit.py**

None

####class Commit_actions####

file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all commit type actions
    

####class Branch_actions####

file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all branch related actions
@requires: Repo obj

####class Remote_actions####

file @ **/goephor/core/plugins/modules/git_kit.py**

This class handles all remote actions
    

   def __init__

      Initialize Repo actions
        

   def _set_ssh_config

      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 

   def _set_dirs

      None

   def attach

      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 

   def _initial_commit

      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md

   def init

      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git

   def clone

      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 

   def untracked_files

      list all untracked files
@return: list of untracked files

   def __init__

      None

   def commit

      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure

   def cherry_pick

      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 

   def diff_tree

      None

   def search_log

      None

   def add

      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure

   def __init__

      None

   def branch

      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  

   def branch_from

      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name

   def branch_is

      provides the current branch
@return: the current branch

   def branch_list

      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 

   def has_reference

      Search for reference
@param branch_name__ string of branch name
@return__  reference obj

   def has_head

      Search for branch head
@param branch_name__ string of branch name
@return__  head obj

   def checkout

      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  

   def push

      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def remote_delete

      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def delete

      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def __init__

      None

   def list

      None

   def has_remote

      None

   def add

      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fork_sync

      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fetch

      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

####class EnvManager####

file @ **/goephor/core/plugins/modules/environment.py**

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.

   def __init__

      Constructor

__param debug__  Bool

   def set

      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value

   def get

      get an environment variable

__param key__  String

   def sanitize

      sanitizes environment variables in a given values

__param values__  List

   def _sanitize

      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

####class Run####

file @ **/goephor/core/plugins/modules/remote.py**

This class represents a remote machine
using SSH to perform all needed actions

   def __init__

      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server

   def is_alive

      Pings the remote to make sure its a valid address
@return: boolean

   def is_alive_poll

      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean

   def is_writable

      Check to make sure the file system is writable
@return: boolean

   def is_writable_poll

      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean

   def has_access

      Does a key already exist on the remote?
@return: boolean

   def has_file

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file

   def has_dir

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean

   def remove

      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean

   def move

      Perform a move operation
        

   def copy

      Perform a copy operation
        

   def set_rsa

      Put a rsa key on the remote
@return: None

   def cmd

      Runs a shell command on the remote
@return: session info

   def find

      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session

   def os_type

      Gets the os type of the system
@return: returns os string

   def onefs_version

      None

   def get_MD5

      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string

   def _clean_MD5

      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

   def waitfor

      poll the child for input

__param fd__  forked process

   def event

      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair

   def set_rsa

      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user

   def create_rsa_public

      generate a public key from the private key

__param rsa_private__  path to private key

   def ssh

      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run

   def rsync

      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src

   def shell

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict

   def _exit_clean

      cleans .tmp_shell files before exit

####class Restful####

file @ **/goephor/core/plugins/modules/http.py**

None

   def __init__

      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>

   def send

      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code

   def post_multipart

      None

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

   def menu

      None

   def parse_envs

      None

   def main

      None

file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

This is the entry point from the cli and runs drives components

   def __init__

      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info

   def read_config

      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict

   def _read_yaml

      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict

   def _read_json

      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict

   def add_envs

      Overrides environment variables from cli

__param **envs__  dictionary of environment variables

   def set_envs

      sets environment variables inside of manifest

   def load_actions

      loads actions in to chain resolves yaml/json to a object

   def execute_actions

      Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

This class represents a receipt maker class
    

   def __init__

      None

   def on_actions

      None

   def custom

      None

file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

This class Represents a call to git
    

   def __init__

      None

   def clone

      None

   def delete

      None

file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

Freebsd specific commands go here

####class pkg####

Freebsd package commands go here

####class jails####

Freebsd jail management commands go here

   def __init__

      None

   def jls

      None

   def jexec

      None

   def fetch

      None

   def __init__

      None

   def install

      None

   def __init__

      None

file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####

None

####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    

   def __new__

      None

   def deco

      None

   def __init__

      None

   def wrapper

      None

file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

This class Represents an example
    

   def __init__

      None

   def set

      None

file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

General nix system commands go here

   def __init__

      None

   def shell

      None

   def rsync

      None

file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

This class can perform ssh commands

   def __init__

      None

   def cmd

      None

file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

This class Represents an example
    

   def __init__

      None

   def runme

      None

file @ **/goephor/core/plugins/jumbler.py**

      Created on Feb 29, 2016

@author: sdouglas2

   def jexec

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

   def jdestroy

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

This class handles all rest actions

   def __init__

      None

   def send

      None

file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####

None

   def __init__

      None

   def add_obj

      None

   def IF

      None

file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

   def _has_keys

      Collect all environment variables
@param str: command string

   def _sanitize

      Replace all environment variables into command
@param str: command string

   def cmd

      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.

####class Action####

Object containing instructions to create and execute actions

   def __init__

      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug

   def to_obj

      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

   def add

      Append an action obj to chain

__param action_obj__  Obj

   def insert

      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj

   def get_index

      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage

   def __init__

      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj

   def __repr__

      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)

   def set_ignore

      catch the ignore parameter and delete it in defaults

   def get_receipt

      return a dictionary of all Action info

   def pprint

      print state about the object pretty

__param title__  String
__param footer__  String

   def _init_instance

      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.

   def execute

      execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####

None

####class Commit_actions####

This class handles all commit type actions
    

####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj

####class Remote_actions####

This class handles all remote actions
    

   def __init__

      Initialize Repo actions
        

   def _set_ssh_config

      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 

   def _set_dirs

      None

   def attach

      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 

   def _initial_commit

      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md

   def init

      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git

   def clone

      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 

   def untracked_files

      list all untracked files
@return: list of untracked files

   def __init__

      None

   def commit

      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure

   def cherry_pick

      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 

   def diff_tree

      None

   def search_log

      None

   def add

      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure

   def __init__

      None

   def branch

      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  

   def branch_from

      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name

   def branch_is

      provides the current branch
@return: the current branch

   def branch_list

      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 

   def has_reference

      Search for reference
@param branch_name__ string of branch name
@return__  reference obj

   def has_head

      Search for branch head
@param branch_name__ string of branch name
@return__  head obj

   def checkout

      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  

   def push

      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def remote_delete

      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def delete

      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def __init__

      None

   def list

      None

   def has_remote

      None

   def add

      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fork_sync

      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fetch

      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.

   def __init__

      Constructor

__param debug__  Bool

   def set

      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value

   def get

      get an environment variable

__param key__  String

   def sanitize

      sanitizes environment variables in a given values

__param values__  List

   def _sanitize

      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

This class represents a remote machine
using SSH to perform all needed actions

   def __init__

      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server

   def is_alive

      Pings the remote to make sure its a valid address
@return: boolean

   def is_alive_poll

      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean

   def is_writable

      Check to make sure the file system is writable
@return: boolean

   def is_writable_poll

      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean

   def has_access

      Does a key already exist on the remote?
@return: boolean

   def has_file

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file

   def has_dir

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean

   def remove

      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean

   def move

      Perform a move operation
        

   def copy

      Perform a copy operation
        

   def set_rsa

      Put a rsa key on the remote
@return: None

   def cmd

      Runs a shell command on the remote
@return: session info

   def find

      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session

   def os_type

      Gets the os type of the system
@return: returns os string

   def onefs_version

      None

   def get_MD5

      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string

   def _clean_MD5

      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

   def waitfor

      poll the child for input

__param fd__  forked process

   def event

      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair

   def set_rsa

      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user

   def create_rsa_public

      generate a public key from the private key

__param rsa_private__  path to private key

   def ssh

      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run

   def rsync

      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src

   def shell

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict

   def _exit_clean

      cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####

None

   def __init__

      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>

   def send

      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code

   def post_multipart

      None

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

   def menu

      None

   def parse_envs

      None

   def main

      None

file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

This is the entry point from the cli and runs drives components

   def __init__

      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info

   def read_config

      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict

   def _read_yaml

      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict

   def _read_json

      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict

   def add_envs

      Overrides environment variables from cli

__param **envs__  dictionary of environment variables

   def set_envs

      sets environment variables inside of manifest

   def load_actions

      loads actions in to chain resolves yaml/json to a object

   def execute_actions

      Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

This class represents a receipt maker class
    

   def __init__

      None

   def on_actions

      None

   def custom

      None

file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

This class Represents a call to git
    

   def __init__

      None

   def clone

      None

   def delete

      None

file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

Freebsd specific commands go here

####class pkg####

Freebsd package commands go here

####class jails####

Freebsd jail management commands go here

   def __init__

      None

   def jls

      None

   def jexec

      None

   def fetch

      None

   def __init__

      None

   def install

      None

   def __init__

      None

file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####

None

####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    

   def __new__

      None

   def deco

      None

   def __init__

      None

   def wrapper

      None

file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

This class Represents an example
    

   def __init__

      None

   def set

      None

file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

General nix system commands go here

   def __init__

      None

   def shell

      None

   def rsync

      None

file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

This class can perform ssh commands

   def __init__

      None

   def cmd

      None

file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

This class Represents an example
    

   def __init__

      None

   def runme

      None

file @ **/goephor/core/plugins/jumbler.py**

      Created on Feb 29, 2016

@author: sdouglas2

   def jexec

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

   def jdestroy

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]
@param cmd__ String command
@param verbose__ bool
@param strict__bool will exit based on code if enabled
@return__   {command, stdout, code} as dict

file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

This class handles all rest actions

   def __init__

      None

   def send

      None

file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####

None

   def __init__

      None

   def add_obj

      None

   def IF

      None

file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

   def _has_keys

      Collect all environment variables
@param str: command string

   def _sanitize

      Replace all environment variables into command
@param str: command string

   def cmd

      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.

####class Action####

Object containing instructions to create and execute actions

   def __init__

      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug

   def to_obj

      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

   def add

      Append an action obj to chain

__param action_obj__  Obj

   def insert

      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj

   def get_index

      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage

   def __init__

      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj

   def __repr__

      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)

   def set_ignore

      catch the ignore parameter and delete it in defaults

   def get_receipt

      return a dictionary of all Action info

   def pprint

      print state about the object pretty

__param title__  String
__param footer__  String

   def _init_instance

      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.

   def execute

      execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####

None

####class Commit_actions####

This class handles all commit type actions
    

####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj

####class Remote_actions####

This class handles all remote actions
    

   def __init__

      Initialize Repo actions
        

   def _set_ssh_config

      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 

   def _set_dirs

      None

   def attach

      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 

   def _initial_commit

      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md

   def init

      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git

   def clone

      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 

   def untracked_files

      list all untracked files
@return: list of untracked files

   def __init__

      None

   def commit

      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure

   def cherry_pick

      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 

   def diff_tree

      None

   def search_log

      None

   def add

      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure

   def __init__

      None

   def branch

      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  

   def branch_from

      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name

   def branch_is

      provides the current branch
@return: the current branch

   def branch_list

      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 

   def has_reference

      Search for reference
@param branch_name__ string of branch name
@return__  reference obj

   def has_head

      Search for branch head
@param branch_name__ string of branch name
@return__  head obj

   def checkout

      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  

   def push

      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def remote_delete

      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def delete

      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def __init__

      None

   def list

      None

   def has_remote

      None

   def add

      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fork_sync

      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fetch

      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.

   def __init__

      Constructor

__param debug__  Bool

   def set

      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value

   def get

      get an environment variable

__param key__  String

   def sanitize

      sanitizes environment variables in a given values

__param values__  List

   def _sanitize

      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

This class represents a remote machine
using SSH to perform all needed actions

   def __init__

      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server

   def is_alive

      Pings the remote to make sure its a valid address
@return: boolean

   def is_alive_poll

      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean

   def is_writable

      Check to make sure the file system is writable
@return: boolean

   def is_writable_poll

      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean

   def has_access

      Does a key already exist on the remote?
@return: boolean

   def has_file

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file

   def has_dir

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean

   def remove

      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean

   def move

      Perform a move operation
        

   def copy

      Perform a copy operation
        

   def set_rsa

      Put a rsa key on the remote
@return: None

   def cmd

      Runs a shell command on the remote
@return: session info

   def find

      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session

   def os_type

      Gets the os type of the system
@return: returns os string

   def onefs_version

      None

   def get_MD5

      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string

   def _clean_MD5

      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

   def waitfor

      poll the child for input

__param fd__  forked process

   def event

      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair

   def set_rsa

      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user

   def create_rsa_public

      generate a public key from the private key

__param rsa_private__  path to private key

   def ssh

      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run

   def rsync

      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src

   def shell

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict

   def _exit_clean

      cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####

None

   def __init__

      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>

   def send

      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code

   def post_multipart

      None

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

   def menu

      None

   def parse_envs

      None

   def main

      None

file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

This is the entry point from the cli and runs drives components

   def __init__

      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info

   def read_config

      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict

   def _read_yaml

      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict

   def _read_json

      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict

   def add_envs

      Overrides environment variables from cli

__param **envs__  dictionary of environment variables

   def set_envs

      sets environment variables inside of manifest

   def load_actions

      loads actions in to chain resolves yaml/json to a object

   def execute_actions

      Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

This class represents a receipt maker class
    

   def __init__

      None

   def on_actions

      None

   def custom

      None

file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

This class Represents a call to git
    

   def __init__

      None

   def clone

      None

   def delete

      None

file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

Freebsd specific commands go here

####class pkg####

Freebsd package commands go here

####class jails####

Freebsd jail management commands go here

   def __init__

      None

   def jls

      None

   def jexec

      None

   def fetch

      None

   def __init__

      None

   def install

      None

   def __init__

      None

file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####

None

####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    

   def __new__

      None

   def deco

      None

   def __init__

      None

   def wrapper

      None

file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

This class Represents an example
    

   def __init__

      None

   def set

      None

file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

General nix system commands go here

   def __init__

      None

   def shell

      None

   def rsync

      None

file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

This class can perform ssh commands

   def __init__

      None

   def cmd

      None

file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

This class Represents an example
    

   def __init__

      None

   def runme

      None

file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

This class handles all rest actions

   def __init__

      None

   def send

      None

file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####

None

   def __init__

      None

   def add_obj

      None

   def IF

      None

file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

   def _has_keys

      Collect all environment variables
@param str: command string

   def _sanitize

      Replace all environment variables into command
@param str: command string

   def cmd

      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.

####class Action####

Object containing instructions to create and execute actions

   def __init__

      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug

   def to_obj

      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

   def add

      Append an action obj to chain

__param action_obj__  Obj

   def insert

      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj

   def get_index

      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage

   def __init__

      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj

   def __repr__

      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)

   def set_ignore

      catch the ignore parameter and delete it in defaults

   def get_receipt

      return a dictionary of all Action info

   def pprint

      print state about the object pretty

__param title__  String
__param footer__  String

   def _init_instance

      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.

   def execute

      execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####

None

####class Commit_actions####

This class handles all commit type actions
    

####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj

####class Remote_actions####

This class handles all remote actions
    

   def __init__

      Initialize Repo actions
        

   def _set_ssh_config

      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 

   def _set_dirs

      None

   def attach

      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 

   def _initial_commit

      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md

   def init

      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git

   def clone

      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 

   def untracked_files

      list all untracked files
@return: list of untracked files

   def __init__

      None

   def commit

      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure

   def cherry_pick

      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 

   def diff_tree

      None

   def search_log

      None

   def add

      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure

   def __init__

      None

   def branch

      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  

   def branch_from

      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name

   def branch_is

      provides the current branch
@return: the current branch

   def branch_list

      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 

   def has_reference

      Search for reference
@param branch_name__ string of branch name
@return__  reference obj

   def has_head

      Search for branch head
@param branch_name__ string of branch name
@return__  head obj

   def checkout

      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  

   def push

      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def remote_delete

      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def delete

      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def __init__

      None

   def list

      None

   def has_remote

      None

   def add

      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fork_sync

      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fetch

      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.

   def __init__

      Constructor

__param debug__  Bool

   def set

      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value

   def get

      get an environment variable

__param key__  String

   def sanitize

      sanitizes environment variables in a given values

__param values__  List

   def _sanitize

      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

This class represents a remote machine
using SSH to perform all needed actions

   def __init__

      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server

   def is_alive

      Pings the remote to make sure its a valid address
@return: boolean

   def is_alive_poll

      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean

   def is_writable

      Check to make sure the file system is writable
@return: boolean

   def is_writable_poll

      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean

   def has_access

      Does a key already exist on the remote?
@return: boolean

   def has_file

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file

   def has_dir

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean

   def remove

      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean

   def move

      Perform a move operation
        

   def copy

      Perform a copy operation
        

   def set_rsa

      Put a rsa key on the remote
@return: None

   def cmd

      Runs a shell command on the remote
@return: session info

   def find

      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session

   def os_type

      Gets the os type of the system
@return: returns os string

   def onefs_version

      None

   def get_MD5

      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string

   def _clean_MD5

      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

   def waitfor

      poll the child for input

__param fd__  forked process

   def event

      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair

   def set_rsa

      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user

   def create_rsa_public

      generate a public key from the private key

__param rsa_private__  path to private key

   def ssh

      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run

   def rsync

      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src

   def shell

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict

   def _exit_clean

      cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####

None

   def __init__

      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>

   def send

      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code

   def post_multipart

      None

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

   def menu

      None

   def parse_envs

      None

   def main

      None

file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

This is the entry point from the cli and runs drives components

   def __init__

      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info

   def read_config

      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict

   def _read_yaml

      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict

   def _read_json

      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict

   def add_envs

      Overrides environment variables from cli

__param **envs__  dictionary of environment variables

   def set_envs

      sets environment variables inside of manifest

   def load_actions

      loads actions in to chain resolves yaml/json to a object

   def execute_actions

      Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

This class represents a receipt maker class
    

   def __init__

      None

   def on_actions

      None

   def custom

      None

file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

This class Represents a call to git
    

   def __init__

      None

   def clone

      None

   def delete

      None

file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

Freebsd specific commands go here

####class pkg####

Freebsd package commands go here

####class jails####

Freebsd jail management commands go here

   def __init__

      None

   def jls

      None

   def jexec

      None

   def fetch

      None

   def __init__

      None

   def install

      None

   def __init__

      None

file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####

None

####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    

   def __new__

      None

   def deco

      None

   def __init__

      None

   def wrapper

      None

file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

This class Represents an example
    

   def __init__

      None

   def set

      None

file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

General nix system commands go here

   def __init__

      None

   def shell

      None

   def rsync

      None

file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

This class can perform ssh commands

   def __init__

      None

   def cmd

      None

file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

This class Represents an example
    

   def __init__

      None

   def runme

      None

file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

This class handles all rest actions

   def __init__

      None

   def send

      None

file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####

None

   def __init__

      None

   def add_obj

      None

   def IF

      None

file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

   def _has_keys

      Collect all environment variables
@param str: command string

   def _sanitize

      Replace all environment variables into command
@param str: command string

   def cmd

      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.

####class Action####

Object containing instructions to create and execute actions

   def __init__

      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug

   def to_obj

      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

   def add

      Append an action obj to chain

__param action_obj__  Obj

   def insert

      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj

   def get_index

      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage

   def __init__

      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj

   def __repr__

      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)

   def set_ignore

      catch the ignore parameter and delete it in defaults

   def get_receipt

      return a dictionary of all Action info

   def pprint

      print state about the object pretty

__param title__  String
__param footer__  String

   def _init_instance

      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.

   def execute

      execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####

None

####class Commit_actions####

This class handles all commit type actions
    

####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj

####class Remote_actions####

This class handles all remote actions
    

   def __init__

      Initialize Repo actions
        

   def _set_ssh_config

      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 

   def _set_dirs

      None

   def attach

      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 

   def _initial_commit

      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md

   def init

      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git

   def clone

      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 

   def untracked_files

      list all untracked files
@return: list of untracked files

   def __init__

      None

   def commit

      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure

   def cherry_pick

      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 

   def diff_tree

      None

   def search_log

      None

   def add

      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure

   def __init__

      None

   def branch

      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  

   def branch_from

      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name

   def branch_is

      provides the current branch
@return: the current branch

   def branch_list

      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 

   def has_reference

      Search for reference
@param branch_name__ string of branch name
@return__  reference obj

   def has_head

      Search for branch head
@param branch_name__ string of branch name
@return__  head obj

   def checkout

      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  

   def push

      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def remote_delete

      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def delete

      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def __init__

      None

   def list

      None

   def has_remote

      None

   def add

      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fork_sync

      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fetch

      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.

   def __init__

      Constructor

__param debug__  Bool

   def set

      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value

   def get

      get an environment variable

__param key__  String

   def sanitize

      sanitizes environment variables in a given values

__param values__  List

   def _sanitize

      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

This class represents a remote machine
using SSH to perform all needed actions

   def __init__

      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server

   def is_alive

      Pings the remote to make sure its a valid address
@return: boolean

   def is_alive_poll

      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean

   def is_writable

      Check to make sure the file system is writable
@return: boolean

   def is_writable_poll

      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean

   def has_access

      Does a key already exist on the remote?
@return: boolean

   def has_file

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file

   def has_dir

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean

   def remove

      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean

   def move

      Perform a move operation
        

   def copy

      Perform a copy operation
        

   def set_rsa

      Put a rsa key on the remote
@return: None

   def cmd

      Runs a shell command on the remote
@return: session info

   def find

      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session

   def os_type

      Gets the os type of the system
@return: returns os string

   def onefs_version

      None

   def get_MD5

      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string

   def _clean_MD5

      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

   def waitfor

      poll the child for input

__param fd__  forked process

   def event

      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair

   def set_rsa

      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user

   def create_rsa_public

      generate a public key from the private key

__param rsa_private__  path to private key

   def ssh

      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run

   def rsync

      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src

   def shell

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict

   def _exit_clean

      cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####

None

   def __init__

      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>

   def send

      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code

   def post_multipart

      None

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

   def menu

      None

   def parse_envs

      None

   def main

      None

file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

This is the entry point from the cli and runs drives components

   def __init__

      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info

   def read_config

      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict

   def _read_yaml

      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict

   def _read_json

      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict

   def add_envs

      Overrides environment variables from cli

__param **envs__  dictionary of environment variables

   def set_envs

      sets environment variables inside of manifest

   def load_actions

      loads actions in to chain resolves yaml/json to a object

   def execute_actions

      Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

This class represents a receipt maker class
    

   def __init__

      None

   def on_actions

      None

   def custom

      None

file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

This class Represents a call to git
    

   def __init__

      None

   def clone

      None

   def delete

      None

file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

Freebsd specific commands go here

####class pkg####

Freebsd package commands go here

####class jails####

Freebsd jail management commands go here

   def __init__

      None

   def jls

      None

   def jexec

      None

   def fetch

      None

   def __init__

      None

   def install

      None

   def __init__

      None

file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####

None

####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    

   def __new__

      None

   def deco

      None

   def __init__

      None

   def wrapper

      None

file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

This class Represents an example
    

   def __init__

      None

   def set

      None

file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

General nix system commands go here

   def __init__

      None

   def shell

      None

   def rsync

      None

file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

This class can perform ssh commands

   def __init__

      None

   def cmd

      None

file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

This class Represents an example
    

   def __init__

      None

   def runme

      None

file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

This class handles all rest actions

   def __init__

      None

   def send

      None

file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####

None

   def __init__

      None

   def add_obj

      None

   def IF

      None

file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

   def _has_keys

      Collect all environment variables
@param str: command string

   def _sanitize

      Replace all environment variables into command
@param str: command string

   def cmd

      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.

####class Action####

Object containing instructions to create and execute actions

   def __init__

      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug

   def to_obj

      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

   def add

      Append an action obj to chain

__param action_obj__  Obj

   def insert

      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj

   def get_index

      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage

   def __init__

      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj

   def __repr__

      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)

   def set_ignore

      catch the ignore parameter and delete it in defaults

   def get_receipt

      return a dictionary of all Action info

   def pprint

      print state about the object pretty

__param title__  String
__param footer__  String

   def _init_instance

      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.

   def execute

      execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####

None

####class Commit_actions####

This class handles all commit type actions
    

####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj

####class Remote_actions####

This class handles all remote actions
    

   def __init__

      Initialize Repo actions
        

   def _set_ssh_config

      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 

   def _set_dirs

      None

   def attach

      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 

   def _initial_commit

      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md

   def init

      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git

   def clone

      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 

   def untracked_files

      list all untracked files
@return: list of untracked files

   def __init__

      None

   def commit

      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure

   def cherry_pick

      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 

   def diff_tree

      None

   def search_log

      None

   def add

      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure

   def __init__

      None

   def branch

      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  

   def branch_from

      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name

   def branch_is

      provides the current branch
@return: the current branch

   def branch_list

      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 

   def has_reference

      Search for reference
@param branch_name__ string of branch name
@return__  reference obj

   def has_head

      Search for branch head
@param branch_name__ string of branch name
@return__  head obj

   def checkout

      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  

   def push

      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def remote_delete

      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def delete

      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def __init__

      None

   def list

      None

   def has_remote

      None

   def add

      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fork_sync

      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fetch

      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.

   def __init__

      Constructor

__param debug__  Bool

   def set

      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value

   def get

      get an environment variable

__param key__  String

   def sanitize

      sanitizes environment variables in a given values

__param values__  List

   def _sanitize

      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

This class represents a remote machine
using SSH to perform all needed actions

   def __init__

      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server

   def is_alive

      Pings the remote to make sure its a valid address
@return: boolean

   def is_alive_poll

      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean

   def is_writable

      Check to make sure the file system is writable
@return: boolean

   def is_writable_poll

      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean

   def has_access

      Does a key already exist on the remote?
@return: boolean

   def has_file

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file

   def has_dir

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean

   def remove

      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean

   def move

      Perform a move operation
        

   def copy

      Perform a copy operation
        

   def set_rsa

      Put a rsa key on the remote
@return: None

   def cmd

      Runs a shell command on the remote
@return: session info

   def find

      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session

   def os_type

      Gets the os type of the system
@return: returns os string

   def onefs_version

      None

   def get_MD5

      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string

   def _clean_MD5

      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

   def waitfor

      poll the child for input

__param fd__  forked process

   def event

      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair

   def set_rsa

      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user

   def create_rsa_public

      generate a public key from the private key

__param rsa_private__  path to private key

   def ssh

      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run

   def rsync

      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src

   def shell

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict

   def _exit_clean

      cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####

None

   def __init__

      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>

   def send

      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code

   def post_multipart

      None

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

   def menu

      None

   def parse_envs

      None

   def main

      None

file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

This is the entry point from the cli and runs drives components

   def __init__

      Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info

   def read_config

      Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict

   def _read_yaml

      Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict

   def _read_json

      Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict

   def add_envs

      Overrides environment variables from cli

__param **envs__  dictionary of environment variables

   def set_envs

      sets environment variables inside of manifest

   def load_actions

      loads actions in to chain resolves yaml/json to a object

   def execute_actions

      Executes all action objects
        

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

This class represents a receipt maker class
    

   def __init__

      None

   def on_actions

      None

   def custom

      None

file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

This class Represents a call to git
    

   def __init__

      None

   def clone

      None

   def delete

      None

file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

Freebsd specific commands go here

####class pkg####

Freebsd package commands go here

####class jails####

Freebsd jail management commands go here

   def __init__

      None

   def jls

      None

   def jexec

      None

   def fetch

      None

   def __init__

      None

   def install

      None

   def __init__

      None

file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####

None

####class Plugin####

This is the base class for plugin which all plugins must inherit from.
    

   def __new__

      None

   def deco

      None

   def __init__

      None

   def wrapper

      None

file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

This class Represents an example
    

   def __init__

      None

   def set

      None

file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

General nix system commands go here

   def __init__

      None

   def shell

      None

   def rsync

      None

file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

This class can perform ssh commands

   def __init__

      None

   def cmd

      None

file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

This class Represents an example
    

   def __init__

      None

   def runme

      None

file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

This class handles all rest actions

   def __init__

      None

   def send

      None

file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####

None

   def __init__

      None

   def add_obj

      None

   def IF

      None

file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

   def _has_keys

      Collect all environment variables
@param str: command string

   def _sanitize

      Replace all environment variables into command
@param str: command string

   def cmd

      Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states.

####class Action####

Object containing instructions to create and execute actions

   def __init__

      Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug

   def to_obj

      Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment.

   def add

      Append an action obj to chain

__param action_obj__  Obj

   def insert

      Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj

   def get_index

      Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage

   def __init__

      Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj

   def __repr__

      Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self)

   def set_ignore

      catch the ignore parameter and delete it in defaults

   def get_receipt

      return a dictionary of all Action info

   def pprint

      print state about the object pretty

__param title__  String
__param footer__  String

   def _init_instance

      Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run.

   def execute

      execute the instruction
        

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####

None

####class Commit_actions####

This class handles all commit type actions
    

####class Branch_actions####

This class handles all branch related actions
@requires: Repo obj

####class Remote_actions####

This class handles all remote actions
    

   def __init__

      Initialize Repo actions
        

   def _set_ssh_config

      This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com 

   def _set_dirs

      None

   def attach

      attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure 

   def _initial_commit

      To fully init an empty repo you need an initial commit, which in this case
is an empty README.md

   def init

      Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git

   def clone

      Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure 

   def untracked_files

      list all untracked files
@return: list of untracked files

   def __init__

      None

   def commit

      Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure

   def cherry_pick

      Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False 

   def diff_tree

      None

   def search_log

      None

   def add

      adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure

   def __init__

      None

   def branch

      Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure  

   def branch_from

      Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name

   def branch_is

      provides the current branch
@return: the current branch

   def branch_list

      provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects 

   def has_reference

      Search for reference
@param branch_name__ string of branch name
@return__  reference obj

   def has_head

      Search for branch head
@param branch_name__ string of branch name
@return__  head obj

   def checkout

      checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure  

   def push

      Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def remote_delete

      Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def delete

      Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean

   def __init__

      None

   def list

      None

   def has_remote

      None

   def add

      add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fork_sync

      Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False 

   def fetch

      Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean  

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager.

   def __init__

      Constructor

__param debug__  Bool

   def set

      set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value

   def get

      get an environment variable

__param key__  String

   def sanitize

      sanitizes environment variables in a given values

__param values__  List

   def _sanitize

      Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

This class represents a remote machine
using SSH to perform all needed actions

   def __init__

      Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server

   def is_alive

      Pings the remote to make sure its a valid address
@return: boolean

   def is_alive_poll

      Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean

   def is_writable

      Check to make sure the file system is writable
@return: boolean

   def is_writable_poll

      Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean

   def has_access

      Does a key already exist on the remote?
@return: boolean

   def has_file

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file

   def has_dir

      Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean

   def remove

      Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean

   def move

      Perform a move operation
        

   def copy

      Perform a copy operation
        

   def set_rsa

      Put a rsa key on the remote
@return: None

   def cmd

      Runs a shell command on the remote
@return: session info

   def find

      Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session

   def os_type

      Gets the os type of the system
@return: returns os string

   def onefs_version

      None

   def get_MD5

      gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string

   def _clean_MD5

      private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

   def waitfor

      poll the child for input

__param fd__  forked process

   def event

      find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair

   def set_rsa

      logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user

   def create_rsa_public

      generate a public key from the private key

__param rsa_private__  path to private key

   def ssh

      Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run

   def rsync

      Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src

   def shell

      Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict

   def _exit_clean

      cleans .tmp_shell files before exit

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####

None

   def __init__

      Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password>

   def send

      Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code

   def post_multipart

      None

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu

 None 

 def parse_envs

 None 

 def main

 None 

file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info 

 def read_config

 Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_yaml

 Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_json

 Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict 

 def add_envs

 Overrides environment variables from cli

__param **envs__  dictionary of environment variables 

 def set_envs

 sets environment variables inside of manifest 

 def load_actions

 loads actions in to chain resolves yaml/json to a object 

 def execute_actions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init

 None 

 def on_actions

 None 

 def custom

 None 

file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init

 None 

 def clone

 None 

 def delete

 None 

file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init

 None 

 def jls

 None 

 def jexec

 None 

 def fetch

 None 

 def init

 None 

 def install

 None 

 def init

 None 

file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####

 None 

####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new

 None 

 def deco

 None 

 def init

 None 

 def wrapper

 None 

file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init

 None 

 def set

 None 

file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init

 None 

 def shell

 None 

 def rsync

 None 

file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init

 None 

 def cmd

 None 

file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init

 None 

 def runme

 None 

file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init

 None 

 def send

 None 

file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####

 None 

 def init

 None 

 def add_obj

 None 

 def IF

 None 

file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def _has_keys

 Collect all environment variables
@param str: command string 

 def _sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug 

 def to_obj

 Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

__param action_obj__  Obj 

 def insert

 Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj 

 def get_index

 Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage 

 def init

 Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj 

 def repr

 Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self) 

 def set_ignore

 catch the ignore parameter and delete it in defaults 

 def get_receipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

__param title__  String
__param footer__  String 

 def _init_instance

 Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####

 None 

####class Commit_actions####

 This class handles all commit type actions
     

####class Branch_actions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remote_actions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def _set_ssh_config

 This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com  

 def _set_dirs

 None 

 def attach

 attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure  

 def _initial_commit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure  

 def untracked_files

 list all untracked files
@return: list of untracked files 

 def init

 None 

 def commit

 Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure 

 def cherry_pick

 Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False  

 def diff_tree

 None 

 def search_log

 None 

 def add

 adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure 

 def init

 None 

 def branch

 Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure   

 def branch_from

 Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name 

 def branch_is

 provides the current branch
@return: the current branch 

 def branch_list

 provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects  

 def has_reference

 Search for reference
@param branch_name__ string of branch name
@return__  reference obj 

 def has_head

 Search for branch head
@param branch_name__ string of branch name
@return__  head obj 

 def checkout

 checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def remote_delete

 Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def init

 None 

 def list

 None 

 def has_remote

 None 

 def add

 add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fork_sync

 Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fetch

 Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

__param debug__  Bool 

 def set

 set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

__param key__  String 

 def sanitize

 sanitizes environment variables in a given values

__param values__  List 

 def _sanitize

 Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server 

 def is_alive

 Pings the remote to make sure its a valid address
@return: boolean 

 def is_alive_poll

 Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean 

 def is_writable

 Check to make sure the file system is writable
@return: boolean 

 def is_writable_poll

 Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean 

 def has_access

 Does a key already exist on the remote?
@return: boolean 

 def has_file

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file 

 def has_dir

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def set_rsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session 

 def os_type

 Gets the os type of the system
@return: returns os string 

 def onefs_version

 None 

 def get_MD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def _clean_MD5

 private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

__param fd__  forked process 

 def event

 find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair 

 def set_rsa

 logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user 

 def create_rsa_public

 generate a public key from the private key

__param rsa_private__  path to private key 

 def ssh

 Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict 

 def _exit_clean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####

 None 

 def init

 Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password> 

 def send

 Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code 

 def post_multipart

 None 

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu

 None 

 def parse_envs

 None 

 def main

 None 

file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info 

 def read_config

 Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_yaml

 Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_json

 Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict 

 def add_envs

 Overrides environment variables from cli

__param **envs__  dictionary of environment variables 

 def set_envs

 sets environment variables inside of manifest 

 def load_actions

 loads actions in to chain resolves yaml/json to a object 

 def execute_actions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init

 None 

 def on_actions

 None 

 def custom

 None 

file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init

 None 

 def clone

 None 

 def delete

 None 

file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init

 None 

 def jls

 None 

 def jexec

 None 

 def fetch

 None 

 def init

 None 

 def install

 None 

 def init

 None 

file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####

 None 

####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new

 None 

 def deco

 None 

 def init

 None 

 def wrapper

 None 

file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init

 None 

 def set

 None 

file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init

 None 

 def shell

 None 

 def rsync

 None 

file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init

 None 

 def cmd

 None 

file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init

 None 

 def runme

 None 

file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init

 None 

 def send

 None 

file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####

 None 

 def init

 None 

 def add_obj

 None 

 def IF

 None 

file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def _has_keys

 Collect all environment variables
@param str: command string 

 def _sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug 

 def to_obj

 Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

__param action_obj__  Obj 

 def insert

 Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj 

 def get_index

 Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage 

 def init

 Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj 

 def repr

 Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self) 

 def set_ignore

 catch the ignore parameter and delete it in defaults 

 def get_receipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

__param title__  String
__param footer__  String 

 def _init_instance

 Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####

 None 

####class Commit_actions####

 This class handles all commit type actions
     

####class Branch_actions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remote_actions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def _set_ssh_config

 This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com  

 def _set_dirs

 None 

 def attach

 attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure  

 def _initial_commit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure  

 def untracked_files

 list all untracked files
@return: list of untracked files 

 def init

 None 

 def commit

 Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure 

 def cherry_pick

 Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False  

 def diff_tree

 None 

 def search_log

 None 

 def add

 adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure 

 def init

 None 

 def branch

 Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure   

 def branch_from

 Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name 

 def branch_is

 provides the current branch
@return: the current branch 

 def branch_list

 provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects  

 def has_reference

 Search for reference
@param branch_name__ string of branch name
@return__  reference obj 

 def has_head

 Search for branch head
@param branch_name__ string of branch name
@return__  head obj 

 def checkout

 checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def remote_delete

 Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def init

 None 

 def list

 None 

 def has_remote

 None 

 def add

 add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fork_sync

 Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fetch

 Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

__param debug__  Bool 

 def set

 set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

__param key__  String 

 def sanitize

 sanitizes environment variables in a given values

__param values__  List 

 def _sanitize

 Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server 

 def is_alive

 Pings the remote to make sure its a valid address
@return: boolean 

 def is_alive_poll

 Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean 

 def is_writable

 Check to make sure the file system is writable
@return: boolean 

 def is_writable_poll

 Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean 

 def has_access

 Does a key already exist on the remote?
@return: boolean 

 def has_file

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file 

 def has_dir

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def set_rsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session 

 def os_type

 Gets the os type of the system
@return: returns os string 

 def onefs_version

 None 

 def get_MD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def _clean_MD5

 private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

__param fd__  forked process 

 def event

 find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair 

 def set_rsa

 logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user 

 def create_rsa_public

 generate a public key from the private key

__param rsa_private__  path to private key 

 def ssh

 Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict 

 def _exit_clean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####

 None 

 def init

 Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password> 

 def send

 Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code 

 def post_multipart

 None 

file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu


 def parse_envs


 def main


file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info 

 def read_config

 Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_yaml

 Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_json

 Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict 

 def add_envs

 Overrides environment variables from cli

__param **envs__  dictionary of environment variables 

 def set_envs

 sets environment variables inside of manifest 

 def load_actions

 loads actions in to chain resolves yaml/json to a object 

 def execute_actions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init


 def on_actions


 def custom


file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init


 def clone


 def delete


file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init


 def jls


 def jexec


 def fetch


 def init


 def install


 def init


file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####


####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new


 def deco


 def init


 def wrapper


file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init


 def set


file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init


 def shell


 def rsync


file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init


 def cmd


file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init


 def runme


file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init


 def send


file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####


 def init


 def add_obj


 def IF


file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def _has_keys

 Collect all environment variables
@param str: command string 

 def _sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug 

 def to_obj

 Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

__param action_obj__  Obj 

 def insert

 Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj 

 def get_index

 Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage 

 def init

 Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj 

 def repr

 Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self) 

 def set_ignore

 catch the ignore parameter and delete it in defaults 

 def get_receipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

__param title__  String
__param footer__  String 

 def _init_instance

 Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####


####class Commit_actions####

 This class handles all commit type actions
     

####class Branch_actions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remote_actions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def _set_ssh_config

 This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com  

 def _set_dirs


 def attach

 attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure  

 def _initial_commit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure  

 def untracked_files

 list all untracked files
@return: list of untracked files 

 def init


 def commit

 Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure 

 def cherry_pick

 Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False  

 def diff_tree


 def search_log


 def add

 adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure 

 def init


 def branch

 Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure   

 def branch_from

 Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name 

 def branch_is

 provides the current branch
@return: the current branch 

 def branch_list

 provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects  

 def has_reference

 Search for reference
@param branch_name__ string of branch name
@return__  reference obj 

 def has_head

 Search for branch head
@param branch_name__ string of branch name
@return__  head obj 

 def checkout

 checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def remote_delete

 Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def init


 def list


 def has_remote


 def add

 add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fork_sync

 Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fetch

 Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

__param debug__  Bool 

 def set

 set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

__param key__  String 

 def sanitize

 sanitizes environment variables in a given values

__param values__  List 

 def _sanitize

 Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server 

 def is_alive

 Pings the remote to make sure its a valid address
@return: boolean 

 def is_alive_poll

 Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean 

 def is_writable

 Check to make sure the file system is writable
@return: boolean 

 def is_writable_poll

 Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean 

 def has_access

 Does a key already exist on the remote?
@return: boolean 

 def has_file

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file 

 def has_dir

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def set_rsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session 

 def os_type

 Gets the os type of the system
@return: returns os string 

 def onefs_version


 def get_MD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def _clean_MD5

 private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

__param fd__  forked process 

 def event

 find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair 

 def set_rsa

 logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user 

 def create_rsa_public

 generate a public key from the private key

__param rsa_private__  path to private key 

 def ssh

 Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict 

 def _exit_clean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####


 def init

 Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password> 

 def send

 Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code 

 def post_multipart


file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**

      

file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu


 def parse_envs


 def main


file @ **/goephor/core/__init__.py**

      None

file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info 

 def read_config

 Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_yaml

 Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_json

 Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict 

 def add_envs

 Overrides environment variables from cli

__param **envs__  dictionary of environment variables 

 def set_envs

 sets environment variables inside of manifest 

 def load_actions

 loads actions in to chain resolves yaml/json to a object 

 def execute_actions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init


 def on_actions


 def custom


file @ **/goephor/core/plugins/__init__.py**

      None

file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init


 def clone


 def delete


file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init


 def jls


 def jexec


 def fetch


 def init


 def install


 def init


file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####


####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new


 def deco


 def init


 def wrapper


file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init


 def set


file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init


 def shell


 def rsync


file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init


 def cmd


file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init


 def runme


file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init


 def send


file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####


 def init


 def add_obj


 def IF


file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def _has_keys

 Collect all environment variables
@param str: command string 

 def _sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug 

 def to_obj

 Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

__param action_obj__  Obj 

 def insert

 Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj 

 def get_index

 Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage 

 def init

 Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj 

 def repr

 Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self) 

 def set_ignore

 catch the ignore parameter and delete it in defaults 

 def get_receipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

__param title__  String
__param footer__  String 

 def _init_instance

 Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####


####class Commit_actions####

 This class handles all commit type actions
     

####class Branch_actions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remote_actions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def _set_ssh_config

 This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com  

 def _set_dirs


 def attach

 attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure  

 def _initial_commit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure  

 def untracked_files

 list all untracked files
@return: list of untracked files 

 def init


 def commit

 Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure 

 def cherry_pick

 Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False  

 def diff_tree


 def search_log


 def add

 adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure 

 def init


 def branch

 Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure   

 def branch_from

 Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name 

 def branch_is

 provides the current branch
@return: the current branch 

 def branch_list

 provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects  

 def has_reference

 Search for reference
@param branch_name__ string of branch name
@return__  reference obj 

 def has_head

 Search for branch head
@param branch_name__ string of branch name
@return__  head obj 

 def checkout

 checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def remote_delete

 Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def init


 def list


 def has_remote


 def add

 add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fork_sync

 Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fetch

 Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**

      None

file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

__param debug__  Bool 

 def set

 set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

__param key__  String 

 def sanitize

 sanitizes environment variables in a given values

__param values__  List 

 def _sanitize

 Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server 

 def is_alive

 Pings the remote to make sure its a valid address
@return: boolean 

 def is_alive_poll

 Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean 

 def is_writable

 Check to make sure the file system is writable
@return: boolean 

 def is_writable_poll

 Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean 

 def has_access

 Does a key already exist on the remote?
@return: boolean 

 def has_file

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file 

 def has_dir

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def set_rsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session 

 def os_type

 Gets the os type of the system
@return: returns os string 

 def onefs_version


 def get_MD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def _clean_MD5

 private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

__param fd__  forked process 

 def event

 find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair 

 def set_rsa

 logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user 

 def create_rsa_public

 generate a public key from the private key

__param rsa_private__  path to private key 

 def ssh

 Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict 

 def _exit_clean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####


 def init

 Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password> 

 def send

 Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code 

 def post_multipart


file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu


 def parse_envs


 def main


file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info 

 def read_config

 Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_yaml

 Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_json

 Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict 

 def add_envs

 Overrides environment variables from cli

__param **envs__  dictionary of environment variables 

 def set_envs

 sets environment variables inside of manifest 

 def load_actions

 loads actions in to chain resolves yaml/json to a object 

 def execute_actions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init


 def on_actions


 def custom


file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init


 def clone


 def delete


file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init


 def jls


 def jexec


 def fetch


 def init


 def install


 def init


file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####


####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new


 def deco


 def init


 def wrapper


file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init


 def set


file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init


 def shell


 def rsync


file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init


 def cmd


file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init


 def runme


file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init


 def send


file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####


 def init


 def add_obj


 def IF


file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def _has_keys

 Collect all environment variables
@param str: command string 

 def _sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug 

 def to_obj

 Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

__param action_obj__  Obj 

 def insert

 Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj 

 def get_index

 Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage 

 def init

 Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj 

 def repr

 Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self) 

 def set_ignore

 catch the ignore parameter and delete it in defaults 

 def get_receipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

__param title__  String
__param footer__  String 

 def _init_instance

 Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####


####class Commit_actions####

 This class handles all commit type actions
     

####class Branch_actions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remote_actions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def _set_ssh_config

 This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com  

 def _set_dirs


 def attach

 attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure  

 def _initial_commit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure  

 def untracked_files

 list all untracked files
@return: list of untracked files 

 def init


 def commit

 Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure 

 def cherry_pick

 Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False  

 def diff_tree


 def search_log


 def add

 adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure 

 def init


 def branch

 Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure   

 def branch_from

 Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name 

 def branch_is

 provides the current branch
@return: the current branch 

 def branch_list

 provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects  

 def has_reference

 Search for reference
@param branch_name__ string of branch name
@return__  reference obj 

 def has_head

 Search for branch head
@param branch_name__ string of branch name
@return__  head obj 

 def checkout

 checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def remote_delete

 Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def init


 def list


 def has_remote


 def add

 add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fork_sync

 Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fetch

 Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

__param debug__  Bool 

 def set

 set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

__param key__  String 

 def sanitize

 sanitizes environment variables in a given values

__param values__  List 

 def _sanitize

 Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server 

 def is_alive

 Pings the remote to make sure its a valid address
@return: boolean 

 def is_alive_poll

 Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean 

 def is_writable

 Check to make sure the file system is writable
@return: boolean 

 def is_writable_poll

 Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean 

 def has_access

 Does a key already exist on the remote?
@return: boolean 

 def has_file

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file 

 def has_dir

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def set_rsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session 

 def os_type

 Gets the os type of the system
@return: returns os string 

 def onefs_version


 def get_MD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def _clean_MD5

 private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

__param fd__  forked process 

 def event

 find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair 

 def set_rsa

 logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user 

 def create_rsa_public

 generate a public key from the private key

__param rsa_private__  path to private key 

 def ssh

 Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict 

 def _exit_clean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####


 def init

 Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password> 

 def send

 Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code 

 def post_multipart


file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu


 def parse_envs


 def main


file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info 

 def read_config

 Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_yaml

 Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict 

 def _read_json

 Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict 

 def add_envs

 Overrides environment variables from cli

__param **envs__  dictionary of environment variables 

 def set_envs

 sets environment variables inside of manifest 

 def load_actions

 loads actions in to chain resolves yaml/json to a object 

 def execute_actions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init


 def on_actions


 def custom


file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init


 def clone


 def delete


file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init


 def jls


 def jexec


 def fetch


 def init


 def install


 def init


file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####


####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new


 def deco


 def init


 def wrapper


file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init


 def set


file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init


 def shell


 def rsync


file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init


 def cmd


file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init


 def runme


file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init


 def send


file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####


 def init


 def add_obj


 def IF


file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def _has_keys

 Collect all environment variables
@param str: command string 

 def _sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug 

 def to_obj

 Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

__param action_obj__  Obj 

 def insert

 Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj 

 def get_index

 Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage 

 def init

 Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj 

 def repr

 Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self) 

 def set_ignore

 catch the ignore parameter and delete it in defaults 

 def get_receipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

__param title__  String
__param footer__  String 

 def _init_instance

 Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repo_actions####


####class Commit_actions####

 This class handles all commit type actions
     

####class Branch_actions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remote_actions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def _set_ssh_config

 This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com  

 def _set_dirs


 def attach

 attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure  

 def _initial_commit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure  

 def untracked_files

 list all untracked files
@return: list of untracked files 

 def init


 def commit

 Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure 

 def cherry_pick

 Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False  

 def diff_tree


 def search_log


 def add

 adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure 

 def init


 def branch

 Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure   

 def branch_from

 Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name 

 def branch_is

 provides the current branch
@return: the current branch 

 def branch_list

 provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects  

 def has_reference

 Search for reference
@param branch_name__ string of branch name
@return__  reference obj 

 def has_head

 Search for branch head
@param branch_name__ string of branch name
@return__  head obj 

 def checkout

 checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def remote_delete

 Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def init


 def list


 def has_remote


 def add

 add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fork_sync

 Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fetch

 Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

__param debug__  Bool 

 def set

 set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

__param key__  String 

 def sanitize

 sanitizes environment variables in a given values

__param values__  List 

 def _sanitize

 Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server 

 def is_alive

 Pings the remote to make sure its a valid address
@return: boolean 

 def is_alive_poll

 Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean 

 def is_writable

 Check to make sure the file system is writable
@return: boolean 

 def is_writable_poll

 Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean 

 def has_access

 Does a key already exist on the remote?
@return: boolean 

 def has_file

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file 

 def has_dir

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def set_rsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session 

 def os_type

 Gets the os type of the system
@return: returns os string 

 def onefs_version


 def get_MD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def _clean_MD5

 private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

__param fd__  forked process 

 def event

 find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair 

 def set_rsa

 logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user 

 def create_rsa_public

 generate a public key from the private key

__param rsa_private__  path to private key 

 def ssh

 Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict 

 def _exit_clean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####


 def init

 Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password> 

 def send

 Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code 

 def post_multipart


file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu


 def parseenvs


 def main


file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info 

 def readconfig

 Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict 

 def readyaml

 Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict 

 def readjson

 Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict 

 def addenvs

 Overrides environment variables from cli

__param **envs__  dictionary of environment variables 

 def setenvs

 sets environment variables inside of manifest 

 def loadactions

 loads actions in to chain resolves yaml/json to a object 

 def executeactions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init


 def onactions


 def custom


file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init


 def clone


 def delete


file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init


 def jls


 def jexec


 def fetch


 def init


 def install


 def init


file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####


####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new


 def deco


 def init


 def wrapper


file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init


 def set


file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init


 def shell


 def rsync


file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init


 def cmd


file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init


 def runme


file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init


 def send


file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####


 def init


 def addobj


 def IF


file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def haskeys

 Collect all environment variables
@param str: command string 

 def sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug 

 def toobj

 Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

__param action_obj__  Obj 

 def insert

 Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj 

 def getindex

 Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage 

 def init

 Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj 

 def repr

 Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self) 

 def setignore

 catch the ignore parameter and delete it in defaults 

 def getreceipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

__param title__  String
__param footer__  String 

 def initinstance

 Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repoactions####


####class Commitactions####

 This class handles all commit type actions
     

####class Branchactions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remoteactions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def setsshconfig

 This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com  

 def setdirs


 def attach

 attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure  

 def initialcommit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure  

 def untrackedfiles

 list all untracked files
@return: list of untracked files 

 def init


 def commit

 Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure 

 def cherrypick

 Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False  

 def difftree


 def searchlog


 def add

 adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure 

 def init


 def branch

 Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure   

 def branchfrom

 Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name 

 def branchis

 provides the current branch
@return: the current branch 

 def branchlist

 provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects  

 def hasreference

 Search for reference
@param branch_name__ string of branch name
@return__  reference obj 

 def hashead

 Search for branch head
@param branch_name__ string of branch name
@return__  head obj 

 def checkout

 checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def remotedelete

 Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def init


 def list


 def hasremote


 def add

 add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def forksync

 Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fetch

 Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

__param debug__  Bool 

 def set

 set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

__param key__  String 

 def sanitize

 sanitizes environment variables in a given values

__param values__  List 

 def sanitize

 Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server 

 def isalive

 Pings the remote to make sure its a valid address
@return: boolean 

 def isalivepoll

 Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean 

 def iswritable

 Check to make sure the file system is writable
@return: boolean 

 def iswritablepoll

 Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean 

 def hasaccess

 Does a key already exist on the remote?
@return: boolean 

 def hasfile

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file 

 def hasdir

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def setrsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session 

 def ostype

 Gets the os type of the system
@return: returns os string 

 def onefsversion


 def getMD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def cleanMD5

 private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

__param fd__  forked process 

 def event

 find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair 

 def setrsa

 logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user 

 def creatersapublic

 generate a public key from the private key

__param rsa_private__  path to private key 

 def ssh

 Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict 

 def exitclean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####


 def init

 Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password> 

 def send

 Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code 

 def postmultipart


file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu


 def parseenvs


 def main


file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

__param config_file__  path to yaml manifest
__param verbose__  print general run info
__param debug__  print debug info 

 def readconfig

 Allows for reading .yaml or .json files

__param config_file__  defines all actions in a build
__return__  dict 

 def readyaml

 Reads in the yaml config

__param config_file__  defines all actions in a build
__return__  dict 

 def readjson

 Reads in the json config

__param config_file__  defines all actions in a build
__return__  dict 

 def addenvs

 Overrides environment variables from cli

__param **envs__  dictionary of environment variables 

 def setenvs

 sets environment variables inside of manifest 

 def loadactions

 loads actions in to chain resolves yaml/json to a object 

 def executeactions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init


 def onactions


 def custom


file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init


 def clone


 def delete


file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init


 def jls


 def jexec


 def fetch


 def init


 def install


 def init


file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####


####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new


 def deco


 def init


 def wrapper


file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init


 def set


file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init


 def shell


 def rsync


file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init


 def cmd


file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init


 def runme


file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init


 def send


file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####


 def init


 def addobj


 def IF


file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def haskeys

 Collect all environment variables
@param str: command string 

 def sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server__ server address
@param cmd__  string shell command
@param rsa_private__ path to the private key file
@param user__  Username used to log into system
@param password__ Password used to log into system
@param strict__  boolean fail on error
@param verbose__ print out all debug messaging
@param show_cmd__  show the command given to remote server
@return__ session info
@note__  environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

__note__  This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

__param config__  nest dict from manifest
__param EnvManager__  Holds the state of the Environment
__param verbose__  set verbosity
__param debug__  set debug 

 def toobj

 Converts action dictionary to action obj

__param action__  base action dict
__param action_manager__  from chain.Run pass in Action_manager
__note__  We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

__param action_obj__  Obj 

 def insert

 Insert action object at a given index in the chain

__param index__  Int of chain
__param action_obj__  Obj 

 def getindex

 Get the index number of an action object in the chain

__param memory_address__  String, of object.__repr__(self)
__note__  See plugins.condition for usage 

 def init

 Constructor

__param name__  String, full resolve path
__param IMP__  String, import name
__param CLASS__  String, class name
__param DEF__  String, definition name
__param parameters__  list
__param defaults__  Dict
__param action_manager__  Obj 

 def repr

 Override container name so we can match the array in the chain

__note__  This is how we match chain to current plugin using object.__repr__(self) 

 def setignore

 catch the ignore parameter and delete it in defaults 

 def getreceipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

__param title__  String
__param footer__  String 

 def initinstance

 Initializes the class
__note__  we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repoactions####


####class Commitactions####

 This class handles all commit type actions
     

####class Branchactions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remoteactions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def setsshconfig

 This turns off host verification
@param ssh_config__ path to <user>/.ssh/config
@param git_host__  example. github.west.isilon.com  

 def setdirs


 def attach

 attach to a git repo on your local system
@param repo_path__ system path to repo
@return__  boolean, success/failure  

 def initialcommit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare__ boolean, default is False, creates a 'bare repo', to run like a src repo 
@return__  boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh__ provide the ssh full info example. git@github.west.isilon.com__ iitow/scm-tools.git
@return: boolean, success/failure  

 def untrackedfiles

 list all untracked files
@return: list of untracked files 

 def init


 def commit

 Commits changes
@param msg__ string, the commit message
@return__  boolean, success/failure 

 def cherrypick

 Cherry picks a commit
@param sha1_str__ sha1 string of commit
@return__  boolean True/False  

 def difftree


 def searchlog


 def add

 adds files to git index
@param file_name__ name of the file to commit
@return__  boolean, success/failure 

 def init


 def branch

 Creates a new local branch
@param branch_name__ string, name of the new branch to create it
@return__  boolean, success/failure   

 def branchfrom

 Create a branch from existing branch
@param src_branch__ original branch name
@param dest_branch__  new branch name 

 def branchis

 provides the current branch
@return: the current branch 

 def branchlist

 provides a list of all branches
@param verbose__ boolean, prints branches out
@return__  list of git.branch objects  

 def hasreference

 Search for reference
@param branch_name__ string of branch name
@return__  reference obj 

 def hashead

 Search for branch head
@param branch_name__ string of branch name
@return__  head obj 

 def checkout

 checks out a specific branch
@param branch_name__ string, branch you wish to checkout
@param remote__  remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def remotedelete

 Deletes branch from github remote
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name__ string branch name
@param remote__  remote reference  
@return: boolean 

 def init


 def list


 def hasremote


 def add

 add a remote to repo
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def forksync

 Syncs a fork of repo with another repository
@param remote__ remote url string example. git@github.west.isilon.com__ iitow/onefs.git
@param name__ reference to the remote example. upstream
@return__  boolean True/False  

 def fetch

 Fetch remote branches
@param remote__ repo url example. git@github.west.isilon.com__ isilon/onefs.git
@param name__ name of the remote
@param branch; branch to switch to when fetching
@param add_remote__  boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

__note__  This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

__param debug__  Bool 

 def set

 set an environment variable

__param key__  String
:param value__ String
__ param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

__param key__  String 

 def sanitize

 sanitizes environment variables in a given values

__param values__  List 

 def sanitize

 Replace all environment variables into command

__param stri__  String,Bool,Int
__note__  when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server__ server address
@param rsa_private__  path to the private key file
@param user__ Username used to log into system
@param password__  Password used to log into system
@param strict__ boolean fail on error
@param verbose__  print out all debug messaging
@param show_cmd: show the command given to remote server 

 def isalive

 Pings the remote to make sure its a valid address
@return: boolean 

 def isalivepoll

 Polls for a ping
@param timeout__ default 30 seconds
@return__  boolean 

 def iswritable

 Check to make sure the file system is writable
@return: boolean 

 def iswritablepoll

 Check to make sure file system is writable poll
@param timeout__ default 30 seconds
@return__  boolean 

 def hasaccess

 Does a key already exist on the remote?
@return: boolean 

 def hasfile

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file 

 def hasdir

 Does a file exist on the remote?
@param path__ path where file should exist
@param file__  name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path__path to file/dir to remove
@param recursive__  adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def setrsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path__ path where file should exist
@param file__  name of the file
@return: output from the session 

 def ostype

 Gets the os type of the system
@return: returns os string 

 def onefsversion


 def getMD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def cleanMD5

 private Cleans the md5 string produced
@param os_type__ type of operating system
@param output__  string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

__param fd__  forked process 

 def event

 find all output and inspect it for searches dict key & value

__param fd__  forked process
__param searches__  dictionary key value pair 

 def setrsa

 logs into system via ssh
and appends to authorized_keys using username password

__param     host__  name over the server
__param  rsa_pub__  absolute path to your id_rsa.pub
__param     user__  host login creds
:param password__ host login creds
__ param home_dir: home directory for user 

 def creatersapublic

 generate a public key from the private key

__param rsa_private__  path to private key 

 def ssh

 Run a single ssh command on a remote server

__param server__  username@servername
__param cmd__  single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

__param   server__  username@server
__param      src__  full path of src directory/file
__param     dest__  full path to dest directory
__param   option__  [pull] get file from a remote,
[push] put a file from your server into a remote
__param   remote__  [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
__param excludes__  exclude directory, or file from array
__note__  --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

__param cmd__  String command
__param verbose__ bool
__param strict__ bool will exit based on code if enabled
__return__   {command, stdout, code} as dict 

 def exitclean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####


 def init

 Generic class to handle All types of
Restful requests and basic authentication

__param base_url__ 
fully qualified path to api path
example__https__ //github.west.isilon.com/api/v3
__param auth_file__ 
a yaml file containing user__ <username> password__  <password> 

 def send

 Generic call to handle all types of restful requests

__param rest_action__ 
Possible option, 'GET','PUT','POST','PATCH'
__param url_ext__ 
added to base url example.https__//github.west.isilon.com/<url_ext>
__ param strict__
False, will permit errors as warning & return code,
True will exit with code
__ param Content_Type__
How info is formed, example application/xml
__ param verify__
Check for Certificates
__ return: String of content, or error exit code 

 def postmultipart


file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu


 def parseenvs


 def main


file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

**param config_file** path to yaml manifest
**param verbose** print general run info
**param debug** print debug info 

 def readconfig

 Allows for reading .yaml or .json files

**param config_file** defines all actions in a build
**return** dict 

 def readyaml

 Reads in the yaml config

**param config_file** defines all actions in a build
**return** dict 

 def readjson

 Reads in the json config

**param config_file** defines all actions in a build
**return** dict 

 def addenvs

 Overrides environment variables from cli

**param **envs** dictionary of environment variables 

 def setenvs

 sets environment variables inside of manifest 

 def loadactions

 loads actions in to chain resolves yaml/json to a object 

 def executeactions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init


 def onactions


 def custom


file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init


 def clone


 def delete


file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init


 def jls


 def jexec


 def fetch


 def init


 def install


 def init


file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####


####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new


 def deco


 def init


 def wrapper


file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init


 def set


file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init


 def shell


 def rsync


file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init


 def cmd


file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init


 def runme


file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init


 def send


file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####


 def init


 def addobj


 def IF


file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def haskeys

 Collect all environment variables
@param str: command string 

 def sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server** server address
@param cmd** string shell command
@param rsa_private** path to the private key file
@param user** Username used to log into system
@param password** Password used to log into system
@param strict** boolean fail on error
@param verbose** print out all debug messaging
@param show_cmd** show the command given to remote server
@return** session info
@note** environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

**note** This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

**param config** nest dict from manifest
**param EnvManager** Holds the state of the Environment
**param verbose** set verbosity
**param debug** set debug 

 def toobj

 Converts action dictionary to action obj

**param action** base action dict
**param action_manager** from chain.Run pass in Action_manager
**note** We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

**param action_obj** Obj 

 def insert

 Insert action object at a given index in the chain

**param index** Int of chain
**param action_obj** Obj 

 def getindex

 Get the index number of an action object in the chain

**param memory_address** String, of object.__repr__(self)
**note** See plugins.condition for usage 

 def init

 Constructor

**param name** String, full resolve path
**param IMP** String, import name
**param CLASS** String, class name
**param DEF** String, definition name
**param parameters** list
**param defaults** Dict
**param action_manager** Obj 

 def repr

 Override container name so we can match the array in the chain

**note** This is how we match chain to current plugin using object.__repr__(self) 

 def setignore

 catch the ignore parameter and delete it in defaults 

 def getreceipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

**param title** String
**param footer** String 

 def initinstance

 Initializes the class
**note** we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repoactions####


####class Commitactions####

 This class handles all commit type actions
     

####class Branchactions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remoteactions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def setsshconfig

 This turns off host verification
@param ssh_config** path to <user>/.ssh/config
@param git_host** example. github.west.isilon.com  

 def setdirs


 def attach

 attach to a git repo on your local system
@param repo_path** system path to repo
@return** boolean, success/failure  

 def initialcommit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare** boolean, default is False, creates a 'bare repo', to run like a src repo 
@return** boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh** provide the ssh full info example. git@github.west.isilon.com**iitow/scm-tools.git
@return: boolean, success/failure  

 def untrackedfiles

 list all untracked files
@return: list of untracked files 

 def init


 def commit

 Commits changes
@param msg** string, the commit message
@return** boolean, success/failure 

 def cherrypick

 Cherry picks a commit
@param sha1_str** sha1 string of commit
@return** boolean True/False  

 def difftree


 def searchlog


 def add

 adds files to git index
@param file_name** name of the file to commit
@return** boolean, success/failure 

 def init


 def branch

 Creates a new local branch
@param branch_name** string, name of the new branch to create it
@return** boolean, success/failure   

 def branchfrom

 Create a branch from existing branch
@param src_branch** original branch name
@param dest_branch** new branch name 

 def branchis

 provides the current branch
@return: the current branch 

 def branchlist

 provides a list of all branches
@param verbose** boolean, prints branches out
@return** list of git.branch objects  

 def hasreference

 Search for reference
@param branch_name** string of branch name
@return** reference obj 

 def hashead

 Search for branch head
@param branch_name** string of branch name
@return** head obj 

 def checkout

 checks out a specific branch
@param branch_name** string, branch you wish to checkout
@param remote** remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name** string branch name
@param remote** remote reference  
@return: boolean 

 def remotedelete

 Deletes branch from github remote
@param branch_name** string branch name
@param remote** remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name** string branch name
@param remote** remote reference  
@return: boolean 

 def init


 def list


 def hasremote


 def add

 add a remote to repo
@param remote** remote url string example. git@github.west.isilon.com**iitow/onefs.git
@param name** reference to the remote example. upstream
@return** boolean True/False  

 def forksync

 Syncs a fork of repo with another repository
@param remote** remote url string example. git@github.west.isilon.com**iitow/onefs.git
@param name** reference to the remote example. upstream
@return** boolean True/False  

 def fetch

 Fetch remote branches
@param remote** repo url example. git@github.west.isilon.com**isilon/onefs.git
@param name** name of the remote
@param branch; branch to switch to when fetching
@param add_remote** boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

**note** This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

**param debug** Bool 

 def set

 set an environment variable

**param key** String
:param value** String
**param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

**param key** String 

 def sanitize

 sanitizes environment variables in a given values

**param values** List 

 def sanitize

 Replace all environment variables into command

**param stri** String,Bool,Int
**note** when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server** server address
@param rsa_private** path to the private key file
@param user** Username used to log into system
@param password** Password used to log into system
@param strict** boolean fail on error
@param verbose** print out all debug messaging
@param show_cmd: show the command given to remote server 

 def isalive

 Pings the remote to make sure its a valid address
@return: boolean 

 def isalivepoll

 Polls for a ping
@param timeout** default 30 seconds
@return** boolean 

 def iswritable

 Check to make sure the file system is writable
@return: boolean 

 def iswritablepoll

 Check to make sure file system is writable poll
@param timeout** default 30 seconds
@return** boolean 

 def hasaccess

 Does a key already exist on the remote?
@return: boolean 

 def hasfile

 Does a file exist on the remote?
@param path** path where file should exist
@param file** name of the file 

 def hasdir

 Does a file exist on the remote?
@param path** path where file should exist
@param file** name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path**path to file/dir to remove
@param recursive** adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def setrsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path** path where file should exist
@param file** name of the file
@return: output from the session 

 def ostype

 Gets the os type of the system
@return: returns os string 

 def onefsversion


 def getMD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def cleanMD5

 private Cleans the md5 string produced
@param os_type** type of operating system
@param output** string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

**param fd** forked process 

 def event

 find all output and inspect it for searches dict key & value

**param fd** forked process
**param searches** dictionary key value pair 

 def setrsa

 logs into system via ssh
and appends to authorized_keys using username password

**param     host** name over the server
**param  rsa_pub** absolute path to your id_rsa.pub
**param     user** host login creds
:param password** host login creds
**param home_dir: home directory for user 

 def creatersapublic

 generate a public key from the private key

**param rsa_private** path to private key 

 def ssh

 Run a single ssh command on a remote server

**param server** username@servername
**param cmd** single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

**param   server** username@server
**param      src** full path of src directory/file
**param     dest** full path to dest directory
**param   option** [pull] get file from a remote,
[push] put a file from your server into a remote
**param   remote** [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
**param excludes** exclude directory, or file from array
**note** --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

**param cmd** String command
**param verbose**bool
**param strict**bool will exit based on code if enabled
**return**  {command, stdout, code} as dict 

 def exitclean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####


 def init

 Generic class to handle All types of
Restful requests and basic authentication

**param base_url**
fully qualified path to api path
example**https**//github.west.isilon.com/api/v3
**param auth_file**
a yaml file containing user** <username> password** <password> 

 def send

 Generic call to handle all types of restful requests

**param rest_action**
Possible option, 'GET','PUT','POST','PATCH'
**param url_ext**
added to base url example.https**//github.west.isilon.com/<url_ext>
**param strict**
False, will permit errors as warning & return code,
True will exit with code
**param Content_Type**
How info is formed, example application/xml
**param verify**
Check for Certificates
**return: String of content, or error exit code 

 def postmultipart


file @ **/goephor.py**

      Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

      Main entry for goephor

 def menu


 def parseenvs


 def main


file @ **/goephor/core/__init__.py**


file @ **/goephor/core/Chain.py**

      Created on Apr 25, 2016

:author: iitow

####class Run####

 This is the entry point from the cli and runs drives components 

 def init

 Constructor

**param config_file** path to yaml manifest
**param verbose** print general run info
**param debug** print debug info 

 def readconfig

 Allows for reading .yaml or .json files

**param config_file** defines all actions in a build
**return** dict 

 def readyaml

 Reads in the yaml config

**param config_file** defines all actions in a build
**return** dict 

 def readjson

 Reads in the json config

**param config_file** defines all actions in a build
**return** dict 

 def addenvs

 Overrides environment variables from cli

**param **envs** dictionary of environment variables 

 def setenvs

 sets environment variables inside of manifest 

 def loadactions

 loads actions in to chain resolves yaml/json to a object 

 def executeactions

 Executes all action objects
         

file @ **/goephor/core/plugins/receipt.py**

      Created on Apr 27, 2016

@author: iitow

####class maker####

 This class represents a receipt maker class
     

 def init


 def onactions


 def custom


file @ **/goephor/core/plugins/__init__.py**


file @ **/goephor/core/plugins/scm.py**

      Created on Apr 28, 2016

@author: iitow

####class git####

 This class Represents a call to git
     

 def init


 def clone


 def delete


file @ **/goephor/core/plugins/freebsd.py**

      Created on Apr 29, 2016

@author: iitow

####class terminal####

 Freebsd specific commands go here 

####class pkg####

 Freebsd package commands go here 

####class jails####

 Freebsd jail management commands go here 

 def init


 def jls


 def jexec


 def fetch


 def init


 def install


 def init


file @ **/goephor/core/plugins/pluginable.py**

      Created on Apr 25, 2016

@author: iitow

####class DecoMeta####


####class Plugin####

 This is the base class for plugin which all plugins must inherit from.
     

 def new


 def deco


 def init


 def wrapper


file @ **/goephor/core/plugins/environment.py**

      Created on Apr 27, 2016

@author: iitow

####class env####

 This class Represents an example
     

 def init


 def set


file @ **/goephor/core/plugins/system.py**

      Created on Apr 25, 2016

@author: iitow

####class terminal####

 General nix system commands go here 

 def init


 def shell


 def rsync


file @ **/goephor/core/plugins/remote.py**

      Created on Apr 28, 2016

@author: iitow

####class ssh####

 This class can perform ssh commands 

 def init


 def cmd


file @ **/goephor/core/plugins/example.py**

      Created on Apr 27, 2016

@author: iitow

####class example####

 This class Represents an example
     

 def init


 def runme


file @ **/goephor/core/plugins/http.py**

      Created on Apr 29, 2016

@author: iitow

####class rest####

 This class handles all rest actions 

 def init


 def send


file @ **/goephor/core/plugins/condition.py**

      Created on Apr 26, 2016

@author: iitow

####class statement####


 def init


 def addobj


 def IF


file @ **/goephor/core/plugins/remotable.py**

      Created on Jan 29, 2016

@author: iitow

 def haskeys

 Collect all environment variables
@param str: command string 

 def sanitize

 Replace all environment variables into command
@param str: command string 

 def cmd

 Initializes a Remote ssh session
@param server** server address
@param cmd** string shell command
@param rsa_private** path to the private key file
@param user** Username used to log into system
@param password** Password used to log into system
@param strict** boolean fail on error
@param verbose** print out all debug messaging
@param show_cmd** show the command given to remote server
@return** session info
@note** environment variables but be as follows ${var} to pass over to ssh 

file @ **/goephor/core/plugins/modules/action.py**

      Created on Apr 26, 2016

@author: iitow

####class Manager####

 This class manages state of action objects

**note** This is passed into each of the plugins and can be used to manage
Serveral states. 

####class Action####

 Object containing instructions to create and execute actions 

 def init

 Constructor

**param config** nest dict from manifest
**param EnvManager** Holds the state of the Environment
**param verbose** set verbosity
**param debug** set debug 

 def toobj

 Converts action dictionary to action obj

**param action** base action dict
**param action_manager** from chain.Run pass in Action_manager
**note** We initialize the action_manager in chain.Run and pass
the obj back to each Action Obj which gives the class full
access to initialize nest actions and have access to environment. 

 def add

 Append an action obj to chain

**param action_obj** Obj 

 def insert

 Insert action object at a given index in the chain

**param index** Int of chain
**param action_obj** Obj 

 def getindex

 Get the index number of an action object in the chain

**param memory_address** String, of object.__repr__(self)
**note** See plugins.condition for usage 

 def init

 Constructor

**param name** String, full resolve path
**param IMP** String, import name
**param CLASS** String, class name
**param DEF** String, definition name
**param parameters** list
**param defaults** Dict
**param action_manager** Obj 

 def repr

 Override container name so we can match the array in the chain

**note** This is how we match chain to current plugin using object.__repr__(self) 

 def setignore

 catch the ignore parameter and delete it in defaults 

 def getreceipt

 return a dictionary of all Action info 

 def pprint

 print state about the object pretty

**param title** String
**param footer** String 

 def initinstance

 Initializes the class
**note** we initialize the plugin class so we can pass info into action Obj before run. 

 def execute

 execute the instruction
         

file @ **/goephor/core/plugins/modules/git_kit.py**

      Created on Oct 8, 2015

@author: iitow

####class Repoactions####


####class Commitactions####

 This class handles all commit type actions
     

####class Branchactions####

 This class handles all branch related actions
@requires: Repo obj 

####class Remoteactions####

 This class handles all remote actions
     

 def init

 Initialize Repo actions
         

 def setsshconfig

 This turns off host verification
@param ssh_config** path to <user>/.ssh/config
@param git_host** example. github.west.isilon.com  

 def setdirs


 def attach

 attach to a git repo on your local system
@param repo_path** system path to repo
@return** boolean, success/failure  

 def initialcommit

 To fully init an empty repo you need an initial commit, which in this case
is an empty README.md 

 def init

 Initialize a new repo on your local system
@param set_bare** boolean, default is False, creates a 'bare repo', to run like a src repo 
@return** boolean, success/failure
@note: Shared repositories should always be created with the set_bare flag and
       should be stored in a directory called <projectname>.git 

 def clone

 Clone a repository from a remote location
@param remote_ssh** provide the ssh full info example. git@github.west.isilon.com**iitow/scm-tools.git
@return: boolean, success/failure  

 def untrackedfiles

 list all untracked files
@return: list of untracked files 

 def init


 def commit

 Commits changes
@param msg** string, the commit message
@return** boolean, success/failure 

 def cherrypick

 Cherry picks a commit
@param sha1_str** sha1 string of commit
@return** boolean True/False  

 def difftree


 def searchlog


 def add

 adds files to git index
@param file_name** name of the file to commit
@return** boolean, success/failure 

 def init


 def branch

 Creates a new local branch
@param branch_name** string, name of the new branch to create it
@return** boolean, success/failure   

 def branchfrom

 Create a branch from existing branch
@param src_branch** original branch name
@param dest_branch** new branch name 

 def branchis

 provides the current branch
@return: the current branch 

 def branchlist

 provides a list of all branches
@param verbose** boolean, prints branches out
@return** list of git.branch objects  

 def hasreference

 Search for reference
@param branch_name** string of branch name
@return** reference obj 

 def hashead

 Search for branch head
@param branch_name** string of branch name
@return** head obj 

 def checkout

 checks out a specific branch
@param branch_name** string, branch you wish to checkout
@param remote** remote name default is origin
@return: boolean, success/failure   

 def push

 Push branch to remote
@param branch_name** string branch name
@param remote** remote reference  
@return: boolean 

 def remotedelete

 Deletes branch from github remote
@param branch_name** string branch name
@param remote** remote reference  
@return: boolean 

 def delete

 Delete local branch
@param branch_name** string branch name
@param remote** remote reference  
@return: boolean 

 def init


 def list


 def hasremote


 def add

 add a remote to repo
@param remote** remote url string example. git@github.west.isilon.com**iitow/onefs.git
@param name** reference to the remote example. upstream
@return** boolean True/False  

 def forksync

 Syncs a fork of repo with another repository
@param remote** remote url string example. git@github.west.isilon.com**iitow/onefs.git
@param name** reference to the remote example. upstream
@return** boolean True/False  

 def fetch

 Fetch remote branches
@param remote** repo url example. git@github.west.isilon.com**isilon/onefs.git
@param name** name of the remote
@param branch; branch to switch to when fetching
@param add_remote** boolean add a remote
@return: boolean   

file @ **/goephor/core/plugins/modules/__init__.py**


file @ **/goephor/core/plugins/modules/environment.py**

      Created on Apr 26, 2016

@author: iitow

####class EnvManager####

 Management of runtime environment

**note** This is passed to each of the plugins when the action obj is initialized
Its contained within the action_manager. 

 def init

 Constructor

**param debug** Bool 

 def set

 set an environment variable

**param key** String
:param value** String
**param reset: Bool, if false it will not override an existing env value 

 def get

 get an environment variable

**param key** String 

 def sanitize

 sanitizes environment variables in a given values

**param values** List 

 def sanitize

 Replace all environment variables into command

**param stri** String,Bool,Int
**note** when nested environment variables are used in a striing convert all 

file @ **/goephor/core/plugins/modules/remote.py**

      Created on Nov 18, 2015

@author: iitow

####class Run####

 This class represents a remote machine
using SSH to perform all needed actions 

 def init

 Initializes a Remote session
@param server** server address
@param rsa_private** path to the private key file
@param user** Username used to log into system
@param password** Password used to log into system
@param strict** boolean fail on error
@param verbose** print out all debug messaging
@param show_cmd: show the command given to remote server 

 def isalive

 Pings the remote to make sure its a valid address
@return: boolean 

 def isalivepoll

 Polls for a ping
@param timeout** default 30 seconds
@return** boolean 

 def iswritable

 Check to make sure the file system is writable
@return: boolean 

 def iswritablepoll

 Check to make sure file system is writable poll
@param timeout** default 30 seconds
@return** boolean 

 def hasaccess

 Does a key already exist on the remote?
@return: boolean 

 def hasfile

 Does a file exist on the remote?
@param path** path where file should exist
@param file** name of the file 

 def hasdir

 Does a file exist on the remote?
@param path** path where file should exist
@param file** name of the file
@return boolean 

 def remove

 Remove a file or directory on remote
@param path**path to file/dir to remove
@param recursive** adds a -r to the rm command
@return: boolean 

 def move

 Perform a move operation
         

 def copy

 Perform a copy operation
         

 def setrsa

 Put a rsa key on the remote
@return: None 

 def cmd

 Runs a shell command on the remote
@return: session info 

 def find

 Finds a file on the remote system returns a list of values
@param path** path where file should exist
@param file** name of the file
@return: output from the session 

 def ostype

 Gets the os type of the system
@return: returns os string 

 def onefsversion


 def getMD5

 gets the md5sum of a file
Supports Freebsd and Linux
@return: md5 string 

 def cleanMD5

 private Cleans the md5 string produced
@param os_type** type of operating system
@param output** string from get_MD5 

file @ **/goephor/core/plugins/modules/terminal.py**

      Created on Nov 18, 2015

:author: iitow

 def waitfor

 poll the child for input

**param fd** forked process 

 def event

 find all output and inspect it for searches dict key & value

**param fd** forked process
**param searches** dictionary key value pair 

 def setrsa

 logs into system via ssh
and appends to authorized_keys using username password

**param     host** name over the server
**param  rsa_pub** absolute path to your id_rsa.pub
**param     user** host login creds
:param password** host login creds
**param home_dir: home directory for user 

 def creatersapublic

 generate a public key from the private key

**param rsa_private** path to private key 

 def ssh

 Run a single ssh command on a remote server

**param server** username@servername
**param cmd** single command you wish to run 

 def rsync

 Performs an rsync of files; requires ssh keys setup.

**param   server** username@server
**param      src** full path of src directory/file
**param     dest** full path to dest directory
**param   option** [pull] get file from a remote,
[push] put a file from your server into a remote
**param   remote** [True] assumes we are working with
a remote system, [False] assumes we are copying files locally
**param excludes** exclude directory, or file from array
**note** --delete will delete files on dest if it does not match src 

 def shell

 Run Shell commands  [Non Blocking, no Buffer, print live, log it]

**param cmd** String command
**param verbose**bool
**param strict**bool will exit based on code if enabled
**return**  {command, stdout, code} as dict 

 def exitclean

 cleans .tmp_shell files before exit 

file @ **/goephor/core/plugins/modules/http.py**

      Created on Jun 2, 2015

@author: iitow

####class Restful####


 def init

 Generic class to handle All types of
Restful requests and basic authentication

**param base_url**
fully qualified path to api path
example**https**//github.west.isilon.com/api/v3
**param auth_file**
a yaml file containing user** <username> password** <password> 

 def send

 Generic call to handle all types of restful requests

**param rest_action**
Possible option, 'GET','PUT','POST','PATCH'
**param url_ext**
added to base url example.https**//github.west.isilon.com/<url_ext>
**param strict**
False, will permit errors as warning & return code,
True will exit with code
**param Content_Type**
How info is formed, example application/xml
**param verify**
Check for Certificates
**return: String of content, or error exit code 

 def postmultipart

