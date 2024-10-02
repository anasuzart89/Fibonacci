import json

# 1) Cálculo da variável SOMA
def calcular_soma(indice):
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    return soma

# 2) Verificação se um número pertence à sequência de Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def verifica_fibonacci(numero):
    fib_sequence = fibonacci(numero)
    return numero in fib_sequence

# 3) Cálculo de faturamento
def calcular_faturamento(dados):
    faturamento = json.loads(dados)['faturamento_diario']
    faturamento_validos = [valor for valor in faturamento if valor > 0]

    if faturamento_validos:
        menor = min(faturamento_validos)
        maior = max(faturamento_validos)
        media = sum(faturamento_validos) / len(faturamento_validos)
        dias_acima_media = sum(1 for valor in faturamento_validos if valor > media)

        return menor, maior, dias_acima_media
    else:
        return None, None, 0

# 4) Cálculo percentual de faturamento por estado
def calcular_percentuais(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}
    return percentuais

# 5) Inversão de caracteres de uma string
def inverte_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# Execução do código

# 1) Cálculo da variável SOMA
indice = 13
soma_resultado = calcular_soma(indice)
print(f"SOMA de 1 a {indice}: {soma_resultado}")

# 2) Verificação de Fibonacci
numero_informado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
if verifica_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")

# 3) Cálculo de faturamento
dados_faturamento = '''
{
    "faturamento_diario": [200, 300, 400, 0, 500, 600, 0, 700, 800, 900, 0, 1000, 200]
}
'''
menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)

if menor is not None:
    print(f"Menor faturamento: R${menor:.2f}")
    print(f"Maior faturamento: R${maior:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")
else:
    print("Não há faturamento válido para calcular.")

# 4) Cálculo percentual de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentuais = calcular_percentuais(faturamento_estados)
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# 5) Inversão de caracteres de uma string
string_informada = input("Informe uma string para inverter: ")
string_invertida = inverte_string(string_informada)
print(f"String invertida: {string_invertida}")
