#!/usr/bin/python3
"""define a class HBNBCommand that is a console"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
  """initialize the console"""
  prompt = "(hbnb) "

  def do_quit(self,arg):
    """Quit command to exit the program"""
    return True

  def do_EOF(self, arg):
    """exit the program"""
    return True

  def emptyline(self):
    """do nothing"""
    pass
    
  def do_create(self, arg):
    """Creates a new instance of BaseModel, saves it, and prints the id"""
    list_of_class = {'BaseModel': BaseModel, 'User': User}
    if arg == "":
      print("** class name missing **")
      return
    elif arg not in list_of_class:
      print("** class doesn't exist **")
    else:
      if arg in list_of_class:
        arg = list_of_class[arg]()
        arg.save()
        print(arg.id)
      
  def do_show(self, arg):
    """"""
    list_of_class = ['BaseModel', 'User']
    args = arg.split()
    if len(args) == 0:
      class_of_instance = ""
    else:
      class_of_instance = args[0]
    if class_of_instance == "":
      print("** class name missing **")
      return
    if class_of_instance not in list_of_class:
      print("** class doesn't exist **")
      return
    if len(args) == 1:
      print("** instance id missing **")
      return
    else:
      id_of_instance = args[1]
      key = f"{class_of_instance}.{id_of_instance}"
      if key not in storage.all().keys():
        print("** no instance found **")
      else:
        print(storage.all()[key])
          
  def do_destroy(self, arg):
    """"""
    list_of_class = ['BaseModel', 'User']
    args = arg.split()
    if len(args) == 0:
      class_of_instance = ""
    else:
      class_of_instance = args[0]
    if class_of_instance == "":
      print("** class name missing **")
      return
    if class_of_instance not in list_of_class:
      print("** class doesn't exist **")
      return
    if len(args) == 1:
      print("** instance id missing **")
      return
    else:
      id_of_instance = args[1]
      key = f"{class_of_instance}.{id_of_instance}"
      if key in storage.all().keys():
          del storage.all()[key]
          print("Object deleted")
          storage.save()
      else:
        print("** no instance found **")

  def do_all(self, arg):
    """"""
    my_list = []
    if arg == "":
      for key, value in storage.all().items():
        my_list.append(BaseModel.__str__(value))
      print(my_list)
    #Añadir para más clases (Ejemplo: all Auto)

  def do_update(self, arg):
    """"""
    args = arg.split()
    list_of_class = ['BaseModel', 'User']
    if len(args) == 0:
      class_of_instance = ""
    else:
      class_of_instance = args[0]
    if class_of_instance == "":
      print("** class name missing **")
      return
    if class_of_instance not in list_of_class:
      print("** class doesn't exist **")
      return
    if len(args) == 1:
      print("** instance id missing **")
      return
    id_of_instance = args[1]
    key = f"{class_of_instance}.{id_of_instance}"
    if key not in storage.all().keys():
      print("** no instance found **")
      return
    if len(args) == 2:
      print("** attribute name missing **")
      return
    if len(args) == 3:
      print("** value missing **")
      return
    attribute_name = args[2]
    attribute_value = args[3]
    setattr(storage.all()[key], attribute_name, attribute_value)
    storage.save()

if __name__ == '__main__':
  HBNBCommand().cmdloop()