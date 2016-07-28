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

### Basic Example Manifest###
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



