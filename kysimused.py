print("Mis on su nimi?")
nimi=input() # =Argo
print("Tere, "+nimi) # Tere, Argo

print("Mis on su perekonnanimi?")

perenimi = input()

print("Sinu täisnimi on: " + nimi + " " + perenimi)


vanus = input("Kui vana sa oled?  ")
bot_vanus = 100
vahe = bot_vanus - int(vanus) # int() loob tekstist numbritüübi - vajalik matem. teheteks
print("Sa oled minust " + str(vahe) + " aastat noorem") # str() loob numbrist teksti tüübi - vajalik tekstide kokku kleepimiseks