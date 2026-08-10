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

#=======================================================================
# DICIONÁRIOS
#=======================================================================
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
    "Melee": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Mage": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Mining": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Smithing": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Woodcutting": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Crafting": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Fishing": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Cooking": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Spellbinding": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    },

    "Alchemy": {
        "xp": 0,
        "level": 0,
        "progresso": 0.0,
        "xp_total": 0,
        "xp_inicial": 0,
        "xp_final": 0
    }
}

#=======================================================================
# VARIÁVEIS GLOBAIS     
#=======================================================================

XP_MAXIMO = max(xp_levels.values())

#=======================================================================
# IMPORTAÇÕES (math, tkinter e os)
#=======================================================================

import tkinter as tk
from tkinter import ttk
from math import ceil

#=======================================================================
# FUNÇÕES
#=======================================================================

#Pretendo criar um append para arquivos .txt para manter levels futuros salvos sem precisar 
# digitar sempre que rodar o código

#====================== Sugestões ======================
# 1 - Criar uma função específica para descobrir o level.
# 2 - Utilizar Tkinter para interface gráfica.
# 3 - ...


def tabela_skills(event=None):
    texto = ""
    for skill, dados in skills.items():
        texto += f'{skill} | XP: {dados["xp"]} | Level: {dados["level"]}\n'

    label_tabela_skills.config(text=texto)

def estatisticas_skills(event=None):
        def pegar_xp(skill):
            return skills[skill]["xp"]
        maior_skill = max(skills, key=pegar_xp)
        menor_skill = min(skills, key=pegar_xp)
        xp_total = 0
        total_levels = 0
        for skill, dados in skills.items():
            xp_total += dados["xp"]
            total_levels += dados["level"]
            
        estatisticas.config(text=f"""
                        Maior skill: {maior_skill}
                        XP: {skills[maior_skill]["xp"]}
                        Menor skill: {menor_skill}
                        XP: {skills[menor_skill]["xp"]}
                        XP total: {xp_total}
                        Levels total: {total_levels}""")


def descobrir_level(skill_escolhida):
    try:
        xp_atual = int(entry_xp_atual.get())
        xp_restante = int(entry_xp_restante.get())
        #Percorre o dicionário para descobrir o level do usuário somente pelo xp digitado
        level_atual = 0
        for level, xp in xp_levels.items():
            if xp_atual >= xp:
                level_atual = level
        #Condição para verificar se o xp não é maior do que o último level e retorna uma mensagem
        if xp_atual >= XP_MAXIMO:
            resultado_level.config(text="Level máximo atingido!")
            erro_level.config(text="")
            print(f"Erro: usuário inseriu o XP máximo.")
            return
            
        elif xp_atual < 0 or xp_restante < 0:
            erro_level.config(text="[Número(s) negativo(s) não são permitidos.]")
            resultado_level.config(text="")
            print("Erro: usuário inseriu número(s) negativo(s).")
            return
        else:
            xp_inicial_level = xp_levels[level_atual]
            xp_final_level = xp_levels[level_atual + 1]
            xp_ganho = xp_atual - xp_inicial_level
            xp_total = xp_final_level - xp_inicial_level 
            progresso = (xp_ganho/xp_total) * 100
            mobs_restantes = (xp_final_level - xp_atual) / xp_restante
            resultado_level.config(text=f"""
    Level: {level_atual}
    XP restante: {xp_final_level - xp_atual:,.0f}
    Progresso: {progresso:,.1f}%
    Restante: {100 - progresso:,.1f}%
    Monstros/Itens restantes: {ceil(mobs_restantes)}""".replace(",", "."))#math.ceil para arredondar número de mobs/itens
            print("Sucesso: Resultado na janela.")
            

        erro_level.config(text="")

        #Armazenando informações da skill:
        skills[skill_escolhida]["xp"] = xp_atual
        skills[skill_escolhida]["level"] = level_atual
        skills[skill_escolhida]["progresso"] = progresso
        skills[skill_escolhida]["xp_total"] = xp_total
        skills[skill_escolhida]["xp_inicial"] = xp_inicial_level
        skills[skill_escolhida]["xp_final"] = xp_final_level
        terminal()

    except ValueError:
        erro_level.config(text="[Somente números!]")
        print("Erro: usuário não digitou números.")
        return 
        
#Terminar de configurar a saída de mensagens na interface. Continue firme, não desista ;)
def meta_personalizada(skill):
    try:
        meta = float(entry_meta.get())
        xp_mob = int(entry_xp.get())
        xp_atual = skills[skill]["xp"]
        xp_total = skills[skill]["xp_total"]
        xp_inicial = skills[skill]["xp_inicial"]
        progresso = skills[skill]["progresso"]
        for level, xp in xp_levels.items():
            if xp_atual >= xp:
                level_atual = level
        
        if meta <= 0 or meta > 100 or xp_mob <= 0:
            erro_meta.config(text="Digite uma meta ou xp \ndo monstro válido!")
            print("Erro: usuário digitou valores inválidos")
            return
        elif meta <= progresso:
            erro_meta.config(text=f"Digite uma meta maior \nque seu progresso {progresso:,.1f}!".replace(",","."))
            print("Erro: usuário digitou uma meta menor que o progresso")
            return
        else:
            xp_ganho_dentro_do_level = xp_total * (meta / 100)
            xp_total_necessario = xp_inicial + xp_ganho_dentro_do_level
            xp_faltante = xp_total_necessario - xp_atual
            mobs_restantes = xp_faltante / xp_mob
            resultado_meta.config(text=f"""
        Meta: {meta}%
        XP restante: {xp_faltante:.0f}
        Monstros restantes: {ceil(mobs_restantes)}""") #math.ceil para arredondar número de mobs
            
            #Depois, tentar corrigir o bug onde o usuário pode colocar uma meta menor do que o progresso 
            #(Dica: retornar a variável "progresso")
            
        terminal()            
        erro_meta.config(text="")

    except(ValueError):
        erro_meta.config(text="Somente números!")
        print("Erro: usuário não digitou números.")

def aba(event=None):
    aba_atual = notebook.select()
    indice = notebook.index(aba_atual)
    if indice == 2:
        tabela_skills()
    elif indice == 3:
        estatisticas_skills()
    
#=======================================================================
# JANELA
#=======================================================================

window = tk.Tk()
window.title("Calculadora CoA")
window.geometry("317x300")

#=======================================================================
# NOTEBOOK
#=======================================================================

notebook = ttk.Notebook(window)

#=======================================================================
# FRAMES
#=======================================================================

aba_descobrir_level = ttk.Frame(notebook)
aba_meta_personalizada = ttk.Frame(notebook)
aba_tabela_skills = ttk.Frame(notebook)
aba_estatisticas = ttk.Frame(notebook)

#=======================================================================
# ADICIONANDO ABAS
#=======================================================================

# .bind serve para fazer o sistema notar que o usuário trocou de aba e chamar as funções
notebook.bind("<<NotebookTabChanged>>", aba)

notebook.add(aba_descobrir_level, text="Level")
notebook.add(aba_meta_personalizada, text="Meta")
notebook.add(aba_tabela_skills, text="Tabela")
notebook.add(aba_estatisticas, text="Estatísticas")
notebook.pack()

#=======================================================================
# RESULTADO
#=======================================================================

resultado_level = ttk.Label(aba_descobrir_level, text="")

resultado_meta = ttk.Label(aba_meta_personalizada, text="")

#=======================================================================
# TRATAMENTO DE ERROS
#=======================================================================

erro_level = tk.Label(aba_descobrir_level, text="", fg="red")

erro_meta = tk.Label(aba_meta_personalizada, text="", fg="red")

#=======================================================================
# COMBOBOX
#=======================================================================

# Descobrir level
skill_box_level = ttk.Combobox(aba_descobrir_level, values=list(skills.keys()), state="readonly")
skill_box_level.current(0)
skill_escolhida_level = skill_box_level.get()

# Meta personalizada
skill_box_meta = ttk.Combobox(aba_meta_personalizada, values=list(skills.keys()), state="readonly")
skill_box_meta.current(0)
skill_escolhida_meta = skill_box_meta.get()

#=======================================================================
# ABA: DESCOBRIR LEVEL
#=======================================================================

# ------------------------------ LABELS ------------------------------ 

label_level = ttk.Label(aba_descobrir_level, text="DESCOBRIR LEVEL")
 
label_textSkill_level = ttk.Label(aba_descobrir_level, text="Skill:")

label_xp_atual = ttk.Label(aba_descobrir_level, text="XP Atual:")

label_xp_restante = ttk.Label(aba_descobrir_level, text="XP do Monstro/Item:")

