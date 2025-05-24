# working with directories

from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

print(path.iterdir())

for p in path.iterdir():
    print(p)


paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)


py_files = [p for p in path.glob("*.py")]
print("python files: ", py_files)

# to search recursively
py_files_all = [p for p in path.glob("**/*.py")]
print(py_files_all)

# other way to search recursively is using path.rglob("*.py")
py_files_all_1 = [p for p in path.rglob("*.py")]
print("all_1", py_files_all_1)
