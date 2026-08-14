"""
🚀 MISSÃO ESPACIAL - EXERCÍCIO DE FUNÇÕES PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SENAI Caçador - Curso Técnico em Desenvolvimento de Sistemas
Lógica de Programação - Professor Kleber

INSTRUÇÕES PARA O ALUNO:
  1. Altere APENAS a variável FASE_ATUAL (linha abaixo)
  2. Leia a documentação das funções disponíveis
  3. Insira chamadas de função dentro da fase correspondente
  4. Execute com F5 no VS Code
  5. Observe o astronauta executar seus comandos no grid!
  6. Ao completar uma fase, mude FASE_ATUAL para a próxima

⚠️  NÃO MODIFIQUE nada fora das áreas marcadas com ========
⚠️  Você só pode acessar uma fase após completar a anterior!
"""

import pygame
import sys
import random
import os

# ╔════════════════════════════════════════════════════════════╗
# ║  CONFIGURAÇÃO - Altere o número da fase (1 a 10)         ║
# ╚════════════════════════════════════════════════════════════╝
FASE_ATUAL = 1


# ╔════════════════════════════════════════════════════════════╗
# ║  ⚡ FUNÇÕES DISPONÍVEIS (NÃO MODIFIQUE)                  ║
# ║                                                            ║
# ║  Leia com atenção o que cada função faz.                   ║
# ║  Cada função recebe parâmetros e executa uma ação.         ║
# ║  Seu trabalho é chamá-las na ordem certa!                  ║
# ╠════════════════════════════════════════════════════════════╣
# ║                                                            ║
# ║  andar_direita(passos)                                     ║
# ║    O que faz: move o astronauta para a DIREITA             ║
# ║    Parâmetro: passos (int) - quantidade de casas           ║
# ║    Exemplo: andar_direita(3) → anda 3 casas à direita     ║
# ║                                                            ║
# ║  andar_esquerda(passos)                                    ║
# ║    O que faz: move o astronauta para a ESQUERDA            ║
# ║    Parâmetro: passos (int) - quantidade de casas           ║
# ║    Exemplo: andar_esquerda(2) → anda 2 casas à esquerda   ║
# ║                                                            ║
# ║  andar_cima(passos)                                        ║
# ║    O que faz: move o astronauta para CIMA                  ║
# ║    Parâmetro: passos (int) - quantidade de casas           ║
# ║    Exemplo: andar_cima(4) → anda 4 casas para cima        ║
# ║                                                            ║
# ║  andar_baixo(passos)                                       ║
# ║    O que faz: move o astronauta para BAIXO                 ║
# ║    Parâmetro: passos (int) - quantidade de casas           ║
# ║    Exemplo: andar_baixo(1) → anda 1 casa para baixo       ║
# ║                                                            ║
# ║  pegar_item()                                              ║
# ║    O que faz: coleta o item na posição atual               ║
# ║    Parâmetro: nenhum                                       ║
# ║    Retorna: True se coletou, False se não havia item       ║
# ║    Exemplo: pegar_item() → coleta cristal ou chave         ║
# ║                                                            ║
# ║  usar_item()                                               ║
# ║    O que faz: usa o item coletado na posição atual         ║
# ║    Parâmetro: nenhum                                       ║
# ║    Retorna: True se usou, False se não tinha item          ║
# ║    Exemplo: usar_item() → abre um portão bloqueado        ║
# ║                                                            ║
# ╚════════════════════════════════════════════════════════════╝

fila_comandos = []


def andar_direita(passos):
    """Move o astronauta para a DIREITA (passos) casas."""
    for _ in range(passos):
        fila_comandos.append("DIREITA")


def andar_esquerda(passos):
    """Move o astronauta para a ESQUERDA (passos) casas."""
    for _ in range(passos):
        fila_comandos.append("ESQUERDA")


def andar_cima(passos):
    """Move o astronauta para CIMA (passos) casas."""
    for _ in range(passos):
        fila_comandos.append("CIMA")


def andar_baixo(passos):
    """Move o astronauta para BAIXO (passos) casas."""
    for _ in range(passos):
        fila_comandos.append("BAIXO")


def pegar_item():
    """Coleta o item (cristal ou chave) na posição atual."""
    fila_comandos.append("PEGAR")


def usar_item():
    """Usa o item coletado (abre portão) na posição atual."""
    fila_comandos.append("USAR")


# ╔════════════════════════════════════════════════════════════╗
# ║  FUNÇÕES EXTRAS - Disponíveis a partir da FASE 8          ║
# ║  ⚠️  Cuidado! Nem todas são úteis para a missão!          ║
# ╠════════════════════════════════════════════════════════════╣
# ║                                                            ║
# ║  girar(graus)                                              ║
# ║    O que faz: gira o astronauta no lugar                   ║
# ║    Parâmetro: graus (int) - ângulo de rotação              ║
# ║    ⚠️  NÃO muda a posição! Apenas gira.                   ║
# ║                                                            ║
# ║  esperar(segundos)                                         ║
# ║    O que faz: astronauta fica parado esperando             ║
# ║    Parâmetro: segundos (int) - tempo de espera             ║
# ║    ⚠️  NÃO move o astronauta!                             ║
# ║                                                            ║
# ║  pular()                                                   ║
# ║    O que faz: astronauta pula no lugar                     ║
# ║    Parâmetro: nenhum                                       ║
# ║    ⚠️  Animação bonita, mas NÃO muda posição!             ║
# ║                                                            ║
# ║  teletransportar()                                         ║
# ║    O que faz: move para posição ALEATÓRIA                  ║
# ║    Parâmetro: nenhum                                       ║
# ║    ⚠️  PERIGOSO! Pode cair em cima de asteroide!          ║
# ║                                                            ║
# ╚════════════════════════════════════════════════════════════╝

