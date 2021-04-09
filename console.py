import sys
import os
from commands import commands

header = "Лабораторная Работа №3. [Version 0.01] \n"
header += "Эмулятор командной строки Windows \n"

'''
print(header)
print("C:\Games>", end='')
_s = input()
args = _s.split(" ")
print(commands[args[0]](args[1].upper()))

_s = input()
args = _s.split(" ")
commands[args[0]]()
'''

class Lab3CLI():
    def __init__(self):
        self.headers = "Лабораторная Работа №3. [Version 0.01] \n " \
        + "Эмулятор командной строки Windows \n\n"
        self.cwd = os.getcwd()

        self.current_screen = self.headers + f'{self.cwd}>'

    def parse_input(self):
        args = input().split(' ')

        args[0] = args[0].upper()        
        if args[0] in commands.keys():
            commands[args[0]](self, args[1:])
        else:
            self.current_screen = f"{args[0]} не является внутренней или внешней командой\r\n"
        
        self.current_screen += f'\n{self.cwd.lower()}>'
        


screen = Lab3CLI()

while True:
    print(screen.current_screen, end='')
    screen.parse_input()