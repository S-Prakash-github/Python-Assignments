#!/usr/bin/env python
# coding: utf-8

# ## 30th JAN Assignment :

# #### 1. Write a program to display the grade according to the criteria
# 
#   > (>90 == A  ,   >80 and <= 90 == B   ,   >60 and <= 80 == c  ,  below 60 == D)
# 

# In[6]:


## Taking user input
n = int(input("Enter the percentage obtained :"))

# Conditions 
if n > 90 :
    print("You have obtained Grade A")
elif n>80 and n <= 90 :
    print("You have obtained Grade B")
elif n>60 and n <=80 :
    print("You have obtained Grade C")
else:
    print("You have obtaineds Grade D")


# #### 2. Write a Python Program to accept cost price of a bike and show the road tax  for that price of the bike 
# > (15% on >100000 , 10% on >50000 and <= 100000  , 5% below 50000)

# In[18]:


## User input
price = int(input("Enter the price of the bike : "))

# Conditions
if price > 100000 :
    # finding the tax on the price
    
    tax = (price /100)*15
    print(tax)
    
    # totalcost price including tax
    total_cost = tax + price
    print(total_cost)

elif price >50000 and price <=100000:
    tax = (price /100)*10
    print(tax)
    total_cost = tax + price
    print(total_cost)
else :
    tax = (price /100)*5
    print(tax)
    total_cost = tax + price
    print(total_cost)


# #### 3. Appect any city from the user and display the monuments in that city?
# > (Argra == Taj Mahal , Delhi == Red Fort , Jaipur == Jal Mahal, Kolkata == Victoria Memorial.)

# In[21]:


city = input("Enter the city name Agra,Delhi,Jaipur,Kolkata")
if city == "Agra" :
    print("Taj Mahal")
elif city == "Delhi" :
    print("Red Fort")
elif city == "Jaipur":
    print("Jal Mahal")
else:
    print("Victoria Mermorial")


# #### 4.Check how many times a given number can be divided by 3 before it is less than or equal to 10?

# In[54]:


## Creating a function 
def divBy3(n):
    times = 0 
    while n > 10:
        n = (n/3)
        if n>=10 :
            times = times +1 
        else:
            print("Not Divisible")
    print(times,"times it can be divided by 3 Before it reaches 10")   

divBy3(13)


# #### 5. Why and when to use while loop give a detailed explanation with example?

# -> While loops are used to repeat a sequence of statements an unknown number of times. 
# This type of loop runs while a given condition is True and it only stops when the condition becomes False.

# In[22]:


## Example of a while loop 
i = 4

while i < 8:
    print(i)
    i += 1


# Explanation - 
# 
# Iteration 1: initially, the value of i is 4, so the condition i < 8 evaluates to True and the loop starts to run. 
#              The value of i is printed (4) and this value is incremented by 1. The loop starts again.
#         
# Iteration 2: now the value of i is 5, so the condition i < 8 evaluates to True. The body of the loop runs, the 
#              value of i is printed (5) and this value i is incremented by 1. The loop starts again.
#         
# Iterations 3 and 4: The same process is repeated for the third and fourth iterations, so the integers 6 and 7 are printed.
#                     Before starting the fifth iteration, the value of i is 8. Now the while loop condition i < 8 evaluates to
#                     False and the loop stops immediately.
#                     (If While loop condition is False at the first iteration then it will to execute the loop)

# #### 6.Use a nested while loop to print three different patters:

# In[16]:


def ranges(high,low):
    
    while high >= low:
        print(high)
        high = high - 1
        y = 0
        x = high
        while x > y:
            print (y, end = " ")
            y = y + 1
ranges(4,2)


# #### 7. Reverse a while loop to display the numbers from 10 to 1?
# 

# In[25]:


i = 10 
while i != 0:
    print(i)
    i -= 1


# #### 8. Reverse a while loop to display the numbers from 10 to 1?

# In[30]:


i = 10 
while i != 0:
    print(i)
    i -= 1


# In[ ]:





# In[ ]:




