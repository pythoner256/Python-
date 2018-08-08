import os

path = '/Users/Administrator/Desktop/images'
files = os.listdir(path)
# print(files)
for f in files:
    if 'know' in f and f.endswith('.png'):
        print("Found it"+f)

    

