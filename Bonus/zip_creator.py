import pathlib
import zipfile

def make_archive(filepaths, dest_dir):
    path = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)



if __name__ == "__main__":   # <- way to test, will run only when function is directly executed
    make_archive(filepaths=["bonus1.py","bonus2.1.py"], dest_dir="dist")