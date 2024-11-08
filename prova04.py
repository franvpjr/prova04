inicio = int(input('digite o primeiro numero da sequencia: ' ))
fim = int(input('digite o ultimo numero da sequencia: ' ))
soma = 0


for i in range(inicio, fim + 1):
    if i % 2 == 0:
       soma += i
    
if soma > 0:
    print(f'A soma dos numeros pares da sequencia de {inicio} a {fim} é {soma}')