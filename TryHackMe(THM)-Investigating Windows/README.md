
# TryHackMe(THM) - Investigating Windows  - WriteUp

> Austin Lai | August 6th, 2021

---

<!-- Description -->

[Room = TryHackMe(THM) - Investigating Windows](https://tryhackme.com/room/investigatingwindows)

Difficulty: **easy**

**Note :** You will need at least basic amount of knowledge regarding registry key, powershell command, scripting and windows event as well as focusing on the event time.

<!-- /Description -->

<br />

## Table of Contents

<!-- TOC -->

- [TryHackMe(THM) - Investigating Windows  - WriteUp](#tryhackmethm---investigating-windows----writeup)
    - [Table of Contents](#table-of-contents)
    - [Question 1](#question-1)
    - [Question 2](#question-2)
    - [Question 3](#question-3)
    - [Question 4](#question-4)
    - [Question 5](#question-5)
    - [Question 6 - 8](#question-6---8)
    - [Question 9](#question-9)
    - [Question 10](#question-10)
    - [Question 11](#question-11)
    - [Question 12](#question-12)
    - [Question 13](#question-13)
    - [Question 14](#question-14)
    - [Question 15](#question-15)
    - [Question 16](#question-16)

<!-- /TOC -->

<br />

## Question 1

Whats the version and year of the windows machine?

This is easy, no explanation required.

## Question 2

Which user logged in last?

<details><summary>Hint given by the question</summary>

```text
That's you just now. But, who logged in before you?
```

</details>

<br />

Check out the Windows Event Log, easy peasy.

<br />

## Question 3

When did John log onto the system last?

Answer format: MM/DD/YYYY H:MM:SS AM/PM

<details><summary>Hint given by the question</summary>

```text
Try using cmd to find this out
```

</details>

<br />

Google it, what is the command or method to check user logon time !

<details><summary>Additional Hint</summary>

```text
netuser
```

</details>

<br />

## Question 4

What IP does the system connect to when it starts?

You notice there are a few command or process spwan during the startup.

However, if you didn't note down, there are ways to check out such as registry or task scheduler.

<br />

## Question 5

What two accounts had admin privileges (other than the Administrator user)?

Easy peasy, think of how you create account, and where you can check the group membership

<details><summary>Additional Hint</summary>

```text
control userpasswords2
```

</details>

<br />

## Question 6 - 8

Whats the name of the scheduled task that is malicious ?

What file was the task trying to run daily?

What port did this file listen locally for?

You can get the answer by checking the task scheduler and the content of it (including the content inside each file)

<br />

## Question 9

When did Jenny last logon?

Again, if you done question 3, then you should get the answer.

<br />

## Question 10

At what date did the compromise take place?

Answer format: MM/DD/YYYY

If you done question 6 -8, then you should know the answer.

<br />

## Question 11

At what time did Windows first assign special privileges to a new logon?

Answer format: MM/DD/YYYY HH:MM:SS AM/PM

<details><summary>Hint given by the question</summary>

```text
00/00/0000 0:00:49 PM
```

</details>

<br />

For this question, we can leveraging the information we get from question 10, check on the Windows Event Log to narrow down.

If you don't know what event to look for, Google it, you will get the event ID and event detail.

<br />

## Question 12

What tool was used to get Windows passwords?

Again, if you done question 6 -8, then you will get the tool, however if you not familiar with the tool, you can Google it !

Then you get the answer !

<br />

## Question 13

What was the attackers external control and command servers IP?

basic information, how a server communicate? DNS?

What would attacker done to get the IP or hostname resolved?

Have you check on hosts?

<br />

## Question 14

What was the extension name of the shell uploaded via the servers website?

For this question, a little bit of prior knowledge will be useful.

If you done basic enumeration, you notice there is a folder in C: drive.

That usually indicate Web Server, have you check what is there ??

Then you will find the answer.

<br />

## Question 15

What was the last port the attacker opened?

<details><summary>Hint given by the question</summary>

```text
Firewall
```

</details>

<br />

It is self-explanatory with the hint given.

<br />

## Question 16

Check for DNS poisoning, what site was targeted?

If you done question 13, you should get the answer !


<br />

---

> Do let me know any command or step can be improve or you have any question you can contact me via THM message or write down comment below or via FB




