import turtle        # importa modulo turtle

t = turtle.Turtle()
t.shape("turtle")    # deixa cursor em formato de tartaruga
t.speed(1)           # velocidade lenta para parecer que está "andando"

# Desenha um quadrado com loop for
for _ in range(4):
    t.forward(100)   # anda 100 pixels para frente
    t.right(90)      # vira à direita

t.left(180)          # vira à esquerda
t.forward(50)        # anda 50 pixels para frente 
turtle.done()        # encerra janela gráfica, finaliza o programa
