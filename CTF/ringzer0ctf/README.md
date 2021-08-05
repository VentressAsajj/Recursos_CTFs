# Reto 172 - Ask your grandpa! -
Me bajo el zip y al descomprimir encuentro una imagen que representa una tarjeta perforada.

![](https://github.com/VentressAsajj/Pupurri/blob/master/CTF/ringzer0ctf/2033bb1b194adace86f99c7bb7d72e81.png)

Busco información sobre las tarjetas perforadas. Se trata de una tarjeta de 80 columnas. Estas tarjetas se dividen en zonas. Por un lado tenemos las filas 12,11,0 y por otro lado las filas del 1 al 9. La combinación de éstas forman el codigo:
- Si encontramos una columna con dos perforaciones, una en alguna de las zonas superiores ( 12,11 ó 0 ) y otra en la zona de digitos ( 1 al 9 ) entonces es una letra.
- Si solo hay perforación en la zona de los digitos entonces en un digito del 1 al 9.
- Dos perforaciones en la zona de digitos equivale a un caracter especial.
Comienzo a construir el codigo comenzando por las letras. 
A -> zona 12 + digito 1 ( z12,d1)
B -> z12,d2
C -> z12,d3 ...

Por ejemplo: La primera columna hay perforación en la zona 12 y el la zona de digito 6 ( z12,d6 ) por lo que será una #F
(https://github.com/VentressAsajj/Pupurri/blob/master/CTF/ringzer0ctf/Captura%20de%20pantalla%20-2021-08-06%2001-49-20.png)

Solución:
![](https://github.com/VentressAsajj/Pupurri/blob/master/CTF/ringzer0ctf/solucion_Ask_your_grandpa.png)
