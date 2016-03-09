#!/bin/bash

pushd /srv/salt
pip install -e /srv/salt
salt-master -l debug
