from argparse import OPTIONAL
import subprocess
import optparse
parser= optparse.OptionParser()
##var = parser()
## OPTIONAL('-i','--interface', dest='interface', help='interface to change mac Address')
parser.parse_args()
interface=input('Please enter your Interface:')
new_mac=input('Please Enter an MAC Address:')
print('[+] Changing MAC Add for'+interface+new_mac)
subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])