def girar(graus):
    """Gira o astronauta no lugar. NÃO muda a posição."""
    fila_comandos.append("GIRAR")


def esperar(segundos):
    """Astronauta fica parado. NÃO muda a posição."""
    for _ in range(segundos):
        fila_comandos.append("ESPERAR")


def pular():
    """Astronauta pula no lugar. NÃO muda a posição."""
    fila_comandos.append("PULAR")


def teletransportar():
    """Move para posição ALEATÓRIA. PERIGOSO!"""
    fila_comandos.append("TELETRANSPORTAR")


# ╔════════════════════════════════════════════════════════════╗
# ║  📋 ÁREA DE COMANDOS - ESCREVA SEUS COMANDOS AQUI         ║
# ╚════════════════════════════════════════════════════════════╝

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 1 - PRIMEIRO CONTATO
# Missão: leve o astronauta até a nave espacial 🛸
# O caminho é reto, sem obstáculos.
# Funções úteis: andar_direita(n)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase1():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_direita(9)


    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 2 - MUDANÇA DE ROTA
# Missão: a nave está em outra direção!
#         Descubra quais funções usar.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase2():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_direita(11)
    andar_baixo(10)


    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 3 - ZIGUE-ZAGUE
# Missão: a nave está longe e o caminho não é reto!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase3():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_cima(6)
    andar_direita(14)
    


    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 4 - ASTEROIDES SIMPLES
# Missão: asteroides bloqueiam o caminho direto!
#         Desvie deles para chegar à nave.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase4():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_cima(2)
    andar_direita(9)
    andar_baixo(3)
    andar_direita(5)
    andar_cima(1)

    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 5 - CRISTAL DE ENERGIA
# Missão: a nave precisa de energia para decolar!
#         Encontre o cristal e leve-o até a nave.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase5():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_cima(2)
    andar_direita(5)
    andar_baixo(2)
    pegar_item()
    andar_direita(8)
    andar_baixo()

    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 6 - COLETA MÚLTIPLA
# Missão: a nave precisa de DOIS cristais para
#         decolar! Colete ambos e chegue à nave.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase6():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_direita(2)
    pegar_item()
    andar_direita(4)
    andar_baixo(6)
    andar_direita(3)
    andar_baixo(3)
    pegar_item()
    andar_direita(6)
    andar_baixo(4)


    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 7 - PORTÃO BLOQUEADO
# Missão: um portão bloqueia o caminho!
#         Encontre um jeito de abri-lo.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase7():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_baixo(7)
    andar_direita(2)
    pegar_item()
    andar_direita(6)
    andar_cima(2)
    andar_direita(1)
    usar_item()
    andar_direita(5)
    andar_baixo(6)
    andar_direita(7)

    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 8 - ARMADILHA DE FUNÇÕES
# Missão: nem todas as funções ajudam!
#         Analise cada uma antes de usar.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase8():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_baixo(5)
    andar_direita(4)
    pegar_item()
    andar_direita(11)
    andar_baixo(9)
    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 9 - LABIRINTO FINAL
# Missão: todos os desafios anteriores combinados.
#         Resolva tudo para alcançar a nave!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase9():
    # ======== INSIRA SEUS COMANDOS ABAIXO ========
    andar_baixo(3)
    andar_direita(3)
    andar_baixo(4)
    pegar_item()
    andar_direita(4)
    andar_cima(3)
    pegar_item()
    andar_direita(4)
    andar_baixo(2)
    usar_item()
    andar_baixo(1)
    andar_direita(2)
    andar_baixo(6)
    andar_direita(4)
    andar_baixo(3)
    # ======== FIM DOS COMANDOS ========
    pass


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FASE 10 - CRIE SUA FUNÇÃO
# Missão: uma função essencial está faltando!
#         Crie-a para completar a missão.
#
# A função andar_diagonal(passos) deve:
#   - Receber um parâmetro: passos (int)
#   - Para cada passo, mover 1 casa para DIREITA
#     e 1 casa para BAIXO
#   - Dica: use andar_direita(1) e andar_baixo(1)
#           dentro de um loop for
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def comandos_fase10():
    # ======== CRIE A FUNÇÃO andar_diagonal ABAIXO ========
    # def andar_diagonal(passos):
    #     ...complete aqui...
    andar_baixo(14)
    andar_direita(14)


    # ======== INSIRA SEUS COMANDOS ABAIXO ========



    # ======== FIM DOS COMANDOS ========
    pass


# ╔════════════════════════════════════════════════════════════╗
# ║  🔧 MOTOR DO JOGO (NÃO MODIFIQUE A PARTIR DAQUI)         ║
# ╚════════════════════════════════════════════════════════════╝

