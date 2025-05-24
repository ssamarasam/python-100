# working with files

from pathlib import Path
from time import ctime

path = Path("ecommerce/__init__.py")
print("file existis: ", path.exists())
# path.rename("init.txt")
# path.unlink()

print(path.stat())
print(path.stat().st_ctime)


# human readable time using ctime
print(ctime(path.stat().st_ctime))

# to read - read_bytes, read_text

print(path.read_text())

# to write - path.write_bytes(), path.write_text("...")

target_file = Path() / "newfile.py"
target_file.write_text(path.read_text())

print("target: ", target_file.read_text())

# above is not the right or better way to copy a file

# use shutil to copy - shutil.copy(source, target)
