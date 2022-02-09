import random

# creating list of dicts
list_of_dicts = []
# set number of dicts
for k in range(4):
    # add random keys and values and number of key-value pairs
    mydict = {chr(random.randint(ord('a'), ord('z'))): random.randint(0, 100) for i in range(1, 6)}
    # add dicts to the list of dicts
    list_of_dicts.append(mydict)
print(list_of_dicts)

# creating common dicts
common_dict = {}
# iterating dicts
for d in list_of_dicts:
    # iterating keys and values in dicts
    for k, v in d.items():
        # adding keys and values to new dict
        common_dict.setdefault(k, []).append(v)
print(common_dict)

# iterating keys and values in new common dict
for k, v in list(common_dict.items()):
    # filtering values by length to filter duplicated keys
    if len(v) > 1:
        # find max value
        max_v = max(v)
        old_key = k
        # creating new key
        new_key = (k,'_',max_v)
        # converting new key to string
        key_edited = (''.join(map(str,new_key)))
        # replace keys
        common_dict[key_edited] = common_dict.pop(old_key)
        # replace values
        common_dict.update({key_edited : max_v})

print(common_dict)

