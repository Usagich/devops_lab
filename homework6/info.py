import sys
import subprocess


print("python ver.", sys.version)
print(subprocess.getoutput("pyenv version-name"))
print("where is python bin:", sys.executable)
print("pip location:", subprocess.getoutput("which pip"))
print("virtual env:", sys.exec_prefix)
print("site-packages location:", next(p for p in sys.path if "site-packages" in p))
print("packages:\n", subprocess.getoutput("pip freeze"))
