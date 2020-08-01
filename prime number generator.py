# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:57:18 2020

@author: jav_0
"""

def suffix(number):
    to_str=str(number)
    if to_str=="11" or to_str=="12" or to_str=="13":
        return "{}th:".format(number)
    elif to_str[-1]=="1":
        return "{}st:".format(number)
    elif to_str[-1]=="2":
        return "{}nd:".format(number)
    elif to_str[-1]=="3":
        return "{}rd:".format(number)
    else:
        return "{}th:".format(number)

nums_to_generate=input("How many prime numbers would you like to generate? => ")
nums_to_generate=int(nums_to_generate)

primes_found=[2,3]
count1=4
while len(primes_found)<nums_to_generate:
    through=0
    for n in primes_found:
        if count1%n==0:
            break
        elif count1%n!=0:
            through+=1
        if through==len(primes_found):
            primes_found.append(count1)
    count1+=1

for n in range(len(primes_found)):
    print("{:<7}{}".format(suffix(n+1),primes_found[n]))