label_resultado_level = ttk.Label(aba_descobrir_level, text="Resultado:")

# ------------------------------ ENTRY ------------------------------ 

entry_xp_atual = ttk.Entry(aba_descobrir_level)

entry_xp_restante = ttk.Entry(aba_descobrir_level)

# ------------------------------ BUTTON ------------------------------

button_xp_atual = ttk.Button(aba_descobrir_level,
                      text="Calcular",
                      command=lambda:descobrir_level(skill_box_level.get())
)

# ------------------------------ LAYOUT ------------------------------

label_level.grid(row=0, columnspan=2)

label_textSkill_level.grid(row=1, column=0, pady=10, sticky="w")
skill_box_level.grid(row=1, column=1, pady=10, sticky="w")

label_xp_atual.grid(row=2, column=0, pady=10, sticky="w")
entry_xp_atual.grid(row=2, column=1, pady=10, sticky="w")

label_xp_restante.grid(row=3, column=0, pady=10, sticky="w")
entry_xp_restante.grid(row=3, column=1, pady=10, sticky="w")

button_xp_atual.grid(row=4, column=0, columnspan=2)

label_resultado_level.grid(row=5, column=0, pady=20)
resultado_level.grid(row=5, column=1)
erro_level.grid(row=5, column=1)

#=======================================================================
# ABA: META PERSONALIZADA
#=======================================================================

# ------------------------------ LABELS ------------------------------

label_aba_meta = ttk.Label(aba_meta_personalizada, text='META PERSONALIZADA')

label_textSkill_meta = ttk.Label(aba_meta_personalizada, text='Skill:')

label_meta = ttk.Label(aba_meta_personalizada, text='Meta:')

label_xp = ttk.Label(aba_meta_personalizada, text='XP do Monstro/Item:')

label_resultado_meta = ttk.Label(aba_meta_personalizada, text='Resultado:')

# ------------------------------ ENTRY ------------------------------ 

entry_meta = ttk.Entry(aba_meta_personalizada)

entry_xp = ttk.Entry(aba_meta_personalizada)

# ------------------------------ BUTTON ------------------------------

button_meta = ttk.Button(aba_meta_personalizada,
                         text="Calcular",
                         command=lambda:meta_personalizada(skill_box_meta.get()))

# ------------------------------ LAYOUT ------------------------------

label_aba_meta.grid(row=0, columnspan=2)

label_textSkill_meta.grid(row=1, column=0, pady=10, sticky="w")
skill_box_meta.grid(row=1, column=1, pady=10, sticky="w")

label_meta.grid(row=2, column=0, pady=10, sticky="w")
entry_meta.grid(row=2, column=1, pady=10, sticky="w")

label_xp.grid(row=3, column=0, pady=10, sticky="w")
entry_xp.grid(row=3, column=1, pady=10, sticky="w")

button_meta.grid(row=4, columnspan=2)

label_resultado_meta.grid(row=5, column=0, pady=20)
resultado_meta.grid(row=5, column=1)
erro_meta.grid(row=5, column=1)

#=======================================================================
# ABA: TABELA DE SKILLS
#=======================================================================

# ------------------------------ LABELS ------------------------------

label_tabela = ttk.Label(aba_tabela_skills, text="TABELA DE SKILLS")

label_tabela_skills = ttk.Label(aba_tabela_skills, text="")

# ------------------------------ LAYOUT ------------------------------

label_tabela.grid(row=0, columnspan=4)

label_tabela_skills.grid(row=1, column=1, pady=10)

#=======================================================================
# ABA: ESTATÍSTICAS
#=======================================================================

# ------------------------------ LABELS ------------------------------

label_estatisticas = ttk.Label(aba_estatisticas, text="ESTATÍSTICAS")

estatisticas = ttk.Label(aba_estatisticas, text="")

# ------------------------------ LAYOUT ------------------------------

label_estatisticas.grid(row=0, columnspan=4)

estatisticas.grid(row=1, column=0)

#=======================================================================
# Acompanhamento pelo terminal
#=======================================================================

print("Mensagens:")

def terminal():
    for skill, dados in skills.items():
        print(f"{skill} - {dados}\n")
terminal()

print(f"Skill escolhida (Aba Level): {skill_escolhida_level}")
print(f"Skill escolhida (Aba Meta): {skill_escolhida_meta}")

#=======================================================================
# LOOP DA JANELA
#=======================================================================

window.mainloop()