CELL = 32
GRID_W = 20
GRID_H = 20
PAINEL_W = 280
JANELA_W = GRID_W * CELL + PAINEL_W
JANELA_H = GRID_H * CELL
VELOCIDADE_ANIMACAO = 200
ARQUIVO_PROGRESSO = "progresso_espacial.txt"

COR_FUNDO = (10, 10, 30)
COR_GRID = (25, 25, 60)
COR_PAINEL = (15, 15, 40)
COR_TEXTO = (180, 180, 230)
COR_TITULO = (200, 200, 255)
COR_DESTAQUE = (255, 200, 50)
COR_SUCESSO = (80, 255, 140)
COR_ERRO = (255, 80, 80)
COR_DICA = (120, 200, 120)
COR_AVISO = (255, 120, 80)

COR_CAPACETE = (220, 230, 255)
COR_VISOR = (30, 80, 180)
COR_TRAJE = (60, 110, 210)
COR_TRAJE_ESCURO = (40, 75, 165)
COR_DETALHE = (255, 170, 30)

COR_ASTEROIDE = (90, 85, 80)
COR_ASTEROIDE_ESCURO = (65, 60, 55)
COR_CRISTAL = (0, 255, 180)
COR_CRISTAL_BRILHO = (150, 255, 220)
COR_NAVE = (255, 190, 40)
COR_NAVE_CORPO = (200, 150, 50)
COR_CHAVE = (255, 220, 50)
COR_PORTAO = (200, 60, 60)
COR_PORTAO_ABERTO = (60, 200, 60)

FASES = {
    1: {
        "nome": "PRIMEIRO CONTATO",
        "missao": "Leve o astronauta ate a nave. Caminho reto!",
        "dica": "Use: andar_direita(n)",
        "inicio": (1, 10),
        "nave": (10, 10),
        "asteroides": [],
        "cristais": [],
        "chaves": [],
        "portoes": [],
        "precisa_cristal": False,
        "precisa_chave": False,
    },
    2: {
        "nome": "MUDANCA DE ROTA",
        "missao": "A nave mudou de posicao! Combine duas direcoes.",
        "dica": "Use: andar_direita(n) + andar_baixo(n)",
        "inicio": (1, 3),
        "nave": (12, 12),
        "asteroides": [],
        "cristais": [],
        "chaves": [],
        "portoes": [],
        "precisa_cristal": False,
        "precisa_chave": False,
    },
    3: {
        "nome": "ZIGUE-ZAGUE",
        "missao": "O caminho exige tres direcoes diferentes!",
        "dica": "Use: direita + baixo + cima",
        "inicio": (1, 10),
        "nave": (14, 4),
        "asteroides": [],
        "cristais": [],
        "chaves": [],
        "portoes": [],
        "precisa_cristal": False,
        "precisa_chave": False,
    },
    4: {
        "nome": "ASTEROIDES SIMPLES",
        "missao": "Asteroides bloqueiam o caminho! Desvie deles.",
        "dica": "Planeje o caminho antes de escrever",
        "inicio": (1, 2),
        "nave": (14, 2),
        "asteroides": [
            (5, 1), (5, 2), (5, 3),
            (10, 0), (10, 1), (10, 2),
        ],
        "cristais": [],
        "chaves": [],
        "portoes": [],
        "precisa_cristal": False,
        "precisa_chave": False,
    },
    5: {
        "nome": "CRISTAL DE ENERGIA",
        "missao": "Colete o cristal e depois va para a nave!",
        "dica": "Use: movimentos + pegar_item()",
        "inicio": (1, 2),
        "nave": (14, 12),
        "asteroides": [
            (4, 1), (4, 2), (4, 3),
            (7, 6), (7, 7), (7, 8),
            (10, 3), (10, 4),
            (12, 9), (12, 10),
        ],
        "cristais": [(6, 2)],
        "chaves": [],
        "portoes": [],
        "precisa_cristal": True,
        "precisa_chave": False,
    },
    6: {
        "nome": "COLETA MULTIPLA",
        "missao": "Colete DOIS cristais e chegue a nave!",
        "dica": "Planeje a rota para pegar os dois",
        "inicio": (1, 1),
        "nave": (16, 14),
        "asteroides": [
            (4, 3), (4, 4), (4, 5),
            (8, 1), (8, 2),
            (8, 8), (8, 9), (8, 10),
            (12, 5), (12, 6),
            (14, 11), (14, 12),
        ],
        "cristais": [(3, 1), (10, 10)],
        "chaves": [],
        "portoes": [],
        "precisa_cristal": True,
        "precisa_chave": False,
    },
    7: {
        "nome": "PORTAO BLOQUEADO",
        "missao": "Pegue a chave, abra o portao e siga ate a nave!",
        "dica": "Use: pegar_item() + usar_item()",
        "inicio": (1, 1),
        "nave": (17, 12),
        "asteroides": [
            (5, 4), (5, 5), (5, 6),
            (10, 1), (10, 2), (10, 3),
            (10, 8), (10, 9), (10, 10),
            (14, 5), (14, 6),
        ],
        "cristais": [],
        "chaves": [(3, 8)],
        "portoes": [(10, 6)],
        "precisa_cristal": False,
        "precisa_chave": True,
    },
    8: {
        "nome": "ARMADILHA DE FUNCOES",
        "missao": "Funcoes falsas no caminho! Ignore as inuteis!",
        "dica": "girar/esperar/pular/teletransportar NAO ajudam!",
        "inicio": (1, 1),
        "nave": (16, 15),
        "asteroides": [
            (3, 3), (3, 4), (3, 5),
            (6, 1), (6, 2),
            (8, 7), (8, 8), (8, 9),
            (11, 4), (11, 5),
            (13, 10), (13, 11), (13, 12),
        ],
        "cristais": [(5, 6)],
        "chaves": [],
        "portoes": [],
        "precisa_cristal": True,
        "precisa_chave": False,
    },
    9: {
        "nome": "LABIRINTO FINAL",
        "missao": "Pegue chave, abra portao, colete cristal, chegue a nave!",
        "dica": "Todas as funcoes uteis sao necessarias!",
        "inicio": (1, 1),
        "nave": (18, 17),
        "asteroides": [
            (3, 0), (3, 1), (3, 2), (3, 3),
            (1, 5), (2, 5), (3, 5),
            (6, 3), (6, 4), (6, 5), (6, 6),
            (6, 10), (6, 11),
            (9, 7), (9, 8),
            (9, 13), (9, 14), (9, 15),
            (12, 2), (12, 3),
            (12, 9), (12, 10), (12, 11),
            (15, 5), (15, 6), (15, 7),
            (15, 14), (15, 15),
            (17, 10), (17, 11),
        ],
        "cristais": [(8, 5)],
        "chaves": [(4, 8)],
        "portoes": [(12, 7)],
        "precisa_cristal": True,
        "precisa_chave": True,
    },
    10: {
        "nome": "CRIE SUA FUNCAO",
        "missao": "Crie andar_diagonal() para vencer! Combine funcoes dentro de um loop.",
        "dica": "def andar_diagonal(p): use for + direita(1) + baixo(1)",
        "inicio": (1, 1),
        "nave": (15, 15),
        "asteroides": [
            (7, 7), (7, 8),
            (11, 11), (11, 12),
        ],
        "cristais": [],
        "chaves": [],
        "portoes": [],
        "precisa_cristal": False,
        "precisa_chave": False,
    },
}

