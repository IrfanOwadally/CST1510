"""
RECORD CHECK  -  my version
===========================

Name  :  Mohammad Irfan Owadally
Lane  :  IT      
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
#Import the library 
import os 
#Declare a variable and initialise to it
count_overlimit = 0
# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
#Define a function which is called check(value, limit)
def check_record(value, limit):
    """Do difference between value and limit and percentage of value over limit times 100"""
    #Do the maths operation
    difference = limit - value
    percent = (value / limit) * 100
    #Check the condition if percent is greater than or equal to 100
    if percent >= 100:
        #Declare a variable which is called status and store OVERLIMIT to it
        status = "OVERLIMIT"
        #Declare count_overlimit as global
        global count_overlimit
        #OVERLIMIT is incremented by 1
        count_overlimit += 1
    #Check the condition if percent is greater than or equal to 90
    elif percent >= 90:
        #Declare a variable which is called status and store WARNING to it
        status = "WARNING"
    #Check the condition if the two conditions above arer not meeting the criteria
    else:
        #Declare a variable which is called status and store OK to it
        status = "OK"
        
    #Return difference, percent and status to a user
    return difference, percent, status
#Define a function which is called print_record(label, value, limit, difference, percent, status)
def print_report(label, value, limit, difference, percent, status):
    """Display all the fields available in the label"""
    #Creating an interface
    print("=" * 34)
    #Display the label
    print(f"  RECORD CHECK  -  {label}")
    #Create another interface
    print("=" * 34)
    #Display the label of used and its value
    print(f"  Used         : {value:>9.2f}")
    #Display the label of total and its value
    print(f"  Total        : {limit:>9.2f}")
    #Display the label of free and its value
    print(f"  Free         : {difference:>9.2f}")
    #Display the label of percent and its value
    print(f"  Percent      : {percent:>9.2f}%")
    #Display the label of status and its value
    print(f"  Status       : {status:>9}")
    #Closing an interface
    print("=" * 34)

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
#Define a function which is called load_records
def load_records(path):
    """Read records and displays information in terms of data that is split in value and limit and write the results for records in a new file."""
    #Check if condition is met
    try:
        #Create a variable which is called records
        records = []
        #Open a file 
        #f is assigned the variable for the opening of the file
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path)) as f:
            #loop to seperate line
            for line in f:
                #Split values on different label types using , as reference point
                label, value, limit = line.strip().split(",")
                #Convert value to float
                value = float(value)
                #Convert limit to float
                limit = float(limit)
                #Add label, value and limit to records
                records.append({"label": label, "value": value, "limit": limit})
            #Open a file 
            #f is assigned the variable for the writing of the file
            with open("results_for_records.txt", "w") as f:
                #Write to clean the file
                f.write("")
            #loop to seperate record from records
            for record in records:
                #Create a variable which is called Status and check if the one of two conditions is met
                Status = "OVERLIMIT" if record["value"] > record["limit"] else "OK"
                #Open a file 
                #f is assigned the variable for the appending of the file
                with open("results_for_records.txt", "a") as f:
                    #Write the records
                    f.write(f"record: {record["label"]}, {Status}\n")
                
    #handling of exception
    except FileNotFoundError:
        #Display a clear message
        print("The file does not exist.")
    #Return records to a user        
    return records 
#Create a variable and stores a function to it
records = load_records("records.txt")
#Print a variable that consits a function
print(records)   

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
#loop to seperate record from records
for record in records:
    #Call the function of check_record() to calculate difference, percent and status
    difference, percent, status = check_record(record["value"], record["limit"])
    #Call the print_report() to print the record
    print_report(record["label"], record["value"], record["limit"], difference, percent, status)
#Display overlimit
print("The number of record of overlimit is: ", count_overlimit)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
