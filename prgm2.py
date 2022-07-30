name=input('enter a string:')
list1=['a','e','i','o','u']
list2=list()
for i in name:
        if i in list1:
            list2.append(i)
count=len(list2)
print('the  count of vowels is:',count)
percentage=(count/len(name))*100
print("the vowel percentage is:",percentage)
