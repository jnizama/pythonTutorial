import os
import sys


def get_operative_system_v1():
    name_os = os.name
    # match only work since Python 3.10 upwards (old version use elif)
    match name_os:
        case "nt":
            name_string = "Windows NT"
        case "posix":
            name_string = "macOS"
        case "dos":
            name_string = "DOS"
        case _:  # default
            name_string = "S.O. Unknown"
    return name_string


def get_operative_system_v2():
    if sys.platform.startswith('aix'):
        name_string = "AIX"
    elif sys.platform.startswith('emscripten'):
        name_string = "Emscripten"
    elif sys.platform.startswith('linux'):
        name_string = "Linux"
    elif sys.platform.startswith('wasi'):
        name_string = "WASI"
    elif sys.platform.startswith('win32'):
        name_string = "Windows"
    elif sys.platform.startswith('cygwin'):
        name_string = "Windows/Cygwin"
    elif sys.platform.startswith('darwin'):
        name_string = "macOS"
    return name_string


# return files from a directory
def get_all_files_from__my_documents():
    documents_path = os.environ['USERPROFILE'] + "\\Documents\\"
    os.chdir(documents_path)
    os.getcwd()
    print(os.listdir(os.getcwd()))
