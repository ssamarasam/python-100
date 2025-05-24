# working with zipfiles

from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")

# for path in Path("ecommerce").rglob("*.*"):
#     zip.write(path)

# zip.close()


# better way to rewrite the abopve code without close fucntion is using 'with'

# with ZipFile("files1.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)


with ZipFile("files1.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print("info: ", info.compress_size)
    zip.extractall("extract")
