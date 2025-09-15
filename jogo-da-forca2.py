import random

# Lista de desenhos do boneco na forca (de 0 a 6 erros)
forca = [
    """
     -----
     |   |
         |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    """
]

# Função para exibir a palavra com as letras corretas
def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

# Função principal do jogo
def jogar_forca():
    # Palavra a ser adivinhada
    palavras = ['python', 'java', 'ruby', 'javascript', 'typescript']
    palavra = random.choice(palavras)
    
    # Variáveis do jogo
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6  # Número de tentativas possíveis (erros)
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        # Exibe a forca e a palavra com as letras corretas
        print(forca[6 - tentativas])  # Exibe o desenho de acordo com o número de erros
        print(exibir_palavra(palavra, letras_corretas))
        
        # Solicita uma letra ao jogador
        tentativa = input("Digite uma letra: ").lower()
        
        # Valida se a entrada é uma letra válida
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        
        # Verifica se a letra foi tentada antes
        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        # Se a letra estiver na palavra
        if tentativa in palavra:
            letras_corretas.add(tentativa)
            print(f"Boa! A letra '{tentativa}' está na palavra.")
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1
            print(f"Ops! A letra '{tentativa}' não está na palavra. Tentativas restantes: {tentativas}")
        
        # Verifica se o jogador acertou todas as letras
        if all(letra in letras_corretas for letra in palavra):
            print(f"Parabéns! Você acertou a palavra: {palavra}")
            break
    else:
        # Se o jogador perder (sem tentativas restantes)
        print(forca[6 - tentativas])
        print(f"Você perdeu! A palavra era: {palavra}")

# Iniciar o jogo
if __name__ == "__main__":
    jogar_forca()
