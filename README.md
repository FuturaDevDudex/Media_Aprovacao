# Media_Aprovacao
Conclusão do desafio 07, da instituição 'Curso em Vídeo', utilizando a linguagem de Python. 

nome = input ('Qual o nome do aluno?'): Esta linha solicita que o usuário digite o nome do aluno e armazena o valor digitado na variável nome. A função input() exibe a mensagem 'Qual o nome do aluno?' no console e aguarda que o usuário insira um valor.

ID = str(input ('Qual é o ID do aluno?')): Esta linha solicita o ID do aluno e o armazena na variável ID. A função str() garante que o valor digitado seja tratado como uma string (texto).

nota01 = int(input ('informe sua nota da avaliação 1:')): Esta linha solicita a nota da primeira avaliação e a armazena na variável nota01. A função int() converte o valor digitado para um número inteiro.

nota02 = int(input ('informe sua nota da avaliação 2:')): Similar à linha anterior, esta solicita a nota da segunda avaliação e a armazena como um número inteiro na variável nota02.

soma = nota01 + nota02: Esta linha calcula a soma das notas das duas avaliações e armazena o resultado na variável soma.

media = soma / 2: Esta linha calcula a média das notas dividindo a soma por 2 (o número de avaliações) e armazena o resultado na variável media.

print (f'A somatória das avaliações {nota01} e {nota02}, correspondem a média {media}'): Esta linha exibe a média calculada no console. O "f" antes da string indica uma "f-string", que permite incluir o valor das variáveis diretamente no texto usando chaves {}.

media_aprovado = 60: Esta linha define a média mínima para aprovação como 60.

O bloco if...else verifica se o aluno foi aprovado ou reprovado:

if media >= media_aprovado:: Se a média do aluno for maior ou igual a 60, a linha print('Aluno Aprovado') é executada.

else:: Caso contrário, a linha print('Aluno Reprovado') é executada.
