#!/usr/bin/python3
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from re import search


class HBNBCommand(cmd.Cmd):
    """This class is the entry point of AirBnB console"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "State", "City", "Amenity",
                  "Place", "Review"]

    doc_header = "Documented commands (type help <topic>):"
    div = '='

    def do_quit(self, line):
        """Quit cmd to exit the console"""
        return True
    def do_EOF(self, line):
        """EOF cmd to exit the console"""
        return True

    def emptyline(self):
        """Return prompt on a new line when empty line"""
        pass

    def do_create(self, arg):
        """creates a new instance and saves it to json"""
        args_list = arg.split()
        if not args_list[0]:
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.class_list:
            new_instance = globals()[args_list[0]]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows the string of an instance 
        based on the class name and id"""
        args_list = arg.split()
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[id_object])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args_list = arg.split()
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(id_object)
                storage.save()

    def do_all(self, arg):
        """Prints all the string instances based or not on the class name"""
        inst_list = []
        args_list = arg.split()
        if len(args_list) == 0:
            for key, value in storage.all().items():
                inst_list.append(str(value))
            print(inst_list)
        elif args_list[0] in HBNBCommand.class_list:
            for key, value in storage.all().items():
                if value.__class__.__name__ == args_list[0]:
                    inst_list.append(str(value))
            print(inst_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args_list = shlex.split(arg[:])
        arg = arg.split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                regex_float = r"\d+\.\d+"
                id_object = "{}.{}".format(args_list[0], args_list[1])
                name_attr = args_list[2]
                value = args_list[3]
                if '"' in arg[3]:
                    pass
                elif search(regex_float, arg[3]):
                    value = float(value)
                elif arg[3].isdigit():
                    value = int(value)
                setattr(storage.all()[id_object], name_attr, value)
                storage.all()[id_object].save()

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        count = 0
        for key, value in storage.all().items():
            if key.split(".")[0] == arg:
                count += 1
        print(count)

    def default(self, arg):
        """Default: The method called on an input line when the cmd prefix
        isn't known. It parses arg as a command name and a string"""
        args_list = arg.split(".", 1)
        if args_list[0] in HBNBCommand.class_list:
            method = args_list[1].split("(")
            if method[0] == "all":
                return self.do_all(args_list[0])
            elif method[0] == "show":
                id_show = args_list[1].split('"')
                args_show = "{} {}".format(args_list[0], id_show[1])
                return self.do_show(args_show)
            elif method[0] == "destroy":
                id_destroy = args_list[1].split('"')
                args_destroy = "{} {}".format(args_list[0], id_destroy[1])
                return self.do_destroy(args_destroy)
            elif method[0] == "count":
                return self.do_count(args_list[0])
            elif method[0] == "update":
                part1 = method[1].replace(")", "")
                is_dict = part1[:].split(", ")
                if is_dict[1][0] == "{":
                    class_id = is_dict[0].replace('"', "")
                    regex_float = r"\d+\.\d+"
                    for i in range(1, len(is_dict)):
                        dict_parse = is_dict[i].replace("{", "", 1)
                        dict_parse = dict_parse.replace("}", "")
                        dict_parse = dict_parse.replace("'", "")
                        dict_parse = dict_parse.split(": ")
                        if '"' in dict_parse[1]:
                            pass
                        elif search(regex_float, dict_parse[1]):
                            dict_parse[1] = float(dict_parse[1])
                        elif dict_parse[1].isdigit():
                            dict_parse[1] = int(dict_parse[1])
                        args_update = "{} {} {} {}".format(args_list[0],
                                                           class_id,
                                                           dict_parse[0],
                                                           dict_parse[1])
                        self.do_update(args_update)
                else:
                    part2 = part1.replace('"', "", 4)
                    part3 = part2.split(", ")
                    args_update = "{} {} {} {}".format(args_list[0], part3[0],
                                                       part3[1], part3[2])
                    return self.do_update(args_update)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
