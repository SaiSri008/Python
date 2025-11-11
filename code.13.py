# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 23:35:45 2025

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 13:43:14 2025

@author:
"""

#pdf


file1 = open(r"C:\Users\Sai\Downloads\ict.txt")

file1 = open(r"C:\Users\Sai\Downloads\ict.txt")
for each in file1:
    print (each)
    
f1 = open(r"C:\Users\Sai\Downloads\ict.txt")    
print (f1.read())


with open(r"C:\Users\Sai\Downloads\ict.txt",'r') as f1:  
    data = f1.read() 
print(data)


f1 = open(r"C:\Users\Sai\Downloads\ict.txt")    
print (f1.read(5))

#data = file.readlines(1)  #-->with argument then it will split specific line

with open(r"C:\Users\Sai\Downloads\ict.txt",'r') as file:
    data = file.readlines()
    
    for line in data:
        word = line.split()
        print (word)

#itterative variable mai print kabhi bahar nhi hosakta it will generate error
#that's why i ko ek aur variable mai store karenge

l1 = [1,2,3]
for i in l1:
    #print(i)
    a = i;
print(a)  


with open("file.txt", "w") as f: 
    f.write("Hello World!!!") 
    f.close()
    
    

file = open("3EK2A.txt",'w')
file.write("ICT ICT ICT \n")
file.write("ICT ICT ICT ICT ICT")
file.close()



#append mode mai write operations hote hai 
#if a<---> w   

file = open("3EK2A.txt",'a') 
file.write("\n Department Department")
file.close()


#OUTPUT:- 
'''
ICT ICT ICT 
ICT ICT ICT ICT ICT
 Department Department
 
'''
file = open("3EK2A.txt",'w') 
file.write("\n Department Department")
file.close()
#OUTPUT:-
'''
 Department Department
'''
#file1 = open()
#'department' in file1
#print true


with open(r'C:\Users\Sai\Downloads\a.tif', 'rb') as file:
    binary_data = file.read()
print(binary_data)


with open('c.tif', 'wb') as f:
    f.write(binary_data)
    f.close()
    
    

# Reading from a CSV file


import csv
with open(r'C:\Users\Sai\Downloads\data-1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



import csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow([      Name,Subject,Mark
    writer.writerow([      Devi, PWP, 9
    writer.writerow([      Sai, PWP, 10
    file.close()
