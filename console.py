#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex
import re

classGroup = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
              "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """
    HBNB Class
    """
    prompt = '(hbnb) '

    # Find before execution
    def default(self, line):
        """Catch commands if nothing else matches then.\n"""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.method() syntax\n"""

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        class_name = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(class_name, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + class_name + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, class_name, uid, s_dict):
        """Helper method for update() with a dictionary.\n"""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not class_name:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[class_name]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()
    # End

    def do_EOF(self, line):
        """End of File command: exit the program\n"""
        return True

    def emptyline(self):
        """ Overwriting the emptyline method\n"""
        return False

    def do_quit(self, line):
        """Quit command exit the program\n"""
        return True

    def do_create(self, line):
        """
        Creates a new BaseModel instance,
        JSON file and prints the id\n
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
            string = line + "()"
            instance = eval(string)
            print(instance.id)
            instance.save()
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints an instance as a string based on the class and id\n"""
        className_line = line.split()
        if len(className_line) == 0:
            print("** class name missing **")
            return
        elif className_line[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        elif len(className_line) == 2:
            instance = className_line[0] + "." + className_line[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class and id\n"""
        className_line = line.split()
        if len(className_line) == 0:
            print("** class name missing **")
            return
        elif className_line[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        elif len(className_line) == 2:
            instance = className_line[0] + "." + className_line[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string representations of instances\n"""
        className_line = shlex.split(arg)
        obj_list = []
        if len(className_line) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif className_line[0] in classGroup:
            for key in models.storage.all():
                if className_line[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class name, id, attribute & value\n"""
        className_line = line.split()
        staticArray = ["id", "created_at", "updated_at"]
        objects = models.storage.all()
        if not line:
            print("** class name missing **")
        elif className_line[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        else:
            instance = className_line[0] + "." + className_line[1]
            if instance not in models.storage.all():
                print("** no instance found **")
            elif len(className_line) < 3:
                print("** attribute name missing **")
            elif len(className_line) < 4:
                print("** value missing **")
            elif className_line[2] not in staticArray:
                ojb = objects[instance]
                ojb.__dict__[className_line[2]] = className_line[3]
                ojb.updated_at = datetime.now()
                ojb.save()

    def do_count(self, line):
        """counts instances of the particular class\n"""
        className_line = line.split()
        if className_line[0] not in classGroup:
            return
        else:
            counter = 0
            keys_list = models.storage.all().keys()
            for searchKey in keys_list:
                len_searchKey = len(className_line[0])
                if searchKey[:len_searchKey] == className_line[0]:
                    counter += 1
            print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
