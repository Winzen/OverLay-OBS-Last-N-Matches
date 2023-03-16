from top8_dq import get_list_top8
from funtions import linhas, clear_html_slots


def winner(valores, names):

    resultados = ["div_name_jogador", "div_name_jogador", "div_score_jogador", "div_score_jogador", False, ""]

    if valores[0] != valores[1]:
        if valores.count("DQ"):
            resultados[valores.index("DQ")] = "div_name_jogador loser"
            resultados[valores.index("DQ") + 2] = "div_score_jogador loser"
            resultados[valores.index(0)] = "div_name_jogador win_name"
            resultados[valores.index(0) + 2] = "div_score_jogador win_name"
            resultados[-1] = valores.index(0)
            resultados[4] = True
        else:
            win = valores.index(max(valores))
            resultados[win] = "div_name_jogador win_name"
            resultados[win+2] = "div_score_jogador win_name"
            loser = valores.index(min(valores))
            resultados[loser] = "div_name_jogador loser"
            resultados[loser + 2] = "div_score_jogador loser"
            resultados[-1] = win
            resultados[4] = True

    for n, nome in enumerate(names):
        if len(nome) >= 10:
            resultados[n] += " name_to_long"

    return resultados


def make_top8_video(link, test=False):

    if not test:

        lugares = get_list_top8(link, top16=False)

    else:

        lugares = link

    with open("modelo/video_top8.html", "r") as hltm_modelo:
        modelo = hltm_modelo.read()

    if lugares:
        for key, slots in lugares.items():
            partida_txt = ""
            for n, slot in enumerate(slots):

                if None in slot:
                    for v, n_ in enumerate(slot):
                        if n_ is None:
                            slot[v] = ""

                resultado = winner([slot[1], slot[3]], [slot[2], slot[4]])

                if resultado[4] and \
                        linhas(str(key)) not in partida_txt or linhas([str(key), str(n)]) not in partida_txt:

                    if key == -3:

                        partida_txt += linhas([str(key), str(n)])

                    else:

                        partida_txt = linhas(str(key))

                modelo = modelo.replace(f"!n{key}{n}0", slot[2])
                modelo = modelo.replace(f"!s{key}{n}0", str(slot[1]))
                modelo = modelo.replace(f"!p{key}{n}0", resultado[0] + " text_animado")
                modelo = modelo.replace(f"!ps{key}{n}0", resultado[2] + " text_animado")

                modelo = modelo.replace(f"!n{key}{n}1", slot[4])
                modelo = modelo.replace(f"!s{key}{n}1", str(slot[3]))
                modelo = modelo.replace(f"!p{key}{n}1", resultado[1] + " text_animado")
                modelo = modelo.replace(f"!ps{key}{n}1", resultado[3] + " text_animado")

                partida_txt += linhas([str(key), str(n), str(resultado[-1])])

            modelo = modelo.replace(f"!{key}", partida_txt)
        modelo = clear_html_slots(modelo)
        with open("Top 8/Top_8.html", "w", encoding="utf-8") as hltm_modelo:
            hltm_modelo.write(modelo)

        return "Top 8 Formado com sucesso"

    else:

        return "Link Invalido\nEvento não selecionado ou talvez link fora do Start.gg"
