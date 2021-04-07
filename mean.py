import csv 
with open("SOCR2.csv",newline='')as dew:
    reader=csv.reader(dew)
    file_data=list(reader)
file_data.pop(0)
new_data=[]   
for i in range(len(file_data)):
    num=file_data[i][1]
    new_data.append(float(num))
n=len(new_data)
sum=0
for t in new_data:
    sum=sum+t
mean= sum/n
print("the mean of the data items is"+str(mean))




