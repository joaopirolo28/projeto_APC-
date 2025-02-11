# Documentação do Projeto APC

## Descrição do Projeto
O projeto APC (Análise do Consumo de Plástico) é uma aplicação que visa conscientizar os usuários sobre o consumo de garrafas PET e suas implicações ambientais. O programa permite que os usuários calculem o consumo anual de garrafas PET e comparem com uma média sustentável, além de fornecer dicas sobre sustentabilidade.

## Estrutura do Projeto
O repositório contém os seguintes arquivos:

- **/Projeto1.0.py**: Arquivo principal que executa a aplicação.
- **/funcoesAPC.py**: Módulo que contém funções auxiliares utilizadas no programa.

## Funcionalidades

### Projeto1.0.py
Este é o arquivo principal que executa a aplicação. As principais funcionalidades incluem:
- Exibir um menu com opções para calcular o consumo de PET, mostrar dicas de sustentabilidade, e exibir créditos.
- Permitir que o usuário insira a quantidade de garrafas PET consumidas por semana e calcular o impacto ambiental.
- Comparar o consumo do usuário com uma média sustentável e exibir os resultados.

### funcoesAPC.py
Este módulo contém funções auxiliares que são utilizadas no arquivo principal. As principais funções incluem:
- `string_p_inteiro(garrafa)`: Converte uma string que pode conter uma vírgula em um inteiro.
- `formata_decimal(valor)`: Formata um valor decimal, trocando o ponto por uma vírgula.
- `exibir_menu()`: Exibe o menu principal da aplicação.
- `limpar()`: Limpa a tela, imprimindo várias linhas em branco.
- `separar()`: Exibe uma linha de separação no console.
- `dicas`: Uma lista de dicas sobre sustentabilidade.

## Como Usar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório:
   ```bash
   git clone https://github.com/joaopirolo28/projeto_APC-.git
   ```
3. Navegue até o diretório do projeto:
   ```bash
   cd projeto_APC-
   ```
4. Execute o arquivo principal:
   ```bash
   python Projeto1.0.py
   ```
5. Siga as instruções exibidas no menu para interagir com a aplicação.

## Participantes
- João Pedro Pirolo Oliveira / 242027371
- Pedro Henrique Figueira Santiago / 242011999
- Francisco Evangelista da Silva Filho / 242033127
