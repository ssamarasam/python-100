# working with paths
# create path objects

from pathlib import Path

# Path(r"c:\Program Files\Microsoft")
# Path("usr/local/bin")
# Path()
# Path("ecommerce/__init__.py")
# Path() / "ecommerce" / "__init__.py"
# Path.home()

path = Path("ecommerce/__init__.py")

print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

# create new file object
path = path.with_name("file.txt")
print(path.name)
print(path.absolute())  # file doesnt exits, its just representing the path

path = path.with_suffix(".zip")
print(path)
