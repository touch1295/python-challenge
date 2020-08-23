# Import Dependencies
import os
import csv


# Declare file location through pathlib
input_file = os.path.join("Resources", "employee_data.csv")

# Creating a Dictionary to store all the States in USA and the abbreviations
usa_state_abbreviations = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Create empty Lists to store data
Employee_ID = []
Full_Name = []
First_Name = []
Last_Name = []
DOB = []
DOB_new = []
SSN = []
SSN_Hide = []
state_abbreviations = []


with open(input_file,newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header labels to iterate with the values
    header = next(csvreader)

    # Iterate through each row stored in csvreader
    for row in csvreader:

        # Append employee id's into list, no formatting changes needed
        Employee_ID.append(row[0])


        # Split Full_Name into First_Name and Last_Name lists
        Full_Name = row[1].split(" ")
        First_Name.append(Full_Name[0])
        Last_Name.append(Full_Name[1])

        # Split DOB with "-"
        # Append and format DOB
        DOB = row[2].split("-")
        DOB_new.append(DOB[1] + "/" + DOB[2] + "/" + DOB[0])
        

        # Split the SSN with "-"
        # Append and format ssn into ssn_private list
        SSN = row[3].split("-")
        SSN_Hide.append("***-**-" + SSN[2])

        # Match the state list item to a dictionary value, if they match, append dictionary key to list abbrev
        state_abbreviations.append(usa_state_abbreviations[row[4]])


# Zip lists together
formated_csv = zip(Employee_ID, First_Name, Last_Name, DOB_new, SSN_Hide, state_abbreviations)

# Set variable for output file
output_file = os.path.join("Formated","FORMATED_EMPLOYEE_DATA.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])

    # Write in zipped rows
    writer.writerows(formated_csv)

