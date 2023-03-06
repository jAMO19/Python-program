import sys 
import csv 
import re 

def main(): 
    file_name = sys.argv[1] 

    size = len(file_name) 
    output_file_name = file_name[:size - 4] 

    with open(file_name, 'r', encoding = 'UTF8', newline = '') as csvin: 
        with open(output_file_name + '_final_percent.csv', 'w', encoding = 'UTF8', newline = '') as csvout:  
            writer = csv.writer(csvout, lineterminator = '\n') 
            reader = csv.reader(csvin) 

            all = [] 
            row = next(reader) 
            row.append('Percent') 
            all.append(row) 

            j = [] 

            for row in reader: 
                percent = float(row[25]) / float(row[24]) 
                row.append(percent) 
                all.append(row)

            writer.writerows(all)

if __name__ == "__main__": 
    main()