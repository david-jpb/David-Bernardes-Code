def celtofahr(x):
    farh = (x * 1.8) + 32
    return farh

def fahrtocel(x):
    cel = (x - 32) * 0.5556
    return cel

def menu():
    while True:
        opcao = input("Temp Converter 1.0\nPara converter Celsius para Fahrenheit, selecione 1.\nPara converter Fahrenheit para Celsius, selecione 2.\nPara sair, escolha outra opção:\n")

        if opcao == '1':
            celsius = float(input("Digite a temperatura em graus Celsius: "))
            resultado = celtofahr(celsius)
            print("A temperatura em Fahrenheit é: %.2f°F\n" % resultado)
        elif opcao == '2':
            fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
            resultado = fahrtocel(fahrenheit)
            print("A temperatura em Celsius é: %.2f°C\n" % resultado)
        else:
            print("Programa terminado com sucesso.")
            break
menu()
