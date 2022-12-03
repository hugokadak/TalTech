from tkinter import *
from tkinter import ttk
from tkinter import font
#baas algus
aken = Tk()
aken.title("Praktikum 12")
aken.geometry("300x600")

#fondid
pealkiri_font = font.Font(family = "Consolas", name = "pealkiri", size = 12, weight = "bold")

#raam
sisu = ttk.Frame(aken, height = 280, width = 600, padding = 10, border = 5, relief = "raised")
andmed = ttk.Frame(sisu, height = 300, width = 300, padding = 10, border = 5, relief = "raised")
tingimused = ttk.Frame(sisu, height = 300, width = 300, padding = 10, border = 5, relief = "raised")

#muutujad
eesnimi = StringVar()
perenimi = StringVar()
email = StringVar()
vanus = StringVar()
sugu = StringVar()
tingimus1 = BooleanVar()
tingimus2 = BooleanVar()
tingimus3 = BooleanVar()

#sildid
sisu_silt = ttk.Label(aken, text = "Sisu")
reg_silt = ttk.Label(sisu, text = "Registreerimisvorm", font = pealkiri_font)
eesnimi_silt = ttk.Label(andmed, text = "Eesnimi")
perenimi_silt = ttk.Label(andmed, text = "Perenimi")
email_silt = ttk.Label(andmed, text = "E-post")
vanus_silt = ttk.Label(andmed, text = "Vanus")
sugu_silt = ttk.Label(andmed, text = "Sugu")
tingimused_silt = ttk.Label(tingimused, text = "Tingimused", font = pealkiri_font)

#andmeväljad
eesnimi_vali = ttk.Entry(andmed, textvariable = eesnimi)
perenimi_vali = ttk.Entry(andmed, textvariable = perenimi)
email_vali = ttk.Entry(andmed, textvariable = email)
vanus_vali = ttk.Entry(andmed, textvariable = vanus)

#raadionupud soo jaoks
mees = ttk.Radiobutton(andmed, text = "Mees", variable = sugu, value = "mees")
naine = ttk.Radiobutton(andmed, text = "Naine", variable = sugu, value = "naine")

#check butonid
tingimus1_check = ttk.Checkbutton(tingimused, text="Üldtingimused", variable = tingimus1, onvalue = True)
tingimus2_check = ttk.Checkbutton(tingimused, text="Kliendiandmete töötlemis kord", variable = tingimus2, onvalue = True)
tingimus3_check = ttk.Checkbutton(tingimused, text="Küpsiste kasutamine", variable = tingimus3, onvalue = True)


def saadataotlus():
    eesnimis6ne = eesnimi.get()
    perenimis6ne = perenimi.get()
    emails6ne = email.get()
    vanusnr = vanus.get()
    sugus6ne = sugu.get()
    t1 = tingimus1.get()
    t2 = tingimus2.get()
    t3 = tingimus3.get()
    try:
        uusklient = {"eesnimi": "{eesnimi}", "perenimi": "{perenimi}", "email": "{email}", "vanus": "{vanus}", "sugu": "{sugu}", "tingimus_1": "{tingimus1}", "tingimus_2": "{tingimus2}", "tingimus_3": "{tingimus3}"}
        #emaili section
        d = len(emails6ne)
       # e = d.split("@")
    #except ((int(vanusnr) < 0) and (int(vanusnr) > 120)):
    #    print("Vanus on vigane.")
    #except (t1 != True) and (t2 != True) and (t3 != True):
    #    print("Kõikide tingimustega ei ole nõustutud!")
    except sugus6ne == "":
        print("Sugu ei ole valitud!")
    except (len(e[1] < 2) or (e.find(".") != -1) or (e.find(" ") != -1)):
        print("E-mail ei vasta nõuetele.")
    except (e.find(".") != -1):
        print("E-mail ei vasta nõuetele.")
    except (e.find(" ") != -1):
        print("E-mail ei vasta nõuetele.")
    except ((taht.isdigit() for taht in eesnimis6ne) == True):
        print("Eesnimi ei tohi sisaldada numbrit (veel).")
    except ((taht.isdigit() for taht in perenimis6ne == True)):
        print("Perenimi ei tohi sisaldada numbrit (veel).")
    except:
        print("Mingi viga.")
    print(uusklient)

def tyhistataotlus():
    poolik_taotlus = {"eesnimi": "{eesnimi}", "perenimi": "{perenimi}", "email": "{email}", "vanus": "{vanus}", "sugu": "{sugu}", "tingimus_1": "{tingimus1}", "tingimus_2": "{tingimus2}", "tingimus_3": "{tingimus3}"}
    print(poolik_taotlus)
#nupud
saada_nupp = ttk.Button(sisu, text = "Saada", command = saadataotlus())
tyhista_nupp = ttk.Button(sisu, text = "Tühista", command = tyhistataotlus())

#grid
sisu.grid(column = 0, row = 0, columnspan = 2)
andmed.grid(column = 0, row = 1, columnspan = 2, padx = 20, pady = 20)
tingimused.grid(column = 0, row = 2, columnspan = 2, padx = 20, pady = 20)
reg_silt.grid(column = 0, row = 0, columnspan = 2, padx = 20, pady = 20)
saada_nupp.grid(column = 0, row = 3)
tyhista_nupp.grid(column = 1, row = 3)

#andmete silt grid
eesnimi_silt.grid(column = 0, row = 0, padx = 5, pady = 5)
perenimi_silt.grid(column = 0, row = 1, padx = 5, pady = 5)
email_silt.grid(column = 0, row = 2, padx = 5, pady = 5)
vanus_silt.grid(column = 0, row = 3, padx = 5, pady = 5)
sugu_silt.grid(column = 0, row = 4, rowspan = 2, padx = 5, pady = 5)

#andmete väli grid
eesnimi_vali.grid(column = 1, row = 0)
perenimi_vali.grid(column = 1, row = 1)
email_vali.grid(column = 1, row = 2)
vanus_vali.grid(column = 1, row = 3)
mees.grid(column = 1, row = 4, sticky = W)
naine.grid(column = 1, row = 5, sticky = W)

#tingimuste grid
tingimused_silt.grid(column = 0, row = 0, padx = 10, pady = 10)
tingimus1_check.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = W)
tingimus2_check.grid(column = 0, row = 2, padx = 5, pady = 5, sticky = W)
tingimus3_check.grid(column = 0, row = 3, padx = 5, pady = 5, sticky = W)

aken.mainloop()