# =================== algandmed =====================
import pandas as panda
import csv

profile1 = []
profile2 = []
profile3 = []
profile4 = []
profile5 = []

with open("ViewingActivity.csv", newline = "") as d: #avan faili
    a = csv.reader(d)
    andmekogum = list(a)
andmekogum.remove(andmekogum[0]) #eemaldada siis kõige esimene rida "prof name" "title"
# =================== algandmed =====================
# === teen siia väiksed txt failid andmetega ===

fail01 = open("profiil1andmed.txt", "w+")
fail02 = open("profiil2andmed.txt", "w+")
fail03 = open("profiil3andmed.txt", "w+")
fail04 = open("profiil4andmed.txt", "w+")
fail05 = open("profiil5andmed.txt", "w+")

# ==============================================

# =================== algsed seadistused =====================
nimedelist = []
for j in range(0, len(andmekogum)):
    nimi = andmekogum[j][0]
    nimedelist.append(nimi)
    j += 1
nimedelist = list(dict.fromkeys(nimedelist)) #siin on nimed stringideks muudetud, et oleks lihtsam teisi viewingactivity faile kasutada
print("Profiilideks sain: " + str(nimedelist))
for j in range(0, len(andmekogum)):
    if andmekogum[j][0] == nimedelist[0]:
        profile1.append(andmekogum[j]) # esimese profiili list
        j += 1
    elif andmekogum[j][0] == nimedelist[1]:
        profile2.append(andmekogum[j])# teise profiili list
        j += 1
    elif andmekogum[j][0] == nimedelist[2]:
        profile3.append(andmekogum[j])# - . . -
        j += 1
    elif andmekogum[j][0] == nimedelist[3]:
        profile4.append(andmekogum[j])# - . . -
        j += 1
    else:
        profile5.append(andmekogum[j])# - . . -
        j += 1
print("Analüüsisin " + str(len(andmekogum)) + " rida ning jaotasin andmed profiilide järgi.") # tahtsin cool output teha aga ka teada
print("Profiili listid tehtud.")                                                              # kui kaugel olen

pandaprof1 = panda.DataFrame(profile1)
pandaprof2 = panda.DataFrame(profile2)
pandaprof3 = panda.DataFrame(profile3) # muudan tagasi panda jaoks mugavaks, et duration lihtsam arvutada oleks
pandaprof4 = panda.DataFrame(profile4)
pandaprof5 = panda.DataFrame(profile5)

# ===================     algsed seadistused        =====================

# =================== esimese profiili analüüsi kood ===================

pandaprof1[1] = panda.to_datetime(pandaprof1[1], utc = True) # et pandale oleks ajaframe selge
pandaprof1[2] = panda.to_timedelta(pandaprof1[2])# duration aega saaks paremini liita
kauaaegalaks1 = pandaprof1[2].sum() # 2 days 01:27:17
splitter1 = (str(kauaaegalaks1)).split() # ['25', 'days', '01:02:26'], saaksin päeva arvu jn käppa
tunnisplit1 = splitter1[2].split(":") #['01', '02', '26']
mituaega1 = str(splitter1[0]) + " päeva, " + str(int(tunnisplit1[0])) + " tundi, " + str(int(tunnisplit1[1])) + " minutit ja " + str(int(tunnisplit1[2])) + " sekundit."
print("Profiil " + str(pandaprof1[0][0]) + " on vaatanud Netflixi " + mituaega1)
print("")
print("=" * 30)
uus001 = []
for j in range(0, len(pandaprof1)):
    d = pandaprof1[4].str.split(":")# teeb paksu nimekirja saadetest
    uus001.append(d[j][0]) # list
uus001 = list(dict.fromkeys(uus001)) # tee dict et duplikaadid eemaldada, tagasi listiks

listnew01 = []
for i in range(0, len(uus001)):
    templist = [] # tulevikuks list of list lihtsam sorteerida
    film = pandaprof1[pandaprof1[4].str.contains(uus001[i], regex = False)]
    a = film.sum()
    n = str(a[2]).split() #['0', 'days', '01:38:38']
    m = n[2].split(":")#['01', '38', '38']
    templist.append(uus001[i])
    templist.append(n[0] + ":" + str(n[2]))
    listnew01.append(templist)
