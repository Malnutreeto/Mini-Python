# terminal error managment

n = input ("inserisci un numero maggiore di 10: ")

try:
    int_n = int(n)     
    if int_n < 10:
       raise Exception ('avevo chiesto maggiore di 10, imbecille')
except ValueError as error:
  print('avevo chiesto un numero')
except Exception as ex:
  print(ex)  



