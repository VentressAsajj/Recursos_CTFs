# [Task 1] Wgel CTF 26/10/2019
Have fun with this easy box.
### Antes de nada scaneo
`nmap -Pn -sT -p- -O -sC -sV -T5`<p>
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)<p>
| ssh-hostkey:<p>
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)<p>
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)<p>
|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)<p>
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))<p>
|_http-server-header: Apache/2.4.18 (Ubuntu)<p>
|_http-title: Apache2 Ubuntu Default Page: It works<p>
<p>
Dos puertos abierto: 22 y 80.<p>
Enumeración de directorios:<p>
`gobuster dir -u http://10.10.14.20/ -w /usr/share/wordlists/dirb/common.txt -t 25 -x php,html,txt -q`<p>

### #1	User flag<p>
### Solución:
`codigo`
Answer format: ********************************


### #2	Root flag
 
Answer format: ********************************

