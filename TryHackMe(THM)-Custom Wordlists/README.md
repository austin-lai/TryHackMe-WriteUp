
# TryHackMe(THM) - Custom Wordlists - WriteUp

> Austin Lai | July 25th, 2021

---

<!-- Description -->

[Room = TryHackMe(THM) - Custom Wordlists](https://tryhackme.com/room/customwordlists)

Difficulty: **easy**

The room recommends using either fcrackzip or John the Ripper for cracking the passwords.

Personally --- suggest to use JTR with zip2john, you can install JTR or it comes with Kali.

Note:

  - Below writeup will be using Windows base WSL 2 - Ubuntu Distro
  - Install with JTR
  - python2.7 (since JTR zip2john require python2.7) & python3.9

<!-- /Description -->

<br />

## Table of Contents

<!-- TOC -->

- [TryHackMe(THM) - Custom Wordlists - WriteUp](#tryhackmethm---custom-wordlists---writeup)
    - [Table of Contents](#table-of-contents)
    - [Task 1](#task-1)
    - [Task 2](#task-2)
    - [Task 3](#task-3)
    - [Task 4](#task-4)
    - [Task 5](#task-5)

<!-- /TOC -->

<br />

## Task 1

For task 1, you may follow-thru the task instruction and get the basic understanding of the room

<br />

## Task 2

For task 2, you may also follow-thru the task instruction and get the tools.

As mentioned, personally would suggest to use JTR.

Do download the [rockyou](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz) from DanielMiessler - SecLists.

If you using kali, it will be in the directory - ` /usr/share/wordlists/ `; do copy it to your working directory as you won't want to modify the original rockyou list.

<br />

## Task 3

**Using grep**

Note:

- Before you start to crack the password, do generate every zip hashes if you plan to use JTR --- ` zip2john flag1.txt.zip > flag1hash.txt `

- Presuming you know JTR command ` john flag1hash.txt --wordlist=rockyou.txt `

<br />

For task 3, read-thru and understand the command.

- Password Requirements: 8 length minimum
  - ` cat rockyou.txt | grep -x '.\{8,20\}' > 8-20_length_wordlist `

- Password Requirements: 1 Uppercase
  - ` cat rockyou.txt | grep -o '[^ ]*[A-Z][^ ]*' > contains_uppercase.txt `

- Password Requirements: 10 length minimum, Uppercase, Special Characters
  - Since we have uppercase list from the above, leveraging it to create wordlist match the requirement
  - Filter to capture only min. 10 length --- ` cat contains_uppercase.txt | grep -x '.\{10,20\}' > 10-20_length_wordlist `
  - Filter to capture only contain special character --- ` grep -v "^[A-Za-z0-9]*$" > 10-20-contains_special.txt `

<br />

## Task 4

**Using sed**

- Password Requirements: 1 Uppercase
  - ` sed -e 's/\b\(.\)/\u\1/g' rockyou.txt > 1-upper-rockyou.txt` 

- Password Requirements: 1 Special Character
  - ` sed -e 's/$/\! &/' rockyou.txt > 1-upper-rockyou.txt` 

<br />

## Task 5

- Download HashcatRulesEngine

  ```
  git clone https://github.com/llamasoft/HashcatRulesEngine

  cd HashcatRulesEngine 

  make
  ```

- Download hashcat rule by Korelogic from https://contest-2010.korelogic.com/rules-hashcat.html
  - Which is port over from JTR rule to match hashcat rule engine base
  - `KoreLogicRulesL33t.rule` and `KoreLogicRulesAppendMonthCurrentYear.rule`

- Prepare your own wordlist, check on the task instruction
  - custom-pass.txt

    ```txt
    HorseShark 

    <!-- Do take note HashcatRulesEngine require additional space to each line when you create inital wordlist before passing it to HashcatRulesEngine --->
    ```

- To use HashcatRulesEngine the syntax is as follows:

  ```bash
  ./hcre rulefile1.rule rulefile2.rule < wordlist.txt > new_wordlist.txt

  # In the task mentioned using 2 rule
  cat custom-pass.txt | ./hcre KoreLogicRulesAppendMonthCurrentYear.rule KoreLogicRulesL33t.rule > new-custom-pass.txt
  ```

<br />

---

> Do let me know any command or step can be improve or you have any question you can contact me via THM message or write down comment below or via FB