listnew01.sort(key = lambda x: x[1], reverse=True) #sorteeri pikkuse järjekorda, max to min
for i in range(0, len(listnew01)): #loe jälle nimekiri läbi
    d = listnew01[i][1].split(":")
    paev = d[0] + " päeva, "
    tund = str(int(d[1])) + " tundi, " # tegin sellised muutujad et 0 korral ei kirjutaks välja "0 päeva" või "0 tundi"
    minut = str(int(d[2])) + " minutit ja "
    if d[0] == "0":
        paev = ""
    if int(d[1]) == 0:
        tund = ""
    if int(d[2]) == 0:
        minut = ""
    print(str(listnew01[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.") #output ilusam nii
    fail01.write(str(listnew01[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
print("")
print("=" * 30)
print("")
print("")
print("")
# =================== esimese profiili analüüsi kood ==================

# ===================  teise profiili analüüsi kood  ===================


pandaprof2[1] = panda.to_datetime(pandaprof2[1], utc = True)
pandaprof2[2] = panda.to_timedelta(pandaprof2[2])
kauaaegalaks2 = pandaprof2[2].sum() 
splitter2 = (str(kauaaegalaks2)).split()
tunnisplit2 = splitter2[2].split(":")
mituaega2 = str(splitter2[0]) + " päeva, " + str(int(tunnisplit2[0])) + " tundi, " + str(int(tunnisplit2[1])) + " minutit ja " + str(int(tunnisplit2[2])) + " sekundit."
print("Profiil " + str(pandaprof2[0][0]) + " on vaatanud Netflixi " + mituaega2)
print("")
print("=" * 30)
uus002 = []
for j in range(0, len(pandaprof2)):
    d = pandaprof2[4].str.split(":")
    uus002.append(d[j][0])
uus002 = list(dict.fromkeys(uus002))

listnew02 = []
for i in range(0, len(uus002)):
    templist = []
    film = pandaprof2[pandaprof2[4].str.contains(uus002[i], regex = False)]
    a = film.sum()
    n = str(a[2]).split()
    m = n[2].split(":")
    templist.append(uus002[i])
    templist.append(n[0] + ":" + str(n[2]))
    listnew02.append(templist)
listnew02.sort(key = lambda x: x[1], reverse=True)

for i in range(0, len(listnew02)):
    d = listnew02[i][1].split(":")
    paev = d[0] + " päeva, "
    tund = str(int(d[1])) + " tundi, "
    minut = str(int(d[2])) + " minutit ja "
    if d[0] == "0":
        paev = ""
    if int(d[1]) == 0:
        tund = ""
    if int(d[2]) == 0:
        minut = ""
    print(str(listnew02[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
    fail02.write(str(listnew02[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
print("")
print("=" * 30)
print("")
print("")
print("")

# ===================  teise profiili analüüsi kood  ===================

# ===================kolmanda profiili analüüsi kood ===================

pandaprof3[1] = panda.to_datetime(pandaprof3[1], utc = True)
pandaprof3[2] = panda.to_timedelta(pandaprof3[2])
kauaaegalaks3 = pandaprof3[2].sum() 
splitter3 = (str(kauaaegalaks3)).split()
tunnisplit3 = splitter2[2].split(":")
mituaega3 = str(splitter3[0]) + " päeva, " + str(int(tunnisplit3[0])) + " tundi, " + str(int(tunnisplit3[1])) + " minutit ja " + str(int(tunnisplit3[2])) + " sekundit."
print("Profiil " + str(pandaprof3[0][0]) + " on vaatanud Netflixi " + mituaega3)
print("")
print("=" * 30)
uus003 = []
for j in range(0, len(pandaprof3)):
    d = pandaprof3[4].str.split(":")
    uus003.append(d[j][0])
uus003 = list(dict.fromkeys(uus003))

listnew03 = []
for i in range(0, len(uus003)):
    templist = []
    film = pandaprof3[pandaprof3[4].str.contains(uus003[i], regex = False)]
    a = film.sum()
    n = str(a[2]).split()
    m = n[2].split(":")
    templist.append(uus003[i])
    templist.append(n[0] + ":" + str(n[2]))
    listnew03.append(templist)
listnew03.sort(key = lambda x: x[1], reverse=True)

for i in range(0, len(listnew03)):
    d = listnew03[i][1].split(":")
    paev = d[0] + " päeva, "
    tund = str(int(d[1])) + " tundi, "
    minut = str(int(d[2])) + " minutit ja "
    if d[0] == "0":
        paev = ""
    if int(d[1]) == 0:
        tund = ""
    if int(d[2]) == 0:
        minut = ""
    print(str(listnew03[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
    fail03.write(str(listnew03[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
print("")
print("=" * 30)
print("")
print("")
print("")

# ===================kolmanda profiili analüüsi kood ===================

# ===================neljanda profiili analüüsi kood ===================

pandaprof4[1] = panda.to_datetime(pandaprof4[1], utc = True)
pandaprof4[2] = panda.to_timedelta(pandaprof4[2])
kauaaegalaks4 = pandaprof4[2].sum() 
splitter4 = (str(kauaaegalaks4)).split()
tunnisplit4 = splitter4[2].split(":")
mituaega4 = str(splitter4[0]) + " päeva, " + str(int(tunnisplit4[0])) + " tundi, " + str(int(tunnisplit4[1])) + " minutit ja " + str(int(tunnisplit4[2])) + " sekundit."
print("Profiil " + str(pandaprof4[0][0]) + " on vaatanud Netflixi " + mituaega4)
print("")
print("=" * 30)
uus004 = []
for j in range(0, len(pandaprof4)):
    d = pandaprof4[4].str.split(":")
    uus004.append(d[j][0])
uus004 = list(dict.fromkeys(uus004))

listnew04 = []
for i in range(0, len(uus004)):
    templist = []
    film = pandaprof4[pandaprof4[4].str.contains(uus004[i], regex = False)]
    a = film.sum()
    n = str(a[2]).split()
    m = n[2].split(":")
    templist.append(uus004[i])
    templist.append(n[0] + ":" + str(n[2]))
    listnew04.append(templist)
listnew04.sort(key = lambda x: x[1], reverse=True)

for i in range(0, len(listnew04)):
    d = listnew04[i][1].split(":")
    paev = d[0] + " päeva, "
    tund = str(int(d[1])) + " tundi, "
    minut = str(int(d[2])) + " minutit ja "
    if d[0] == "0":
        paev = ""
    if int(d[1]) == 0:
        tund = ""
    if int(d[2]) == 0:
        minut = ""
    print(str(listnew04[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
    fail04.write(str(listnew04[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
print("")
print("=" * 30)
print("")
print("")
print("")

# ===================neljanda profiili analüüsi kood ===================

# =================== viienda profiili analüüsi kood ===================

pandaprof5[1] = panda.to_datetime(pandaprof5[1], utc = True)
pandaprof5[2] = panda.to_timedelta(pandaprof5[2])
kauaaegalaks5 = pandaprof5[2].sum()
splitter5 = (str(kauaaegalaks5)).split()
tunnisplit5 = splitter5[2].split(":")
mituaega5 = str(splitter5[0]) + " päeva, " + str(int(tunnisplit5[0])) + " tundi, " + str(int(tunnisplit5[1])) + " minutit ja " + str(int(tunnisplit5[2])) + " sekundit."
print("Profiil " + str(pandaprof5[0][0]) + " on vaatanud Netflixi " + str(kauaaegalaks5))
print("")
print("=" * 30)
uus3 = []
for j in range(0, len(pandaprof5)):
    d = pandaprof5[4].str.split(":")# teeb paksu nimekirja saadetest
    uus3.append(d[j][0]) # list
    j += 1
uus3 = list(dict.fromkeys(uus3)) # tee dict et duplikaadid eemaldada, tagasi listiks

listnew = []
for i in range(0, len(uus3)):
    templist = [] # tulevikuks list of list lihtsam sorteerida
    film = pandaprof5[pandaprof5[4].str.contains(uus3[i], regex = False)]
    a = film.sum()
    n = str(a[2]).split() #['0', 'days', '01:38:38']
    m = n[2].split(":")#['01', '38', '38']
    templist.append(uus3[i])
    templist.append(n[0] + ":" + str(n[2]))
    listnew.append(templist)
listnew.sort(key = lambda x: x[1], reverse=True) #sorteeri pikkuse järjekorda, max to min

for i in range(0, len(listnew)): #loe jälle nimekiri läbi
    d = listnew[i][1].split(":")
    paev = d[0] + " päeva, "
    tund = str(int(d[1])) + " tundi, " # tegin sellised muutujad et 0 korral ei kirjutaks välja "0 päeva" või "0 tundi"
    minut = str(int(d[2])) + " minutit ja "
    if d[0] == "0":
        paev = ""
    if int(d[1]) == 0:
        tund = ""
    if int(d[2]) == 0:
        minut = ""
    print(str(listnew[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.") #output ilusam nii
    fail05.write(str(listnew[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
print("")
print("=" * 30)

# =================== viienda profiili analüüsi kood ===================

fail01.close()
fail02.close()
fail03.close()
fail04.close()
fail05.close()