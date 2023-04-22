# user analysis

# Creare un programma che stampi tutte le mail degli utenti nel file `data/01_data.json`.



import json


with open('01_data.json', 'r') as f:
    user_list = json.load(f)

#d = dictionary
    for d in user_list:
      print(d['email']) 
      
        
    for d in user_list:
       if (d['email']=="hollandoliver@electonic.com"):
          print("The user named", d["name"], "has got", len(d["friends"]), "firends")


#stampare numero di amici per ogni utente:
# 

for d in user_list:
   print(d["name"], "has got", len(d["friends"]), "firends" )        