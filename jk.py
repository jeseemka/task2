# import the library panda

import pandas as pd



# read excellfile

excel_file = "jeseem.xlsx" 
data = pd.read_excel(excel_file)



# write the excelfile

text_file = "output1.txt"  
with open(text_file, "w") as file:
    file.write(data.to_string(index=False))
