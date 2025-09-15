# Função para mostrar o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

# Função para verificar se houve vitória
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    # Verificar diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

# Função para verificar se o jogo terminou em empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:  # Se houver alguma posição vazia, o jogo ainda não terminou
            return False
    return True

# Função para validar a jogada
def validar_jogada(tabuleiro, linha, coluna):
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:  # Checar se a posição está dentro do tabuleiro
        print("Posição inválida! Tente novamente.")
        return False
    if tabuleiro[linha][coluna] != " ":  # Checar se a posição já está ocupada
        print("Essa posição já está ocupada! Tente novamente.")
        return False
    return True

# Função principal para jogar
def jogar():
    # Criando o tabuleiro (3x3)
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    
    # Jogadores: X e O
    jogadores = ["X", "O"]
    turno = 0
    
    # Iniciar o jogo
    while True:
        exibir_tabuleiro(tabuleiro)
        jogador_atual = jogadores[turno % 2]
        print(f"É a vez do jogador {jogador_atual}.")
        
        # Pedir a jogada do jogador
        try:
            linha = int(input("Digite a linha (0, 1, 2): "))
            coluna = int(input("Digite a coluna (0, 1, 2): "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue
        
        if validar_jogada(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = jogador_atual
            
            # Verificar se alguém venceu
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns! O jogador {jogador_atual} venceu!")
                break
            
            # Verificar se houve empate
            if verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                break
            
            # Alternar o turno
            turno += 1

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
