#importing the used functions 
import random as rd
import string as st 

class RandomPassword():
    def generate(self):
        # inputing the number of characters the user will enter
        chra = int(input("Enter number of characters: "))
        x = input("Do you want letters included? (yes/no): ").lower()
        
        y=0
        
        while y < chra:
        
            #condtion if i need chracters and numbers in my password
            if x == "yes":
                print(rd.choice([rd.choice(st.ascii_lowercase), rd.randint(0, 9)]), end=" ")
            
            #condition if i need just nymbers in my password
            else:
                number = rd.randint(0, 9)
                print(number, end=" ")
 
            y += 1
            
# create object + call method
rp = RandomPassword()
rp.generate()
    
     


