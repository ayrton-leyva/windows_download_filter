import os
import shutil

# windows username
username = ""

# IMAGES
doc_img = "C:\\Users\\" + username + "\\Pictures\\Documents_Images"
other_img = "C:\\Users\\" + username + "\\Pictures\\Other_Images"
gif_img = "C:\\Users\\" + username + "\\Pictures\\Gif"
vector_img = "C:\\Users\\" + username + "\\Pictures\\Vector"

# DOCUMENTS
docs = "C:\\Users\\" + username + "\\Documents\\Docs"
excel = "C:\\Users\\" + username + "\\Documents\\Excel"
exe = "C:\\Users\\" + username + "\\Documents\\Exe"
pdf = "C:\\Users\\" + username + "\\Documents\\Pdf"
txt = "C:\\Users\\" + username + "\\Documents\\Txt"


def custom_filter(path_entry):
    entrys = os.listdir(path_entry)
    for file in entrys:
        path = path_entry + "\\" + file
        # IMAGES
        if "doc" in file and (".png" in file or ".jpeg" in file or ".jpg" in file):
            shutil.move(path, doc_img)
        elif not "doc" in file and (
            ".png" in file or ".jpeg" in file or ".jpg" in file
        ):
            shutil.move(path, other_img)
        elif ".svg" in file:
            shutil.move(path, vector_img)
        elif ".gif" in file:
            shutil.move(path, gif_img)

        # DOCUMENTS
        elif ".doc" in file or ".docx" in file or ".docm" in file:
            shutil.move(path, docs)
        elif ".csv" in file or ".xls" in file or ".xlsx" in file:
            shutil.move(path, excel)
        elif ".exe" in file:
            shutil.move(path, exe)
        elif ".pdf" in file:
            shutil.move(path, pdf)
        elif ".txt" in file:
            shutil.move(path, txt)
        pass


list_dir = [doc_img, other_img, gif_img, vector_img, docs, excel, exe, pdf, txt]

# check if directories exist else create them
for dir in list_dir:
    if not os.path.isdir(dir):
        os.mkdir(dir)

# path to filter
path_to_filter = [
    "C:\\Users\\" + username + "\\Downloads",
    "C:\\Users\\" + username + "\\Desktop",
]

# execute filter for every instance
for path in path_to_filter:
    custom_filter(path)
