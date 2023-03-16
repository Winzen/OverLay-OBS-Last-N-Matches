import requests as link
import json


def clear_link(text_link):

    """Tenta limpar um link passado para conseguir um evento do Start.gg"""

    try:
        link_event = (text_link.split("/"))
        index = link_event.index("tournament")

        if len(link_event) > 6 or str(link_event[0]).lower() == "tournament" and len(link_event) > 3:
            link_event = "/".join(link_event[index:index + 4])
            return link_event
        else:
            raise ValueError
    except ValueError:
        return False


def query_graphiql(query):
    """Retorna um objeto JSON de uma query para o Start.gg"""

    pedido = link.post(
        "https://www.start.gg/api/-/gql",
        headers={
            "client-version": "20",
            'Content-Type': 'application/json'
        },
        json={
            "query": query
        }
    )
    query_json = json.loads(pedido.text)
    return query_json


def winner(valores, names):

    resultados = ["nome", "nome", "nome round"]

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


def long_name(names):

    resultados = ["nome", "nome", "nome round"]

    for n, nome in enumerate(names):

        if len(nome) >= 9:
            resultados[n] += " long_name"

    return resultados


def clear_none(slot):
    for v, n_ in enumerate(slot):
        if n_ is None:
            slot[v] = ""
    if slot[1] == "" and len(slot[2]) > 0:
        slot[1] = 0
    if slot[3] == "" and len(slot[4]) > 0:
        slot[3] = 0

    return slot


def separar_nome(nome):

    f = nome[1]
    if f.lower() == "dq":
        h = [nome[3], nome[5]]
    else:
        h = f.split(" - ")
        h[0] = h[0][:len(h[0]) - 1].strip()
        h[1] = h[1][:len(h[1]) - 1].strip()
    return h

