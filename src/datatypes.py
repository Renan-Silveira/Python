# DATATYPES #
#o motivo desse arquivo é para que tenha registro do basico do python no meu github :)

#integers
valorInteiro = 1
valorDecimal =  1.2
valorTexto =  str('eh só um texto kkkk') # type: ignore
valorBooleano = True or False #type: ignore
valorLista = [0,1,2,3,4,5] 
valorDicionario = {'key0': 'valor0', 'key1': 'valor1'}

# STRING METHODS #
upper = valorTexto.upper() #converte o texto em uppercase
#EH SÓ UM TEXTO KKKK

lower = valorTexto.lower() #converte o texto em lowercase
#eh só um texto kkkk

title = valorTexto.title() #converte em title case (primeira maiuscula de cada palavra)
#Eh Só Um Texto Kkkk

stringCount = valorTexto.count('e') #conta quantas letras E tem no texto
#2

stringFind = valorTexto.find('e') #posição da letra pesquisada na primeira ocorrencia
#0

stringReplace = valorTexto.replace('h', '') #troca as ocorrencias do primeiro parametro pela do segundo parametro
print(stringReplace)

