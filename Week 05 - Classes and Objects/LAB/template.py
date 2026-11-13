"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Irfan Owadally
Lane  : IT      
Date  : 13/11/206

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.
# Call the library
import os
# your class goes here
# create a record class
# create a record class 
class Record: 
    """One server and how much of its disk is used.""" 
    WARNING_AT = 90     
    # class-level: shared by every Record 
    OVER_AT = 100 
    # constructor 
    def __init__(self, label, value, limit):
        """Create a Record from hostname, GB used and GB total."""
        # hostname 
        self.label = label
        # GB used       
        self.value = value
        # GB total       
        self.limit = limit      
    # Define a method which is called percent(self)     
    def percent(self): 
        """Return how full the disk is, as a percentage.""" 
        # Do maths operation
        return self.value / self.limit * 100 
    # Define a method which is called status(self)
    def status(self): 
        """Return OVER LIMIT, WARNING or OK depending on how full the disk is.""" 
        # Store calling method
        used = self.percent()
        # Check if used is greater than or equal to 100 
        if used >= Record.OVER_AT: 
            # Return OVER LIMIT
            return "OVER LIMIT"
        #  Check if used is greater than or equal to 90
        elif used >= Record.WARNING_AT: 
            # Return WARNING
            return "WARNING" 
        #Check if the two above criterias have not met
        else: 
            # Return OK
            return "OK" 

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.
# Declare a variable that stores a list
records = []
# Define a function which is called load_records(path)
def load_records(path): 
    """Read hostname,used,total lines from a file and return a list of Records."""
    # Open the file
    # f is assigned the variable for the opening of the file
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path)) as f:
        # Go through the file line at a time
        for line in f: 
            # Remove spaces and the newline character from both ends of the line 
            line = line.strip() 
            # Check whether the line is empty or not
            if line == "":
                # Skip the blank line and move on to the next one 
                continue 
            # try the code below, which may fall if the line is badly formed
            try: 
                # Split the line at each comma into three paths
                label, value, limit = line.split(",")
                # Convert the numbers to floats, build a Record and add it to the list
                records.append(Record(label, float(value), float(limit))) 
            # handling expection
            except ValueError: 
                # Display the bad line
                print(f"Skipping bad line: {line}") 
    # Return records
    return records 


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

# loop to seperate record from records
for record in records:
        # Display nothing
        print()
        # Creating an interface
        print("=" * 34)
        # Display its label
        print(f"  RECORD CHECK  -  {record.label}")
        # Closing an interface
        print("=" * 34)

# Define a function which is called print_report(record, status)
def print_report(record, status): 
    """Display one record as a bordered report."""
    # Creating an interface  
    print("=" * 34) 
    # Display its label
    print(f"{'Host:':<9}{record.label:<24}")
    # Creating another interface 
    print("=" * 34)
    # Display its value over limit
    print(f"{'Used:':<9}{record.value:.1f} GB of {record.limit:.1f} GB") 
    # Display its percent
    print(f"{'Usage:':<9}{record.percent():.1f}%") 
    # Display its status
    print(f"{'Status:':<9}{status:<24}") 
    print("=" *34) 

# Define a function which is called main()
def main(): 
    """Load the records, print a report for each, then count the overloaded ones.""" 
    # Try the code below, which may fail if the file is missing
    try: 
        # call load_records to read the file and store the return list of Records
        localrecord = load_records("servers.txt")
        # Declare a variable and initialise it to 0
        over_count = 0 
        # Loop to seperate record from records
        for record in records: 
            # Ask the record for its status
            status = record.status()  
            # Display the record and status      
            print_report(record, status) 
            # Check whether its status is OVER LIMIT 
            if status == "OVER LIMIT":
                # over_count is incremented by 1 
                over_count += 1 
        # Display how many localrecord are over limit
        print(f"{over_count} of {len(localrecord)} servers are OVER LIMIT")
    # handling exception  
    except FileNotFoundError:
        # Display a message 
        print("Could not find servers.txt")
    # Return to end the function
    return 

main() 


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring

