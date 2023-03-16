def winner(valores, names):

    resultados = ["div_name_jogador", "div_name_jogador"]

    if valores[0] != valores[1]:
        if valores.count("DQ"):
            resultados[valores.index("DQ")] += ""
            resultados[valores.index(0)] += " vencedor"

        else:
            win = valores.index(max(valores))
            resultados[win] += " vencedor"
            loser = valores.index(min(valores))
            resultados[loser] += ""

    for n, nome in enumerate(names):
        if len(nome) >= 10:
            resultados[n] += " name_to_long"

    return resultados

def separar_nome():
    f = 'DMX | RonaldinhoBR 3 - JUNINHO-RAS 2'
    h = f.split(" - ")
    return h
