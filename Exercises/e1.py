import glob

myfiles = glob.glob("../Files/*.txt")

print(myfiles)  # this will return all .txt files in a given folder

# using the file list to access contents of the files
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())


