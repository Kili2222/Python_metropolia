people = {"John": ["John", 30 , "Engineer"],
          "Emily": ["Emily", 25 , "Artist"],
          "Anna": ["Anna", 22 , "Student"]
          }
print(people["john"][0], people["john"][1], people["Emily"][2])
people["Anna"][2]="Teacher"
people["James"]=["James", 28 , "Writer"]
people["Sophia"]=["Sophia", 35 , "Doctor"]
del people["Emily"]
print(people)
