from parse_names import beautify_string
import os

folder_path = "city info/raw/"
ENCODING = "UTF-8"

def delete_folder():
    dec = input("Would you like to delete assembly html files? (1 for yes, 0 for no): ")
    if dec == "1":
        folder_path = "assembly html files/"
        for filename in os.listdir(folder_path):
            if os.path.exists(folder_path+filename):
                os.remove(folder_path+filename)
    dec = input("Would you like to delete raw files? (1 for yes, 0 for no): ")
    if dec == "1":
        folder_path = "city info/raw/"
        for filename in os.listdir(folder_path):
            if os.path.exists(folder_path+filename):
                os.remove(folder_path+filename)
    dec = input("Would you like to delete formatted files? (1 for yes, 0 for no): ")
    if dec == "1":
        folder_path = "city info/formatted/"
        for filename in os.listdir(folder_path):
            if os.path.exists(folder_path+filename):
                os.remove(folder_path+filename)

def merge_files(a, b):
    # merges two lists and saves 
    # them in b, also deletes a
    a = beautify_string(a)
    b = beautify_string(b)
    a += ".txt"
    b += ".txt"
    read_a = open(folder_path+a, "r", encoding=ENCODING)
    a_context = read_a.readlines()
    read_a.close()

    read_b = open(folder_path+b, "r", encoding=ENCODING)
    b_context = read_b.readlines()
    read_b.close()

    for i in a_context:
        if i != '':
            b_context.append(i)

    write_b = open(folder_path+b,"w",encoding=ENCODING)
    for line in b_context:
        write_b.write(line)
    os.remove(folder_path+a)



def format_files():
    # this function fixes the format issues in the city information
    # some issues are particular city not existing anymore because it
    # changed it's name, united with another city or is not recognized  
    # as a city of Turkey anymore
    merge_files("BATUM", "ARTVİN")
    merge_files("BAYAZIT", "AĞRI")
    merge_files("BİGA", "ÇANAKKALE")
    merge_files("BOZOK", "YOZGAT")
    merge_files("CANİK", "SAMSUN")
    merge_files("CEBELİBEREKET", "OSMANİYE")
    merge_files("DERSİM", "TUNCELİ")
    merge_files("ERGANİ", "DİYARBAKIR")
    merge_files("ERTUĞRUL", "BİLECİK")
    merge_files("GENÇ", "BİNGÖL")
    merge_files("KARAHİSARI SAHİP", "AFYONKARAHİSAR")
    merge_files("KARESİ", "BALIKESİR")
    merge_files("KOZAN", "ADANA")
    merge_files("LAZİSTAN", "RİZE")
    merge_files("MENTEŞE", "MUĞLA")
    merge_files("OLTU", "ERZURUM")
    merge_files("SARUHAN", "MANİSA")
    merge_files("SEYHAN", "ADANA")
    merge_files("SİVEREK", "ŞANLIURFA")
    merge_files("ÇORUH", "ARTVİN")
    merge_files("ŞEBİNKARAHİSAR", "GİRESUN")
    merge_files("ÇATALCA", "İSTANBUL")
    merge_files("KARAHİSARI ŞARKİ", "GİRESUN")
    merge_files("GELİBOLU", "ÇANAKKALE")
    

while True:
    dec = input("Welcome to formatting panel for city information. Press 1 for deleting the content of the folder, 2 for other formatting utilities \nChoice :  ")
    if dec == "1":
        delete_folder()
        break
    elif dec == "2":
        format_files()
        os.rename(folder_path+".txt", folder_path+"bakanlar.txt")
        # ministers do not have city information which causes them
        # to be clustered in ".txt"
        break

