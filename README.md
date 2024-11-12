# Jogo da Velha em Python

Este é um jogo da velha (ou "Tic-Tac-Toe") simples implementado em Python, jogado no console, onde dois jogadores se alternam para inserir seus símbolos ("X" ou "O") em um tabuleiro 3x3. O objetivo é conseguir uma sequência de três símbolos iguais em uma linha, coluna ou diagonal para vencer.

## Funcionalidades

- **Exibição do Tabuleiro**: Mostra o estado atual do tabuleiro no console.
- **Detecção de Vitória**: Identifica quando um jogador conseguiu três símbolos consecutivos em linha, coluna ou diagonal.
- **Controle de Empate**: Detecta automaticamente se todas as posições foram preenchidas sem que haja um vencedor, resultando em um empate.
- **Alternância entre Jogadores**: Alterna automaticamente entre os jogadores "X" e "O".

## Como Jogar

1. Execute o script.
2. O tabuleiro vazio será exibido, e o primeiro jogador poderá escolher uma posição.
3. Insira o número da linha e da coluna (de 0 a 2) onde deseja jogar. 
4. O jogo verifica se a posição está livre; se estiver, marca a posição com o símbolo do jogador atual.
5. A cada jogada, o script verifica se houve vitória ou empate e encerra o jogo se uma dessas condições for atendida.
6. Caso contrário, alterna para o próximo jogador e repete o processo.

### Exemplo de Jogo

```plaintext
   |   |  
---------
   |   |  
---------
   |   |  

Jogador X, escolha sua posição:
Digite o número da linha (0, 1 ou 2): 1
Digite o número da coluna (0, 1 ou 2): 1

   |   |  
---------
   | X |  
---------
   |   |  
```

O jogo continua até que um jogador vença ou ocorra um empate.

## Estrutura do Código

1. **Função `exibir_tabuleiro`**: Exibe o estado atual do tabuleiro.
2. **Função `verificar_vitoria`**: Verifica se um jogador conseguiu três símbolos consecutivos em linha, coluna ou diagonal.
3. **Função `jogar`**: Controla o fluxo do jogo, gerenciando turnos, alternância de jogadores, verificação de vitória e controle de empate.

## Melhorias Futuras

- **Validação de Entradas**: Melhorar o controle de entradas para evitar erros ao digitar valores fora do intervalo (0 a 2).
- **Interface Gráfica**: Adicionar uma interface gráfica para tornar o jogo mais interativo.
- **Modo de Jogo contra o Computador**: Implementar um modo de jogo onde o usuário pode jogar contra um oponente controlado pelo computador.
