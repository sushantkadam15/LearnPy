from pathlib import Path
import sys, os
platform = sys.platform
p = Path('Desktop', 'learnPython', 'AutomateBoringStuff')
print(p, platform)

homeFolder = Path('Desktop')
subFolder = Path('learnPython')
#print(str(homeFolder / subFolder))
current = Path.cwd()
test = "test"


#os.mkdir(current / test)
#os.rmdir(current / test)

print(os.listdir(current), os.getcwd(), os.path.getsize(current))

print(list(current.glob('*.py')))
print(current.is_dir())
print(current.is_file())

