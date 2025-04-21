import os
import platform
import subprocess


def open_file(filepath):
    system = platform.system()
    if system == "Darwin":
        subprocess.call(["open", filepath])
    elif system == "Windows":
        os.startfile(filepath)
    elif system == "Linux":
        subprocess.call(["xdg-open", filepath])
    else:
        raise RuntimeError(f"Unsupported OS: {system}")
