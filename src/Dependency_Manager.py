import os
import json
import importlib
import subprocess
import sys


#1 - Retrieve the list of dependencies from a json file

def retrieve_modules(baseDir, programName):

    with open(os.path.join(baseDir, "dependencies.json"), "r") as file:
        
        dependencies = json.load(file)
    
    for program in dependencies:

        if (program["program"] == programName):

            return program["modules"]
    
    print("\nWarning! No dependencies found associated to the program selected!")

#2 - Checks whether an array of modules is installed and installs them if not

def check_modules(modules):

    for module in modules:

        try:

            importlib.import_module(module)

            print("\n✅ Module '{Module}' already installed." .format(Module = module))
            
        except ImportError:

            print("\n❌ Module '{Module}' not found. Installing..." .format(Module = module))
            
            try:

                subprocess.check_call([sys.executable, "-m", "pip", "install", module])

                print("\n✅ Module '{Module}' installed successfully!" .format(Module = module))

            except subprocess.CalledProcessError as err:

                print("\n❌ An error occured while installing the module '{Module}': {Error}" .format(Module = module, Error = err))
