import fi

contents = ["first file content","second file content","third file content"]

filenames = ["docs.txt","report.txt","presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open( f"../Files/{filename}",'w') # relative path to Bonus dir, here our code is in Bonus dir
    file.write(content)
    file.close()
