# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/1/5 16:16

def check_kuohao(s):
    stack = []  #
    for char in s:
        if char in {'(','[','{'}:
            stack.append(char)
        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif char == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    result = check_kuohao("(){}]")
    print(result)