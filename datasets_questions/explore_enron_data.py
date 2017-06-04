#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print enron_data

count = 0

for key in enron_data:
    #	print key
    #	print enron_data[key]['total_payments']
    if enron_data[key]['poi'] == 'True':
        if enron_data[key]['total_payments'] == 'NaN':
            count = count + 1
print count

# count = 0

# for key in enron_data:
#        print key
#        print enron_data[key]['total_payments']
#        if enron_data[key]['poi']  == True:
#        	count = count + 1
# print count

# print enron_data['PRENTICE JAMES']
# print enron_data['PRENTICE JAMES']['total_stock_value']

# print enron_data['COLWELL WESLEY']
# print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# print enron_data['SKILLING JEFFREY K']
# print enron_data['SKILLING JEFFREY K']['total_payments']

print enron_data['LAY KENNETH L']
# print enron_data['LAY KENNETH L']['total_payments']

# print enron_data['FASTOW ANDREW S']
# print enron_data['FASTOW ANDREW S']['total_payments']


