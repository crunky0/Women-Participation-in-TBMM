from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import MaxNLocator

from parse_names import beautify_string
from matplotlib.axis import Axis
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pandas as pd



region_list_tr = ["ic anadolu", "marmara", "akdeniz", "ege", "dogu anadolu", "guneydogu anadolu", "karadeniz"]
region_list_en = ["Central Anatolia", "Marmara", "Mediterranean", "Aegean", "Eastern Anatolia", "Southeastern Anatolia", "Black Sea"]

# prevents '0%'  from being printed
def my_autopct(pct):
    if pct > 0:
        return '{:.2f}%'.format(pct)
    else:
        return ''

while True:        
    mode = input("Please enter the mode you want to create your graph\n1 for Line Chart\n2 for Stacked Bar Chart\n3 for Pie Chart\nChoice: ") 
    if mode == "1": #line chart for cities for female count
        city_list = []
        fig, ax = plt.subplots()
        while True:
            user_input = input("Which city would you like to see about? (exit to stop): ").lower().strip()
            city_list.append(user_input)
            user_input = beautify_string(user_input)
            name = ""
            for i in user_input:
                if ord(i) in range(256):
                    name += i
            user_input = name
            if user_input == "exit":
                break
            infile = "city info/formatted/" + user_input + ".csv"
            

            df = pd.read_csv(infile)
            ax.plot(df['Year'], df['Female MP Count'])
            ax.grid(alpha = 0.8)
            ax.set_xticks(df["Year"])

            ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        for idx, city in enumerate(city_list):
            city_list[idx] = beautify_string(city).title()
            
        plt.title("Female MP's Over Time")
        plt.xlabel("Years")
        plt.xticks(rotation=45)  
        plt.ylabel("MP Count")
        plt.legend(city_list, loc = 'upper left', fontsize = 15)
        plt.show()

    elif mode == "2":  #stacked bar chart for one city for female and male
        while True:
            user_input = input("Which city would you like to see about? ").lower().strip()
            user_input = beautify_string(user_input)
            name = ""
            for i in user_input:
                if ord(i) in range(256):
                    name += i
            user_input = name
            if user_input == "exit":
                break
            infile = "city info/formatted/" + user_input + ".csv"
            
            try:
                df = pd.read_csv(infile)
                ax = df.plot.bar(x='Year', y = ['Female MP Count', 'Male MP Count'], stacked=True, title='Count of MP\'s Over Time in {}'.format(user_input.title()))
                break
            except:
                print("Invalid city name. Please check your input format.")

        ax.grid(axis='y', alpha = 0.8)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlabel("Years")
        plt.ylabel("MP Count")
        plt.xticks(rotation = 45)
        plt.show()
    
    elif mode == "3": #pie chart for a city and assembly for female and male
        city_list = []
        fig, ax = plt.subplots()
        while True:
            user_input = input("Which city would you like to see about? ").lower().strip() #sehrin gecerliligini kontrol et
            city_list.append(user_input)
            user_input = beautify_string(user_input)
            name = ""
            for i in user_input:
                if ord(i) in range(256):
                    name += i
            user_input = name
            if user_input == "exit":
                break
            infile = "city info/formatted/" + user_input + ".csv"
            query = int(input("Which assembly would you like to learn about? ")) #sayı girene kadar tekrar iste
            try:
                df = pd.read_csv(infile)
                ax = df.iloc[query-1]
                break
            except:
                print("Invalid city name. Please check your input format.")
        Female = ax['Female MP Count']
        Male = ax['Male MP Count']
        colors = ['#ff0000','#028ac9']
        plt.pie([Female, Male], autopct=my_autopct, shadow = True, explode=(0.1, 0.1), colors = colors)
        plt.title("Distribution of Male and Female MP's in Assembly No {} in {}".format(query, user_input.title()))
        plt.legend(["Female Count ({})".format(Female), "Male Count ({})".format(Male)], loc = "upper right")
        plt.show()
   
    elif mode == "4": #pie chart for regions for female contribution
        term = int(input("Please type in the term you want to search for: "))
        mp_count_list = []
        legend_list = region_list_en.copy()
        for idx, region in enumerate(region_list_tr):
            infile = "city info/formatted/" + region + ".csv"
            df = pd.read_csv(infile)
            mp_count = df.loc[term - 1]["Female MP Count"]
            mp_count_list.append(mp_count)
            
            legend_list[idx] += " ({})".format(mp_count)

        plt.pie(mp_count_list, autopct=my_autopct, shadow = True, explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1))
        plt.title("Contribution of Regions for Female MP's in Assembly No {}".format(term))
        plt.legend(legend_list, bbox_to_anchor = (1.4, 1), loc = "upper right", fontsize = 10)
        plt.show()
        
    elif mode == "5": #line chart for regions for every term
        
        fig, ax = plt.subplots()
        for region in region_list_tr:
            infile = "city info/formatted/" + region + ".csv"
            

            df = pd.read_csv(infile)
            ax.plot(df['Year'], df['Female MP Count'])
            ax.set_xticks(df["Year"])
            ax.grid(alpha = 0.8)

        legend_list = [i.title() for i in region_list_en]
        plt.title("Female MP's Over Time")
        plt.xlabel("Years")
        plt.xticks(rotation=45)  
        plt.ylabel("MP Count")
        plt.legend(legend_list, loc = 'upper left', fontsize = 15)
        plt.show()
    
    elif mode == "6": #pie chart for regions and all terms
        term = int(input("Please enter the term you want to search for: "))        
        region = beautify_string(input("Please enter the region (in Turkish): "))
        idx = region_list_tr.index(region)
        infile = "city info/formatted/" + region + ".csv"

        df = pd.read_csv(infile)
        total_female = int(df["Female MP Count"].sum())
        total_male = int(df["Male MP Count"].sum())
        data = ["Male ({})".format(total_male), "Female ({})".format(total_female)]
        plt.pie([total_male, total_female], autopct=my_autopct, shadow = True, explode=(0.1, 0.1))
        plt.title("Comparison of total counts of Male and Female MP  in {} Region (for all terms)".format(region_list_en[idx].title()))
        plt.legend(data, loc = "upper right")
        plt.show()
    
    elif mode == "7": #pie chart for turkey
        infile = "city info/formatted/turkiye.csv"
        df = pd.read_csv(infile)
        female_count = df["Female MP Count"].sum()   
        male_count = df["Male MP Count"].sum()   
        data = [male_count, female_count]
        plt.title("Comparison of Male and Female MP's in Turkey (for all terms)")
        plt.pie(data, autopct=my_autopct, shadow = True, explode=(0.1, 0.1))
        plt.legend(["Male {}".format(male_count), "Female {}".format(female_count)])
        plt.show()
    