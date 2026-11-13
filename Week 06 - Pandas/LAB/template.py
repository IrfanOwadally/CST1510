"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Irfan Owadally
Lane  : IT      
Date  : 13/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# import the pandas library and named it pd
import pandas as pd
# import the matplotlib library and named it plt
import matplotlib.pyplot as plt 
# import the os module
import os
# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

# Create a variable that stores read the file
df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),"servers.csv")) 
# add a percent column 
df["percent"] = (df["used_gb"] / df["total_gb"] * 100).round(1) 
# Display the table
print(df) 

# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["status"] = df["percent"].apply( 
lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK") 
) 
print(df[df["status"] != "OK"]) 


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

# Group the rows by status and count how many Records are in each group
counts = df.groupby("status").size() 
# Display the count for each status
print(counts) 
#Save the DataFrame to a new csv file
df.to_csv("servers_report.csv", index=False)

# Draw plot
# Draw the count per status as a bar chart 
counts.plot(kind="bar") 
# Name it the title
plt.title("Servers per disk status") 
# Name it the x-axis
plt.xlabel("Status") 
# Name it the y-axis
plt.ylabel("Number of servers") 
# Change the layout
plt.tight_layout() 
# Save the bar chart to a png file
plt.savefig("servers_status.png")
# Display the bar chart 
plt.show() 


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
