import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a tela do jogo
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('RPG com Pygame')

# Define cores
cor_fundo = (0, 0, 0)
cor_grade = (50, 50, 50)
cor_personagem = (0, 255, 0)

# Configura o mapa
tamanho_quadrado = 40
mapa_largura = largura // tamanho_quadrado
mapa_altura = altura // tamanho_quadrado

# Posição inicial do personagem (no centro do mapa)
posicao_x, posicao_y = mapa_largura // 2, mapa_altura // 2

# Loop principal do jogo
while True:
    # Lida com eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                posicao_x -= 1
            elif evento.key == pygame.K_RIGHT:
                posicao_x += 1
            elif evento.key == pygame.K_UP:
                posicao_y -= 1
            elif evento.key == pygame.K_DOWN:
                posicao_y += 1

    # Mantém o personagem dentro dos limites do mapa
    posicao_x = max(0, min(mapa_largura - 1, posicao_x))
    posicao_y = max(0, min(mapa_altura - 1, posicao_y))

    # Preenche a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenha a grade do mapa
    for x in range(mapa_largura):
        for y in range(mapa_altura):
            rect = pygame.Rect(x * tamanho_quadrado, y * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado)
            pygame.draw.rect(tela, cor_grade, rect, 1)

    # Desenha o personagem
    rect_personagem = pygame.Rect(posicao_x * tamanho_quadrado, posicao_y * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado)
    pygame.draw.rect(tela, cor_personagem, rect_personagem)

    # Atualiza a tela
    pygame.display.flip()

    # Define a taxa de atualizacao (frames por segundo)
    pygame.time.Clock().tick(60)
