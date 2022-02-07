Nome = input("Qual o nome do produto? ")
Valor = input("Qual o valor do produto")
Valor = Valor.replace(",",".")
Valor = float(Valor)

Despacho = Valor + 15.00
Taxado = (Valor*60)/100
ICMS = (Valor*18)/100
Premium = (Valor*16)/100
Frete = Valor + 30
Total = 15 + Taxado + ICMS + Premium + 30


print("\nNome do produto :",Nome)
print("Valor do produto no Alixpress :",Valor)
print("\nTaxas:")
print("Despacho -R$15 = ",Despacho)
print("Caso taxado, taxa maxima de 60% = ",Taxado)
print("ICMS de SP 18% = ",ICMS)
print("Mercado Premium 16% = ",Premium)
print("Frete gratis -R$30 = ",Frete)
if Valor < 120:
    Menor = Valor + 5
    Total = Total + 5
    print("Valor abaixo de 120 -R$5 = ",Menor)
    print("\nValor final = ", Total)
else:
    print("\nValor final = ",Total)






