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

### Example Manifests ###
https://github.com/itow0001/goephor/tree/master/src/examples

### manifest.yaml ###
```
  name: "Project Name"
  description: "Project Description"
  globals:
    # change var1, var2 to see different paths use -E "var1=1"
    - var1: 2
    - var2: 2
  actions:
       # This is an if statement
       -  condition.statement.IF:
                            - "${var1}"
                            - "=="
                            - "${var2}"
                            - THEN:
                              - system.terminal.shell:
                                - 'echo "(THEN 1)"'
                            - ELSE:
                              - system.terminal.shell:
                                - "echo '(ELSE 1)'"
                              # This is a nested if statement
                              -  condition.statement.IF:
                                                  - "${var1}"
                                                  - "=="
                                                  - "1"
                                                  - THEN:
                                                    - system.terminal.shell:
                                                      - 'echo "(IF NEST 1)"'
       # This is how to check for a token from output
       - system.terminal.shell:
                           - "echo '(PASS)'"
                           - set_env: "var3"
       - condition.statement.HAS_TOKEN:
                           - "(PASS)"
                           - "${var3}"
                           - set_env: "IS_TOKEN"
       - system.terminal.shell:
                           - ' echo "IS_TOKEN: ${IS_TOKEN}"'
```



