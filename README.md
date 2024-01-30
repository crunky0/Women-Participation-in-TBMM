#######################     Group 18 CS210 Project     #######################

This project is prepared by Group 18 members for 2022-2023 Spring Semester CS210 Lecture

Göktuğ Aygün  	30608

Efe Ballar 	    30641

Mert Rodop 	    30745

Burak Yılmaz	  30994

Kemal Yılmaz	  31097


This project aims to detect the imbalance in the numbers of count of MP's in the Grand Assembly of Turkey. By investigating this topic, we are aiming to make a great contribution in the field. What motivated us for studying this topic are the Sustainable Development Goals determined by the United Nations in 2015. To be more specific, we are focusing on SDG #10 Reduced Inequalities and #16 Peace, Justice and Strong Institutions. 

download_assembly.py

In this file, we utilized Selenium in order to imitate user behavior and collect data from the official website "https://www.tbmm.gov.tr/Kutuphane/MazbataArama". It gets the source file for the website as HTML code and saves them in a folder called "assembly html files".

download_name_dict.py

This file also uses Selenium and downloads HTML code for male and female name dictionaries from "http://hleventustun.com/isimlersozlugu.php". The codes are saved in two files that can be found in the folder "name dictionary". The raw information scraped from the website is then processed using "parse_names.py" and saved in seperate files.

parse_names.py

This file is used in order to process the name information. Non-english characters are converted into English characters. Lowercasing is another technique being applied here. A function called beautifty_string is defined here which will be used in other files as well. This functions converts non-English characters to English characters, lowers them and also changes the characters from outside the ASCII interval of [0,127] to their equivalances. The names are seperated into three categories being "Male", "Female" and "Unisex" names. 16 names are manually added in unisex list because they were detected by the intersection. Finally, these names are written to their seperate .txt files.

parse_assembly.py

This file utilizes BeatifulSoup and obtains the name and city information of each MP for each legislative term. The information is saved in files in the format of "city_name.txt" in the folder "raw".

format_cities.py

This file works like a menu making it possible for the user to delete unwanted files. Besides doing so, it also fixes the formatting issues of having files of cities that do not exist anymore.

read_csv.py

This file is used in order to read csv information that is decided manually by users. This happens because the software is unable to detect the gender information because the names do not appear in the name dictionary. These informations are also saved in a seperate dictionary in order to avoid repetition.

scrape_wiki.py

This file downloads the starting year information for each legislative term from wikipedia.org.

assign_points.py

This file processes the information recieved from the files in "city info/raw". These .txt files are converted into .csv files later to be read and plotted with the use of pandas and matplotlib.pyplot. Genders are decided based on the name information parsed in parse_names.py. If it is not possible to make the decision, external influence is needed. 1 .csv file is created for Turkey, 7 created for regions and 81 created for each city. Additionally, the information about cities and the regions they are located in is obtained from "https://github.com/yigith/TurkiyeSehirlerBolgeler" are used.

regression_current.ipynb

This file is used in order to make predictions about last 6 terms using scraped and processed information of 21 past terms. Linear regression and Polynomial regression are the models that are trained for this task. The r2 score for polynomial regression is higher which means that this model is able to make more accurate predictions. Thus, the predictions produced by this model are used in analysis.ipynb

regression_future.ipynb

This file uses a machine learning model that predicts next 4 legislative terms and corresponding female MP counts. Two models are being trained one using the last 8 terms and the other using last 15 terms. 


analysis.ipynb

Finally, this notebook contains the code cell blocks that are used in order to generate descriptive and analytical images. These images transform from the numerical value that is challenging for human brain to understand at first glance to visuals which are easier to absorb.
