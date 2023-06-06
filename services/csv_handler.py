import csv

def read_csv(file_name):
    array = []

    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            sub_arr = []

            for num in row:
                if num != '':
                    sub_arr.append(int(num))
            
            array.append(sub_arr)
    
    return array

def write_csv(matches):
    with open("result.csv", 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for i in range(len(matches)):
            if matches[i] != -1:
                writer.writerow([matches[i] + 1, i + 1])
