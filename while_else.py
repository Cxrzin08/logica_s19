# Exercício Python: While com Else
# Crie um laço loop while que se repete 
# enquanto uma determinada condição for verdadeira.

while True:
    idade_entrada = int(input("Digite a temperatura da água para verificar a temperatura está liguida\nDigite sua opção:"))
    if idade_entrada >= 100:
        print("A água está em ebulição\nPrograma encerrado...")
        break
    else:
        print("A água está liquida")


while True:
    primo_input = int(input("Digite um número para verificar se é primo: "))

    if primo_input <= 1:
        print("O número não é primo")
    else:
        divisor = 2
        while divisor * divisor <= primo_input:
            if primo_input % divisor == 0:
                print("O número não é primo")
                break
            divisor += 1
        else:
            print("Seu número é primo")
    
    break



# O loop while deve ter um else para 
# executar quanto o loop while for finalizado 
# normalmente.

# A implementação deve pedir por um número 
# maior que 1 e menor ou igual 100 e verificar 
# se a condição é verdadeira, 
# faça um loop while para verificar também 
# se o número é um número primo.

# Atenção: não faça uma condição loop `divisor <= numero`