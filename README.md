# AirBnB Clone Project

## Background Context

Welcome to the AirBnB clone project! This project is your first step toward building a full web application - an AirBnB clone. The initial focus is on creating a command interpreter to manage AirBnB objects. This step is crucial as it sets the foundation for subsequent tasks such as HTML/CSS templating, database storage, API integration, and front-end development.

In this project, you will:

- Create a parent class, `BaseModel`, responsible for initializing, serializing, and deserializing instances.
- Establish a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> File
- Define classes for various AirBnB objects (User, State, City, Place, etc.) that inherit from `BaseModel`.
- Implement the first abstracted storage engine, File storage.
- Develop comprehensive unit tests to validate all classes and the storage engine.

## What's a Command Interpreter?

Think of the command interpreter as a specialized shell designed for managing objects in our AirBnB project. It enables the following actions:

- Creating new objects (e.g., User, Place)
- Retrieving objects from files or databases
- Performing operations on objects (e.g., counting, computing stats)
- Updating object attributes
- Deleting objects

## Resources

To succeed in this project, review the following resources:

- [`cmd` module](https://docs.python.org/3/library/cmd.html)
- [In-depth `cmd` module guide](https://pymotw.com/3/cmd/)
- [Python packages concept page](https://packaging.python.org/tutorials/packaging-projects/)
- [`uuid` module](https://docs.python.org/3/library/uuid.html)
- [`datetime` module](https://docs.python.org/3/library/datetime.html)
- [`unittest` module](https://docs.python.org/3/library/unittest.html)
- Args/Kwargs (Positional and Keyword Arguments)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
- [`cmd` module wiki page](https://en.wikipedia.org/wiki/Cmd.exe)
- [Python Testing](https://realpython.com/python-testing/)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

- Creating a Python package
- Developing a command interpreter using the `cmd` module
- Implementing unit testing in a larger project
- Serializing and deserializing a class
- Reading and writing JSON files
- Managing datetime in Python
- Understanding UUIDs (Universally Unique Identifiers)
- Using `*args` and `**kwargs` in function parameters
- Handling named arguments in functions

## Copyright - Plagiarism

Remember, the tasks and solutions in this project should be your own. Plagiarism is strictly prohibited and will result in removal from the program. Uphold the learning objectives by creating original solutions.

## Requirements

### Python Scripts

- Use editors: vi, vim, emacs
- Compatibility: Ubuntu 20.04 LTS, Python 3.8.5
- Files end with a newline character
- First line of files: `#!/usr/bin/python3`
- Mandatory `README.md` at the project's root
- Code adheres to `pycodestyle` (version 2.8.*)
- All files are executable
- Module documentation present (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Class documentation present (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- Function documentation present (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation should be meaningful sentences

### Python Unit Tests

- Use editors: vi, vim, emacs
- Files end with a newline character
- Test files within a `tests` folder
- Use the `unittest` module for testing
- Test files are Python files (`.py` extension)
- Test files/folders start with `test_`
- Test file organization mirrors project's structure
- Execute tests with `python3 -m unittest discover tests` or test file by file
- Documentation for modules, classes, and functions as above
- Collaboration on test cases is encouraged to cover all edge cases

Remember, this project is an opportunity to apply your understanding. Happy coding!

