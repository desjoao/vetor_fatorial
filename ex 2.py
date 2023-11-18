def leitura():
    vetor = [0]*10
    for i in range(10):
        vetor[i] = int(input(f'Informe um {i + 1}º valor inteiro e positivo: '))
        while vetor[i] <=0:
            vetor[i] = int(input(f'Informe um {i + 1}º valor inteiro e POSITIVO: '))
    return vetor

def fatorial(vetor):
    vetor2 = [0]*10
    for i in range(10):
        vetor2[i] = vetor[i]
        x = vetor[i] - 1
        while x > 0:
            vetor2[i]*=x
            x-=1
    return vetor2

valores = leitura()
fatoriais = fatorial(valores)

print(valores)
print(fatoriais)
