def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogadores[jogador_atual]

            if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogadores[jogador_atual]} venceu!")
                break

            if all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
                exibir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                break

            jogador_atual = 1 - jogador_atual
        else:
            print("Essa posição já está ocupada. Escolha outra.")

if __name__ == "__main__":
    jogar()
