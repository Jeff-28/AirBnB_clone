#!/usr/bin/python3
"""
    Console Module
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class for the console"""

    prompt = '(hbnb) '

    """Commands"""
    def do_EOF(self, args):
        return True

    def do_quit(self, args):
        return True

    def do_create(self, args):
        if len(args) == 0:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)

    def do_show(self, *args):
        print(len(args))
        """
        if len(args) == 1:
            print("** class name missing **")
            return
        if args[1] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) <= 2:
            print("** instance id missing **")
            return
        instance = args[1]
        if instance.id != args[2]:
            print("** no instance found **")
            return
        print(instance.__str__)"""

    """Help documentation"""
    def help_EOF(self):
        print ("End-of-file command to exit the program\n")

    def help_quit(self):
        print ("Quit command to exit the program\n")

    def help_create(self):
        print("Create command to create a new instane of BaseModel\n")

    def help_show(self):
        print("Show command to show the string representation of instance\n")

    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
