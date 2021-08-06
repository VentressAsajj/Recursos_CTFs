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

Por ejemplo: La primera columna hay perforación en la zona 12 y el la zona de digito 6 ( z12,d6 ) por lo que será una F
(https://github.com/VentressAsajj/Pupurri/blob/master/CTF/ringzer0ctf/Captura%20de%20pantalla%20-2021-08-06%2001-49-20.png)
## Código
A -> [Z12,D1] B -> [Z12,D2] C -> [Z12,D3] D -> [Z12,D4] E -> [Z12,D5] F -> [Z12,D6]
G -> [Z12,D7] H -> [Z12,D8] I -> [Z12,D9] J -> [Z11,D1] K -> [Z11,D2] L -> [Z11,D3]
M -> [Z11,D4] N -> [Z11,D5] O -> [Z11,D6] P -> [Z11,D7] Q -> [Z11,D8] R -> [Z11,D9]
S -> [Z00,D2] T -> [Z00,D3] U -> [Z00,D4] V -> [Z00,D5] W -> [Z00,D6] X -> [Z00,D7] 
Y -> [Z00,D8] Z -> [Z00,D9] 

Caracteres especiales y el número 0:
Z11 -> -  Z12 -> &   Z00 -> 0
Z12,D3-D8 -> .  Z12,D4-D8 -> <   Z12,D5-D8 -> (  Z12,D6-D8 -> +  Z12,D7-D8 -> |   
Z11,D2-D8 -> !  Z11,D3-D8 -> $   Z11,D4-D8 -> *  Z11,D5-D8 -> )  Z11,D6-D8 -> ;  
Z00,D3-D8 -> ,  Z00,D4-D8 -> %   Z00,D7-D8 -> ?  Z00,D5-D8 -> _  Z00,D6-D8 -> >  
Z00,D7-D8 ¬
Z00-D1    -> /  
D2-D8 -> :   D3-D8 -> #   D4-D8 -> @   D5-D8 -> '  D6-D8 -> =   D7-D8 -> "

Para los caracteres especiales encontré una url que es un [emulador](https://www.masswerk.at/keypunch/) de tarjetas perforadas. Para ver si es correcto el código que he escrito con el código que aparece en la imagen extraida, escribo en el emulador la palabra FLAG y compruebo que es correcto. Comienzo a decodificar.


## Solución:
![](https://github.com/VentressAsajj/Pupurri/blob/master/CTF/ringzer0ctf/solucion_Ask_your_grandpa.png)
