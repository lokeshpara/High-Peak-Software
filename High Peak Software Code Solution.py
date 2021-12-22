#!/usr/bin/env python
# coding: utf-8

# In[294]:


# read the input file and get data from that file
def collectingInput(filename):
    listFormat = []
    dictonary = {}
    f = open(filename)
    for line in f:
        val = line.split(":")
        listFormat.append(val)
        
# del line spaces    

    for i,v in enumerate(listFormat): 
        if len(v) != 2:
            del listFormat[i]
            
# convert dictonary

    for i in listFormat[2:]:
        dictonary[i[0]] = int(i[1])
        
# sorting

    sorted_dict = sorted(dictonary.items(),key = lambda v: v[1])
   
    return sorted_dict, int(listFormat[0][1])


# In[299]:


data,employees=collectingInput("input3.txt")


# In[300]:


def number(employees,sorted_dict):
   
    miniDifference = 0
    te=employees-1
    startindex = 0
    stopindex = 0
    
    for i in range((len(sorted_dict)-employees)):
        difference = sorted_dict[te][1]-sorted_dict[i][1] 
        te+=1
        if miniDifference == 0 or difference < miniDifference :
            miniDifference = difference
            startindex = i
            stopindex = te
            
#     create new file for output file
    f = open("output3.txt", "a")
    f.write("The goodies selected for distribution are:\n")
    f.write("\n")
    for i in range(startindex,stopindex):
        f.write(f"{sorted_dict[i][0]} : {sorted_dict[i][1]} \n")
    f.write(f"And the difference between the chosen goodie with highest price and the lowest price is {miniDifference} \n")
    f.close()
    f = open("output3.txt")
    return print(f.read())
number(employees,data)  


# In[ ]:




