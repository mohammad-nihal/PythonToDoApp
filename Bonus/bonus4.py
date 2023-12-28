filenames = ["1.Raw Data.txt","2.Reports.txt","3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)

filenamet = ("1.Raw Data.txt","2.Reports.txt","3.Presentations.txt")  #tuple cannot be changed
print(filenamet[0])
#filenamet[0] = "something new"  <- this will give an error