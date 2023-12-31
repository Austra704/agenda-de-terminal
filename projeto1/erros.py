# Erros em tempo de compilação
# Erros em tempo de execução
# Erros de lógica


def divisao(a, b):
    try:
        print(a/b)
    except Exception as e:
        print("Divisao inválida")
        print(e)


divisao(20, 0)