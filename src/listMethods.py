#criando uma lista
paises = ['USA', 'India', 'China', 'Brazil'] #lembrando que o indice sempre começa com 0
#[0,1,2,3,etc]

#criando uma lista vazia
listaVazia = []

#indexação de uma lista
paises[0] #retornando o valor na casa 0 da lista
#print USA

paises[3] #retornando o valor na casa 3 da lista
#print Brazil

paises[2] #retornando o valor na casa 2 da lista
#print China


#cortando uma lista
paises[0:2] #retorna paises na casa 0 até a casa 1
#print ['USA', 'India']

paises[1:] #retorna a lista a partir do indice 1
#print ['India', 'China', 'Brazil']

paises[:2] #retorna a lista até o indice 1, o indice final é sempre x-1
#print ['USA', 'India']

#adicionando itens a uma lista
paises.append('Canadá') #adiciona na lista após o ultimo indice
#print ['USA', 'India', 'China', 'Brazil', 'Canadá']

paises.insert(0,'Canadá') #adiciona na lista conforme o indice passado no parâmetro
#print ['Canadá', 'USA', 'India', 'China', 'Brazil']

#lista aninhada
listaAninhada = [paises, paises] #type: ignore

#remover elementos
paises.remove('Brazil') #remove um elemento especifico da lista
#print ['USA', 'India', 'China']

paises.pop(0) #remove o elemento conforme o indice

del paises[0] #remove o elemento conforme o indice

#criando uma nova lista
numeros = [4, 3, 10, 7, 1, 2]

numeros.sort() #ordenando uma lista
#print [1, 2, 3, 4, 7, 10]

numeros.sort(reverse=True) #ordenando uma lista na ordem reversa
#print [10, 7, 4, 3, 2, 1]


