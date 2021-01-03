import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
# Function to add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 
  
# Function to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divide(num1, num2): 
    return num1 / num2 
  
print("Wybierz działanie, które chcesz wykonać: \n" 
        "1. Dodawanie\n" 
        "2. Odejmowanie\n" 
        "3. Mnożenie\n" 
        "4. Dzielenie\n") 
  
  
# Take input from the user  
select = int(input("Podaj działania, posługując się odpowiednią liczbą: 1, 2, 3, 4 :")) 
  
number_1 = float(input("Wprowadź pierwszą liczbę: ")) 
number_2 = float(input("Wprowadź drugą liczbę: ")) 
  
if select == 1: 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == 2: 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == 3: 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == 4: 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Niepoprawna wartość")

if __name__ == "__main__":
    logging.debug("Nowe obliczenie")
    logging.debug("Wybrane dzialanie to %s" % select)
    logging.debug("Pierwszy parametr to %s" % number_1)
    logging.debug("Drugi parametr to %s" % number_2)