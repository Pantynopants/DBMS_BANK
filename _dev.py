import os, sys, shutil
try:
    shutil.rmtree("migrations")
    os.remove("data.db")
    os.remove("app/data.db")
except :
    print("already removed")


