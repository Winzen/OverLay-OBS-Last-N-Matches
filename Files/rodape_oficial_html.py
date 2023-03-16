from funtions import clear_none
from get_match_on_event import get_list_last_10_match
from loadconfig_save import ler


def html_partida(round_, jogador1, score1, jogador2, score2):

    partida = f"""
        <div class="partida ordem">
    <div class="round"><span class="txt_round">{round_}</span></div>
    <div class="p">
        <div class="name"><span class="txt">{jogador1}</span></div>
        <div class="score">{str(score1).zfill(2)}</div>
    </div>
    <div class="p">
        <div class="name"><span class="txt">{jogador2}</span></div>
        <div class="score">{str(score2).zfill(2)}</div>
    </div>
</div>
    """
    return partida


def reader_html(partidas, placares=3000):

    reader = f"""
<link rel="stylesheet" href="../css/placares.css">

<div class="placar"></div>
    {partidas}
<script src="../js/funtions.js"></script>
<script>mudar_all("ordem", {placares})</script>
"""
    return reader


def conjunto_partidas(partidas):
    partidas_direta = ""

    if partidas:
        print(partidas)
        print(partidas[::-1])
        for partida in partidas[::-1]:

            partida = clear_none(partida)

            # tags = long_name([partida[3], partida[5], partida[0]])

            partidas_direta += html_partida(round_=partida[0],
                                            jogador1=partida[3], score1=partida[2],
                                            jogador2=partida[5], score2=partida[4])

    return partidas_direta


def rodape_html(dic_partidas, placares=2000):

    if dic_partidas:
        paridas = conjunto_partidas(dic_partidas)

        txt_html = reader_html(paridas, placares)
        with open("Resultado/Placares.html", "w", encoding="utf-8") as html:
            html.write(txt_html)
        return "Atualização Ativa"
    else:
        raise ValueError


def montar_placares(link):
    try:
        config = ler()

        att = rodape_html(get_list_last_10_match(link), config["placares"])

        return att

    except ValueError:

        return "Falha ao começar atualizar"
