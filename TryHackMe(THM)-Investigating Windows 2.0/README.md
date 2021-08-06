
# TryHackMe(THM) - Investigating Windows 2.0  - WriteUp

> Austin Lai | August 1st, 2021

---

<!-- Description -->

[Room = TryHackMe(THM) - Investigating Windows 2.0](https://tryhackme.com/room/investigatingwindows2)

Difficulty: **Medium**

The question is jump back and forth, so ...

**Note :** You will need at least basic amount of knowledge regarding registry key, powershell command, scripting and windows event as well as focusing on the event time.

<!-- /Description -->

<br />

## Table of Contents

<!-- TOC -->

- [TryHackMe(THM) - Investigating Windows 2.0  - WriteUp](#tryhackmethm---investigating-windows-20----writeup)
    - [Table of Contents](#table-of-contents)
    - [Question 1](#question-1)
    - [Question 2](#question-2)
    - [Question 3 - 7 , 15 - 24 , 26 - 28](#question-3---7--15---24--26---28)
    - [Question 8](#question-8)
    - [Question 9](#question-9)
    - [Question 10](#question-10)
    - [Question 11 - 13](#question-11---13)
    - [Question 14](#question-14)
    - [Question 25](#question-25)
    - [Question 29](#question-29)
    - [Question 30](#question-30)

<!-- /TOC -->

<br />

## Question 1

- Question 1 = What registry key contains the same command that is executed within a scheduled task?

Have you check on the task scheduler ?

Any detail?

Then go to registry editor (regedit), search for the detail.

You will find the answer there.

<br />

## Question 2

- Question 2 = What analysis tool will immediately close if/when you attempt to launch it?

Check out the "Tools" folder on the desktop.

Have you launch the most common SysInternals tool which allow you to view process?

<br />

## Question 3 - 7 , 15 - 24 , 26 - 28

- Question 3 = What is the full WQL Query associated with this script?

- Question 4 = What is the script language?

- Question 5 = What is the name of the other script?

- Question 6 = What is the name of the software company visible within the script?

- Question 7 = What 2 websites are associated with this software company? (answer, answer)

Since "loki" is provided in the "Tools" folder, why not have it run?

Remember to store the output so you can make it as reference for following questions

Once you have the loki result, you will find the answer.

Alternatives, since you know where the script located, why not open up and examine the content ?!

<br />

- Question 15 = Run Loki. Inspect the output. What is the name of the module after `Init`?

- Question 16 = Regarding the 2nd warning, what is the name of the eventFilter?

- Question 17 = For the 4th warning, what is the class name?

- Question 18 = What binary alert has the following 4d5a90000300000004000000ffff0000b8000000 as FIRST_BYTES?

- Question 19 = According to the results, what is the description listed for reason 1?

- Question 20 = Which binary alert is marked as APT Cloaked?

- Question 21 = What are the matches? (str1, str2)

- Question 22 = Which binary alert is associated with somethingwindows.dmp found in C:\TMP?

- Question 23 = Which binary is encrypted that is similar to a trojan?

- Question 24 = There is a binary that can masquerade itself as a legitimate core Windows process/image. What is the full path of this binary?

- Question 26 = What is the description listed for reason 1?

- Question 27 = There is a file in the same folder location that is labeled as a hacktool. What is the name of the file?

- Question 28 = What is the name of the Yara Rule MATCH?

Once again for the questions mentioned above can be found in loki output !!!

<br />

## Question 8

- Question 8 = Search online for the name of the script from Q5 and one of the websites from the previous answer. What attack script comes up in your search?

Google it

<br />

## Question 9

- Question 9 = What is the location of this file within the local machine?

You know the answer by now !

<br />

## Question 10

- Question 10 = Which 2 processes open and close very quickly every few minutes? (answer, answer)

You know the answer by now !

<br />

## Question 11 - 13

- Question 11 = What is the parent process for these 2 processes?

- Question 12 = What is the first operation for the first of the 2 processes?

- Question 13 = Inspect the properties for the 1st occurrence of this process. In the Event tab what are the 4 pieces of information displayed? (answer, answer, answer, answer)

Try to track the parent process from ProcMon (Process Monitor) tool from SysInternals

You may filter the event that allow you to get the answer for question 12

Answer for question 13 is right in front of you !

<br />

## Question 14

- Question 14 = Inspect the disk operations, what is the name of the unusual process?

Hint given to use "Process Hacker"

<br />

## Question 25

- Question 25 = What is the full path location for the legitimate version?

Google it with the answer you get in question 24

<br />

## Question 29

- Question 29 = Which binary didn't show in the Loki results?

You should know the answer by now !

<br />

## Question 30

- Question 30 = Complete the yar rule file located within the Tools folder on the Desktop. What are 3 strings to complete the rule in order to detect the binary Loki didn't hit on? (answer, answer, answer)

Check the yara rule against the binary with keyword "strings" !

Which is "strings64.exe" offered by SysInternals

<br />

---

> Do let me know any command or step can be improve or you have any question you can contact me via THM message or write down comment below or via FB




