import string
import random

# creating list of dicts
list_of_dicts = []
# set number of dicts
for k in range(random.randint(2, 10)):
    # add random keys and values and number of key-value pairs
    mydict = {chr(random.randint(ord('a'), ord('z'))): random.randint(0, 100) for i in range(random.randint(1, 100))}
    # add dicts to the list of dicts
    list_of_dicts.append(mydict)
print('list of dicts:', list_of_dicts)

#creating temporary dict
tmp_dict = {}
#getting numbers of list elements
for i, d in enumerate(list_of_dicts):
    #iterating each dict in list
    for k, v in d.items():
        if k not in tmp_dict:

            tmp_dict[k] = {"max": v, "index": i, "count": 0}
        elif v > tmp_dict[k]["max"]:
            tmp_dict[k]["max"] = v
            tmp_dict[k]["index"] = i
            tmp_dict[k]["count"] += 1

result_dict = {}
for k, v in tmp_dict.items():
    if v["count"] == 1:
        result_key = k
    else:
        result_key = "%s_%d" % (k, v["index"])

    result_dict[result_key] = v["max"]

print('Result dict:', result_dict)

