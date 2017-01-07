import os
import hashlib

rootdir = '/vagrant/p1/static/images/'
albumid = -1
sequencenum = 0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file[0] == 'f':
            albumid = 2
        elif (file[0] == 'w'):
            albumid = 3
        elif (file[0] == 's'):
            if file[2] == 'a':
                albumid = 4
            elif file[2] == 'o':
                albumid = 1

        if file == 'load_data.py':
            continue
        if albumid == -1:
            continue

        m = hashlib.md5(str(albumid) + file)
        os.rename(rootdir + file, m.hexdigest() + ".jpg")
