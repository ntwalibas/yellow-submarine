#!/usr/bin/env python

import sys
import subprocess

def main(n_calls):
    use_s = 1
    use_d = 1
    use_ng = 0
    for i in range(int(n_calls)):
        subprocess.run(['python', 'main.py', str(i), str(use_s), str(use_d), str(use_ng)])

if __name__ == '__main__':
    main(sys.argv[1])
