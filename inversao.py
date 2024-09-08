#Exercício para inverter uma string.


#Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

# Solicita ao usuário para digitar uma frase
string = input("Digite uma frase para inverter: ")

# Inicializa uma string vazia para armazenar o resultado
string_invertida = ''

# Loop para construir a string invertida
for char in string:
    # Adiciona cada caractere no início da string invertida
    string_invertida = char + string_invertida

# Exibe a string invertida
print("Frase invertida:", string_invertida)

