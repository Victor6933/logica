import turtle     # importa módulo turtle que cria gráficos e desenhos com comandos simples

# Cria a tartaruga
t = turtle.Turtle()
t.shape("turtle")    # deixa o cursor com formato de tartaruga
t.speed(1)            # velocidade lenta para parecer que está "andando"

# Movimento da tartaruga
t.forward(100)     # anda 100 pixels para frente
t.right(90)            # vira à direita
t.forward(100)     # anda mais 100 pixels
t.right(90)            # vira à direita
t.forward(100)     # anda mais um pouco
t. right(90)           # vira à direita
t.forward(100)     # anda mais um pouco
t.left(90)              # vira à esquerda
t.forward(50)       # anda mais um pouco

# Finaliza
turtle.done()      # encerra janela gráfica, finaliza o programa; mantém tela aberta após desenho
