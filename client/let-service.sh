#!/usr/bin/env bash
cd /home/pi/punch-bug-p150716
chown root.root punch-bag-service.sh
chmod 755 punch-bag-service.sh
cp punch-bag-service.sh /etc/init.d/
chmod 755 sample-150716.py
update-rc.d punch-bag-service.sh defaults
ls -l /etc/rc?.d/*punch-bag-service.sh