test_dict={'codingal':7, 'is':7, 'best':7, 'for':7, 'coding':10}
print("The orignal dictionary : " + str(test_dict))
k=7
res=0
for key in test_dict:
    if test_dict[key]==k:
        res= res+1
print("Frequency of k is: "+str(res))
    