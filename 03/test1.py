print("odpovídej ano nebo ne.")

umim_retezec = input("Umíš programovat?")
if umim_retezec == "ano" or umim_retezec == "Ano" :
    umim = True
elif umim_retezec == "ne" or umim_retezec == "Ne":
     umim = False
else :
        print("nerozumím")

neumím_retezec = input("umíš matematiku?")
if neumím_retezec == "ano" or neumím_retezec == "Ano" :
    neumim = True
elif neumím_retezec == "ne" or neumím_retezec == "Ne" :
    neumím = False
else :
  print("nerozumím")

if umim and neumím :
    print("Gratuluji<3")

elif umim :
    print("Super:)")

elif neumím : 
    print("No tak se běž učit:D")

else :
    print("máš co dohánět!")
