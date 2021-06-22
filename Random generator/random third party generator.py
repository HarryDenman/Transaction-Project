#https://github.com/smashew/NameDatabases/commit/4a714a09ed69147c373d9b9f2bce20ef79a63381
#github of public list of names
#last name list contained some email addresses, 
#numbers, commas and some fragments of sentences, manually removed from
#the text file by searching for @, variation, 1-9, ',' ' ', '(' and deleting
#some double line breaks leading to some probablility of returning an emtpy last name
#double lines removed by copy and pasting into word and replacing ^p^p with ^p

#create title list
title_list = ["", "Mr", "Mrs"]

#load lists from file
#create first name list
firstnames = open("NameDatabases-master/NamesDatabases/first names/all.txt","r") 
fname_list = firstnames.readlines()
#create last name list
lastnames = open("NameDatabases-master/NamesDatabases/surnames/all.txt","r") 
lname_list = lastnames.readlines()
# import random module for random generation
import random


#randomly choose variables for each list
n_title = random.randint(0, len(title_list) - 1)
n_fname = random.randint(0, len(fname_list) - 1)
n_lname = random.randint(0, len(lname_list) - 1)   

#generate name from variables
#string slicing by -1 needed to remove newline character from loaded first name and last name files
random_name = title_list[n_title] + " " + fname_list[n_fname][:-1] + " " + lname_list[n_lname][:-1]
print(random_name)
#sometimes names are used always without title in transaction descriptions, same name always without title also generated
random_name_no_title = fname_list[n_fname][:-1] + " " + lname_list[n_lname][:-1]
print(random_name_no_title)

#some transactions have a receipt number which is a random six digit number
#randomize a random integer between 0 and 999,999, convert to string for compatibility with later operations
receipt_number_integer = str(random.randint(0, 999999))
#format to be six digits long always
receipt_number = '{:0>6}'.format(receipt_number_integer)
#same concept for account number and bsb; bsb is six digits long, account number is 9 digits long
bsb_number_integer = str(random.randint(0, 999999))
bsb_number = '{:0>6}'.format(bsb_number_integer)
account_number_integer = str(random.randint(0, 999999999))
account_number = '{:0>9}'.format(account_number_integer)

#third party transfers appear as multiple different types
transfertype = random.randint(1,4)
if transfertype == 1:
    #transfers of type 1 follow the format Transfer to [name] - Receipt [n] To [n] [n]  - Transfer to [name] - 
    #Receipt [n] To [n] [n]
    #generate receipt string portion
    receipt = " - Receipt " + receipt_number + " To " + bsb_number + " " + account_number
    #generate transaction description string
    transaction_string = (  "Transfer to " + random_name_no_title + receipt + " - Transfer to " + 
                            random_name_no_title + receipt )
    print(transaction_string)
elif transfertype == 2:
    #transfers of type 2 follow the format [name] - Osko Payment to [n] [n] - Receipt [n]
    transaction_string = ( random_name_no_title + "- Osko Payment to " + bsb_number + " " + 
                            account_number + " - Receipt " + receipt_number)
    print(transaction_string)
elif transfertype == 3:
    #transfers of type 3 follow the format [name] - Transfer to [n] [n] - Receipt [n]
    transaction_string = ( random_name_no_title + " - Transfer to " + bsb_number + " " +
                            account_number + " - Receipt " + receipt_number)
    print(transaction_string)
elif transfertype == 4:
    #transfers of type 4 follow the format [name] - Transfer to [name] - Receipt [n] To [n] [n]
    transaction_string = ( random_name_no_title + " - Transfer to " + random_name_no_title +
                            " - Receipt " + receipt_number + " To " + bsb_number + " " + account_number)
    print(transaction_string)