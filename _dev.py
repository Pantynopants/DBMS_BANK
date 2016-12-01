import os, sys, shutil
try:
    shutil.rmtree("migrations")
    
except :
    print("already removed")
try:
    os.remove("data.db")
except :
    print("already removed")

try:
    os.remove("app/data.db")
except :
    print("already removed") 
    
