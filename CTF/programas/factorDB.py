"""
author: @nuria_imeq
Resolucion de picoCTF 
Mind your Ps and Qs
Description
In RSA, a small e value can be problematic, but what about N? 
Can you decrypt this? values

Te dan los valores del 
c => ciphertext 
n =>  el modulo de las claves publica y privada. Tengo que encontrar dos primos p y q
e => exponente

Al ser n pequeño puedo buscar dos primos.(jejeje tiene gracia :D )
uso la base de datos factorDB para obtener dos primos.

"""
from factordb.factordb import FactorDB
from Crypto.Util.number import inverse


c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e = 65537
f = FactorDB(n) # uso el modulo factordb para conectarme a factordb.com y 
                # traerme los primos.
f.connect()
p,q= f.get_factor_list()
#print("p ",p)
#print("q ",q)

ph = (p-1)*(q-1)
d=inverse(e,ph)
flag=pow(c,d,n)
print("Flag: {}".format(bytearray.fromhex(format(flag, 'x')).decode()))
