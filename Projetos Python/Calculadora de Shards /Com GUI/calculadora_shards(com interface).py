#===============================================================
# IMPORTAÇÃO DAS BIBLIOTECAS (tkinter, os, math)
#===============================================================

import tkinter as tk
import os
from math import ceil

#===============================================================
# OS (Colocar imagens na GUI)
#===============================================================

pasta = os.path.dirname(__file__)
gold_png = os.path.join(pasta, "gold.png")
lollipop_png = os.path.join(pasta, "lollipop.png")
shard_png = os.path.join(pasta, "shard.png")

#===============================================================
# FUNÇÕES
#===============================================================

#Contador de Shards

#Calcula quantos shards você terá e qual o valor de acordo com oque o usuário digitar
def calcular_lollipop():
    try:
        lolli = int(lollipop_entry.get())
        valor = int(valor_gold_entry.get())
        if lolli > 0 and valor > 0:
            valor_final = lolli * valor
            total_shards = lolli * 5
            resultado.config(text=f'Shards total: "{total_shards:,}"\nValor final: {valor_final:,} de gold'.replace(",", "."))
        else:
            mensagem_erro.config(text="[Digite um número maior que 0!]")
            return

        mensagem_erro.config(text="")

    except ValueError:
        mensagem_erro.config(text="[Somente números!]")

#Calcula quantos lollipop o usuário terá
def calcular_shards():
    try:
        shard = int(shards_entry.get())
        if shard > 0:
            total_lolli = shard / 5
            resultado.config(text=f'Você terá um total de "{ceil(total_lolli)}" Lollipops'.replace(",", "."))
        else:
            mensagem_erro.config(text="[Digite um número maior que 0!]")
            return

        mensagem_erro.config(text="")

    except ValueError:
        mensagem_erro.config(text="[Somente números!]")

#Converte todo o seu gold em lollipop e shards, de acordo com o valor do lollipop que o usuário digitar
def converter_gold():
    try:
        gold = int(quantidade_gold_entry.get())
        valor_lolli = int(valor_lollipop_entry.get())
        if gold > 0 and valor_lolli > 0:
            conversão = gold // valor_lolli
            resultado.config(text=f'Você poderá comprar "{conversão:,.0f}" Lollipops e terá {conversão*5:,.0f} Shards'.replace(",", "."))
        else:
            mensagem_erro.config(text="[Digite um número maior que 0!]")
            return

        mensagem_erro.config(text="") 

    except ValueError:  
        mensagem_erro.config(text="[Somente números!]")

#===============================================================
# JANELA
#===============================================================

window = tk.Tk()
window.title("Calculadora de Shards")
window.geometry("500x500")

#===============================================================
# FRAMES
#===============================================================

frame_title = tk.Frame(window)
frame_lollipop = tk.Frame(window)
frame_shards = tk.Frame(window)
frame_converter_gold = tk.Frame(window)
frame_resultado = tk.Frame(window)
frame_erros = tk.Frame(window)

#===============================================================
# IMAGENS
#===============================================================

#Imagens
gold_image = tk.PhotoImage(file=gold_png)
lollipop_image = tk.PhotoImage(file=lollipop_png)
shard_image = tk.PhotoImage(file=shard_png)
#Diminuir tamanho das imagens
gold_image = gold_image.subsample(3, 3)
lollipop_image = lollipop_image.subsample(3, 3)
shard_image = shard_image.subsample(3, 3)
#Logos 
logo_gold = tk.Label(frame_converter_gold, image=gold_image)
logo_lollipop = tk.Label(frame_lollipop, image=lollipop_image)
logo_shard = tk.Label(frame_shards, image=shard_image)

#===============================================================
# LABELS
#===============================================================

title_text = tk.Label(frame_title, text="Calculadora de Shards")

label_lollipop = tk.Label(frame_lollipop, text="Quantidade de Lollipops:")

label_valor_gold = tk.Label(frame_lollipop, text="Valor do Lollipop:")

label_shards = tk.Label(frame_shards, text="Quantidade de Shards:")

label_quantidade_gold = tk.Label(frame_converter_gold, text="Quantidade de Gold:")

label_valor_lollipop = tk.Label(frame_converter_gold, text="Valor do Lollipop:")

espaco = tk.Label(window, text="")
espaco1 = tk.Label(window, text="")

#===============================================================
# RESULTADO
#===============================================================

label_resultado = tk.Label(frame_resultado, text="Resultado:")

resultado = tk.Label(frame_resultado, text="")

#===============================================================
# TRATAMENTO DE ERROS
#===============================================================

mensagem_erro = tk.Label(window, text="", fg="red")

#===============================================================
# ENTRYS
#===============================================================

lollipop_entry = tk.Entry(frame_lollipop)

valor_gold_entry = tk.Entry(frame_lollipop)

shards_entry = tk.Entry(frame_shards)

quantidade_gold_entry = tk.Entry(frame_converter_gold)

valor_lollipop_entry = tk.Entry(frame_converter_gold)

#===============================================================
# WIDGETS
#===============================================================

lollipop_button = tk.Button(frame_lollipop, 
                            text="Converter lollipop para shard", 
                            command=calcular_lollipop)

shard_button = tk.Button(frame_shards, 
                        text="Converter shard para lollipop",
                        command=calcular_shards)

gold_button = tk.Button(frame_converter_gold, 
                        text="Converter gold para lollipop",
                        command=converter_gold)

#===============================================================
# PACKS - Estrutura do Código utilizando .pack()
#===============================================================

#Título do projeto.
frame_title.pack()
title_text.pack()

#Calcular lollipop
frame_lollipop.pack()
logo_lollipop.grid(row=0, column=0, sticky="w")
label_lollipop.grid(row=0, column=1, sticky="w")
lollipop_entry.grid(row=0, column=2, sticky="w")
label_valor_gold.grid(row=1, column=1, sticky="e")
valor_gold_entry.grid(row=1, column=2, sticky="w")
lollipop_button.grid(row=2, column=1, columnspan=2, pady=10)

espaco.pack()
#Calcular shards.
frame_shards.pack()
logo_shard.grid(row=0, column=0, sticky="w")
label_shards.grid(row=0, column=1, sticky="w")
shards_entry.grid(row=0, column=2, sticky="w")
shard_button.grid(row=1, column=1, columnspan=2, pady=10)

espaco1.pack()
#Converter quantidade de gold para lollipop.
frame_converter_gold.pack()
logo_gold.grid(row=0, column=0, sticky="w")
label_quantidade_gold.grid(row=0, column=1, sticky="w")
quantidade_gold_entry.grid(row=0, column=2, sticky="w")
label_valor_lollipop.grid(row=1, column=1, sticky="e")
valor_lollipop_entry.grid(row=1, column=2, sticky="w")
gold_button.grid(row=2, column=1, columnspan=2, pady=10)

#Mostrar o resultado
frame_resultado.pack()
label_resultado.pack()
resultado.pack()

#Mensagem de Erro
mensagem_erro.pack()

#===============================================================
# LOOP DA JANELA
#===============================================================

window.mainloop()


# * Sugestões *
#Criar uma definição para o valor da lollipop.
#Histórico dos valores digitados pelo usuário