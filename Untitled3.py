#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
# opening and reading the xml file from hard disk
with open('/Users/sanjayplal/Downloads/orders.xml', 'r') as f:
    data = f.read()
# parsing the xml to extract data using beautiful soup library and using xml parser
bs = BeautifulSoup(data, "xml")
hm = {}

# finding all the tags related to add order
addbook = bs.findall('AddOrder')

# finding all the tags related to delete order
deletebook = bs.findall('DeleteOrder')
print(addbook.size())
print(addbook[0])
print(addbook[1])

# adding all the books with its order in operations
for i in addbook:
    book = str(i['book'])
    operation=str(i['operation'])
    price=str(i['price'])
    volume=str(i['volume'])
    orderid=str(i['orderId'])
    if book not in hm:
        hm[book]=

# deleting all the books from hashmap
for i in deletebook:
    book = str(i['book'])
    orderid=str(i['orderId'])
    if book in hm:
        del hm[book]
        
        
# We can use hashmap data structure to store all the books and its value will be array in which indexed position
# will be stored in this manner 0 for array of operation, 1 for array of price, 2 for volume, and 3 for array of
# different order ids and whenever the order is placed for add book we will look up the book and retrieve the data
# from array and change the array by changing the price and decreasing or increasing the volume of book and will 
# perform the operation of buying and sellling and index in operation array are corresponding to buying or selling 
# price array for different orders and to print the order book we can iterate over hashmap using bookid and than 
# print all the data from value pair by iterating over array of operation and price and printing it simultaneously 
# and deletion of orders is performed after adding all the orders and deleting the specific key value pair from
# hashmap


# In[2]:


print(bs)
#deletebook = bs.findall('DeleteOrder')


# In[ ]:




