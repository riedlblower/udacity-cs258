# List of files to use as initial seed
file_list=[
  "test_files/test1.txt",    
  "test_files/test2.txt",    
  "test_files/test3.txt",
  ]

# List of applications to test

app = "gedit"

fuzz_output = "test_files/fuzz"

FuzzFactor = 250
num_tests = 10000

########### end configuration ##########

import math
import random
import string
import subprocess
import time
import os

stats = []

for i in range(num_tests):
    file_choice = random.choice(file_list)
    #app = random.choice(apps)

    buf = bytearray(open(file_choice, 'rb').read())

    # start Charlie Miller code
    numwrites=random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1

    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c"%(rbyte)
    #end Charlie Miller code

    open(fuzz_output, 'wb').write(buf)
    process = subprocess.Popen([app, fuzz_output])
    statinfo = os.stat(file_choice)
    time.sleep(int(statinfo.st_size/10000))
    crashed = process.poll()
    if not crashed:
	process.terminate()
    else:
        stats.append((app, file_choice))

results = open("test_files/stats.monkey", "wt")
print "%d crashes\n" % len(stats)
for c in stats:
    print c
    results.write(c[0] + c[1])
