import ast


def ler():
    with open("config/config.txt", "r", encoding="utf-8") as txt_json:

        txt = ast.literal_eval(txt_json.read())

        return txt


def escrever(sleep=0, placares=0):
    configs = ler()
    try:
        if sleep and 60000 >= int(sleep) >= 30000:
            configs["sleep"] = int(sleep)
        if placares and 30000 >= int(placares) >= 1000:
            configs["placares"] = int(placares)

        with open("config/config.txt", "w", encoding="utf-8") as txt_json:
            txt_json.write(str(configs))

            return configs
    except ValueError:
        configs["sleep"] = "Error"
        configs["placares"] = "Error"
        return configs


