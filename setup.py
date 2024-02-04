from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but some modules need help
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows
base = None

setup(  name = "Wonsz",
        version = "0.1",
        description = "Prosty projekt węża",
        options = {"build_exe": build_exe_options},
        executables = [Executable("wonsz.py", base=base)])