import subprocess

host = "www.google.com"
p1 = subprocess.Popen( [ 'ping', '-c 2', host ], stdout=subprocess.PIPE )
output = p1.communicate()[0]
print "-----------------------------------"
print output
print "-----------------------------------"
