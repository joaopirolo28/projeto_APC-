import funcoesAPC
import random

qtdSustentavel=(3, 29.72, 0.08, 926.64, 113.26)

while True:
    funcoesAPC.exibir_menu()
    
    opcao = input("Digite o numero da opção que deseja acessar (Utilize apenas numeros inteiros).\n")
    funcoesAPC.limpar()
    funcoesAPC.separar()
    
    if opcao == "1":
        while True:
            print("==== Calculo consumo de PET ====\n")
            
            qntGarrafas = (input("Quantas garrafas você utiliza por semana? Favor informar em números inteiros.\n"))
            
            if qntGarrafas.isdigit():
                qntGarrafas=funcoesAPC.string_p_inteiro(qntGarrafas)#Substitui o "," para "." caso necessário e deixa a variável "qntGarrafas" do tipo inteiro
            
                if qntGarrafas > 0:
                    # calcula consumo anual de garrafas.
                    garrafasAnuais = qntGarrafas * 52
                    # calcula total em Kg do peso das garrafas consumidas em 1 ano.
                    garrafasKg = garrafasAnuais * 0.033
                    # calcula o total de energia elétrica para fazer a garrafa economizada em 1 ano.
                    energia = garrafasKg * 5.774
                    # calcula o tempo em horas de tv ligada comparada a garrada economizada em 1 ano.
                    tempoTvHoras = energia/0.1
                    # calcula o total de barril(is) de petróleo para fazer a garrafa economizada em 1 ano.
                    petroleo = garrafasKg * 0.0163
                    # calcula o total de água para fazer a garrafa economizada em 1 ano.
                    agua = garrafasKg * 180.0
                    # calcula a quantidade de banhos de 15 minutos que se pode tomar.
                    banho15min = agua / 100
                    # calcula o total de m³ de aterro sanitário para descartar a garrafa economizada em 1 ano.
                    aterro = garrafasKg * 22
                    
                    if qntGarrafas < qtdSustentavel[0]:
                        energia = qtdSustentavel[1] - energia
                        petroleo = qtdSustentavel[2] - petroleo
                        agua = qtdSustentavel[3] - agua
                        aterro = qtdSustentavel[4] - aterro
                        
                        # Trocar o "ponto" pela vírugla nas casas decimais.
                        garrafasKg = funcoesAPC.formata_decimal(garrafasKg)
                        energia = funcoesAPC.formata_decimal(energia)
                        petroleo = funcoesAPC.formata_decimal(petroleo)
                        agua = funcoesAPC.formata_decimal(agua)
                        aterro = funcoesAPC.formata_decimal(aterro)
                        
                        tempoTvHoras = funcoesAPC.formata_decimal(tempoTvHoras)
                        banho15min = funcoesAPC.formata_decimal(banho15min)
                        
                        print(f"\nSeu consumo anual é de {garrafasKg}kg de plástico PET;\n")
                        
                        print(f"Você ECONOMIZOU em relação à média considerada sustentável (3 garrafas por semana):")
                        print(f"{energia} KWh de energia elétrica;\n{petroleo} barril(is) de petróleo;\n{agua} litros de água;\n{aterro} m³ de aterro sanitário;\n")
                        print(f"A energia gasta seria suficiente para assistir à televisão por {tempoTvHoras} horas;\nA água gasta na produção das garrafas PET que você consome em um ano é equivalente a {banho15min} banhos de 15 minutos.\n")
                        
                    else:
                        energia=energia-qtdSustentavel[1]
                        petroleo=petroleo-qtdSustentavel[2]
                        agua=agua-qtdSustentavel[3]
                        aterro=aterro-qtdSustentavel[4]
                        # Trocar o "ponto" pela vírugla nas casas decimais.
                        garrafasKg = funcoesAPC.formata_decimal(garrafasKg)
                        energia = funcoesAPC.formata_decimal(energia)
                        petroleo = funcoesAPC.formata_decimal(petroleo)
                        agua = funcoesAPC.formata_decimal(agua)
                        aterro = funcoesAPC.formata_decimal(aterro)
                        
                        tempoTvHoras = funcoesAPC.formata_decimal(tempoTvHoras)
                        banho15min = funcoesAPC.formata_decimal(banho15min)
                        
                        print(f"\nSeu consumo anual é de {garrafasKg}kg de plástico PET;\n")
                        print(f"Você DESPERDIÇOU em relação à média considerada sustentável (3 garrafas por semana):")
                        print(f"{energia} KWh de energia elétrica;\n{petroleo} barril(is) de petróleo;\n{agua} litros de água;\n{aterro} m³ de aterro sanitário;\n")
                        print(f"A energia gasta seria suficiente para assistir à televisão por {tempoTvHoras} horas;\nA água gasta na produção das garrafas PET que você consome em um ano é equivalente a {banho15min} banhos de 15 minutos.\n")
                        
                 
                    op=input('Digite n para voltar ao menu ou qualquer outra tecla para continuar: ')
                    funcoesAPC.limpar()
                    funcoesAPC.separar()
                else:
                    print("Digite apenas números inteiros positivos.")
                    op=input('Digite n para voltar ao menu ou qualquer outra tecla para continuar: ')
                    funcoesAPC.limpar()
                    funcoesAPC.separar()
            else:
                print("Digite apenas números inteiros positivos.")
                op=input('Digite n para voltar ao menu ou qualquer outra tecla para continuar: ')
                funcoesAPC.limpar()
                funcoesAPC.separar()

            if op.lower()=='n':#Encerra o programa mesmo que o usuário insira "n" de forma maiúscula
                break
                

    elif opcao == "2":
        while True:
            print("======= Dica aleatoria =======\n")
            frase_aleatoria = random.choice(funcoesAPC.dicas)
            print(frase_aleatoria)
            
                                
            funcoesAPC.separar()
            
            print("Digite n para voltar ao menu ou qualquer outra tecla para continuar: ")
            op = input()
            if op.lower()=='n':#Encerra o programa mesmo que o usuário insira "n" de forma maiúscula
                funcoesAPC.limpar()
                break
                
            
            funcoesAPC.limpar()
            #funcoesAPC.separar()
        
        
    elif opcao == "3":
        print("========Creditos========\n")
        print("Projeto feito por:\n- João Pedro Pirolo Oliveira / 242027371\n- Pedro Henrique Figueira Santiago / 242011999\n- Francisco Evangelista da Silva Filho / 242033127")
        funcoesAPC.separar()
        
        print("Digite qualquer coisa para voltar ao menu.")
        input()
        funcoesAPC.limpar()
        #funcoesAPC.separar()
        
    elif opcao == "0":
        print("Encerrando programa...")
        break
        # Adicione aqui o código para executar a Opção 3
    else:
        print("Opção inválida.\n")
