# Exercício - Código para calcular gastos

gabriel = {
    'nome': 'Gabriel',
    'gastos': [49, 200, 9.99]
}

carol = {
    'nome': 'Carol',
    'gastos': [300, 420, 59.90, 33.80]
}

joao = {
    'nome': 'João',
    'gastos': [39.90, 23.50, 6.10, 19.50]
}

pessoas = [gabriel, carol, joao] 

for pessoas in range(1):
    print(f"{gabriel['nome']}")
    pessoa_gabriel = (gabriel['gastos'][0], gabriel['gastos'][1], gabriel['gastos'][2])
    pessoa1 = (gabriel['gastos'][0] + gabriel['gastos'][1] + gabriel['gastos'][2])
    print(f"O total gasto por {gabriel['nome']} é {pessoa1}")
    menor_valor = min(pessoa_gabriel)
    print(f"O menor valor de {gabriel['nome']} é {menor_valor}")
    menor_valor = max(pessoa_gabriel)
    print(f"O maior valor de {gabriel['nome']} é {menor_valor}\n")

    print(f"{carol['nome']}")
    pessoa_carol = (carol['gastos'][0], carol['gastos'][1], carol['gastos'][2])
    pessoa2 = (carol['gastos'][0] + carol['gastos'][1] + carol['gastos'][2])
    print(f"O total gasto por {carol['nome']} é {pessoa2}")
    menor_valor = min(pessoa_carol)
    print(f"O menor valor de {carol['nome']} é {menor_valor}")
    menor_valor = max(pessoa_carol)
    print(f"O maior valor de {carol['nome']} é {menor_valor}\n")

    print(f"{joao['nome']}")
    pessoa_joao = (joao['gastos'][0], joao['gastos'][1], joao['gastos'][2])
    pessoa3 = (joao['gastos'][0] + joao['gastos'][1] + joao['gastos'][2])
    print(f"O total gasto por {joao['nome']} é {pessoa3}")
    menor_valor = min(pessoa_joao)
    print(f"O menor valor de {joao['nome']} é {menor_valor}")
    menor_valor = max(pessoa_joao)
    print(f"O maior valor de {joao['nome']} é {menor_valor}")
    

# Implemente um loop for 
# para exibir por pessoa o:
# total gasto
# o menor valor gasto
# o maior valor gasto