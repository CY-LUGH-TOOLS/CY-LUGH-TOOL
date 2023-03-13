import subprocess, sys
path_dir='/CY-LUGH-TOOL/REPO-MENU'
open_dir = "open" if sys.platform == "darwin" else "xdg-open"
subprocess.call((open_dir, path_dir))
exec(open('CY-LUGH.py', encoding="utf-8").read(), globals())