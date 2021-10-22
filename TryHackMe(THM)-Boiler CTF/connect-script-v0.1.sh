#!/bin/bash

# Set your variable accordingly
ipaddr="10.10.32.200"
username="stoner"
password="superduperp@\$\$no1knows" # superduperp@$$no1knows
# username="basterd"
# password="superduperp@\$\$"

sshpass -v -p "$password" ssh -o StrictHostKeyChecking=no $username@$ipaddr -p 55007
