#!/usr/bin/python3
"""
    Console Module
"""


import cmd
import json
from models import storage
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


    def do_show(self, info):
        if len(info) == 0:
            print("** class name missing **")
            return
        x = info.split(' ')
        if x[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(x) == 1:
            print("** instance id missing **")
            return
        k = "{:s}.{:s}".format(x[0], x[1])
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if (obj_id == k):
                obj = all_objs[obj_id]
                print(obj)
                return
        print("** instance no found **")


    def do_destroy(self, info):
        if len(info) == 0:
            print("** class name missing **")
            return
        x = info.split(' ')
        if x[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(x) == 1:
            print("** instance id missing **")
            return
        k = "{:s}.{:s}".format(x[0], x[1])
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if (obj_id == k):
                obj = all_objs[obj_id]
                print(obj)
                return
            print("** instance no found **")


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
