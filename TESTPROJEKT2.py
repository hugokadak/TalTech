# =================== algandmed =====================

import pandas as panda
import random

# ===================     algsed seadistused        =====================

koik_andmed = panda.read_csv("ViewingActivity.csv")

# Change data types
koik_andmed["Start Time"] = panda.to_datetime(koik_andmed["Start Time"], utc = True)
koik_andmed["Duration"] = panda.to_timedelta(koik_andmed["Duration"])

# Remove trailers or hooks etc...
koik_andmed = koik_andmed[koik_andmed["Supplemental Video Type"].isna()]
koik_andmed = koik_andmed[koik_andmed["Duration"] > "0 days 00:01:00"]

# Calculate show name
koik_andmed["Show Name"] = koik_andmed["Title"].str.split(":", expand=True)[0]

# tulbad: ["Profile Name", "Start Time", "Duration", "Attributes", "Title", "Supplemental Video Type", "Device Type"; "Bookmark", "Latest Bookmark", "Country"]

# Profile finder
nimedelist = koik_andmed["Profile Name"].unique()
print("Profiilideks sain: ", nimedelist)

profiilid = []
for nimi in nimedelist:
    subselection = koik_andmed[ koik_andmed["Profile Name"] == nimi ]
    profiilid.append(subselection)

print(profiilid)

# Lines of code analysed
andmepunktide_arv = koik_andmed.shape[0]
print("Analüüsisin " + str(andmepunktide_arv) + " rida ning jaotasin andmed profiilide järgi.")

# =================== profiili analüüsi kood ========================
def kestus_ilusaks_soneks(duration):
    sum_duration = str(duration).split() # '0', 'days', '01:25:41']
    paev = sum_duration[0] + " päeva, "
    hourminsec = sum_duration[2].split(":")# [01, 25, 41]
    tund = str(int(hourminsec[0])) + " tundi, "
    minut = str(int(hourminsec[1])) + " minutit ja "
    sekund = str(int(hourminsec[2])) + " sekundit."
    if sum_duration[0] == "0": #remove if 0
        paev = ""
    if int(hourminsec[0]) == 0:#remove if 0
        tund = ""
    if int(hourminsec[1]) == 0:#remove if 0
        minut = ""
    whole_string = paev + tund + minut + sekund
    return whole_string

def profiilianalyysija(profiil):
    print("Profiil:\n", profiil)#profile portrait et aru saada mis toimub
    profile_name = str(profiil["Profile Name"].iloc[0]) #uniqueifier :p
    print("Profile name", profile_name)# Profile name {name}
    kauaaegalaks = profiil["Duration"].sum() #['9', 'days', '17:21:09']
    splitter = (str(kauaaegalaks)).split() #['0', 'days', '01:38:38']
    tunnisplit = splitter[2].split(":")#['01', '38', '38']
    mituaega = str(splitter[0]) + " päeva, " + str(int(tunnisplit[0])) + " tundi, " + str(int(tunnisplit[1])) + " minutit ja " + str(int(tunnisplit[2])) + " sekundit."
    print("Profiil " + profile_name + " on vaatanud Netflixi " + str(mituaega))

    # Separator
    print("")
    print("=" * 30)
    ## Build list of show names
    all_show_names = profiil["Show Name"].unique()
    lst1 = []
    for show_name in all_show_names:
        lst2 = [] #templist sest mulle meeldib liste nestida
        ainult_need_vaatamised = profiil[ profiil["Show Name"] == show_name ] #et järgmine rida sum()-da
        sum_duration = ainult_need_vaatamised["Duration"].sum()
        lst2.append(show_name)
        lst2.append(sum_duration)
        lst1.append(lst2)# nested list
    lst1.sort(key = lambda x: x[1], reverse=True) #max to min
    printer(lst1) #output cleaned data
    
def printer(list_of_shows_sorted):
    for item in list_of_shows_sorted:
        print("Saadet:",item[0],"on vaadatud",kestus_ilusaks_soneks(item[1])) #data printer go brr
# =================== main stuffs ===================
for profiil in profiilid:
    profiilianalyysija(profiil) #analyse each profile generated
    print("Andmed edukalt väljastatud ning müüdud Meta Inc.-le.\nTulu saadud:", round(int(profiil.shape[0])*0.05, 2),"€")