estrelas = [(random.randint(0, GRID_W * CELL), random.randint(0, GRID_H * CELL)) for _ in range(120)]


# ── SISTEMA DE PROGRESSO ──

def carregar_progresso():
    """Carrega as fases concluídas do arquivo de progresso."""
    if not os.path.exists(ARQUIVO_PROGRESSO):
        return set()
    try:
        with open(ARQUIVO_PROGRESSO, "r") as f:
            linhas = f.read().strip().split("\n")
        if len(linhas) != 2:
            return set()
        dados_codificados = linhas[0]
        assinatura_salva = linhas[1]
        import hashlib
        import base64
        chave = "S3N4I_C4C4D0R_2025"
        assinatura_esperada = hashlib.sha256(
            (dados_codificados + chave).encode()
        ).hexdigest()
        if assinatura_salva != assinatura_esperada:
            return set()
        dados = base64.b64decode(dados_codificados.encode()).decode()
        fases = set()
        for parte in dados.split(","):
            parte = parte.strip()
            if parte.isdigit():
                fases.add(int(parte))
        return fases
    except Exception:
        return set()


def salvar_progresso(fases_concluidas):
    """Salva as fases concluídas no arquivo de progresso (codificado)."""
    import hashlib
    import base64
    chave = "S3N4I_C4C4D0R_2025"
    dados = ",".join(str(n) for n in sorted(fases_concluidas))
    dados_codificados = base64.b64encode(dados.encode()).decode()
    assinatura = hashlib.sha256(
        (dados_codificados + chave).encode()
    ).hexdigest()
    with open(ARQUIVO_PROGRESSO, "w") as f:
        f.write(f"{dados_codificados}\n{assinatura}")


def verificar_acesso(fase_atual):
    """Verifica se o aluno pode acessar a fase solicitada."""
    if fase_atual == 1:
        return True
    concluidas = carregar_progresso()
    return (fase_atual - 1) in concluidas


# ── DESENHO ──

def desenhar_fundo(tela):
    tela.fill(COR_FUNDO)
    for sx, sy in estrelas:
        brilho = random.randint(150, 255)
        tamanho = random.choice([1, 1, 1, 2])
        pygame.draw.circle(tela, (brilho, brilho, brilho), (sx, sy), tamanho)


def desenhar_grid(tela):
    for x in range(GRID_W + 1):
        pygame.draw.line(tela, COR_GRID, (x * CELL, 0), (x * CELL, GRID_H * CELL))
    for y in range(GRID_H + 1):
        pygame.draw.line(tela, COR_GRID, (0, y * CELL), (GRID_W * CELL, y * CELL))


