# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 17:47
'''
getattr()
setattr()
hasattr()
'''


class dispatcher():
    # cmds = {}
    # def cmd1(self):
    #     print('cmd1')
    def reg(self,cmd, fn):
        if isinstance(cmd, str):
            setattr(self.__class__,cmd,fn)
        else:
            print('error')

    def run(self):
        while True:
            cmd = input("plz input command: ")
            if cmd.strip() == "quit":
                return
            getattr(self,cmd.strip(), self.defaultfn)()

    def defaultfn(self):
        print('default')


# reg, run = dispatcher()
dis = dispatcher()
dis.reg('cmd1', lambda self : print(1))
dis.reg('cmd2', lambda self : print(2))
dis.run()
