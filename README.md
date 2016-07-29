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
 File @ ***/goephor.py***

Created on Jan 9, 2016


**:author:** iitow

**:note:** Look to __main__.py for menu logic

**********************************************
 File @ ***/__init__.py***

None

**********************************************
 File @ ***/tests.py***

Created on May 4, 2016

**:author:** iitow

**:note:** All integration tests go here.

**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/__init__.py***

goephor __init__.py

**********************************************
 File @ ***/goephor/_version.py***

None

**********************************************
 File @ ***/goephor/__main__.py***

Main entry for goephor to menu here

**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/__init__.py***

Core __init__.py

**********************************************
 File @ ***/goephor/core/Chain.py***

Contained in this file is the main loops

**:author:** iitow

**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/receipt.py***

Created on Apr 27, 2016


**:author:** iitow

**********************************************
**********************************************

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
**********************************************

***def on_actions***:

This creates a receipt of all actions in the chain


**:param path:** String, system path to put receipt

**:param defaults:** additional params

**:example:**
```
- receipt.maker.on_actions:
    - "./receipt.yaml"
```
**********************************************

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
**********************************************

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
**********************************************

***def read***:

Reads in a custom receipt and generates environment variables

**:param defaults:** additional params

**:note:** Consumes only files from a custom receipt

**:example:**
```
- receipt.maker.read:
   - "receipt.yaml"
```
**********************************************

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
 
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/__init__.py***

modules __init__.py

**********************************************
 File @ ***/goephor/core/plugins/release.py***

Created on May 12, 2016

@author: iitow

**********************************************
**********************************************

***def date***:

get the current date


**:param prefix:** %m/%d/%y"

**:example:**
```
release.utils.date:
   - '%m/%d/%y'
```
**********************************************

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
**********************************************
**********************************************

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
 File @ ***/goephor/core/plugins/string.py***

Created on May 13, 2016

@author: iitow

**********************************************
**********************************************

***def println***:

Generic print line

**:param msg_type:** String: header, info, success, warning, fail, error

**:param text:** String
```
string.utils.println:
   - 'info'
   - "HELLO WORLD"
```
**********************************************

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
**********************************************

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
**********************************************

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
**********************************************

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
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/scm.py***

Created on Apr 28, 2016

@author: iitow

**********************************************
**********************************************

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
**********************************************

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
**********************************************

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
**********************************************

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
 File @ ***/goephor/core/plugins/handler.py***

Created on Jul 1, 2016

@author: iitow

**********************************************
**********************************************

***def readconfig***:

General read configs into environment currently only supports ConfigParser

**:param path:** String, full path to file

**:return:** key value pairs become environment variables

**:example:**
```
- handler.file.readconfig:
   - "${CFG}"
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/freebsd.py***

Created on Apr 29, 2016


**:author:** iitow

**********************************************
**********************************************
**********************************************
**********************************************

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
**********************************************

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
**********************************************

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
**********************************************
**********************************************

***def install***:

Install a package

**:param name:** String

**:return:** output

**:example:**
```
- freebsd.pkg.install
    - "texinfo"
```
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/pluginable.py***

Created on Apr 25, 2016


**:author:** iitow

**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/environment.py***

Created on Apr 27, 2016


**:author:** iitow

**********************************************
**********************************************
**********************************************

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
**********************************************

***def unset***:

Unset an environment variable


**:param key:** String

**:param value:** String

**:example:**
```
- environment.env.unset:
   - "VAR1"
```
**********************************************
**********************************************

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
 File @ ***/goephor/core/plugins/system.py***

Created on Apr 25, 2016


**:author:** iitow

**********************************************
**********************************************
**********************************************

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
**********************************************
**********************************************

***def shell***:

Run a shell command


**:param cmd:** String

**:example:**
```
- system.terminal.shell:
    - 'echo " THIS IS IT"'
```
**********************************************

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
 File @ ***/goephor/core/plugins/remote.py***

Created on Apr 28, 2016


**:author:** iitow

**********************************************
**********************************************

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
 File @ ***/goephor/core/plugins/example.py***

Created on Apr 27, 2016


**:author:** iitow

**********************************************
**********************************************

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
 File @ ***/goephor/core/plugins/http.py***

Created on Apr 29, 2016


**:author:** iitow

**********************************************
**********************************************

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
 File @ ***/goephor/core/plugins/condition.py***

Created on Apr 26, 2016


**:author:** iitow

**********************************************
**********************************************
**********************************************

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
**********************************************

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
**********************************************

***def FAIL***:

Cause a failure generally used with a IF

**:param text:** String
    ```
        - condition.statement.FAIL:
           - "Failed because of some issue"
    ```
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/action.py***

Created on Apr 26, 2016


**:author:** iitow

**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/git_kit.py***

Created on Oct 8, 2015


**:author:** iitow

**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/__init__.py***

None

**********************************************
 File @ ***/goephor/core/plugins/modules/log.py***

Created on Jun 3, 2016


**:author:** iitow

**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/environment.py***

Created on Apr 26, 2016


**:author:** iitow

**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/remote.py***

Created on Nov 18, 2015


**:author:** iitow

**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/terminal.py***

Created on Nov 18, 2015


**:author:** iitow

**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
**********************************************
 File @ ***/goephor/core/plugins/modules/http.py***

Created on Jun 2, 2015


**:author:** iitow

**********************************************
**********************************************
**********************************************