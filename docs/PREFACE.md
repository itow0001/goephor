##User Tutorial##
TBD
##Development Tutorial## 
RBD
##Generating A Call Graph##
* pip install pycallgraph
```
pycallgraph -e argparse* -e gettext* -e posixpath* -e importlib* -e os* -e re* -e UserDict* -e yaml* -e pickle* -e subprocess* -e sre_parse* -e encodings* -e sre_compile* -e codecs* -e atexit* -e shlex* -e pty* -e statement* -e genericpath* -e stat* -e tty* -e locale* graphviz --output-file=../docs/goephor_ex_system.png -- goephor.py -f ./examples/ex_system.yaml -e
```
## Docs ##
