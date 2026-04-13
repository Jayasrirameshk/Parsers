import pandas as pd

#Getting input from user
file_name = input("Enter the file name or path: ") 

#viewing the table
table_with_header = pd.read_csv(file_name,sep ='\t', skiprows= 1, index_col=0)
print(table_with_header)

#calculating taxa count
taxa_count = table_with_header.sum(axis=1)

#Printing top three taxa
top_taxa = taxa_count.sort_values(ascending=False).head(3)
print (f"Top Three taxa: {top_taxa}")