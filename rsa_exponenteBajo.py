'''
Solucion para ctf cuyo exponente es muy bajo, se buscan ataques de exponentes bajos (exponent attack)
RSA C = M^e (mod n) pero cuando n, modulus, es mucho mas grande que exponente y el mensaje cifrado no es muy largo (M pequeño)
entonces M^e(mod n) = M^e entonces M se encuentra calculando la raiz n-esima de C.
'''
import gmpy2

n = 0x9ffa2a58ad286990fc5fe97b669e8cb2752e81fafa5ac774ea856d8ca124089ba4b06fe21a5d588c1dcb9602838d32cd70e50b85dec21fa79944543176c7a3b8b804ab754af2978f23b09f2905103dd5a4c748df8d9e9a079a5b38f6f69051b3c6582ebc2d2d199b3a97cb7e58af79b90fe08884626d188e194816bd51960a45
e = 0x3
c = 0x10652cdfaa6a6f6f688b98219cd32ce42c4d4df94afaea31cd94dfac50678b1f50f3ab1fd389f9998b6727ffd1a2c06ee6bde21ae85daef63fd0fa694a93f3674dc3f9ea0f2e3283a3d9897137aea12458aa3b8f96c61f3bf74a510bab7e7d8b7af52290d2621f1e06e52e6a7be4896c6465


gs = gmpy2.mpz(c)
gm = gmpy2.mpz(n)
ge = gmpy2.mpz(e)

root, exact = gmpy2.iroot(gs, ge)
print(bytes.fromhex((format(root, 'x'))))
