# this mini program allows you to sort any directory on your pc into folders

import os
import shutil

path = input("Enter Path: ")
files = os.listdir(path.strip())

for file in files:
    filename, exstension = os.path.splitext(file)
    exstension = exstension[1:]

    if os.path.exists(path + '/' + exstension):
        shutil.move(path + '/' + file, path + '/' + exstension + '/' + file)
    else:
        os.makedirs(path+'/'+exstension)
        shutil.move(path + '/' + file, path + '/' + exstension + '/' + file)


