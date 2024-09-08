#Exercício para calcular a sequência de Fibonacci.

# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


print('')
print('Sequência de Fibonacci.')
print("")

# Solicita ao usuário o número de termos que ele deseja mostrar
number = int(input('Quantos termos você quer mostrar? \n'))

# Inicializa os dois primeiros termos da sequência de Fibonacci
termOne = 0
termTwo = 1

# Imprime os dois primeiros termos da sequência
print('{}, {}'.format(termOne, termTwo), end='')

# Inicializa o contador para a próxima posição na sequência
cont = 3

# Calcula e imprime os termos seguintes da sequência até o número especificado
while cont <= number:
    # Calcula o próximo termo como a soma dos dois termos anteriores
    termThree = termOne + termTwo
    # Imprime o próximo termo
    print(', {}'.format(termThree), end='')
    # Atualiza os termos para o próximo cálculo
    termOne = termTwo
    termTwo = termThree
    # Incrementa o contador
    cont += 1

# Imprime uma mensagem final indicando que a sequência foi gerada
print('\n \nSequência de Fibonacci, feita!')