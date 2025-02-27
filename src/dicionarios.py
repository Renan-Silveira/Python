#criando um dicionario
meus_dados = {'name': 'Renan', 'age': 30}

#criando um dicionario vazio
dic_vazio = {}

meus_dados['name'] #retornando o valor da key name
#print Renan

#retornando as keys do dicionario
meus_dados.keys()
#print dict_keys(['name', 'age'])

#retornando os valores das keys
meus_dados.values()
#print dict_values(['Renan', 30])

#retornando o par de key-valores
meus_dados.items()
#print dict_items([('name', 'Renan'), ('age', 30)])

#adicionando/atualizando itens de um dicionario
meus_dados['altura'] = 1.7
meus_dados.update({'idiomas': ['Português', 'Françês']})

#removendo um item
meus_dados.pop('altura') #removendo por uma key
del meus_dados['idiomas'] #removendo por uma key
meus_dados.clear() #limpando todo o dict

#copiando um dicionario 
novo_dict = meus_dados.copy()

