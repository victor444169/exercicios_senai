from colorama import init, Fore
init(autoreset=True)

print("|",30*"_","|")
print('| SISTEMA DE PROVAS')
print("|",30*"_","|")
nome = input('| Nome do aluno? ')

nota_1 = float(input('| Nota da primeira prova: '))
nota_2 = float(input('| Nota da segunda prova: '))
nota_3 = float(input('| Nota da segunda prova: '))

print("|",30*"_","|")
media = round((nota_1 + nota_2 + nota_3) /3, 2)
print('| ALUNO:', nome )
print('| MEDIA', media)
if media >=5:
    print("| ",Fore.GREEN+'Aluno Aprovado')
else:
    print("| ",Fore.RED+'Aluno Reprovado')    

print("|",30*"_","|")