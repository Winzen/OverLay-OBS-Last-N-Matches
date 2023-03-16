from funtions import query_graphiql, clear_link


def pagina_txt(link_):
    query = """query{event(slug:\"""" + link_ + """\"){
  sets(
    page:1
    perPage:6
    sortType: RECENT
    filters:{
    state: 3
    
  }){
    nodes{
      fullRoundText
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
        entrant{
          participants{
            gamerTag
            prefix
            
          }
        }
      }
    }
  }
}}"""

    return query


def get_list_last_10_match(text_link):

    link_event = clear_link(text_link)
    try:
        if link_event:
            lugares = []

            query_json = query_graphiql(pagina_txt(link_event))

            lista_partidas = list()
            list_match = list()

            for partidas in query_json["data"]["event"]["sets"]["nodes"]:
                # rounds = partidas["round"]

                list_match.append(partidas["fullRoundText"])
                list_match.append(partidas["displayScore"])

                for jogadores in partidas["slots"]:
                    score = jogadores["standing"]["stats"]["score"]["value"] if jogadores["standing"] is not None else ""
                    score = score if score != -1 else "DQ"
                    score = score if score is not None else ""
                    nick = jogadores["entrant"]["participants"][0]["gamerTag"] if jogadores["entrant"] is not None else ""
                    list_match.append(score), list_match.append(nick)

                lista_partidas.append(list_match.copy())

                lugares.append(list_match.copy())

                list_match.clear()
            print(lugares)

            return lugares

    except TypeError:

        return False


# if __name__ == '__main__':
#
#     get_list_last_10_match("https://www.start.gg/tournament/86-br-kumite-etapa-08-08/event/"
#                            "street-fighter-v-champion-edition/brackets/1246840/1915945")
