# =================== algandmed =====================

import pandas as panda
import csv

profile1 = []
profile2 = []
profile3 = []
profile4 = []
profile5 = []

# ===================     algsed seadistused        =====================

with open("ViewingActivity.csv", newline = "") as d: #avan faili
    a = csv.reader(d)
    andmekogum = list(a)
    andmekogum.remove(andmekogum[0]) #eemaldada siis kõige esimene rida "prof name" "title"
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

# ===================neljanda profiili analüüsi kood ===================
def profiilianalyysija(profiil):
    profiil[1] = panda.to_datetime(profiil[1], utc = True)
    profiil[2] = panda.to_timedelta(profiil[2])
    kauaaegalaks = profiil[2].sum()
    splitter = (str(kauaaegalaks)).split()
    tunnisplit = splitter[2].split(":")
    mituaega = str(splitter[0]) + " päeva, " + str(int(tunnisplit[0])) + " tundi, " + str(int(tunnisplit[1])) + " minutit ja " + str(int(tunnisplit[2])) + " sekundit."
    print("Profiil " + str(profiil[0][0]) + " on vaatanud Netflixi " + str(mituaega))
    print("")
    print("=" * 30)
    uuslst = []
    for j in range(0, len(profiil)):
        d = profiil[4].str.split(":")# teeb paksu nimekirja saadetest
        uuslst.append(d[j][0]) # list
        j += 1
    uuslst = list(dict.fromkeys(uuslst)) # tee dict et duplikaadid eemaldada, tagasi listiks

    listnew = []
    for i in range(0, len(uuslst)):
        templist = [] # tulevikuks list of list lihtsam sorteerida
        film = profiil[profiil[4].str.contains(uuslst[i], regex = False)]
        a = film.sum()
        n = str(a[2]).split() #['0', 'days', '01:38:38']
        m = n[2].split(":")#['01', '38', '38']
        templist.append(uuslst[i])
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
        #fail05.write(str(listnew[i][0])+" vaatasite " + paev + tund + minut + str(int(d[3])) + " sekundit.")
    print("")
    print("=" * 30)
# =================== main stuffs ===================
avoidrepetition = [pandaprof1, pandaprof2, pandaprof3, pandaprof4, pandaprof5]
for profiil in avoidrepetition:
    profiilianalyysija(profiil)