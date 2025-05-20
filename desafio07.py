nome = input ('Qual o nome do aluno?')
ID = str(input ('Qual é o ID do aluno?'))
nota01 = int(input ('informe sua nota da avaliação 1:'))
nota02 = int(input ('informe sua nota da avaliação 2:'))

soma = nota01 + nota02
media = soma / 2

print (f'A somatória das avaliações {nota01} e {nota02}, correspondem a média {media}')

media_aprovado = 60

if media >= media_aprovado:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')