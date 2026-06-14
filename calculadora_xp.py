xp_levels = {
    1: 0,
    2: 46,
    3: 99,
    4: 159,
    5: 229,
    6: 309,
    7: 401,
    8: 507,
    9: 628,
    10: 768,
    11: 928,
    12: 1112,
    13: 1324,
    14: 1567,
    15: 1847,
    16: 2168,
    17: 2537,
    18: 2961,
    19: 3448,
    20: 4008,
    21: 4651,
    22: 5389,
    23: 6237,
    24: 7212,
    25: 8332,
    26: 9618,
    27: 11095,
    28: 12792,
    29: 14742,
    30: 16982,
    31: 19555,
    32: 22510,
    33: 25905,
    34: 29805,
    35: 34285,
    36: 39431,
    37: 45342,
    38: 52132,
    39: 59932,
    40: 68892,
    41: 79184,
    42: 91006,
    43: 104586,
    44: 120186,
    45: 138106,
    46: 158690,
    47: 182335,
    48: 209496,
    49: 240696,
    50: 276536,
    51: 317705,
    52: 364996,
    53: 419319,
    54: 481720,
    55: 553400,
    56: 635738,
    57: 730320,
    58: 838966,
    59: 963768,
    60: 1107128,
    61: 1271805,
    62: 1460969,
    63: 1678262,
    64: 1927866,
    65: 2214586,
    66: 2543940,
    67: 2922269,
    68: 3356855,
    69: 3856063,
    70: 4429503,
    71: 5088212,
    72: 5844870,
    73: 6714042,
    74: 7712459,
    75: 8859339,
    76: 10176758,
    77: 11690075,
    78: 13428420,
    79: 15425254,
    80: 17719014,
    81: 20353852,
    82: 23380486,
    83: 26857176,
    84: 30850844,
    85: 35438364,
    86: 40708040,
    87: 46761308,
    88: 53714688,
    89: 61702024,
    90: 70877064,
    91: 81416417,
    92: 93522954,
    93: 107429714,
    94: 123404386,
    95: 141754466,
    96: 162833172,
    97: 187046247,
    98: 214859767,
    99: 246809111,
    100: 283509271,
    101: 325666684,
    102: 374092835,
    103: 429719875,
    104: 493618564,
    105: 567018884,
    106: 651333710,
    107: 748186012,
    108: 859440093,
    109: 987237472,
    110: 1134038112,
    111: 1302667765,
    112: 1496372370,
    113: 1718880532,
    114: 1974475291,
    115: 2268076571,
    116: 2605335878,
    117: 2992745089,
    118: 3437761413,
    119: 3948950932,
    120: 4536153492
}

#CSCOA (Calculadora de Skill do CoA) 
# ==================================================
# CALCULADORA DE XP - CURSE OF AROS
#
# "Esforça-te, e tem bom ânimo; não temas,
# nem te espantes, porque o Senhor teu Deus
# é contigo por onde quer que andares."
# - Josué 1:9
#
# Todo projeto grande é concluído uma etapa de cada vez.
# ==================================================

import math #Arredondar o número de mobs

def linha():
    print(30*"-")

def descobrir_level():
    linha()
    xp_atual = int(input("Digite seu XP atual: "))
    for level, xp in xp_levels.items():
        if xp_atual >= xp:
            level_atual = level
    xp_inicial_level = xp_levels[level_atual]
    xp_final_level = xp_levels[level_atual + 1]
    xp_ganho = xp_atual - xp_inicial_level
    xp_total = xp_final_level - xp_inicial_level 
    progresso = (xp_ganho/xp_total) * 100
    print(f"\nLevel: {level_atual}")
    print(f"XP restante para o level {level_atual + 1}: {xp_final_level - xp_atual}")
    print(f"Progresso: {progresso:.1f}%")
    print(f"Restante: {100 - progresso:.1f}%")
    linha()
    return xp_atual, level_atual, xp_final_level, xp_total, xp_inicial_level


def monstros_restantes(xp_final_level, xp_atual):
    linha()
    xp_mob = int(input("Digite o XP do Monstro: "))
    mobs_restantes = (xp_final_level - xp_atual) / xp_mob
    print(f"Monstros restantes: {mobs_restantes:.0f}")
    linha()


def meta_personalizada(xp_atual, xp_inicial_level, xp_total):
    linha()
    meta = float(input("Digite uma porcentagem desejada (Ex: 12.3): "))
    xp_mob = int(input("Digite o XP do Monstro: "))
    print("xp_atual =", xp_atual)
    print("xp_inicial_level =", xp_inicial_level)
    print("xp_total =", xp_total)
    xp_ganho_dentro_do_level = xp_total * (meta / 100)
    xp_total_necessario = xp_inicial_level + xp_ganho_dentro_do_level
    xp_faltante = xp_total_necessario - xp_atual
    mobs_restantes = (xp_faltante - xp_atual) / xp_mob
    print(f"Meta: {meta}%")
    print(f"XP restante: {xp_faltante:.0f}")
    print(f"Monstros restantes: {mobs_restantes} ")
    linha()

    
def menu():
    xp_inicial_level = None
    xp_total = None
    xp_atual = None
    xp_final_level = None

    while True:
    #Menu interativo
        try:
            linha()
            print("       CALCULADORA COA")
            linha()
            print("[1] - Descobrir level")
            print("[2] - Calcular monstros")
            print("[3] - Meta personalizada")
            print("[4] - Sair")
            opcao = int(input("Selecione alguma opção acima: "))
        except:
            print('Somente números!')
            continue

        match opcao:
            case 1:
                xp_atual, level_atual, xp_final_level, xp_total, xp_inicial_level = descobrir_level()
            case 2:
                if xp_atual is None or xp_final_level is None:
                    print("\nPrimeiro, descubra seu level atual (Opção 1).")
                else:
                
                    monstros_restantes(xp_final_level, xp_atual)
            case 3:
                if xp_atual is None:
                    print("\nPrimeiro, descubra seu level atual (Opção 1).")
                else:
                    meta_personalizada(xp_atual, xp_inicial_level, xp_total)
            case 4:
                print("\nEncerrando programa...")
                break
            case _:
                print("Opção inválida! Tente novamente.")

menu()