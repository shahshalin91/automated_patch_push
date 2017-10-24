import subprocess
import getpass
from jsonrpclib import Server
import pexpect
import sys


user = raw_input("Username:") #Input the username of an account on the switch
password = getpass.getpass("Password:") #Input the password of an account on the switch
extension_file = raw_input("Extension file name:") #Input the name of extension file to be copied
myfile = "./%s" %(extension_file) #Mention any extension that you are trying to push to the switches

with open("./hosts.txt") as host_list:
    ips = host_list.readlines()

for ip in ips:
  ip = ip.rstrip()
  destination = "%s@%s:" % (user, ip)
  scp_cmd = "scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null " + myfile + " " + destination
  print "\nCOPYING FILE %s TO SWITCH %s \n Please wait for few secs....." %(extension_file, ip)
  try:
    pexpect.run(scp_cmd)
    child = pexpect.spawn(scp_cmd)
    child.expect(r'.*assword:')
    child.sendline(password)
    child.expect(pexpect.EOF,timeout=5)
    output_lines = child.before
    print output_lines
  except:
    print "COPYING FILE %s TO SWITCH %s FAILED" % (extension_file,ip)
  else:
    print "COPYING FILE %s TO SWITCH %s SUCCESFUL" % (extension_file,ip)
  url = "http://%s:%s@%s/command-api" %(user,password,ip)
  copy_cmd = "copy flash:%s extension:" %(extension_file)
  extension_cmd = "extension %s" %(extension_file)
  cmds = ["enable","configure",copy_cmd, extension_cmd, "copy installed-extensions boot-extensions"]
  try:
    switch = Server(url)
    extension_push = switch.runCmds(1,cmds,"json")
  except:
    print "INSTALLING EXTENSION %s FAILED for %s" % (ip)
    print "=================================================================================================="

    with open('./output_logs', 'a') as f:     
      status = "%s:             FAILED\n" % (ip)
      f.write(status)
  else:
    print "INSTALLING EXTENSION %s SUCCESFUL for %s" % (ip)
    print "=================================================================================================="
    with open('./output_logs.txt', 'a') as f:     
      status = "%s:            SUCCESFUL\n" % (ip)
      f.write(status)
