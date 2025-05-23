dict_one = {'key1':{'key2':['DataStructures']}}
dict_two = {'key1':[{'key2':['looks nested',[(['DataStructures'],'DataTypes')]]}]} 
print(dict_one['key1']['key2'][0])
print(dict_two['key1'][0]['key2'][1][0][0])
print(dict_two['key1'][0]['key2'][1][0][0], dict_two['key1'][0]['key2'][1][0][1])

