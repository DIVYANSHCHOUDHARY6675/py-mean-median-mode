import csv
from collections import Counter
with open("SOCR2.csv",newline='')as dew:
    reader=csv.reader(dew)
    file_data=list(reader)
file_data.pop(0)
new_data=[] 
for i in range(len(file_data)):
    num=file_data[i][1]
    new_data.append(float(num))
n=len(new_data)
data=Counter(new_data)
mode_data={
"50-60":0,
"60-70":0,
"70-80":0
}
for height,occurrence in data.items():
    if 50<float(height)<60:
        mode_data["50-60"]+=occurrence
    elif 60<float(height)<70:
        mode_data["60-70"]+=occurrence
    elif 70<float(height)<80:
        mode_data["70-80"]+=occurrence
mode_range, mode_occurence = 0, 0
for range, occurence in mode_data.items(): 
    if occurence > mode_occurence:
         mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence 
mode = float((mode_range[0] + mode_range[1]) / 2) 
print("the mode of the data is"+str(mode)) 


