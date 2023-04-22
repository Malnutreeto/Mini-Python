# creo programma che richieda un numero indefinito di parole, per consentire l'analisi del programma, inserire la parola "stop"

i = True
phrase = []
#inseriamo le info che ci servono per il problema sotto forma di simboli in una lista
comma = ","
marks = [".", "!", "?"]

while (i):
  word = input("insert word: ")
  if (word == "stop"):
      print("end")
      break
  phrase.append(word)

# oppure senza i = True

#   while word != "stop":
#      phrase.append(word)
#      word = input("another word: ")

#phrase precompilata
#phrase = ["ciao", ",", "sono", "manu", ".", "tu", "come", "ti", "chiami", "?", "manu"]
#creo altri contenitori, uno per frase singola e l'altro a lista che conterrà le frasi finite
sentence = ""
joint = []

for element in phrase:
   if element in marks:
      #se l'elemento (word) in phrase c'è anche in marks[...] cancello gli spazi prima e dopo il carattere
      sentence = sentence.strip()
      #rimpiazzo l'indice 0 di sentence (che è l'elemento) trasformandolo in upper, 1 sola volta, altrimenti mi uppera tutti gli elementi uguali allo 0
      sentence = sentence.replace(sentence[0], sentence[0].upper(), 1)
      #appendo sentence in joint assieme all'element, il + concatena senza spazi
      joint.append(sentence + element)
      #svuoto sentence alla fine logica di una frase (!, ., o ?) per iniziarne una nuova
      sentence = ""

   elif element == comma:
      #comma ha un ragionamento diverso in quanto non ha uno spazio prima, quindi se l'element è una virgola aggiungi a sentence la virgola senza spazio
      sentence += comma
   else:
      #altrimenti aggiungiamo a sentence spazio + element
      sentence += " " + element

# con queste altre 3 righe dico che le frasi possono anche finire senza un mark
sentence = sentence.strip()  
sentence = sentence.replace(sentence[0], sentence[0].upper(), 1)
joint.append(sentence)  
     

full_phrase = "\n".join(joint)

     #print sentence
print(full_phrase)

clean_words = []
for c in phrase:
   if c not in marks and c != comma:
      clean_words.append(c)

#questo for potrebbe essere riassunto in una riga con la list comprehension seguente:
# clean_words = [c for c in phrase if c not in marks and c != comma], oppure:
# clean_words = [word for word in phrase if word not in marks and c != comma]
#SENZA FARE APPEND()

print ("number of joined words: ", len(clean_words))
print ("number of marks: ", len(phrase) - len(clean_words))
print ("sentences are: ", len(joint))

letters_dict = {}
# ad ogni ciclo uso un contatore con lettera diversa, di fatto ora x rappresenta il carattere
for x in full_phrase:
   # se il carattere non è ne un new line ne uno spazio 
   if x not in ["\n", " "]:
   # aggiungiamo una nuova voce al dict, in caso già fosse contata la key aumentiamo il valore value
      if x in letters_dict:
         letters_dict[x] += 1
   # altrimenti creiamo una key:value nuova
      else:
         letters_dict[x] = 1

print ("our dictionary has: ", letters_dict)

# estrapolo le valutazioni minime e massime di comparsa caratteri
max_char_count = max(letters_dict.values())
min_char_count = min(letters_dict.values())

print ("max char is: ", max_char_count)
print ("min char is: ", min_char_count)

# creo liste vuote per inserire solo le keys corrispondenti a max e min
max_chars =[]
min_chars =[]

# k= keys, v = values
for k, v in letters_dict.items():
   if v == max_char_count:
      max_chars.append(k)
   if v == min_char_count:
      min_chars.append(k)

print ("max ({}) char is/are: ". format(max_char_count), " ".join(max_chars))
print ("min ({}) char is/are: ". format(min_char_count), " ".join(min_chars))









   



