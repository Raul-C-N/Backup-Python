# Python program to explain shutil.copytree() method
	
# importing os module
import os

# importing shutil module
import shutil

from datetime import date


# path
path = 'C:/Users/47889004/Documents/teste'

#define a data de hoje
today = date.today()
today_str = str(today)

# List files and directories
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'
print("Before copying file:")
print(os.listdir(path))


# Source path
src = 'W:/ATIVOS DE T.I'

# Destination path using today's timestamp
dest = path+'/'+today_str

# Copy the content of
# source to destination
destination = shutil.copytree(src, dest)

# List files and directories
# in "C:/Users / Rajnish / Desktop / GeeksforGeeks"
print("After copying file:")
print(os.listdir(path))

# Print path of newly
# created file
print("Destination path:", destination)
