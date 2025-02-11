#func 1
#verificar se o usuario botou ',' em vez de '.' e trocar
def string_p_inteiro(garrafa):
    for _ in garrafa:#percorre a string 
        if ',' in garrafa:#se encontrar uma ",", troca-a por "."
            garrafa=str(garrafa).replace(",",".")
    garrafa=float(garrafa)
    garrafa=int(garrafa)
    return garrafa


#func 2
# Trocar o "ponto" pela vírugla nas casas decimais.
def formata_decimal (valor):
    vlr_arredondado = round(valor,2)#arredonda o valor
    vlr_formatado = str(vlr_arredondado).replace(".",",")#transforma o valor em string, e troca o "." por ","
    return vlr_formatado

def exibir_menu():
    print("=========== Menu ============")
    print("1. Calculo consumo de PET")
    print("2. Dicas sustentabilidade")
    print("3. Creditos")
    print("0. Encerrar programa")
    print("=============================")
    
def limpar():
    limpador = [print("\n") for i in range(10)]
    
def separar():
    print("\n======================================\n")
    
dicas = ["Use garrafas reutilizáveis como as de aço inoxidável, vidro ou plástico Tritan, que são livres de BPA e podem ser usadas repetidamente.",
        "Compre produtos com embalagens sustentáveis que venham em embalagens reutilizáveis, recicláveis ou biodegradáveis.",
        "Se precisar usar garrafas PET, certifique-se de descartá-las na lixeira correta para que sejam recicladas.",
        "Compartilhe essas dicas com amigos, familiares e colegas para que mais pessoas se juntem a esse movimento de redução do uso de plástico."]
    