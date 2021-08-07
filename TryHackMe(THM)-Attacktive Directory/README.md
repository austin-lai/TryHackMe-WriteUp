
# TryHackMe(THM) - Attacktive Directory - WriteUp

> Austin Lai | August 6th, 2021

---

<!-- Description -->

[Room = TryHackMe(THM) - Attacktive Directory](https://tryhackme.com/room/attacktivedirectorys)

Difficulty: **Medium**

However, I rate it as quite easy.

The room is completed on June 16th, 2021

<!-- /Description -->

<br />

## Table of Contents

<!-- TOC -->

- [TryHackMe(THM) - Attacktive Directory - WriteUp](#tryhackmethm---attacktive-directory---writeup)
    - [Table of Contents](#table-of-contents)
    - [Task 1 - 2](#task-1---2)
    - [Task 3](#task-3)
    - [Task 4](#task-4)
    - [Task 5](#task-5)
    - [Task 6](#task-6)
    - [Task 7](#task-7)
    - [Task 8](#task-8)

<!-- /TOC -->

<br />

## Task 1 - 2

Nothing to solve, read through the introduction.

## Task 3

Quite easy, have  you done basic enumeration? Fire up NMAP perhaps?

You will all the answer there.

<br />

## Task 4

Quite easy as well, instruction given to get start on a tool called "Kerbrute".

Do some basic research on how to use the tool, you will find all the answer there.

<br />

## Task 5

Quite easy as well, instruction given to get start on a tool called "Impacket".

Do some basic research on how to use the tool, you will find all the answer there.

Remember what are the users you found in previous task.

Then you will get the hash, google it, you will find the answer as well.

Now, you know it, cracked the hash !

If you have no idea what tools to use, check out JTR, hashcat ...

<br />

## Task 6

Now you got the username and password.

As the task stated, back to basic !

Do some basic enumeration, have you done any enumeration relevant to file server? samba? smb?

You will find the content is an encoded string, what base it used?

<br />

## Task 7

Quite easy as well, instruction given to get start on a subset tool called "secretsdump[.]py" within "Impacket".

Research how to use it, you will find the answer.

Tho, do you research on the method we used to get the hash?

<br />

## Task 8

Now you have all the user login.

Time to submit the flag !!!

<br />

---

> Do let me know any command or step can be improve or you have any question you can contact me via THM message or write down comment below or via FB




