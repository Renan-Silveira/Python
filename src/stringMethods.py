from datatypes import valorTexto #um import para usar a mesma variavel

# STRING METHODS #
upper = valorTexto.upper() #converte o texto em uppercase
#print EH SÓ UM TEXTO KKKK

lower = valorTexto.lower() #converte o texto em lowercase
#print eh só um texto kkkk

title = valorTexto.title() #converte em title case (primeira maiuscula de cada palavra)
#print Eh Só Um Texto Kkkk

stringCount = valorTexto.count('e') #conta quantas letras E tem no texto
#print 2

stringFind = valorTexto.find('e') #posição da letra pesquisada na primeira ocorrencia
#print 0

stringReplace = valorTexto.replace('h', '') #troca as ocorrencias do primeiro parametro pela do segundo parametro
#print e só um texto kkkk

#conectando strings#
mensagem_1  = "eu estou aprendendo python"
mensagem_2= "e é divertido"

#concatenando strings com operador +
mensagem = mensagem_1 + ' ' + mensagem_2 #concatena com uma string de espaço e com a segunda variavel
#print eu estou aprendendo python e é divertido

#concatenando com f-string
mensagemFString = f'{mensagem_1} {mensagem_2}'
#print eu estou aprendendo python e é divertido

#concatenando com valores atribuidos
mensagemAtribuida = '%s %s' %(mensagem_1,mensagem_2)
#print eu estou aprendendo python e é divertido