
print("--Benvenuti al Manu Casinò--\n\n")
n = int(input("Quanti account vuoi registrare oggi? ")) # write number of users you want to register in your site
nickname_list = []
male_list = []
female_list = []
age_list = []

users_list = []
user = {}


for i in range(n):
    nickname = input("insert nickname number {}: ". format(i+1)).capitalize()
    if (nickname in nickname_list):
        print("nickname already used!")
        break
    nickname_list.append(nickname)
    gender = input("Are you Male or Female? Please write M or F: ").upper()
    age = int(input("How old are you?: "))
    age_list.append(age)
    user = {"Nickname" : nickname, "Gender" : gender, "Age" : age }
    users_list.append(user)
    print("Congrats user number {}, submit completed! ". format(i+1))
    if (gender == "M"):
        male_list.append(gender)
else:
    female_list.append(gender)
  
    print("How many girls are here?", len(female_list), "!")
    print("How many men are here?", len(male_list), "!")
    print("The average age of our users is: ", (sum(age_list) / len(age_list)))
    
          
   
    # print(nickname_list)
    # print(gender_list)
    # print(age_list)
    # print(user)
    # print(users_list)

  
  




