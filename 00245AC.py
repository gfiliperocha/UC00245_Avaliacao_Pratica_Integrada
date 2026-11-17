urgentes = 0
total_minutos = 0
maior_tempo = 0

for pedido in range(1, 11):

    # Validação da prioridade
    while True:
        try:
            prioridade = int(
                input(f"Pedido {pedido} - Prioridade (1 a 5): ")
            )

            if 1 <= prioridade <= 5:
                break

            print("Erro: a prioridade deve estar entre 1 e 5.")

        except ValueError:
            print("Erro: introduza um número inteiro.")

    # Validação do tempo
    while True:
        try:
            tempo = int(
                input("Tempo estimado de resolução, em minutos: ")
            )

            if tempo > 0:
                break

            print("Erro: o tempo deve ser superior a zero.")

        except ValueError:
            print("Erro: introduza um número inteiro.")

    # Contagem dos pedidos urgentes
    if prioridade == 1 or prioridade == 2:
        urgentes += 1

    # Atualização do total
    total_minutos += tempo

    # Atualização do maior tempo
    if tempo > maior_tempo:
        maior_tempo = tempo

# Cálculo da média
media = total_minutos / 10

# Classificação da carga
if urgentes >= 5 or total_minutos > 600:
    classificacao = "CRÍTICA"
elif urgentes >= 3 or total_minutos > 480:
    classificacao = "ELEVADA"
else:
    classificacao = "NORMAL"

# Apresentação dos resultados
print("\n----- RESUMO DA CARGA DE TRABALHO -----")
print(f"Pedidos urgentes: {urgentes}")
print(f"Total de minutos: {total_minutos}")
print(f"Média por pedido: {media:.2f} minutos")
print(f"Maior estimativa: {maior_tempo} minutos")
print(f"Classificação: {classificacao}")