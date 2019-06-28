nome = str(input("Digite seu nome: "))

if nome == 'Eudson':
    print("Que nome bonito!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome é bem popular no Brasil.")
#Esse "in" diz que se nome conter qualquer um desses nomes
elif nome in 'Ana Cládia Jéssica Juliana':
    print("Belo nome feminino") 
else:
    print("Nome generico")
print("Tenha um bom dia,{}!".format(nome))