import random

# Criar tabuleiro 5x5
tabuleiro = [["~" for _ in range(5)] for _ in range(5)]

# Posicionar navio aleatoriamente
navio_linha = random.randint(0, 4)
navio_coluna = random.randint(0, 4)

tentativas = 5
acertou = False

print("🚢 JOGO DE BATALHA NAVAL")
print("Tabuleiro 5x5")
print("Você tem 5 tentativas para acertar o navio.")

while tentativas > 0 and not acertou:
    linha = int(input("Digite a linha (0 a 4): "))
    coluna = int(input("Digite a coluna (0 a 4): "))

    if linha == navio_linha and coluna == navio_coluna:
        print("🎯 Você acertou o navio!")
        acertou = True
        tabuleiro[linha][coluna] = "X"
    else:
        print("💦 Água!")
        tentativas -= 1

        if 0 <= linha <= 4 and 0 <= coluna <= 4:
            tabuleiro[linha][coluna] = "O"

    print("Tentativas restantes:", tentativas)
    for linha_tab in tabuleiro:
        print(" ".join(linha_tab))

if not acertou:
    print("❌ Fim de jogo! O navio estava em:", navio_linha, navio_coluna)
