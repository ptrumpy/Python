import csv

name = input("What is your name? ")
age = input("How old are you? ")
username = input("What would you like your username to be? ")
#print("Your name is " + name +", you are " + age + " years old, and your username is " + username)

with open('data.csv', 'x') as my_data_file:
  csv_writer = csv.writer(my_data_file,delimiter=',')
  person = [name, age, username]
  csv_writer.writerow(person)
print("One record written to " + my_data_file.name)
