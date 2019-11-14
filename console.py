#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
"""
    This modual contains console class.
"""


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand - console class
        @attibutes
            prompt: class attributes - custom prompt
        @methods
            do_quit: quit command
            do_EOF: ctrl-d to quit
            emptyline: do nothing for empty line
    """
    prompt = "(hbnb) "
    my_model = []
    clss = {"BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}

    def do_create(self, args):
        """creates an instance"""
        if args in type(self).clss.keys():
            mod = type(self).clss[args]()
            type(self).my_model.append(mod)
            print(mod.id)
        elif args is "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
        # print("type(self).my_model--->", type(self).my_model)

    def do_show(self, args):
        """shows an instance"""
        argsDelim = args.split()
        if args and argsDelim[0] in type(self).clss.keys():
            if len(argsDelim) < 2:
                print("** instance id missing **")
            else:
                for i in type(self).my_model:
                    if i.id == argsDelim[1]:
                        print(i)
                        break
                else:
                    print("** no instance found **")
        elif args is "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """destroys a created instance"""
        argsDelim = args.split()
        if args and argsDelim[0] in type(self).clss.keys():
            if len(argsDelim) < 2:
                print("** instance id missing **")
            else:
                for i in type(self).my_model:
                    if i.id == argsDelim[1]:
                        type(self).my_model.remove(i)
                        break
                else:
                    print("** no instance found **")
        elif args is "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """prints all instances created"""
        if args == "":
            templist = [str(i) for i in type(self).my_model]
            templist.reverse()
            print(templist)
        elif args in type(self).clss.keys():
            templist = list()
            for i in type(self).my_model:
                if type(i) == type(self).clss[args]:
                    templist.append(str(i))
            templist.reverse()
            print(templist)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """adds attributes to instance"""
        # print(args)
        argsDelim = args.split(" ", 3)
        if args and argsDelim[0] in type(self).clss.keys():
            if len(argsDelim) < 2:
                print("** instance id missing **")
            elif len(argsDelim) < 3:
                print("** attribute name missing **")
            elif len(argsDelim) < 4:
                print("** value missing **")
            else:
                for i in type(self).my_model:
                    if i.id == argsDelim[1]:
                        if '"' in argsDelim[3]:
                            if '"' == argsDelim[3][-1]:
                                value = argsDelim[3].split('"')[0]
                            else:
                                value = argsDelim[3].split('"')[1]
                        elif '.' in argsDelim[3]:
                            value = float(argsDelim[3])
                        else:
                            try:
                                value = int(argsDelim[3])
                            except Exception:
                                value = argsDelim[3]
                        # print("type->", type(value))
                        setattr(i, argsDelim[2], value)
                        i.save()
                        break
                    else:
                        print("** no instance found **")
        elif args is "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_quit(self, args):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, args):
        """End Of File :)"""
        print()
        exit()

    def emptyline(self):
        """Do nothing for empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
