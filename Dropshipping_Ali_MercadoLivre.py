def real(valor):
  a = "{:,.2f}".format(float(valor))
  b = a.replace(',','v')
  c = b.replace('.',',')
  return c.replace('v','.')

Nome = input("Qual o nome do produto?: ")
Valor = input("Qual o valor do produto em dolares? (xxxx,xx): ")
Valor = Valor.replace(",",".")
Valor = float(Valor) * 5.25
Dolar = Valor


Despacho = Valor + 15.00
Taxado = (Valor*60)/100
ICMS = (Valor*18)/100
Premium = (Valor*16)/100
Frete = Valor + 30
Total = Valor + 15 + Taxado + ICMS + Premium + 30
TotalImposto = Valor + 15 + Premium + 30


print("\nTaxas:")
print("Valor do produto em reais: ",real(Dolar))
print("Despacho -R$15 = ",real(Despacho))
print("Caso taxado, taxa maxima de 60% = ",real(Taxado))
print("ICMS de SP 18% = ",real(ICMS))
print("Mercado Premium 16% = ",real(Premium))
print("Frete gratis -R$30 = ",real(Frete))
if Valor < 120:
    Menor = Valor + 5
    Total = Total + 5
    TotalImposto = TotalImposto + 5
    print("Valor abaixo de 120 -R$5 = ",real(Menor))
    print("\nValor final = ", real(Total))
    print("Valor final sem impostos = ",real(TotalImposto))
else:
    print("\nValor final = ",real(Total))
    print("Valor final sem impostos = ", real(TotalImposto))

Deseja = input("\nQual valor deseja vender (xxx,xx)? ")
Deseja = Deseja.replace(",",".")
Deseja = float(Deseja)
LucroImposto = Deseja-Total
Lucro = Deseja-TotalImposto

print("\nLucro com impostos é ",real(LucroImposto))
print("Lucro sem impostos é ",real(Lucro))






