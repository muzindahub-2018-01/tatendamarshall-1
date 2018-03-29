import random

birthdays = {
        "Wallace Chirimuko" : "02/01/1983",
        "Steve Jobs" : "02/24/1955",
        "Albert Einstein" : "03/14/1879",
        "Nelson Mandela" : "07/18/1918",
        "Martin Luther King Jr" : "01/15/1929",
        "Fidel Castro" : "08/13/1926",
        "Abraham Lincolin" : "02/12/1809",
        "Strive Masiyiwa" : "01/29/1961",
        "Bob Marley" : "02/06/1945",
        "Donald Trump" : "06/14/1946",
        "Bill Gates" : "10/28/1955",
        "Tatenda Marshall" : "07/23/1996"}

print(" ")
print("Welcome to the birthday Dictionary Game. We know the birthdays of: ")
for name in birthdays:
  print(name)
    
    
print("Whose birthday do you want to look up? ")
name = str(input())

  
  

# birthday calculator
# import the datime module for handling dates 
import datetime

def date_calculator(birthday):
  
  birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y')
  today_date = datetime.datetime.now()
  
  if birthday.month > today_date.month:
    age = today_date.year - birthday.year - 1
    
  else:
    age = today_date.year - birthday.year
    
  return age


#current_age = date_calculator(birthdays[name])

if name in birthdays :
  current_age = date_calculator(birthdays[name]) 
  print("{}'s birthday is {}.".format(name, birthdays [name]))
  print('{} is now {}  years old'.format(name, current_age))
  
else:
    print("Sadly, we don't have {}'s birthday.".format(name))
    
   

