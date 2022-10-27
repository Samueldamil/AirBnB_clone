#!/usr/bin/python3
"""Console command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Command interpreter - console\n"""

    def __init__(self):
        """Initinalizes the HBNBCommand console\n"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """End Of File (EOF) signal to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