def desenhar_astronauta(tela, gx, gy):
    cx = gx * CELL + CELL // 2
    cy = gy * CELL + CELL // 2
    pygame.draw.circle(tela, COR_CAPACETE, (cx, cy - 8), 10)
    pygame.draw.rect(tela, COR_VISOR, (cx - 6, cy - 12, 12, 7), border_radius=2)
    pygame.draw.rect(tela, COR_TRAJE, (cx - 8, cy + 2, 16, 12), border_radius=3)
    pygame.draw.rect(tela, COR_DETALHE, (cx - 4, cy + 4, 3, 3))
    pygame.draw.rect(tela, COR_ERRO, (cx + 1, cy + 4, 3, 3))
    pygame.draw.rect(tela, COR_TRAJE_ESCURO, (cx - 7, cy + 14, 6, 5), border_radius=2)
    pygame.draw.rect(tela, COR_TRAJE_ESCURO, (cx + 1, cy + 14, 6, 5), border_radius=2)
    pygame.draw.rect(tela, COR_TRAJE, (cx - 12, cy + 3, 5, 3), border_radius=1)
    pygame.draw.rect(tela, COR_TRAJE, (cx + 7, cy + 3, 5, 3), border_radius=1)


def desenhar_asteroide(tela, gx, gy):
    cx = gx * CELL + CELL // 2
    cy = gy * CELL + CELL // 2
    pygame.draw.circle(tela, COR_ASTEROIDE, (cx, cy), 13)
    pygame.draw.circle(tela, COR_ASTEROIDE_ESCURO, (cx - 3, cy - 2), 4)
    pygame.draw.circle(tela, COR_ASTEROIDE_ESCURO, (cx + 4, cy + 3), 3)
    pygame.draw.circle(tela, COR_ASTEROIDE_ESCURO, (cx + 1, cy - 5), 2)


def desenhar_cristal(tela, gx, gy):
    cx = gx * CELL + CELL // 2
    cy = gy * CELL + CELL // 2
    pontos = [(cx, cy - 12), (cx + 8, cy), (cx, cy + 12), (cx - 8, cy)]
    pygame.draw.polygon(tela, COR_CRISTAL, pontos)
    pygame.draw.polygon(tela, COR_CRISTAL_BRILHO, pontos, 2)
    pygame.draw.circle(tela, (255, 255, 255), (cx - 2, cy - 3), 2)


def desenhar_nave(tela, gx, gy):
    cx = gx * CELL + CELL // 2
    cy = gy * CELL + CELL // 2
    pygame.draw.ellipse(tela, COR_NAVE_CORPO, (cx - 14, cy - 4, 28, 14))
    pygame.draw.ellipse(tela, COR_NAVE, (cx - 14, cy - 4, 28, 14), 2)
    pygame.draw.ellipse(tela, COR_VISOR, (cx - 6, cy - 10, 12, 10))
    pygame.draw.ellipse(tela, (100, 180, 255), (cx - 6, cy - 10, 12, 10), 1)
    pygame.draw.circle(tela, COR_NAVE, (cx - 10, cy + 8), 3)
    pygame.draw.circle(tela, COR_NAVE, (cx, cy + 10), 3)
    pygame.draw.circle(tela, COR_NAVE, (cx + 10, cy + 8), 3)


def desenhar_chave(tela, gx, gy):
    cx = gx * CELL + CELL // 2
    cy = gy * CELL + CELL // 2
    pygame.draw.circle(tela, COR_CHAVE, (cx - 4, cy - 4), 6, 2)
    pygame.draw.rect(tela, COR_CHAVE, (cx, cy - 1, 12, 3))
    pygame.draw.rect(tela, COR_CHAVE, (cx + 8, cy + 2, 3, 4))
    pygame.draw.rect(tela, COR_CHAVE, (cx + 4, cy + 2, 3, 3))


