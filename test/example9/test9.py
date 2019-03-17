# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/16 21:41
def cmds_dispatcher():
    commands = {}
    #注册
    def reg(name):
        def _reg(fn):
            if not name in commands.keys():
                commands[name] = fn
                # print(commands)
                return fn
            else:
                print("the {} is register".format(name))
                exit(1)
        return _reg

    def defaultFunc():
        print("Unknown command")
    def dispatcher():
        print(commands)
        while True:
            cmd = input(">> ")
            if cmd.strip() == "quit":
                return
            commands.get(cmd,defaultFunc)()
    return reg,dispatcher

reg,dispatcher = cmds_dispatcher()
@reg('fool1')  #相当于reg('fool1')(fn)
def fool1():
    print("welcom fool1")

@reg("fool2")
def fool2():
    print("welcom fool2")
#
# @reg("fool2")
# def fool2():
#     print("xxxx")
dispatcher()