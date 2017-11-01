import json
import sys
import subprocess
with open('list.json') as file:
	data=json.load(file)
	s=''
	for i in data:
		s = s + i[1] + ' '
	print(s)
	if(sys.argv[1]=='backup'):
		for i in data:
			subprocess.call("cp "+i[0]+" "+i[1], shell=True)
	elif(sys.argv[1]=='restore'):
		for i in data:
			subprocess.call("cp "+i[1]+" "+i[0], shell=True)		
	elif(sys.argv[1]=='push'):
		for i in data:
			subprocess.call("git add " + s)
			subprocess.call("git commit")
			subprocess.call("git push")
