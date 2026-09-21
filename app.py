# Define o tipo de imóvel e o consumo de água
tipo = input("Digite o tipo do imóvel (casa, apartamento, comercial): ")
consumoAgua = float(input("Digite o consumo de água em m³: "))

# Verifica se o imóvel é comercial
if tipo == "comercial":
    print("Tarifa comercial aplicada - consulte o plano corporativo.")

# Verifica o consumo de água de uma casa
elif tipo == "casa":
    
    if consumoAgua <= 25:

        print("Consumo moderado - dentro do padrão residencial.")

    else:

        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")

# Verifica o consumo de água de um apartamento
elif tipo == "apartamento":

    if consumoAgua < 10:

        print("Consumo econômico - excelente controle de água!")

    elif consumoAgua <= 25:

        print("Consumo moderado - dentro do padrão residencial.")

    else:

        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
else:

    print("Tipo de imóvel inválido. Por favor, insira 'casa', 'apartamento' ou 'comercial'.")        