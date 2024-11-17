import importlib
import subprocess
import sys

def check_modules(modules):          #Checks whether an array of modules is installed and installs them if not

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
