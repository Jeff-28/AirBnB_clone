#!/usr/bin/python3
"""
    Console Module
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the console"""

    prompt = '(hbnb) '

    def do_EOF(self, args):
        return True

    def do_quit(self, args):
        return True

    def help_EOF(self):
        print ("End-of-file command to exit the program\n")

    def help_quit(self):
        print ("Quit command to exit the program\n")

    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
