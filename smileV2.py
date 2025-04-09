#!/bin/ !python
#:  Blind Monitoring Eyes
#:  Author: ostronics(fg daemon)
#:  Synposis: Run with 'pkexec' on parrot os
#:              sudo pkexec
#:              python3 smile.py
#:  Date:   08-04-2025
#:  Version:    v2
#:  Warning!!!: Do not implement this in your malware, for Education purpose
#:              and slf use only.

import getpass 
import random
import subprocess
import sys
import time

vo = random.randint(1,10)
if getpass.getuser() != 'root':
    print("You must run this program as root using: sudo /usr/bin/pkexec")
    sys.exit(1)
else:
    while True:
        try:
            for _ in range(vo):
                subprocess.run(['/usr/sbin/mate-power-backlight-helper', '--set-brightness', '0'])
                time.sleep(_)
                subprocess.run(['/usr/sbin/mate-power-backlight-helper', '--set-brightness', '80'])
                time.sleep(_)
        except KeyboardInterrupt:
            break
            sys.exit(7)
            print('\n :}')
subprocess.call(['/usr/sbin/mate-power-backlight-helper', '--set-brightness', '500'])
