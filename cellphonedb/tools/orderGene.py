#!/usr/bin/python
import sys
import csv
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

if len(sys.argv) != 4:
    print("Usage: python {} interaction_input.csv complex_input.csv protein_input.csv".format(__file__))
    sys.exit()

[file_int, file_com, file_pro] = sys.argv[1:]
rec = dict()

with open(file_com) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    #print(">", headers[0], headers[10])
    for row in f_csv:
        [cid, receptor] = [row[i] for i in [0,10]]
        rec[cid] = receptor

with open(file_pro) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    #print(">", headers[0], headers[7])
    for row in f_csv:
        [pid, receptor] = [row[i] for i in [0,7]]
        rec[pid] = receptor

with open(file_int) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(",".join(headers))
    #print(">", headers[1:3])
    for row in f_csv:
        [partner_a, partner_b] = row[1:3]
        if rec[partner_a] == "True" and (rec[partner_b] == "False"):
            row[0] = row[0].replace("CPI-","CPF-")
            row[1:5] = [row[i] for i in [2,1,4,3]]
        sys.stdout.write(",".join(row) + "\n")
