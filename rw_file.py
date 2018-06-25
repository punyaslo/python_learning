import os
import sys

file_to_write = input("Enter File name:")
print("opening the file for writing")

try:
   file_handle = open(file_to_write, "w")
except IOError:
    print("failed to open the file")


file_input = " "

while file_input != "exit":
    file_input = input("Enter a line: ")
    if file_input == "exit":
        file_handle.close()
        break
    file_handle.write(file_input)
    file_handle.write("\n")


file_handle.close()

print("dumping the contents")

try:
    file_handle = open(file_to_write, "r")
except IOError:
    print("failed to open the file")


contents = file_handle.read()
print(contents)