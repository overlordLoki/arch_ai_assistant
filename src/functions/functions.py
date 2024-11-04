# src/functions/functions.py

import os
import platform

def get_system_info():
    """Retrieve system information."""
    return {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "architecture": platform.architecture(),
        "processor": platform.processor(),
    }

def list_directory(directory_path: str):
    """List contents of a directory."""
    try:
        return os.listdir(directory_path)
    except Exception as e:
        return str(e)

def read_file(file_path: str, mode: str = 'r'):
    """Read content of a file."""
    try:
        with open(file_path, mode) as file:
            return file.read()
    except Exception as e:
        return str(e)

def execute_shell_command(command: str):
    """Execute a shell command."""
    try:
        return os.popen(command).read()
    except Exception as e:
        return str(e)


def list_fuction_names():
    """List all function names in the functions module."""
    fuc_list = ['get_system_info(), ', 'list_directory(directory_path: str), ',
                "read_file(file_path: str, mode: str = 'r'), ",
                'execute_shell_command(command: str), ']
    return fuc_list