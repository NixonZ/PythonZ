import os
try:
    if os.path.exists("readme.txt"):
        os.remove("readme.txt")
    file=open("readme.txt","xt")
    file.write("John mc yolo")
    file.close()
    file=open("readme.txt",'rt')
    print(file.read())
except Exception as e:
    print("cannot open file")
finally:
    file.close()