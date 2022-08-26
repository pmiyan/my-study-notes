def json_traversal(json_dict, parent):
    for key in list(json_dict.keys()):
        sub_str = parent + '_' + key
        lst.append(sub_str)

        if(list(json_dict.values())[0] == None): #base case - no children
            return
        else:
            json_traversal(json_dict[key], sub_str) #recursive case

# TEST:
json_dict = {'a': {'b': {'e' : None}, 'c':{'d':None}}}
parent = list(json_dict.keys())[0] #init a
lst = [parent]
json_traversal(json_dict[parent], parent)
print("The final list is, %s" % lst)