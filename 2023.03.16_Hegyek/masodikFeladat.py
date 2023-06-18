napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek"]
maganhangzok = "aáeéiíoóöőuúüű"


def maganhangzokSzama(index):
    db = 0
    for betu in napok[index]:
        if betu in maganhangzok:
            db += 1
    return db


maxi = 0
for i in range(len(napok)):
    if maganhangzokSzama(i) > maganhangzokSzama(maxi):
        maxi = i

print(napok[maxi])