def desenhar_portao(tela, gx, gy, aberto):
    cx = gx * CELL
    cy = gy * CELL
    cor = COR_PORTAO_ABERTO if aberto else COR_PORTAO
    if aberto:
        pygame.draw.rect(tela, cor, (cx + 2, cy + 2, CELL - 4, CELL - 4), 2, border_radius=4)
    else:
        pygame.draw.rect(tela, cor, (cx + 2, cy + 2, CELL - 4, CELL - 4), border_radius=4)
        pygame.draw.line(tela, (255, 255, 255), (cx + CELL // 2, cy + 4), (cx + CELL // 2, cy + CELL - 4), 2)
        pygame.draw.line(tela, (255, 255, 255), (cx + 4, cy + CELL // 2), (cx + CELL - 4, cy + CELL // 2), 2)


def desenhar_marcador_inicio(tela, gx, gy):
    cx = gx * CELL + CELL // 2
    cy = gy * CELL + CELL // 2
    pygame.draw.rect(tela, (30, 80, 30), (gx * CELL + 1, gy * CELL + 1, CELL - 2, CELL - 2), 1, border_radius=4)


def desenhar_painel(tela, fonte_titulo, fonte_texto, fase_info, vidas, cristais_coletados,
                    chaves_coletadas, passos, mensagem, cor_mensagem):
    px = GRID_W * CELL
    pygame.draw.rect(tela, COR_PAINEL, (px, 0, PAINEL_W, JANELA_H))
    pygame.draw.line(tela, COR_GRID, (px, 0), (px, JANELA_H), 2)

    y = 15
    titulo = fonte_titulo.render(f"FASE {FASE_ATUAL} / 10", True, COR_TITULO)
    tela.blit(titulo, (px + 15, y))
    y += 30

    nome = fonte_texto.render(fase_info["nome"], True, COR_DESTAQUE)
    tela.blit(nome, (px + 15, y))
    y += 35

    pygame.draw.line(tela, COR_GRID, (px + 15, y), (px + PAINEL_W - 15, y))
    y += 15

    lbl_missao = fonte_titulo.render("MISSAO", True, COR_DESTAQUE)
    tela.blit(lbl_missao, (px + 15, y))
    y += 22

    palavras = fase_info["missao"].split()
    linha = ""
    for p in palavras:
        teste = f"{linha} {p}".strip()
        if fonte_texto.size(teste)[0] > PAINEL_W - 40:
            surf = fonte_texto.render(linha, True, COR_TEXTO)
            tela.blit(surf, (px + 15, y))
            y += 18
            linha = p
        else:
            linha = teste
    if linha:
        surf = fonte_texto.render(linha, True, COR_TEXTO)
        tela.blit(surf, (px + 15, y))
        y += 25

    dica_surf = fonte_texto.render(fase_info["dica"], True, COR_DICA)
    tela.blit(dica_surf, (px + 15, y))
    y += 35

    pygame.draw.line(tela, COR_GRID, (px + 15, y), (px + PAINEL_W - 15, y))
    y += 15

    lbl_status = fonte_titulo.render("STATUS", True, COR_DESTAQUE)
    tela.blit(lbl_status, (px + 15, y))
    y += 25

    vida_txt = fonte_texto.render(f"Vidas: {vidas}", True, COR_ERRO if vidas <= 1 else COR_TEXTO)
    tela.blit(vida_txt, (px + 15, y))
    y += 20

    passo_txt = fonte_texto.render(f"Passos: {passos}", True, COR_TEXTO)
    tela.blit(passo_txt, (px + 15, y))
    y += 20

    if fase_info["precisa_cristal"]:
        total_c = len(fase_info["cristais"])
        ct = fonte_texto.render(f"Cristais: {cristais_coletados}/{total_c}", True, COR_CRISTAL)
        tela.blit(ct, (px + 15, y))
        y += 20

    if fase_info["precisa_chave"]:
        ch = fonte_texto.render(f"Chave: {'SIM' if chaves_coletadas > 0 else 'NAO'}", True, COR_CHAVE)
        tela.blit(ch, (px + 15, y))
        y += 20

    y += 15
    pygame.draw.line(tela, COR_GRID, (px + 15, y), (px + PAINEL_W - 15, y))
    y += 15

    lbl_func = fonte_titulo.render("FUNCOES", True, COR_DICA)
    tela.blit(lbl_func, (px + 15, y))
    y += 22

    funcoes = ["andar_direita(n)", "andar_esquerda(n)", "andar_cima(n)", "andar_baixo(n)"]
    if FASE_ATUAL >= 5:
        funcoes.append("pegar_item()")
    if FASE_ATUAL >= 7:
        funcoes.append("usar_item()")
    if FASE_ATUAL >= 8:
        funcoes.extend(["girar(n)  [!]", "esperar(n)  [!]", "pular()  [!]", "teletransportar()  [!]"])

    for f in funcoes:
        cor = COR_AVISO if "[!]" in f else COR_DICA
        fs = fonte_texto.render(f, True, cor)
        tela.blit(fs, (px + 15, y))
        y += 18

    if mensagem:
        y = JANELA_H - 80
        pygame.draw.rect(tela, (20, 20, 50), (px + 10, y - 5, PAINEL_W - 20, 60), border_radius=6)

        palavras_m = mensagem.split()
        linha_m = ""
        ym = y
        for p in palavras_m:
            teste = f"{linha_m} {p}".strip()
            if fonte_texto.size(teste)[0] > PAINEL_W - 40:
                ms = fonte_texto.render(linha_m, True, cor_mensagem)
                tela.blit(ms, (px + 18, ym))
                ym += 18
                linha_m = p
            else:
                linha_m = teste
        if linha_m:
            ms = fonte_texto.render(linha_m, True, cor_mensagem)
            tela.blit(ms, (px + 18, ym))


def mostrar_tela_final(tela, fonte_grande, fonte_texto, sucesso):
    overlay = pygame.Surface((JANELA_W, JANELA_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    tela.blit(overlay, (0, 0))

    if sucesso:
        msg1 = fonte_grande.render("MISSAO COMPLETA!", True, COR_SUCESSO)
        if FASE_ATUAL < 10:
            msg2 = fonte_texto.render(f"Fase {FASE_ATUAL} concluida!", True, COR_TEXTO)
            msg3 = fonte_texto.render(f"Mude FASE_ATUAL para {FASE_ATUAL + 1}", True, COR_DESTAQUE)
        else:
            msg2 = fonte_texto.render("Parabens! Todas as fases concluidas!", True, COR_SUCESSO)
            msg3 = fonte_texto.render("Voce dominou as funcoes Python!", True, COR_DESTAQUE)
    else:
        msg1 = fonte_grande.render("MISSAO FALHOU!", True, COR_ERRO)
        msg2 = fonte_texto.render("Revise seus comandos e tente novamente", True, COR_TEXTO)
        msg3 = fonte_texto.render("Pressione ESC para fechar", True, COR_DESTAQUE)

    tela.blit(msg1, (JANELA_W // 2 - msg1.get_width() // 2, JANELA_H // 2 - 60))
    tela.blit(msg2, (JANELA_W // 2 - msg2.get_width() // 2, JANELA_H // 2))
    tela.blit(msg3, (JANELA_W // 2 - msg3.get_width() // 2, JANELA_H // 2 + 30))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE or evento.key == pygame.K_RETURN:
                    esperando = False


def executar_jogo():
    global fila_comandos, FASE_ATUAL

    concluidas = carregar_progresso()
    if concluidas:
        proxima = 1
        for i in range(1, 11):
            if i not in concluidas:
                proxima = i
                break
        else:
            proxima = 10
        if FASE_ATUAL <= max(concluidas) and FASE_ATUAL in concluidas:
            FASE_ATUAL = proxima
            print(f"  Fase anterior ja concluida! Avancando para fase {FASE_ATUAL}.")

    if FASE_ATUAL not in FASES:
        print()
        print("=" * 50)
        print(f"  Fase {FASE_ATUAL} nao existe. Use 1 a 10.")
        print("=" * 50)
        return

    if not verificar_acesso(FASE_ATUAL):
        print()
        print("=" * 50)
        print(f"  FASE {FASE_ATUAL} BLOQUEADA!")
        print(f"  Complete a fase {FASE_ATUAL - 1} antes.")
        if concluidas:
            print(f"  Fases concluidas: {sorted(concluidas)}")
        else:
            print("  Nenhuma fase concluida ainda.")
        print("=" * 50)
        print()
        return

    fase_info = FASES[FASE_ATUAL]

    fila_comandos = []

    funcao_comandos = {
        1: comandos_fase1,
        2: comandos_fase2,
        3: comandos_fase3,
        4: comandos_fase4,
        5: comandos_fase5,
        6: comandos_fase6,
        7: comandos_fase7,
        8: comandos_fase8,
        9: comandos_fase9,
        10: comandos_fase10,
    }
    funcao_comandos[FASE_ATUAL]()

    if not fila_comandos:
        print()
        print("=" * 50)
        print(f"  FASE {FASE_ATUAL}: {fase_info['nome']}")
        print()
        print("  Nenhum comando inserido!")
        print(f"  Edite a funcao comandos_fase{FASE_ATUAL}()")
        print("  e insira suas chamadas de funcao.")
        print("=" * 50)
        print()
        return

    pygame.init()
    tela = pygame.display.set_mode((JANELA_W, JANELA_H))
    pygame.display.set_caption(f"Missao Espacial - Fase {FASE_ATUAL}: {fase_info['nome']}")
    clock = pygame.time.Clock()

    try:
        fonte_titulo = pygame.font.SysFont("consolas", 16, bold=True)
        fonte_texto = pygame.font.SysFont("consolas", 13)
        fonte_grande = pygame.font.SysFont("consolas", 28, bold=True)
    except Exception:
        fonte_titulo = pygame.font.Font(None, 20)
        fonte_texto = pygame.font.Font(None, 16)
        fonte_grande = pygame.font.Font(None, 36)

    astro_x, astro_y = fase_info["inicio"]
    vidas = 3
    passos = 0
    cristais_coletados = 0
    chaves_coletadas = 0
    inventario = []
    portoes_abertos = set()

    cristais_no_mapa = list(fase_info["cristais"])
    chaves_no_mapa = list(fase_info["chaves"])

    mensagem = "Executando comandos..."
    cor_mensagem = COR_TEXTO
    sucesso = False
    falhou = False

    idx_comando = 0
    ultimo_tick = pygame.time.get_ticks()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        agora = pygame.time.get_ticks()

        if not sucesso and not falhou and idx_comando < len(fila_comandos) and agora - ultimo_tick >= VELOCIDADE_ANIMACAO:
            cmd = fila_comandos[idx_comando]
            idx_comando += 1
            ultimo_tick = agora

            nx, ny = astro_x, astro_y

            if cmd == "DIREITA":
                nx += 1
                passos += 1
            elif cmd == "ESQUERDA":
                nx -= 1
                passos += 1
            elif cmd == "CIMA":
                ny -= 1
                passos += 1
            elif cmd == "BAIXO":
                ny += 1
                passos += 1
            elif cmd == "PEGAR":
                item_pego = False
                if (astro_x, astro_y) in cristais_no_mapa:
                    cristais_no_mapa.remove((astro_x, astro_y))
                    cristais_coletados += 1
                    inventario.append("cristal")
                    mensagem = "Cristal coletado!"
                    cor_mensagem = COR_CRISTAL
                    item_pego = True
                if (astro_x, astro_y) in chaves_no_mapa:
                    chaves_no_mapa.remove((astro_x, astro_y))
                    chaves_coletadas += 1
                    inventario.append("chave")
                    mensagem = "Chave coletada!"
                    cor_mensagem = COR_CHAVE
                    item_pego = True
                if not item_pego:
                    mensagem = "Nada para coletar aqui!"
                    cor_mensagem = COR_AVISO
                nx, ny = astro_x, astro_y
            elif cmd == "USAR":
                portao_pos = None
                for p in fase_info["portoes"]:
                    if p == (astro_x, astro_y) or p in [
                        (astro_x + 1, astro_y), (astro_x - 1, astro_y),
                        (astro_x, astro_y + 1), (astro_x, astro_y - 1)
                    ]:
                        portao_pos = p
                        break
                if portao_pos and "chave" in inventario:
                    portoes_abertos.add(portao_pos)
                    inventario.remove("chave")
                    mensagem = "Portao desbloqueado!"
                    cor_mensagem = COR_SUCESSO
                elif portao_pos and "chave" not in inventario:
                    mensagem = "Voce nao tem a chave!"
                    cor_mensagem = COR_ERRO
                else:
                    mensagem = "Nada para usar aqui!"
                    cor_mensagem = COR_AVISO
                nx, ny = astro_x, astro_y
            elif cmd == "GIRAR":
                mensagem = "Astronauta girou... mas nao saiu do lugar!"
                cor_mensagem = COR_AVISO
                nx, ny = astro_x, astro_y
            elif cmd == "ESPERAR":
                mensagem = "Astronauta esperando... tempo perdido!"
                cor_mensagem = COR_AVISO
                nx, ny = astro_x, astro_y
            elif cmd == "PULAR":
                mensagem = "Astronauta pulou... mas caiu no mesmo lugar!"
                cor_mensagem = COR_AVISO
                nx, ny = astro_x, astro_y
            elif cmd == "TELETRANSPORTAR":
                nx = random.randint(0, GRID_W - 1)
                ny = random.randint(0, GRID_H - 1)
                mensagem = f"Teletransportou para ({nx},{ny})... Sorte?"
                cor_mensagem = COR_AVISO
                passos += 1

            if cmd in ("DIREITA", "ESQUERDA", "CIMA", "BAIXO", "TELETRANSPORTAR"):
                if nx < 0 or nx >= GRID_W or ny < 0 or ny >= GRID_H:
                    mensagem = "Fora do grid! Voce se perdeu no espaco!"
                    cor_mensagem = COR_ERRO
                    vidas -= 1
                    if vidas <= 0:
                        falhou = True
                        mensagem = "Sem vidas! Missao falhou!"
                elif (nx, ny) in fase_info["asteroides"]:
                    mensagem = "COLISAO com asteroide! -1 vida"
                    cor_mensagem = COR_ERRO
                    vidas -= 1
                    if vidas <= 0:
                        falhou = True
                        mensagem = "Sem vidas! Missao falhou!"
                elif (nx, ny) in fase_info["portoes"] and (nx, ny) not in portoes_abertos:
                    mensagem = "Portao bloqueado! Use a chave primeiro!"
                    cor_mensagem = COR_ERRO
                else:
                    astro_x, astro_y = nx, ny
                    if cmd not in ("PEGAR", "USAR", "TELETRANSPORTAR"):
                        mensagem = f"Moveu para ({astro_x}, {astro_y})"
                        cor_mensagem = COR_TEXTO

            if (astro_x, astro_y) == fase_info["nave"]:
                pode_vencer = True
                if fase_info["precisa_cristal"] and cristais_coletados < len(fase_info["cristais"]):
                    mensagem = "Colete todos os cristais antes!"
                    cor_mensagem = COR_AVISO
                    pode_vencer = False
                if fase_info["precisa_chave"] and len(fase_info["portoes"]) > len(portoes_abertos):
                    mensagem = "Abra todos os portoes antes!"
                    cor_mensagem = COR_AVISO
                    pode_vencer = False
                if pode_vencer:
                    sucesso = True
                    mensagem = "MISSAO COMPLETA!"
                    cor_mensagem = COR_SUCESSO

        if not sucesso and not falhou and idx_comando >= len(fila_comandos) and agora - ultimo_tick >= VELOCIDADE_ANIMACAO:
            if (astro_x, astro_y) != fase_info["nave"]:
                falhou = True
                mensagem = "Comandos acabaram! Nao chegou a nave."
                cor_mensagem = COR_ERRO

        desenhar_fundo(tela)
        desenhar_grid(tela)

        desenhar_marcador_inicio(tela, *fase_info["inicio"])

        for ax, ay in fase_info["asteroides"]:
            desenhar_asteroide(tela, ax, ay)

        for cx, cy in cristais_no_mapa:
            desenhar_cristal(tela, cx, cy)

        for kx, ky in chaves_no_mapa:
            desenhar_chave(tela, kx, ky)

        for px_p, py_p in fase_info["portoes"]:
            desenhar_portao(tela, px_p, py_p, (px_p, py_p) in portoes_abertos)

        desenhar_nave(tela, *fase_info["nave"])
        desenhar_astronauta(tela, astro_x, astro_y)

        desenhar_painel(tela, fonte_titulo, fonte_texto, fase_info, vidas,
                        cristais_coletados, chaves_coletadas, passos, mensagem, cor_mensagem)

        pygame.display.flip()
        clock.tick(60)

        if sucesso or falhou:
            pygame.time.wait(500)
            if sucesso:
                concluidas = carregar_progresso()
                concluidas.add(FASE_ATUAL)
                salvar_progresso(concluidas)
            mostrar_tela_final(tela, fonte_grande, fonte_texto, sucesso)
            rodando = False

    pygame.quit()


if __name__ == "__main__":
    executar_jogo()