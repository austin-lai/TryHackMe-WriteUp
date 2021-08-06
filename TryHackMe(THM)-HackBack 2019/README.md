
# TryHackMe(THM) - HackBack 2019  - WriteUp

> Austin Lai | August 6th, 2021

---

<!-- Description -->

[Room = TryHackMe(THM) - HackBack 2019](https://tryhackme.com/room/hackback2019)

Difficulty: **Medium**

<!-- /Description -->

<br />

## Table of Contents

<!-- TOC -->

- [TryHackMeTHM - HackBack 2019  - WriteUp](#tryhackmethm---hackback-2019----writeup)
    - [Table of Contents](#table-of-contents)
    - [Task 1 - 2](#task-1---2)
    - [Task 3](#task-3)

<!-- /TOC -->

<br />

## Task 1 - 2

Nothing to solve

## Task 3

You need to write a script that connects to this webserver on the correct port, do an operation on a number and then move onto the next port. Start your original number at 0.

The format is: operation, number, next port.

For example the website might display, add 900 3212 which would be: add 900 and move onto port 3212.

Then if it was minus 212 3499, you'd minus 212 (from the previous number which was 900) and move onto the next port 3499

Do this until you the page response is STOP (or you hit port 9765).

Each port is also only live for 4 seconds. After that it goes to the next port. You might have to wait until port 1337 becomes live again...

Go to: ` http://<machines_ip>:3010 ` to start...

Once you have done all operations, what number do you get (rounded to 2 decimal places at the end of your calculation)?



[Please check out the full script here](python-http-connect.py)


<br />

---

> Do let me know any command or step can be improve or you have any question you can contact me via THM message or write down comment below or via FB




