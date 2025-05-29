# run enternal progress

import subprocess

# completed = subprocess.run(["dir", "/Q"], capture_output=True, text=True)
# completed = subprocess.run(["python", "other.py"])
try:
    completed = subprocess.run(
        ["false"], capture_output=True, text=True, check=True)
    print(completed.args)
    print(completed.returncode)
    print(completed.stderr)
    print(completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
