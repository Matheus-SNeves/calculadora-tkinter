import tkinter as tk

expressao = ""

def clicar(valor):
    global expressao
    expressao += str(valor)
    entrada.delete(0, tk.END)
    entrada.insert(0, expressao)

def limpar():
    global expressao
    expressao = ""
    entrada.delete(0, tk.END)

def calcular():
    global expressao
    try:
        resultado = eval(expressao)
            
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
        expressao = str(resultado)
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")
        expressao = ""

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def botoes1():
    botaodivisao = tk.Button(janela, text="/", width=5, height=2, command=lambda: clicar("/"))
    botaomultiplicacao = tk.Button(janela, text="*", width=5, height=2, command=lambda: clicar("*"))
    botaomenos = tk.Button(janela, text="-", width=5, height=2, command=lambda: clicar("-"))
    botaomais = tk.Button(janela, text="+", width=5, height=2, command=lambda: clicar("+"))

    botaodivisao.grid(row=1, column=0, padx=2, pady=2)
    botaomultiplicacao.grid(row=1, column=1, padx=2, pady=2)
    botaomenos.grid(row=1, column=2, padx=2, pady=2)
    botaomais.grid(row=1, column=3, padx=2, pady=2)

def botoes2():
    botao7 = tk.Button(janela, text="7", width=5, height=2, command=lambda: clicar("7"))
    botao8 = tk.Button(janela, text="8", width=5, height=2, command=lambda: clicar("8"))
    botao9 = tk.Button(janela, text="9", width=5, height=2, command=lambda: clicar("9"))
    botaolimpar = tk.Button(janela, text="C", width=5, height=2, command=limpar)

    botao7.grid(row=2, column=0, padx=2, pady=2)
    botao8.grid(row=2, column=1, padx=2, pady=2)
    botao9.grid(row=2, column=2, padx=2, pady=2)
    botaolimpar.grid(row=2, column=3, padx=2, pady=2)

def botoes3():
    botao4 = tk.Button(janela, text="4", width=5, height=2, command=lambda: clicar("4"))
    botao5 = tk.Button(janela, text="5", width=5, height=2, command=lambda: clicar("5"))
    botao6 = tk.Button(janela, text="6", width=5, height=2, command=lambda: clicar("6"))

    botao4.grid(row=3, column=0, padx=2, pady=2)
    botao5.grid(row=3, column=1, padx=2, pady=2)
    botao6.grid(row=3, column=2, padx=2, pady=2)

def botoes4():
    botao1 = tk.Button(janela, text="1", width=5, height=2, command=lambda: clicar("1"))
    botao2 = tk.Button(janela, text="2", width=5, height=2, command=lambda: clicar("2"))
    botao3 = tk.Button(janela, text="3", width=5, height=2, command=lambda: clicar("3"))

    botao1.grid(row=4, column=0, padx=2, pady=2)
    botao2.grid(row=4, column=1, padx=2, pady=2)
    botao3.grid(row=4, column=2, padx=2, pady=2)

def botoes5():
    botao0 = tk.Button(janela, text="0", width=5, height=2, command=lambda: clicar("0"))
    botaovirgula = tk.Button(janela, text=".", width=5, height=2, command=lambda: clicar("."))
    botaoenviar = tk.Button(janela, text="=", width=5, height=2, command=calcular)

    botao0.grid(row=5, column=0, padx=2, pady=2)
    botaovirgula.grid(row=5, column=1, padx=2, pady=2)
    botaoenviar.grid(row=4, column=3, rowspan=2, columnspan=1, sticky="ns", padx=2, pady=2)

botoes1()
botoes2()
botoes3()
botoes4()
botoes5()

janela.mainloop()