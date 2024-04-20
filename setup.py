import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "includes": ["tkinter", "random", "string", "pyperclip"],
    "include_files": [],  # Add any additional files here
}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Password Manager",
    version="1.0",
    description="A simple password manager application",
    options={"build_exe": build_exe_options},
    executables=[Executable("password_manager.py", base=base)]
)
