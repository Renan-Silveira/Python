#criando uma condicional

x = 1 #criando uma variavel só para testar a condicional
if x == 3: #se for 3 vai printar a frase abaixo
    print("é igual 3")
elif x == 2: #como não foi 3, se for 2 vai printar a frase abaixo
    print("é igual a 2")
else: #como não foi as outras condicionais, printa a frase abaixo
    print("é igual a 1")

#loops 
#loops de for
for x in [1,3,5,7,9]: #para cada item da lista, atribui o valor de x dentro do loop
    print(x)

#loop de for com enumerator
for i, element in enumerate([1,3,5,7,9]): #percorre a lista numerando os indices
    print(i) #numero no indice
    print(element) #valor do indice


#loop de for para obter elementos de dicionarios
meus_dados = {'name': 'Renan', 'age': 30}
for key, value in meus_dados.items():
    print(key) #printa a key dentro do loop
    print(value) #printa o valor da key dentro do loop

#while loop:
x = 0
while x <=10: #enquanto o valor de x for menor que o valor imposto fica dentro do loop
    x = x+1
    print(x)

#para que não ocorra problemas com os loops
#podemos implementar comandos para loops
#break: para a execução do loop
#continue: pula para próxima interação
#pass: não faz nada, geralmente usado para quando exige algum comando.

#funções
#as funções em python exigem que sejam definidas como a palavra reservada def
#exemplo
def soma(x,y): 
    #def de definir a função
    #soma é o nome dado a função
    #(x,y) são os parâmetros da função. variaveis necessárias para rodar a função.
    return x + y
    #return é para retornar o valor da função, pode ser para salvar o valor executado na função em uma variavel

valorSomado = soma(2,10) #atribui o valor somado a uma variavel passando os parametros 2 e 10, retornando a soma dos valores em 12


#importando modulos
#para importar modulos, precisamos usar a palavra reservada import seguida do modulo
import os #importando o modulo built-in OS (modulo que controla o sistema operacional)
import os as windows #nomeando o modulo os como windows
from os import getcwd #importando somente a funcao getcwd() do modulo os









