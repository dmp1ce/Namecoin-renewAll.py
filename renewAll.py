#!/usr/bin/python
import json
import commands

(name_list_status, name_list_output)=commands.getstatusoutput('./namecoind name_list')

data = ""
if name_list_status == 0:
	data = json.loads(name_list_output)
else:
	print "Failed"
	exit()

for name in data:
	if name["expires_in"] < 2000:
		update_command = './namecoind name_update '+ name["name"] + ' ' + name["value"].replace('"', '\\"')
		print update_command
		update = commands.getoutput ('./namecoind name_update '+ name["name"] + ' ' + name["value"].replace('"', '\\"'))
		print update
		#exit()
