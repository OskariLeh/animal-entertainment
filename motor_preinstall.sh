#!/bin/bash
# Scripts that should be run as super user to make stepper mootors work

chown root.gpio /dev/gpiomem 
chmod g+rw /dev/gpiomem
