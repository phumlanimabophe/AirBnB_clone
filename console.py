#!/usr/bin/python3
"""
This is the console base for the unit
"""
# Import the cmd module
import cmd
# Import the BaseModel class
from models.base_model import BaseModel
# Import the storage module from the models package
from models import storage
# Import the json module
import json
# Import the shlex module for parsing
import shlex
# Import specific classes from the models package
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity




# Define a command-line interface class for managing Holberton models data
class HBNBCommand(cmd.Cmd):
    """ command prompt to access models data """

    # Prompt format for the command prompt
    prompt = '(hbnb) '

    # Dictionary mapping model class names to their corresponding classes
    my_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    # Command method: mynothing
    def mynothing(self, arg):
        """ Does nothing """
        pass

    # Command method: myquit
    def myquit(self, arg):
        """ Close program and save data safely """
        return True

    # Command method: myEOF
    def myEOF(self, arg):
        """ Close program and save data safely when user input is CTRL + D """
        print("")
        return True

    # Override the behavior of an empty line
    def emptyline(self):
        """ Overrides the empty line method """
        pass

    # Define a method named 'mycreate' within a class, which takes a 'self' parameter and an 'arg' parameter.
    def mycreate(self, arg):
        """ Creates a new instance of the basemodel class
        Structure: create [class name]
        """
        # Check if the 'arg' parameter is not provided.
        if not arg:
            print("** class name missing **")
            return
        
        # Split the 'arg' using shell-like syntax and store the result in 'my_data'.
        my_data = shlex.split(arg)
        
        # Check if the first element of 'my_data' is not a key in the 'my_dict' dictionary of the 'HBNBCommand' class.
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        
        # Create a new instance of the class specified by the first element of 'my_data' and store it in 'new_instance'.
        new_instance = HBNBCommand.my_dict[my_data[0]]()
        
        # Call the 'save' method on 'new_instance' to save it in some manner.
        new_instance.save()
        
        # Print the 'id' attribute of the 'new_instance'.
        print(new_instance.id)


    # Define a method named 'myshow' within a class, which takes a 'self' parameter and an 'arg' parameter.
    def myshow(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        Structure: show [class name] [id]
        """
        # Split the 'arg' using shell-like syntax and store the result in 'tokens'.
        tokens = shlex.split(arg)
        
        # Check if 'tokens' is empty.
        if len(tokens) == 0:
            print("** class name missing **")
            return
        
        # Check if the first element of 'tokens' is not a key in the 'my_dict' dictionary of the 'HBNBCommand' class.
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        
        # Check if the length of 'tokens' is less than or equal to 1.
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        
        # Reload data from storage (assuming a 'storage' object exists).
        storage.reload()
        
        # Get a dictionary of all objects from storage.
        objs_dict = storage.all()
        
        # Create a key by concatenating class name and id.
        key = tokens[0] + "." + tokens[1]
        
        # Check if the key exists in the 'objs_dict'.
        if key in objs_dict:
            # Convert the object instance to a string representation.
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")


    # Define a method named 'mydestroy' within a class, which takes a 'self' parameter and an 'arg' parameter.
    def mydestroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (saves the changes into the JSON file)
        Structure: destroy [class name] [id]
        """
        # Split the 'arg' using shell-like syntax and store the result in 'tokens'.
        tokens = shlex.split(arg)
        
        # Check if 'tokens' is empty.
        if len(tokens) == 0:
            print("** class name missing **")
            return
        
        # Check if the first element of 'tokens' is not a key in the 'my_dict' dictionary of the 'HBNBCommand' class.
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        
        # Check if the length of 'tokens' is less than or equal to 1.
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        
        # Reload data from storage (assuming a 'storage' object exists).
        storage.reload()
        
        # Get a dictionary of all objects from storage.
        objs_dict = storage.all()
        
        # Create a key by concatenating class name and id.
        key = tokens[0] + "." + tokens[1]
        
        # Check if the key exists in the 'objs_dict'.
        if key in objs_dict:
            # Delete the object instance from the dictionary.
            del objs_dict[key]
            
            # Save the changes back to the storage (e.g., JSON file).
            storage.save()
        else:
            print("** no instance found **")

    # Define a method named 'myall' within a class, which takes a 'self' parameter and an 'arg' parameter.
    def myall(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        Structure: all [class name] or all
        """
        # Reload data from storage (assuming a 'storage' object exists).
        storage.reload()
        
        # Create an empty list to store JSON representations of instances.
        my_json = []
        
        # Get a dictionary of all objects from storage.
        objects_dict = storage.all()
        
        # Check if 'arg' is empty.
        if not arg:
            # Loop through all keys in the objects dictionary and append string representations to 'my_json'.
            for key in objects_dict:
                my_json.append(str(objects_dict[key]))
            
            # Print the JSON representation of all instances.
            print(json.dumps(my_json))
            return
        
        # Split the 'arg' using shell-like syntax and store the result in 'token'.
        token = shlex.split(arg)
        
        # Check if the first element of 'token' is in the keys of the 'my_dict' dictionary of the 'HBNBCommand' class.
        if token[0] in HBNBCommand.my_dict.keys():
            # Loop through all keys in the objects dictionary.
            for key in objects_dict:
                # Check if the class name from 'token' is a substring of the key.
                if token[0] in key:
                    # Append string representation of instances matching the class name to 'my_json'.
                    my_json.append(str(objects_dict[key]))
            
            # Print the JSON representation of selected instances.
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")

    # Define a method named 'myupdate' within a class, which takes a 'self' parameter and an 'arg' parameter.
    def myupdate(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Structure: update [class name] [id] [arg_name] [arg_value]
        """
        # Check if 'arg' is empty.
        if not arg:
            print("** class name missing **")
            return
        
        # Split the 'arg' using shell-like syntax and store the result in 'my_data'.
        my_data = shlex.split(arg)
        
        # Reload data from storage (assuming a 'storage' object exists).
        storage.reload()
        
        # Get a dictionary of all objects from storage.
        objs_dict = storage.all()
        
        # Check if the first element of 'my_data' is not a key in the 'my_dict' dictionary of the 'HBNBCommand' class.
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        
        # Check if the length of 'my_data' is 1, indicating missing instance id.
        if len(my_data) == 1:
            print("** instance id missing **")
            return
        
        try:
            # Create a key by concatenating class name and id.
            key = my_data[0] + "." + my_data[1]
            # Access the object instance using the key; this may raise a KeyError.
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        
        # Check if the length of 'my_data' is 2, indicating missing attribute name.
        if len(my_data) == 2:
            print("** attribute name missing **")
            return
        
        # Check if the length of 'my_data' is 3, indicating missing value.
        if len(my_data) == 3:
            print("** value missing **")
            return
        
        # Get the object instance from the 'objs_dict' using the key.
        my_instance = objs_dict[key]
        
        # Check if the attribute exists in the object instance.
        if hasattr(my_instance, my_data[2]):
            # Get the current data type of the attribute.
            data_type = type(getattr(my_instance, my_data[2]))
            # Set the attribute with the new value, converting it to the appropriate data type.
            setattr(my_instance, my_data[2], data_type(my_data[3]))
        else:
            # If the attribute does not exist, set it directly.
            setattr(my_instance, my_data[2], my_data[3])
        
        # Save the changes back to the storage (e.g., JSON file).
        storage.save()

    # Define a method named 'myotherupdate' within a class, which takes a 'self' parameter and an 'arg' parameter.
    def myotherupdate(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Structure: update [class name] [id] [dictionary]
        """
        # Check if 'arg' is empty.
        if not arg:
            print("** class name missing **")
            return
        
        # Extract the dictionary part from 'arg'.
        my_dictionary = "{" + arg.split("{")[1]
        
        # Split the 'arg' using shell-like syntax and store the result in 'my_data'.
        my_data = shlex.split(arg)
        
        # Reload data from storage (assuming a 'storage' object exists).
        storage.reload()
        
        # Get a dictionary of all objects from storage.
        objs_dict = storage.all()
        
        # Check if the first element of 'my_data' is not a key in the 'my_dict' dictionary of the 'HBNBCommand' class.
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        
        # Check if the length of 'my_data' is 1, indicating missing instance id.
        if len(my_data) == 1:
            print("** instance id missing **")
            return
        
        try:
            # Create a key by concatenating class name and id.
            key = my_data[0] + "." + my_data[1]
            # Access the object instance using the key; this may raise a KeyError.
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        
        # Check if the dictionary is empty.
        if (my_dictionary == "{"):
            print("** attribute name missing **")
            return
        
        # Replace single quotes with double quotes for valid JSON format.
        my_dictionary = my_dictionary.replace("\'", "\"")
        
        # Load the dictionary from the JSON format.
        my_dictionary = json.loads(my_dictionary)
        
        # Get the object instance from the 'objs_dict' using the key.
        my_instance = objs_dict[key]
        
        # Update attributes in the object instance using the values from the dictionary.
        for my_key in my_dictionary:
            if hasattr(my_instance, my_key):
                data_type = type(getattr(my_instance, my_key))
                setattr(my_instance, my_key, my_dictionary[my_key])
            else:
                setattr(my_instance, my_key, my_dictionary[my_key])
        
        # Save the changes back to the storage (e.g., JSON file).
        storage.save()

    # Define a method named 'mycount' within a class, which takes a 'self' parameter and an 'arg' parameter.
    def mycount(self, arg):
        """
        Counts number of instances of a class
        """
        # Initialize a counter to keep track of the number of instances.
        counter = 0
        
        # Get a dictionary of all objects from storage.
        objects_dict = storage.all()
        
        # Loop through all keys in the objects dictionary.
        for key in objects_dict:
            # Check if the argument 'arg' is a substring of the key.
            if (arg in key):
                # Increment the counter for each matching instance.
                counter += 1
        
        # Print the final count of instances.
        print(counter)


    # Define a method named 'default' within a class, which takes a 'self' parameter and an 'arg' parameter.
    def default(self, arg):
        """ handle new ways of inputing data """
        
        # Create a dictionary mapping new commands to corresponding methods.
        val_dict = {
            "all": self.myall,
            "count": self.mycount,
            "show": self.myshow,
            "destroy": self.mydestroy,
            "update": self.myupdate
        }
        
        # Strip any leading/trailing whitespace from the argument.
        arg = arg.strip()
        
        # Split the argument into parts using the dot as a separator.
        values = arg.split(".")
        
        # Check if the split resulted in two parts (class_name.command()).
        if len(values) != 2:
            # If not, use the default behavior of the parent class.
            cmd.Cmd.default(self, arg)
            return
        
        # Extract class name and command from the split values.
        class_name = values[0]
        command = values[1].split("(")[0]
        line = ""
        
        # Check if the command is "update" and the argument includes a complete dictionary.
        if (command == "update" and values[1].split("(")[1][-2] == "}"):
            inputs = values[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            
            # Call the 'myotherupdate' method with the generated line.
            self.myotherupdate(line.strip())
            return
        
        try:
            # Split the command arguments using commas.
            inputs = values[1].split("(")[1].split(",")
            
            # Construct the line string by extracting values from inputs.
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        
        # Construct the final line using class name and constructed line.
        line = class_name + line
        
        # Check if the command exists in the val_dict.
        if (command in val_dict.keys()):
            # Call the corresponding method with the generated line.
            val_dict[command](line.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
