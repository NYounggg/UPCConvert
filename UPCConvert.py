import pandas as pd 
import csv
import os
import subprocess
import tkinter
from tkinter import filedialog

try:
    print('Select File ...')
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfilename(filetypes=[("CSV File", "*.csv")])
    
    file = open(file_path)
    df = pd.read_csv(file, dtype=str) 

    #initialize data
    upce = df['UPC-E'].to_list()
    upce = [str(i) for i in upce]
    upca = []
    upca_nocheck = []

    # add leading zeros where necessary
    for i in range(len(upce)):
        if len(upce[i]) == 7: # leading 0
            upce[i] = '0' + upce[i]

    # generate UPC-A values
    for code in upce:
        if len(code) > 8:
            print(code, "is long. Skipping")
            upca.append(code)
        elif code[6] in ['0', '1', '2']:
            upca.append(code[0] + code[1:3] + code[6] + '0000' + code[3:6] + code[7])
        elif code[6] == '3':
            upca.append(code[0] + code[1:4] + '00000' + code[4:6] + code[7])
        elif code[6] == '4':
            upca.append(code[0] + code[1:5] + '00000' + code[5] + code[7])
        elif code[6] in ['5', '6', '7', '8', '9']:
            upca.append(code[0] + code[1:6] + '0000' + code[6] + code[7])

    # remove check digit if there is one
    upca_nocheck = [i[:-1] if len(i)==12 else i for i in upca]

    df['UPC-A'] = upca
    df['UPC-A No-Check'] = upca_nocheck

    # formating for output csv
    outdf = df[['UPC-A No-Check', 'Quantity']]
    outdf.to_csv('out.csv', index=False)
    print('UPC-A file saved to', os.path.abspath('out.csv'))

    # ask to open file explorer
    choice = True
    while(choice):
        open_explorer = input('Would you like open in file explorer? (y/n) >>> ').lower()
        if open_explorer == 'y':
            subprocess.Popen(r'explorer /select,' + os.path.abspath('out.csv'))
            choice = False
        elif open_explorer == 'n':
            choice = False
        else:
            print('Invalid choice')

    file.close()
except FileNotFoundError:
    print('File not found.  Try re-typing path.')