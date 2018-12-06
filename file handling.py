try:
    file=open("readme.txt","rt")
    print(file.read())
    file.seek(0)
    print(file.read(5))
    file.seek(0)
    for x in file:
        print(x)
except Exception as e:
    print("cannot open file")
finally:
    file.close()
