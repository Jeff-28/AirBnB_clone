#!/usr/bin/python3
"""
    Console Module
"""


import cmd
import json
from models.engine.file_storage import FileStorage
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
        storage = FileStorage()
        for key in storage.__objects:
            print(key)
            s = key.split('.')
            if s[1] == x[1]:
                print(s[0])
                print(storage.__objects[key])
                obj = s[0](**storage.__objects[key])
                print(obj.__str__)
                return

        """
        with open("file.json", 'r') as myfile:
            obj_dict = json.load(myfile)
            for key in obj_dict.keys():
                s = key.split('.')
                if s[1] == x[1]:
                    print(key.__str__)
                    return
            print("** no instance found **")"""

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
