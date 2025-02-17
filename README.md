
# pyZipApp

 a local python zip app using the built in zip module

It's a incrediably simple program for creating zipped versions of a folder.

## required modules

none. uses built-in modules

## running

Running by double-clicking won't work; this is a command line program.

### Windows

Assuming that you downloaded Python through the Python website.

`py zipAFolder.py [zip_file_to_zip_to] [folder_to_zip]`

`zip_file_to_zip_to`: The name of the zip file to output to, e.g. `output.zip`. (Include the file extension.) Use `same` if you want to use the value for `folder_to_zip`.

`folder_to_zip`: To make things easy to handle, this program archives entire folders at a time. Give the name of the folder to zip from.(A TestFolder has been provided as an example.)

### Example usage

`py zipAFolder.py output.zip TestFolder`

Uses the TestFolder provided inside the repository.
