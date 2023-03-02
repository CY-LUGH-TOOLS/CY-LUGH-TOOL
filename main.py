import subprocess, sys

path_dir="/CY-LUGH-TOOL/config/CY-LUGH.py"

open_dir = 'open' if sys.platform == 'darwin' else "xdg-open"

subprocess.call((open_dir, path_dir))