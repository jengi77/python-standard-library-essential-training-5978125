# Working with ZIP files in Python
import zipfile


# TODO: Create a new ZIP archive
zfile = zipfile.ZipFile("archive.zip", "w")
zfile.write("file1.txt")
zfile.write("file2.txt")
zfile.write("file3.txt")
zfile.close()

# TODO: Check validity of the file
print("Is ZipFile: ", zipfile.is_zipfile("archive.zip"))

# TODO: Read the properties of a ZIP archive
zfile = zipfile.ZipFile("archive.zip")
print(zfile.infolist())
print("---------------")
print(zfile.namelist())

# TODO: Read the properties of ZIP contents
zinfo = zfile.getinfo("file1.txt")
print(zinfo.file_size)
print(zinfo.filename)
print(zfile.read("file1.txt"))

# TODO: Extract ZIP file contents
zfile.extract("file2.txt", "extracted")
zfile.extractall("all_extracted")

# TODO: Ensure that the file is closed
zfile.close()