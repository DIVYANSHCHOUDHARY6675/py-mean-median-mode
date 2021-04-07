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
new_data.sort()
if (n%2==0):
    m1=float(new_data[n//2]) 
    m2=float(new_data[n//2-1]) 
    median=(m1+m2)/2
else:
    median=float(new_data[n//2])    
print("the median of the data is"+str(median))    
    