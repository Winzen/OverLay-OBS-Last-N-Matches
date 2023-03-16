from funtions import separar_nome, winner
from get_match_on_event import get_list_last_10_match
from time import sleep


def html_partida(round_, jogador1, jogador2, placar1, placar2, tag, tag2):
    partida = f"""
        <div class="partida">
            <div class="round_text">{round_}</div>
            <div class="jogadores_vaga ">
                <div class="nome_jogador {tag}">{jogador1}</div>
                <div class="placar {tag} ">{placar1}</div>
                <div class="meio">x</div>
                <div class="nome_jogador {tag2}">{jogador2}</div>
                <div class="placar {tag2} ">{placar2}</div>
            </div>
        </div>
        
    """
    return partida


def winner_side(partida_winners):
    winners = f"""
    <div class="winner_side">
        {partida_winners}
    </div>
"""
    return winners


def loser_side(loser_winners):
    losers = f"""
    <div class="loser_side">
        {loser_winners}
    </div>
"""
    return losers


def reader_html(partidas):
    reader = f"""
<link rel="stylesheet" href="../css/estilo.css">

<script src="../js/funtion.js"></script>

<div class="color_fundo">
    <div class="img_icon">
        <img style="width: 15%;" src="https://static-cdn.jtvnw.net/jtv_user_pictures/f2a3c9cd-72f7-412d-a056-d34b52a3ff19-profile_image-300x300.png" alt="">
    </div>
</div>
<div class="center">
    {partidas}
</div>
<script>movimetation()</script>
"""
    return reader


def conjunto_partidas(partidas):
    conjunto = ""

    if partidas["winners"]:
        partidas_winner = ""
        for w in partidas["winners"]:
            nomes = separar_nome(w)

            tags = winner([w[2], w[4]], nomes)
            partidas_winner += html_partida(w[0], nomes[0], nomes[1], w[2], w[4], tags[0], tags[1])
        conjuto_winner = winner_side(partidas_winner)
        conjunto += conjuto_winner

    if partidas["losers"]:
        partidas_losers = ""
        for i in partidas["losers"]:
            nomes = separar_nome(i)
            tags = winner([i[2], i[4]], nomes)
            partidas_losers += html_partida(i[0], nomes[0], nomes[1], i[2], i[4], tags[0], tags[1])
        conjuto_losers = loser_side(partidas_losers)
        conjunto += conjuto_losers

    return conjunto


def rodape_html(dic_partidas):
    txt_html = reader_html(conjunto_partidas(dic_partidas))
    with open("modelo/rodape_paulo.html", "w", encoding="utf-8") as html:
        html.write(txt_html)


if __name__ == '__main__':
    # dic = {"winners": [["Winner 1", "João 10", "Pedro 2", "vencedor", "Derrotado"],
    #                    ["Winner 1", "TUcaadcasdas 3", "Dark 5", "derrotado", "vencedor"],
    #                    ["Winner 1", "TUcaadcasdas 3", "Dark 5", "derrotado", "vencedor"]],
    #        "losers": [["Loser 1", "João 10", "Pedro 2", "vencedor", "Derrotado"],
    #                   ["Winner 1", "TUcaadcasdas 3", "Dark 5", "derrotado", "vencedor"]]}
    #
    # dic2 = {"winners": [["Winner 1", "João 10", "Pedro 2", "vencedor", "Derrotado"]],
    #         "losers": [["Loser 1", "João 10", "Pedro 2", "vencedor", "Derrotado"]]}

    dic = get_list_last_10_match("https://www.start.gg/tournament/86-br-kumite-etapa-08-08/event/"
                           "street-fighter-v-champion-edition/brackets/1246840/1915945")
    rodape_html(dic)
    sleep(30)
    dic = get_list_last_10_match("https://www.start.gg/tournament/pogchamp-101/"
                                 "event/etapa-4-6-do-8-circuito-de-sfv/brackets/1194555/1846554")
    rodape_html(dic)
