import zipfile
import os
from sys import argv

def copyToZip(filepath, file_to_copy):
    """
    copies a file into a zip archive, ensuring it can last throughout the furry apocalypse :3

    Args:
        filepath (str): path to the zip archive
        file_to_copy (str): Path to the file to be copied."""
    with zipfile.ZipFile(filepath, 'a') as z:
        z.write(file_to_copy, os.path.basename(file_to_copy))


zipFilepath = argv[1] # get the first command line awgument
if argv[1] == "same": # compawison
    zipFilepath = argv[2] + ".zip"  # concatenate the second cmd-wine awg with '.zip'
folderToZip = argv[2] # foldewToZip
print(f"Copying {len(os.listdir(folderToZip))} files into {zipFilepath}.zip...")
for index,item in enumerate(os.listdir(folderToZip)):
    copyToZip(zipFilepath, folderToZip + "/" + item)
    print(f"File '{item}' copied to '{zipFilepath}'")
print(f"{len(os.listdir(folderToZip))} files zipped into {folderToZip}.zip")