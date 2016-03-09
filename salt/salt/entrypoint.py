#!/usr/bin/env python

import os
import pip
import subprocess
import sys
import threading

pip.main(['install', '/srv/salt'])


class Thread(object):
    threads = []

    @classmethod
    def start(cls, saltcmd):
        cmd = [saltcmd]
        if len(sys.argv) > 1:
            cmd.extend(sys.argv[1:])
        t = threading.Thread(target=subprocess.call, args=(cmd,))
        cls.threads.append(t)
        t.start()

if os.environ.get('SALT_MASTER', 'False') == 'True':
    Thread.start('salt-master')
if os.environ.get('SALT_API', 'False') == 'True':
    subprocess.call(['salt-call', '--local', 'tls.create_self_signed_cert'])
    Thread.start('salt-api')
if os.environ.get('SALT_MINION', 'False') == 'True':
    Thread.start('salt-minion')
if os.environ.get('SALT_PROXY', 'False') == 'True':
    Thread.start('salt-proxy')

for thread in Thread.threads:
    thread.join()
