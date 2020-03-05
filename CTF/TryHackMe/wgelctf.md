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
Esta vez nos hemos encontrado con un directorio muy interesante  **/.ssh** Cuando nos conectamos a esa página vemos el fichero con la clave privada de ssh. Dado que sólo tenemos un usuario, probamos a conectarnos vía ssh al server. Antes de nada hay que cambiar los permisos al fichero.
 ```
 $ chmod 600 id_rsa
 $ ssh -i ./id_rsa jessie@ip
 ```
 
 
 
### #1	User flag<p>
### Solución:
`codigo`
Answer format: ********************************


### #2	Root flag
 
Answer format: ********************************

