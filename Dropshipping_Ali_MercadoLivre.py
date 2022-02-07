#Função deixar formatação em reais
def real(valor):
  a = "{:,.2f}".format(float(valor))
  b = a.replace(',','v')
  c = b.replace('.',',')
  return c.replace('v','.')

#Variaveis
Nome = input("Qual o nome do produto?: ")
Valor = input("Qual o valor do produto em dolares? (xxxx,xx): ")
Valor = Valor.replace(",",".")
Valor = float(Valor) * 5.25
Dolar = Valor
DolarPrint = Valor/5.25
Continuar =""
Despacho = Valor + 15.00
Taxado = (Valor*60)/100
ICMS = (Valor*18)/100
Premium = (Valor*16)/100
Frete = Valor + 30
Total = Valor + 15 + Taxado + ICMS + Premium + 30
TotalImposto = Valor + 15 + Premium + 30

#Prints de taxas
print("\nTaxas:")
print("Valor do produto em reais: R$",real(Dolar))
print("Despacho -R$15: R$",real(Despacho))
print("Caso taxado, taxa maxima de 60%: R$",real(Taxado))
print("ICMS de SP 18%: R$",real(ICMS))
print("Mercado Premium 16%: R$",real(Premium))
print("Frete gratis -R$30: R$",real(Frete))

#Valor menor que 120 é tributado pelo Mercado Livre
if Valor < 120:
    Menor = Valor + 5
    Total = Total + 5
    TotalImposto = TotalImposto + 5
    print("Valor abaixo de 120 -R$5: R$",real(Menor))
    print("\nValor final = R$", real(Total))
    print("Valor final sem impostos = R$",real(TotalImposto))
else:
    print("\nValor final = ",real(Total))
    print("Valor final sem impostos = R$", real(TotalImposto))

#Variaveis pedindo valor de venda
Deseja = input("\nQual valor deseja vender (xxx,xx)? ")
Deseja = Deseja.replace(",", ".")
Deseja = float(Deseja)
LucroImposto = Deseja - Total
Lucro = Deseja - TotalImposto

#Print mostrando lucros
print("\nLucro com impostos é: R$", real(LucroImposto))
print("Lucro sem impostos é: R$", real(Lucro))

#Loop para confirmar valor de venda
while Continuar != "s":
    Continuar = input("\nConfirmar valor? (s)Sim (n)Não  ").lower()

    if Continuar == "s":
        break
    elif Continuar == "n":
        Deseja = input("\nQual valor deseja vender (xxx,xx)? ")
        Deseja = Deseja.replace(",", ".")
        Deseja = float(Deseja)
        LucroImposto = Deseja - Total
        Lucro = Deseja - TotalImposto
        print("\nLucro com impostos é: R$", real(LucroImposto))
        print("Lucro sem impostos é: R$", real(Lucro))
        continue


    else:
        print("Digite (s)Sim (n)Não")

#Variavel para salvar em txt
Salvar = input("\nSalvar pesquisa? (s)Sim (n)Não ").lower()

#loop para confirmação de salvamento
if Salvar == "n":
    print("")
elif Salvar == "s":
    Site = input("Qual o site do Alibaba? ")
    x = open(Nome + ".txt","w")
    print("Produto: ",Nome,file=open(Nome + ".txt","a"))
    print("Url: ",Site,file=open(Nome + ".txt","a"))
    print("Preço em Dolar: $",DolarPrint,file=open(Nome + ".txt","a"))
    print("\nTaxas:", file=open(Nome + ".txt", "a"))
    print("Valor do produto em reais: R$", real(Dolar), file=open(Nome + ".txt", "a"))
    print("Despacho -R$15: R$ ", real(Despacho), file=open(Nome + ".txt", "a"))
    print("Caso taxado, taxa maxima de 60%: R$ ", real(Taxado), file=open(Nome + ".txt", "a"))
    print("ICMS de SP 18%: R$ ", real(ICMS), file=open(Nome + ".txt", "a"))
    print("Mercado Premium 16%: R$ ", real(Premium), file=open(Nome + ".txt", "a"))
    print("Frete gratis -R$30: R$ ", real(Frete), file=open(Nome + ".txt", "a"))
    if Valor < 120:
        print("Valor abaixo de 120 -R$5: R$", real(Menor), file=open(Nome + ".txt", "a"))
        print("\nValor final: R$", real(Total), file=open(Nome + ".txt", "a"))
        print("Valor final sem impostos: R$", real(TotalImposto), file=open(Nome + ".txt", "a"))
    else:
        print("\nValor final: R$", real(Total), file=open(Nome + ".txt", "a"))
        print("Valor final sem impostos: R$", real(TotalImposto), file=open(Nome + ".txt", "a"))
    print("\nVendendo por: R$",real(Deseja), file=open(Nome + ".txt", "a"))
    print("\nLucro com impostos é: R$", real(LucroImposto), file=open(Nome + ".txt", "a"))
    print("Lucro sem impostos é: R$", real(Lucro), file=open(Nome + ".txt", "a"))













