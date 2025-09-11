perguntas = [
    ("Qual a capital do Brasil?", "brasilia"),
    ("Quanto é 5 + 7?", "12"),
    ("Cor primária que começa com V?", "vermelho"),
    ("qual pais começa com f?", "frança"),
    ("qual a outra cor que começa com v?", "verde" )
]    

pontos = 0

for pergunta, resposta_correta in perguntas:
    resposta = input(pergunta + " ").lower()
    if resposta == resposta_correta:
        print("✅ Correto!")
        pontos += 1
    else:
        print("❌ Errado!")

print(f"Você fez {pontos} ponto(s) de {len(perguntas)}.")
