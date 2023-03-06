import sys 
import csv

def main(): 
    file_name = sys.argv[1] 
    watershed_name = sys.argv[2]

    input_File = open(file_name, "r") 

    watershed = [] 

    data = [] 

    unique = [] 

    not_unique = [] 

    w_2 = [] 

    id_2 = []

    # Reads all input from csv file and puts all elements into a series of lists
    with open(file_name, 'r') as f: 
        reader = csv.reader(f, delimiter = ',') 
        row1 = next(reader)
        for row in reader: 
            
            # Adds all unique licences to data list
            if row[0] not in unique:
                if row[2] == "Current" and row[9] == "Irrigation: Private" and row[14] == watershed_name:
                    data.append(row) 
                watershed.append(row[14])
                unique.append(row[0]) 
            
            # Adds non-unique licences to another list
            else: 
                if row[2] == "Current" and row[9] == "Irrigation: Private" and row[14] == watershed_name:
                    not_unique.append(row) 
                w_2.append(row[14]) 
                id_2.append(row[0])

    watershed.pop(0) 

    data.pop(0) 
    
    data_1_len = len(data) 

    not_unique_len = len(not_unique) 

    unique_2 = [] 

    # Checks for duplicate water licences that are within the watershed given in argument #2
    for i in range(not_unique_len):  

        if w_2[i] == watershed_name: 
            if id_2[i] not in unique_2:
                data.append(not_unique[i]) 
                unique_2.append(id_2[i]) 

    
    data_2_len = len(data) 


    size = len(file_name)
    output_file_name = file_name[:size - 4] 
    
    data_3_len = len(data) 

    # Writes all filtered data to the new csv file
    with open(output_file_name + '_filtered.csv', 'w', encoding = 'UTF8', newline = '') as f: 
        writer = csv.writer(f) 
        writer.writerow(row1) 
        
        all = []
        for row in range(data_3_len): 
            writer.writerow(data[row])  
 

if __name__ == "__main__": 
    main()