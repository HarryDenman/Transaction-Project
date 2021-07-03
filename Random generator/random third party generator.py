#https://github.com/smashew/NameDatabases/commit/4a714a09ed69147c373d9b9f2bce20ef79a63381
#github of public list of names
#last name list contained some email addresses, 
#numbers, commas and some fragments of sentences, manually removed from
#the text file by searching for @, variation, 1-9, ',' ' ', '(' and deleting
#some double line breaks leading to some probablility of returning an emtpy last name
#double lines removed by copy and pasting into word and replacing ^p^p with ^p


#todo: make this into a function callable from different files
#also add optional name variables to the function

#create title list
title_list = ["", "Mr", "Mrs"]

#load lists from file
#create first name list
firstnames = open("NameDatabases-master/NamesDatabases/first names/all.txt","r") 
fname_list = firstnames.readlines()
#create last name list
lastnames = open("NameDatabases-master/NamesDatabases/surnames/all.txt","r") 
lname_list = lastnames.readlines()
#create open field list
openfields = open(r"open field examples/open.txt", "r")
ofields_list =  openfields.readlines()
# import random module for random generation
import random


#randomly choose variables for each list
n_title = random.randint(0, len(title_list) - 1)
n_fname = random.randint(0, len(fname_list) - 1)
n_lname = random.randint(0, len(lname_list) - 1)   
n_ofield = random.randint(0, len(ofields_list)-1)
n_ofieldref = random.randint(0, len(ofields_list)-1)

#generate name from variables
#string slicing by -1 needed to remove newline character from loaded first name and last name files
random_name = title_list[n_title] + " " + fname_list[n_fname][:-1] + " " + lname_list[n_lname][:-1]
#print(random_name)
#uncomment to test output

#sometimes names are used always without title in transaction descriptions, same name always without title also generated
random_name_no_title = fname_list[n_fname][:-1] + " " + lname_list[n_lname][:-1]
#print(random_name_no_title)
#uncomment to test output

#some transactions have an open field which the sender can put in a custom message
#these can be put either in a field toward the beginning or in the reference part
#of the transaction at the end
open_field = ofields_list[n_ofield][:-1]
open_field_ref =  ofields_list[n_ofieldref][:-1]
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
transfertype = random.randint(1,7)
if transfertype == 1:
    #transfers of type 1 follow the format Transfer to [name] - Receipt [n] To [n] [n]  - Transfer to [name] - 
    #Receipt [n] To [n] [n]
    #generate receipt string portion
    receipt = " - Receipt " + receipt_number + " To " + bsb_number + " " + account_number
    #generate transaction description string
    transaction_string = (  "Transfer to " + random_name_no_title + receipt + " - Transfer to " + 
                            random_name_no_title + receipt )
elif transfertype == 2:
    #transfers of type 2 follow the format [name] - Osko Payment to [n] [n] - Receipt [n]
    transaction_string = ( random_name_no_title + " - Osko Payment to " + bsb_number + " " + 
                            account_number + " - Receipt " + receipt_number)
elif transfertype == 3:
    #transfers of type 3 follow the format [name] - Transfer to [n] [n] - Receipt [n]
    transaction_string = ( random_name_no_title + " - Transfer to " + bsb_number + " " +
                            account_number + " - Receipt " + receipt_number)
elif transfertype == 4:
    #transfers of type 4 follow the format [open field] - Transfer to [name] - Receipt [n] To [n] [n]
    transaction_string = ( open_field + " - Transfer to " + random_name_no_title +
                            " - Receipt " + receipt_number + " To " + bsb_number + " " + account_number)
elif transfertype == 5:
    #transfers of type 5 follow the format [name with title] [open field] - Deposit - Receipt [n]
    transaction_string = (random_name + " " + open_field + " - Deposit - Receipt " + receipt_number)
elif transfertype == 6:
    #transfers of type 6 follow the format [name] [open field] - Receipt [n]
    transaction_string = (random_name + " " + open_field + " - Receipt " + receipt_number)
elif transfertype == 7:
    #transfers of type 7 follow the format [open field] - Osko Payment - Receipt [n] - Ref [ref open field]
    transaction_string = (open_field + " - Osko Payment - Receipt " + receipt_number +
                            " - Ref " + open_field_ref)
print(transaction_string)