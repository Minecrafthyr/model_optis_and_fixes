import os

os.chdir(os.path.dirname(__file__))

for r, d, ff in os.walk(os.getcwd()):
    for f in ff:
        if f.endswith((".json", ".png", ".png.mcmeta")):
            ipath = os.path.relpath(os.path.join(r, f), os.getcwd())
            opath = ipath + ".rpo"
            print(f"{opath}")
            with open(opath, "w", encoding="utf-8") as newf:
                newf.write('{"condition": "tweaks.normal.crossCorrection"}')
            os.remove(ipath)
