import time

# Definindo a senha fixa
SENHA_CORRETA = "1234"

# Função de login
def realizar_login():
    tentativas = 3  # Número máximo de tentativas
    tempo_limite = 30  # Tempo limite em segundos
    tempo_inicio = time.time()  # Marca o início do tempo
    
    while tentativas > 0:
        # Verifica o tempo decorrido
        tempo_decorrido = time.time() - tempo_inicio
        if tempo_decorrido > tempo_limite:
            print("Tempo expirado! Você excedeu o limite de 30 segundos.")
            break
        
        # Solicita a senha do usuário
        senha_usuario = input(f"Tentativa {4 - tentativas} de 3: Digite a senha: ")
        
        if senha_usuario == SENHA_CORRETA:
            print("Acesso concedido!")
            break
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Senha incorreta. Você ainda tem {tentativas} tentativa(s).")
            else:
                print("Número de tentativas excedido! Acesso negado.")

# Executando o sistema de login
if __name__ == "__main__":
    realizar_login()
