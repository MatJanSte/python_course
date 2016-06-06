import os
import glob
from shutil import copyfile
base = os.getcwd() + "/files"
nazwa = []
roboczy = base + "/roboczy"
if  os.path.exists(base + "/roboczy"):
    pass
else:
    os.mkdir(os.path.join(base, "roboczy"))

for i in glob.glob1(base, "tmp*"):
    with open(base + "/" + i, "r") as plik:
        for j in plik.readlines():
            nazwa = str("".join(j[10:]))
            if os.path.exists(roboczy + "/" + nazwa):
                pass
            else:
                os.mkdir(os.path.join(roboczy, nazwa))
                pass
            copyfile(base + "/" + i, roboczy + "/" + nazwa + "/" + i)
        # str("".join([i[:i.find("$")] + " " for i in text.split("ok")])).strip()