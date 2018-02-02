import sys
import os

try:
        out_file = sys.argv[2]
except:
        out_file = "out.txt"
filename = sys.argv[1]
buf = ''

f = open(filename, 'r')
for k, line in enumerate(f.readlines()):
	if k == 0:
		out = '>'
	else: 
		out = '>>'

	inst = 'echo "' + line.strip("\n") + '" {} {}; '.format(out, out_file)

	buf += inst	

print buf
f.close()
