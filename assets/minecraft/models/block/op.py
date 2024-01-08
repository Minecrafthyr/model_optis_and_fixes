import os
import pathlib


os.chdir(os.path.dirname(__file__))


files = pathlib.Path().glob("*.rpo")

for file in files:
  with open(file,"r") as read_file:
    lines = read_file.readlines()
    for line in lines:
      if (line.find("optimizations.all")) != -1:
        read_file.close()
        os.remove(file)