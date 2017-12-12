import sys
import subprocess
import json
import yaml

class PythonFields:
    def __init__(self):
        self.version = sys.version
        self.pyenv = subprocess.getoutput("pyenv version-name")
        self.pythonBin = sys.executable
        self.pipLocal = subprocess.getoutput("which pip")
        self.virtualEnv = sys.exec_prefix
        self.sitePackages = next(p for p in sys.path if "site-packages" in p)
        self.packages = subprocess.getoutput("pip freeze")

    def __str__(self):
        return (str("python ver. " + self.version + "\npyenv ver.: " + self.pyenv + "\nwhere is python bin: " + self.pythonBin + "\npip location: " + self.pipLocal + "\nvirtual env: " + self.virtualEnv + "\nsite-packages location: " + self.sitePackages + "\npackages:\n" + self.packages))

pf = PythonFields()

print("python ver.", pf.version)
print("pyenv ver.:", pf.pyenv)
print("where is python bin:", pf.pythonBin)
print("pip location:", pf.pipLocal)
print("virtual env:", pf.virtualEnv)
print("site-packages location:", pf.sitePackages)
print("packages:\n", pf.packages)

json_file = "pf.json"
yaml_file = "pf.yaml"
with open(json_file, "w") as json_out:
    json_out.write(json.dumps(str(pf), indent=4, sort_keys=False))

with open(yaml_file, "w") as yml_out:
    yml_out.write(yaml.dump(str(pf), default_flow_style=False))
