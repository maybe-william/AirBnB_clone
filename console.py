#!/usr/bin/python3
import cmd
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
