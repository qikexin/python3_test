# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 23:33
import subprocess
from subprocess import Popen,PIPE
proc = Popen('echo "hello"',shell=True,stdout=PIPE)
code = proc.wait()
txt = proc.stdout.read()
print(code,txt)