def calcular_pagamento(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

if __name__ == "__main__":
    horas = float(input("Horas trabalhadas: "))
    valor = float(input("Valor por hora: R$ "))
    pagamento = calcular_pagamento(horas, valor)
    print(f"Pagamento total: R$ {pagamento:.2f}")
