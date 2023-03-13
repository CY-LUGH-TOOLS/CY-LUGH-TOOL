import os
main_path = '''./CY-LUGH-TOOL'''
for root, subFolder, filename in os.walk(main_path):
 for folder in subFolder:
  os.system('cd REPO-MENU')