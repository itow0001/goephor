SOME RANDOME
TEXT

file @ **/goephor.py**

   Created on Jan 9, 2016

:author: iitow
:note: Look to __main__.py for menu logic

file @ **/goephor/__init__.py**


file @ **/goephor/__main__.py**

   Main entry for goephor

 def menu

 None 

 def parseenvs

 None 

 def main

 None 

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

 None 

 def onactions

 None 

 def custom

 None 

file @ **/goephor/core/plugins/__init__.py**


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

 def addobj

 None 

 def IF

 None 

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

 None 

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

 None 

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

 None 

 def commit

 Commits changes
@param msg** string, the commit message
@return** boolean, success/failure 

 def cherrypick

 Cherry picks a commit
@param sha1_str** sha1 string of commit
@return** boolean True/False  

 def difftree

 None 

 def searchlog

 None 

 def add

 adds files to git index
@param file_name** name of the file to commit
@return** boolean, success/failure 

 def init

 None 

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

 None 

 def list

 None 

 def hasremote

 None 

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

 None 

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

 None 

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

 None 
