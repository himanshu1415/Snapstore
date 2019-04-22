from cx_Freeze import setup, Executable
import os
import sys
base = None    
executables = [Executable("menu.py", base=base)]
packages = ["idna","os","sys"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Security",
    options = options,
    version = "1.0",
    description = 'To protect system from unauthorized use',
    executables = executables
)
