#!/bin/ !python
#:  Blind Monitoring Eyes
#:  Author: ostronics(fg daemon)
#:  Synposis: Run with 'pkexec' on parrot os
#:              sudo pkexec
#:              python3 smile.py
#:  Date:   08-04-2025
#:  Version:    v1
#:  Warning!!!: Do not implement this in your malware, for Education purpose
#:              and slf use only.

import subprocess
import sys
import time

while True:
    try:
        for _ in range(10):
            subprocess.run(['/usr/sbin/mate-power-backlight-helper', '--set-brightness', '0'])
            time.sleep(3)
            subprocess.run(['/usr/sbin/mate-power-backlight-helper', '--set-brightness', '500'])
            time.sleep(5)
    except KeyboardInterrupt:
        break
        sys.exit(7)
        print('\n :}')
