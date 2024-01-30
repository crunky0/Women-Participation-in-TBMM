from parse_names import beautify_string
import csv
import os

ENCODING = "utf-8"


female_mps = [] # holds the names for female mps decided by group members

with open('females.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        female_mps.append(beautify_string(row[1]))

termcount = [0 for i in range(27)]

# matches the cities with their regions
region_city_dict = {}
with open('SehirlerBolgeler.csv', 'r', encoding=ENCODING) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Access the row data
        region_city_dict[beautify_string(row[0])] = beautify_string(row[1])

region_dict = {}
for i in region_city_dict.values():
    if i not in region_dict:
        region_dict[i] = [[0 for i in range(27)],[0 for i in range(27)]]
        # first one for female, second is for male



gender_dict = {}


# assign points according to the information given by the group members
def fix(full_name, gender_dict, male_counter, female_counter, region_name, term): 
    if term < 5: 
        # this is because the right for election of women is granted
        # in assembly no 5, correspondingto 1935
        male_counter[term - 1] += 1
        region_dict[region_name][1][term - 1] += 1
        tr_male_counter[term - 1] += 1
    else:
        try:
            dec = gender_dict[full_name]
        except:
            dec = full_name in female_mps
        if int(dec) == 0:
            male_counter[term - 1] += 1
            region_dict[region_name][1][term - 1] += 1
            tr_male_counter[term - 1] += 1
        else:
            female_counter[term - 1] += 1
            region_dict[region_name][0][term - 1] += 1
            tr_female_counter[term - 1] += 1
            
        gender_dict[full_name] = dec

def create_list(file):
    mylist= []
    for i in file.readlines():
        mylist.append(i.strip())
    return mylist



female_txt = open("name dictionary/female_name.txt", "r", encoding=ENCODING)
female_list = create_list(female_txt)

male_txt = open("name dictionary/male_name.txt", "r", encoding=ENCODING)
male_list = create_list(male_txt)

unisex_txt = open("name dictionary/us_name.txt", "r", encoding=ENCODING)
unisex_list = create_list(unisex_txt)



year_info = open("year_assembly_no.txt", "r", encoding=ENCODING)
year_list = create_list(year_info)
folder_path = "city info/"




tr_female_counter = [0 for i in range(27)]
tr_male_counter = [0 for i in range(27)]
    

for filename in os.listdir(folder_path+"raw/"):
    filename = beautify_string(filename)
    if filename == "bakanlar.txt":
        continue

    city_name = filename[:-4]
    region_name = region_city_dict[city_name]
    

    infile = open(folder_path + "raw/" + filename , "r", encoding=ENCODING)
    female_counter = [0 for i in range(27)]
    male_counter = [0 for i in range(27)]
    

    content = infile.readlines()

    for line in content:
        if (len(line) > 2):
            donem = int(line.split(" ")[0]) # due to indexing
            termcount[donem -1] += 1
            full_name = line[line.find(" ") + 1:].strip()
            full_name = full_name.lower()
            try:
                name = full_name.split(" ")[0]
            except:
                name = full_name
            if name in unisex_list:
                fix(full_name, gender_dict, male_counter, female_counter, region_name, donem)
            elif name in female_list:
                female_counter[donem - 1] += 1
                tr_female_counter[donem - 1] += 1
                region_dict[region_name][0][donem - 1] += 1
            elif name in male_list:
                male_counter[donem - 1] += 1
                tr_male_counter[donem - 1] += 1
                region_dict[region_name][1][donem - 1] += 1
            else:
                # if full_name not in out_list:
                #     out_list.append(full_name)
                fix(full_name, gender_dict, male_counter, female_counter, region_name, donem)



    counter = 0
    for i in male_counter:
        counter += i
    for i in female_counter:
        counter += i

    


    header = ["Assembly No","Year", "Male MP Count", "Female MP Count"]
    # until this point all the decisions have been made
    # writes for cities
    with open(folder_path + "/formatted/" + filename.split(".")[0]+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for i in range(27):
            writer.writerow([i+1, year_list[i].split(" ")[1], male_counter[i], female_counter[i]])
    
    with open(folder_path + "/formatted/" + region_name+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for i in range(27):
            writer.writerow([i+1, year_list[i].split(" ")[1], region_dict[region_name][1][i], region_dict[region_name][0][i]])


terms = {}
for i in range(27):
    terms[i+1] = [0,0]
 

for region in region_dict:
    female_list = region_dict[region][0]
    male_list = region_dict[region][1]
    for idx in range(len(female_list)):
        terms[idx+1][0] += female_list[idx]
        terms[idx+1][1] += male_list[idx]

header = ["Term", "Year", "Female MP Count", "Male MP Count","Total Count"]
with open(folder_path + "/formatted/" + 'terms.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for i in range(27):
            writer.writerow([i+1, year_list[i].split(" ")[1], terms[i+1][0], terms[i+1][1], terms[i+1][0]+ terms[i+1][1] ])


with open(folder_path + "/formatted/" + 'turkiye.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for i in range(27):
            writer.writerow([i+1, year_list[i].split(" ")[1], tr_female_counter[i], tr_male_counter[i], tr_female_counter[i]+ tr_male_counter[i] ])
