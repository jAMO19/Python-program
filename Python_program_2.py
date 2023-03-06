import sys 
import csv 
import re 
from decimal import Decimal 

# Converts list of first element into one decimal number
def convert(p): 
    s = [str(i) for i in p] 
    res = float(''.join(s)) 
    return(res)

def main(): 
    
    file_name = sys.argv[1] 

    size = len(file_name)
    output_file_name = file_name[:size - 4] 
    

    with open(file_name, 'r', encoding = 'UTF8', newline = '') as csvin: 
        with open(output_file_name + '_final.csv', 'w', encoding = 'UTF8', newline = '') as csvout: 
            writer = csv.writer(csvout, lineterminator = '\n') 
            reader = csv.reader(csvin) 

            all = [] 
            row = next(reader) 
            row.append('Allotted Area (Acres)') 
            all.append(row) 

            j = []

            for row in reader: 
                if "AC" in row[15] or "ACS" in row[15]: 
                    if "ACRES" in row[15]: 
                        print(row[0]) 
                        d = row[15].rpartition('ACRES')[0] 
                        j = re.findall('\d*\.?\d+', d)[-1]

                        w = convert(j) 
                        row.append(w) 
                        all.append(row)
                    
                    else: 
                        p = (list(str(x) for x in re.findall('\d*\.?\d+', row[15])[0]))  
                        b = convert(p) 
                        row.append(b) 
                        all.append(row) 

            writer.writerows(all)
    


if __name__ == "__main__": 
    main()