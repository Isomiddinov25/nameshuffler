import os 
os.system("cls")

# 1Name Shuffler


def name_shuffler(str_):

    name_parts = str_.split()
    
 
    if len(name_parts) != 2:
        return "isim familiya kiriting"
    
  
    firstname, lastname = name_parts
    swapped_name = f"{lastname} {firstname}"
    
    return swapped_name


full_name = "isomiddinov isfandiyor"
print(name_shuffler(full_name)) 
