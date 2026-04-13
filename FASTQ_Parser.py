import gzip
import os

#Getting input from user
file_name = input("Enter the file name or path: ") 

#Defining function for converting into phred scores
def phred_scores(char):
    return ord(char)-33

#Defining function for calculating average scores
def avg_score(scores):
    average = sum(scores)/len(scores)
    return average

#Initializing variables
low_quality = 0
total_reads = 0
header = ""
sequence = ""
separator = ""
q_scores = ""
store_read_id =[]
store_quality_score =[]

#Calculating average phred scores
if file_name.endswith('.gz'):
        file = gzip.open(file_name,'rt')
else:
        file = open(file_name,'r')

for i, line in enumerate(file):
    line = line.strip()

    if i % 4 == 0:
         header = line
    elif i % 4 == 1:
         sequence = line
    elif i % 4 == 2:
        separator = line
    elif i % 4 == 3:
        q_scores = line
        total_reads += 1  
              
        scores = [phred_scores(char) for char in q_scores]
        average = avg_score(scores)

        if average < 20:
            read_id = header[1:]
            read_quality_average = average
            low_quality +=1

            store_read_id.append(read_id)
            store_quality_score.append(read_quality_average)                                   
file.close()

#Saving the results to a file
save_path = os.path.expanduser("~/Desktop")
output_file = input ("Enter output file name (no extension):")
complete_name = os.path.join(save_path,output_file + ".txt")

with open(complete_name,"w") as f:
     f.write("Low quality reads:\n")
     f.write("Read ID\t Average Quality\n")
     for i in range(len(store_read_id)):
          read_id = store_read_id[i]
          avg = store_quality_score[i]
          f.write(f"{read_id}\t{avg}\n")

 #Printing output file path, total reads and low quality reads       
print(f"Total reads:{total_reads}")
print(f"Low quality reads(reads < Q20): {low_quality}")
print(f"Output file is saved at: {complete_name}")
                                