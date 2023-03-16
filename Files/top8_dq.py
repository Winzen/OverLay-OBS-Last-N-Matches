from funtions import query_graphiql, clear_link
from query_id_top8 import get_id_top8


def pagina_txt(link_, phasegroupids):
    query = """query{event(slug: \"""" + link_ + """\"){
 
  sets(
    page: 1
    perPage: 100
    filters:{
      phaseGroupIds: """ + str(phasegroupids) + """
    })
  {
    nodes{
      round
      displayScore
      slots{
        standing{
          stats{
            score {
              value
            }
          }
        }
        entrant {
          participants{
              gamerTag
            }
          }
        }
    }       
  }           
}
}"""

    return query


def get_list_top8(text_link, top16=False):

    link_event = clear_link(text_link)
    try:
        if link_event:
            lugares = {}
            id_fases = get_id_top8(link_event, top16)

            query_json = query_graphiql(pagina_txt(link_event, id_fases))

            lista_partidas = list()
            list_match = list()

            for partidas in query_json["data"]["event"]["sets"]["nodes"]:
                rounds = partidas["round"]
                displayscores = partidas["displayScore"]
                list_match.append(displayscores)

                for jogadores in partidas["slots"]:
                    score = jogadores["standing"]["stats"]["score"]["value"] if jogadores["standing"] is not None else ""
                    score = score if score != -1 else "DQ"
                    score = score if score is not None else ""
                    nick = jogadores["entrant"]["participants"][0]["gamerTag"] if jogadores["entrant"] is not None else ""
                    list_match.append(score), list_match.append(nick)

                lista_partidas.append(list_match.copy())

                try:
                    lugares[rounds].append(list_match.copy())

                except KeyError:

                    lugares[rounds] = [list_match.copy()]

                list_match.clear()

            return lugares

    except TypeError:

        return False

