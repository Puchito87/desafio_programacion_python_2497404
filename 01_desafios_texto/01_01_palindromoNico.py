#meter una linea de texto que chequee si es palindormo.
#no reconoce may ni minusculas

texto=input("Ingrese el texto:").lower().replace(" ","") 
#con lower pongo todo en min, si pongo upper() pasaria a mayuscula
#con replace(" ","") elimino todos los espacios

invertido=texto[::-1] #Aca creo la variable invertido con el [::-1] que lo invierte

#print(texto)
#print(invertido) #Estas son lineas para chequear que salia bien, las pongo en #

if texto==invertido:
  print("Ta igualio, pa.. es palindromo")
else:print("Nah papi, es no e' palindromo")
#Compara las dos variables, si son iguales da que si, sinó sale el otro.