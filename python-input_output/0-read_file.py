def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as myFile:
        line = myFile.read()
        print(line)
