import sys
import subprocess


class PythonFields:
    def __init__(self):
        self.version = sys.version
        self.pyenv = subprocess.getoutput("pyenv version-name")
        self.pythonBin = sys.executable
        self.pipLocal = subprocess.getoutput("which pip")
        self.virtualEnv = sys.exec_prefix
        self.sitePackages = next(p for p in sys.path if "site-packages" in p)
        self.packages = subprocess.getoutput("pip freeze")

pf = PythonFields()

print("python ver.", pf.version)
print("pyenv ver.:", pf.pyenv)
print("where is python bin:", pf.pythonBin)
print("pip location:", pf.pipLocal)
print("virtual env:", pf.virtualEnv)
print("site-packages location:", pf.sitePackages)
print("packages:\n", pf.packages)
