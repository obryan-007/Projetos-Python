#Esse dicionário foi necessário, porque o sistema de levels dentro do jogo não tem um padrão de conta. 
#Por isso, o dicionário ficou grande.

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

skills = {
    "Melee": 0, 
    "Mage": 0, 
    "Mining": 0, 
    "Smithing": 0, 
    "Woodcutting": 0, 
    "Crafting": 0, 
    "Fishing": 0, 
    "Cooking": 0, 
    "Spellbinding": 0, 
    "Alchemy": 0, 
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

import math as m

def linha():
    print(30*"-")

#Pretendo criar um append para arquivos .txt para manter levels futuros salvos sem precisar 
# digitar sempre que rodar o código

#====================== Sugestões ======================
# 1 - Criar uma função específica para descobrir o level.
# 2 - Utilizar Tkinter para interface gráfica.
# 3 - ...


def tabela_skills():
    linha()
    print("\n===== TABELA DE SKILLS =====")
    for skill, xp_skill in skills.items():
        for level, xp in xp_levels.items():
            if xp_skill >= xp:
                level_atual = level
        print(f"{skill}")
        print(f"| XP: {xp_skill}")
        print(f"| Level: {level_atual}")


def estatisticas_skills():

    if not any(xp > 0 for xp in skills.values()):
        print("Skill não encontrada.")
    else:
        maior_skill = max(skills, key=skills.get)
        menor_skill = min(skills, key=skills.get)
        xp_total = 0
        total_levels = 0
        for skill, xp in skills.items():
            xp_total += xp
            level_atual = 0
            for level, xp_level in sorted(xp_levels.items()):
                if xp >= xp_level:
                    level_atual = level
                else:
                    break
            total_levels += level_atual
            
        print("\n===== ESTATÍSTICAS =====")
        print(f"Maior skill: {maior_skill}")
        print(f"XP: {skills[maior_skill]}")
        print(f"\nMenor skill: {menor_skill}")
        print(f"XP: {skills[menor_skill]}")
        print(f"\nXP total: {xp_total}")
        print(f"Levels total: {total_levels}")
        

def selecionar_skill(skill_escolhida):
    skills = ["Melee", "Mage", "Mining", "Smithing", "Woodcutting", 'Crafting', 'Fishing', 'Cooking', 'Spellbinding', 'Alchemy']
    print("\n===== SKILLS =====")
    for num, skill in enumerate(skills, start=1):
        print(f"{num} - {skill}")
    skill_escolhida = str(input("Selecione uma skill: "))
    if skill_escolhida not in skills:
        print("Skill não existente! Tente novamente.")
        skill_escolhida = "Não selecionado."
    return skill_escolhida


def descobrir_level(skill_escolhida):
    try:
        linha()    
        xp_atual = int(input("\nDigite seu XP atual: "))
        #Percorre o dicionário para descobrir o level do usuário somente pelo xp digitado
        for level, xp in xp_levels.items():
            if xp_atual >= xp:
                level_atual = level
        #Condição para verificar se o xp não é maior do que o último level e retorna uma mensagem
        if xp_atual >= 4536153492:
            print("Level máximo atingido!")
            return xp_atual, None, None, None, None
        elif xp_atual < 0:
            print("Números negativos não são permitidos.")
            return xp_atual, None, None, None, None
        else:
            skills[skill_escolhida] = xp_atual
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
    except ValueError:
        print("Somente números!")
        return None, None, None, None, None

#Calcular quantos monstros faltam para o próximo level
def monstros_restantes(xp_final_level, xp_atual):
    try:  
        linha()
        xp_mob = int(input("\nDigite o XP do Monstro: "))
        if xp_mob <= 0:
            print("Erro: Somente números maiores que 0!")
        else:
            mobs_restantes = (xp_final_level - xp_atual) / xp_mob
            print(f"Monstros restantes: {m.ceil(mobs_restantes)}") #math.ceil para arredondar número de mobs
            linha()
    except(ValueError):
        print("Erro: Somente números!")
    


def meta_personalizada(xp_atual, xp_inicial_level, xp_total):
    try:
        print("\n===== META PERSONALIZADA =====")
        meta = float(input("Digite uma porcentagem desejada (Ex: 12.3): "))
        xp_mob = int(input("Digite o XP do Monstro: "))
        if meta <= 0 or meta > 100 or xp_mob <= 0:
            print("Digite uma meta ou xp do monstro válido!")
        else:
            xp_ganho_dentro_do_level = xp_total * (meta / 100)
            xp_total_necessario = xp_inicial_level + xp_ganho_dentro_do_level
            xp_faltante = xp_total_necessario - xp_atual
            mobs_restantes = xp_faltante / xp_mob
            print(f"Meta: {meta}%")
            print(f"XP restante: {xp_faltante:.0f}")
            print(f"Monstros restantes: {m.ceil(mobs_restantes)} ") #math.ceil para arredondar número de mobs
            #Depois, tentar corrigir o bug onde o usuário pode colocar uma meta menor do que o progresso 
            #(Dica: retornar a variável "progresso")
            linha()
    except (ValueError):
        print("Somente números!")

    
def menu():
    xp_inicial_level = None
    xp_total = None
    xp_atual = None
    xp_final_level = None
    skill_escolhida = "Não selecionado."

    while True:
    #Menu interativo
        try:
            print("\n")
            linha()
            print("       CALCULADORA COA")
            linha()
            print(f"Skill: {skill_escolhida}")
            print("[1] - Selecionar Skill")
            print("[2] - Descobrir level")
            print("[3] - Calcular monstros")
            print("[4] - Meta personalizada")
            print("[5] - Tabela de Skills")
            print("[6] - Estatísticas")
            print("[7] - Sair")
            opcao = int(input("Selecione alguma opção acima: "))
        except (ValueError):
            print('Somente números!')
            continue

        match opcao:
            case 1:
                skill_escolhida = selecionar_skill(skill_escolhida)
                xp_atual = None
                xp_total = None
                xp_final_level = None
                xp_inicial_level = None
            case 2:
                if skill_escolhida == "Não selecionado.":
                    print("Selecione alguma skill primeiro!")
                else:
                    xp_atual, level_atual, xp_final_level, xp_total, xp_inicial_level = descobrir_level(skill_escolhida)
            case 3:
                if xp_atual is None:
                    print("\nPrimeiro, descubra seu level atual (Opção 1).")
                else:
                    monstros_restantes(xp_final_level, xp_atual)
            case 4:
                if xp_atual is None:
                    print("\nPrimeiro, descubra seu level atual (Opção 1).")
                else:
                    meta_personalizada(xp_atual, xp_inicial_level, xp_total)
            case 5:
                tabela_skills()
            case 6:
                estatisticas_skills()
            case 7:
                print("\nEncerrando programa...")
                break
            case _:
                print("Opção inválida! Tente novamente.")
                
    return skill_escolhida
menu()