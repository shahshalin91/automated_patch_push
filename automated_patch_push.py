import subprocess
import getpass
from jsonrpclib import Server
import pexpect
import sys


myfile = "./SecurityAdvisory0030-Hotfix.swix" #Mention any extension that you are trying to push to the switches

with open("./hosts.txt") as host_list:
    ips = host_list.readlines()

user = raw_input("Username:") #Input the username of an account on the switch
password = getpass.getpass("Password:") #Input the password of an account on the switch

for ip in ips:
	ip = ip.rstrip()
	destination = "%s@%s:" % (user, ip)
	scp_cmd = "scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null " + myfile + " " + destination
	print "\nCOPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH %s \n Please wait for few secs....." %(ip)
 	try:
 		pexpect.run(scp_cmd)
 		child = pexpect.spawn(scp_cmd)
		child.expect('Password:')
		child.sendline(password)
		child.expect(pexpect.EOF,timeout=5)
		output_lines = child.before
		print output_lines
	except:
		print "COPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH %s FAILED" % (ip)
	else:
		print "COPYING FILE SecurityAdvisory0030-Hotfix.swix TO SWITCH %s SUCCESFUL" % (ip)
	url = "http://%s:%s@%s/command-api" %(user,password,ip)
	cmds = ["enable","configure","copy flash:SecurityAdvisory0030-Hotfix.swix extension:","extension SecurityAdvisory0030-Hotfix.swix","copy installed-extensions boot-extensions"]
	try:
		switch = Server(url)
		extension_push = switch.runCmds(1,cmds,"json")
	except:
		print "INSTALLING EXTENSION SecurityAdvisory0030-Hotfix.swix FAILED for %s" % (ip)
		print "=================================================================================================="

		with open('./output_logs', 'a') as f:			
			status = "%s:             FAILED\n" % (ip)
			f.write(status)
	else:
		print "INSTALLING EXTENSION SecurityAdvisory0030-Hotfix.swix SUCCESFUL for %s" % (ip)
		print "=================================================================================================="
		with open('./output_logs.txt', 'a') as f:			
			status = "%s:            SUCCESFUL\n" % (ip)
			f.write(status)