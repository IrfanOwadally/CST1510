"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Irfan Owadally
Lane  : IT
Date  : 13/111/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import os
# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line): 
    """Turn one messy 'host, used=..., total=...' line into a clean dict.""" 
    line = raw_line.strip().strip(' \t\n",').lower() 
    hostname_part, rest = line.split(",", 1) 
    record = {"hostname": hostname_part.strip()} 
    for piece in rest.split(","): 
        key, value = piece.split("=") 
        record[key.strip()] = float(value.strip()) 
    return record 

def status_of(record): 
    """Return OVER LIMIT, WARNING or OK for one server record.""" 
    percent = record["used"] / record["total"] * 100 
    if percent >= 100: 
        return "OVER LIMIT" 
    elif percent >= 90: 
        return "WARNING" 
    return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []
def load_lines(path): 
    """Return the non-blank lines from a text file.""" 
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), path)) as f: 
        return [line for line in f if line.strip() != ""]   


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

def main(): 
    """Parse every line in the file, print each record and a summary."""
    lines = load_lines("servers_raw.txt") 
    total = 0 
    flagged = 0 
    for raw in lines:
        try:
            record = parse_line(raw) 
            #call main function 
        except ValueError:
            print(f"Could not parse: {raw.strip()}")
            continue                      # skip this line, go to the next one
        status = status_of(record)        # only reached if parsing worked
        print(f"{record}  ->  {status}")
        total += 1 
        if status != "OK": 
            flagged += 1 
    print(f"{total} records parsed, {flagged} flagged") #after the loop
main() 


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
