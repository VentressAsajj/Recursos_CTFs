# [Task 1] Wgel CTF 26/10/2019
Have fun with this easy box.
### Antes de nada scaneo
```
$ nmap -Pn -sT -p- -O -sC -sV -T5
```
<p>
Es scaner nos indica la existencia de dos puertos, 22 y 80. Abrimos navegador y nos vamos al servidor http. La conexión solo muestra la página de información de apache, pero si vemos el código fuente nos desvela la existencia del comentario:
<p>
 
```
!-- Jessie don't forget to udate the webiste -->
```

<p>
Pasamos a enumerar las páginas:
<p>
 
```
gobuster dir -u http://IP/ -w /usr/share/wordlists/dirb/common.txt -t 25 -x php,html,txt -q
```
<p>
Nos quedamos con el directorio sitemap y volvemos a enumerar.
<p>
 
 ```
gobuster dir -u http://IP/sitemap -w /usr/share/wordlists/dirb/common.txt -t 25 -x php,html,txt -q 
 ```

<p>
Esta vez nos hemos encontrado con un directorio muy interesante  **/.ssh **
 
 
### #1	User flag<p>
### Solución:
`codigo`
Answer format: ********************************


### #2	Root flag
 
Answer format: ********************************

