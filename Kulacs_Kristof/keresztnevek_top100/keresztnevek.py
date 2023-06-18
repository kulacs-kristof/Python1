# készítsünk k_nevek.txt néven szöveges állományt amely a 100 legnépszerűbb nevet tartalmazza
# készítsünk függvényt amely a paraméterével átadott string magánhangzóinak számát határozza meg
# határozzuk meg a legtöbb magánhangzót tartalmazó keresztnév indexét és nevét (holtverseny esetén mindet írjuk ki)
# készíts függvényt amely igaz értékkel tér vissza ha a paraméterével átadott srting első és utolsó karaktere a kis és nagy karakterek figyelembevétele nélkül
# határozzuk meg azt a legrövidebb nevet melynek első és utolsó karaktere megegyezik (holtverseny esetén mindet írjuk ki)


def maganhangzo_torles(s):
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    massalhangzos_s = ""
    for k in s:
        if k not in maganhangzok:
            massalhangzos_s += k
    return massalhangzos_s


print(maganhangzo_torles("informatika") == "nfrmtk")
print(maganhangzo_torles("aábeéiífoóöőujúüűpAÁEÉIÍOÓÖŐUÚÜŰs") == "bfjps")
