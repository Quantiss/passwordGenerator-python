# import random class to randomize output
import random
# HEre we have 3 different charts for different password rules/criteria
characterCHART1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*?'
characterCHART2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
characterCHART3 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Takes input to ask which chart it needs
chartREQ = input('''Please choose your password chart - 
(1) (A-Z) | (a-z) | (0-9) | (!@#$%&*?)
(2) (A-Z) | (a-z) | (0-9)
(3) (A-Z) | (a-z)\n INPUT:''')

# Takes input for pass length
passSIZE = input('\nPlease enter password size (3-16) - ')

# Function to clean things up and keep it organized passes the var chartREG and passSIZE
def passwordGEN (chartREQ, passSIZE):
    # Check input to see what chart we will use for our password
    if chartREQ == 1:
        #creates var password1 then joins nothing ("") with the .join call and then inside pulls random.sample which randomizes the char and
        #passes in the chart or string and then the length so how many times we want to repeat to get the full length
        password1 = "".join(random.sample(characterCHART1,passSIZE))
        # Prints the output of password1
        print(password1)

    elif chartREQ == 2:
        password2 = "".join(random.sample(characterCHART2, passSIZE))
        print(password2)

    elif chartREQ == 3:
        password3 = "".join(random.sample(characterCHART3, passSIZE))
        print(password3)

# Prints a clean output passing in the input we recieved.
print('\nGENERATED PASSWORD - ', passwordGEN(int(chartREQ), int(passSIZE)))