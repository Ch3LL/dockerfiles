#!/bin/bash

pushd /srv/salt
pip install -e /srv/salt
salt-minion -l debug
