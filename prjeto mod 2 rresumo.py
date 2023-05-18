# Função para buscar candidatos com base nos critérios
def buscar_candidatos(candidatos, nota_entre, nota_teo, nota_prat, nota_soft):
    candidatos_encontrados = []  # Lista para armazenar os candidatos encontrados
    
    for candidato in candidatos:  # Percorre cada candidato na lista de candidatos
        nome = candidato['candidato']  # Obtém o nome do candidato
        entre = candidato['entre']  # Obtém a nota do candidato na etapa de entrevista
        teo = candidato['teo']  # Obtém a nota do candidato no teste teórico
        prat = candidato['prat']  # Obtém a nota do candidato no teste prático
        soft = candidato['soft']  # Obtém a nota do candidato na avaliação de soft skills
        
        # Verifica se as notas do candidato são maiores ou iguais às notas mínimas desejadas
        if entre >= nota_entre and teo >= nota_teo and prat >= nota_prat and soft >= nota_soft:
            candidatos_encontrados.append(nome)  # Adiciona o nome do candidato à lista de candidatos encontrados
    
    return candidatos_encontrados  # Retorna a lista de candidatos encontrados

# Lista de candidatos e seus resultados
candidatos = [
    {'candidato': 'Pamela', 'entre': 5, 'teo': 5, 'prat': 8, 'soft': 7},
    {'candidato': 'Luara',  'entre':  4, 'teo': 6, 'prat': 8, 'soft': 3},
    {'candidato': 'Amanda', 'entre': 3, 'teo': 4, 'prat': 7, 'soft': 8},
    {'candidato': 'Ariane', 'entre': 7, 'teo': 8, 'prat': 4, 'soft': 5},
    {'candidato': 'Paloma', 'entre': 5, 'teo': 2, 'prat': 9, 'soft': 7}
]

# Solicita ao usuário as notas mínimas desejadas
nota_entre = int(input('Nota mínima em entrevista: '))
nota_teo = int(input('Nota mínima no teste teórico: '))
nota_prat = int(input('Nota mínima no teste prático: '))
nota_soft = int(input('Nota mínima em avaliação de soft skills: '))

# Chama a função de busca com as notas digitadas pelo usuário
candidatos_encontrados = buscar_candidatos(candidatos, nota_entre, nota_teo, nota_prat, nota_soft)

# Exibe os candidatos encontrados
if candidatos_encontrados:
    print("Candidatos encontrados:")
    for candidato in candidatos_encontrados:
        print(candidato)
else:
    print("Nenhum candidato encontrado com as notas mínimas desejadas.")
