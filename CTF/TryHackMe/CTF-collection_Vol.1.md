## [Task 2] 
Can you decode the following?
VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==

#### #1	Feed me the flag!<p>
### Solución:
`printf "..." | base64 -d ` <p>
THM{}<p>

## [Task 3] Meta meta02/01/2020<p>
Meta! meta! meta! meta...................................<p>

#### #1 I'm hungry, I need the flag.<p>
### Solución:
`exiftool Fidme.jpg`<p>
THM{}<p>

## [Task 4] Mon, are we going to be okay?02/01/2020<p>
Something is hiding. That's all you need to know.<p>
<p>

#### #1	It is sad. Feed me the flag.<p>
### Solución:
`steghide extract -sf Extinction.jpg`<p>
THM{}

## [Task 5] Erm......Magick02/01/2020
Huh, where is the flag?

#### #1	Did you find the flag?
### Solución:
En este reto, puedes tirar de las herramientas de desarrollador y buscar el párrafo correspondiente a task 5 o ...
señala con el ratón todo el texto de esta parte :D
THM{}

## [Task 6] QRrrrr02/01/2020
Such technology is quite reliable.

### #1 More flag please!
### Solución:
Buscamos cualquier herramienta que decodifique QR online.  [Por ejemplo](https://www.onlinebarcodereader.com/es.html)

THM{}

## [Task 7] Reverse it or read it?02/01/2020
Both works, it's all up to you.

### #1	Found the flag?
### Solución:
` strings hello.hello|grep THM`<p>
THM{}

## [Task 8] Another decoding stuff02/01/2020
Can you decode it?
3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L

### #1	Oh, Oh, Did you get it?
### Solución:
`hashid -mje 3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L`<p>
`Analyzing '3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L'<p>
[+] BigCrypt [JtR Format: bigcrypt]`

THM{}
