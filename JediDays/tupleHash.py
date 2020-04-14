# tuple + hash

n = 2
integer_list = [1 2]

tupleN = tuple(integer_list)
tupleN_hash = hash(tupleN)
integer_list_hash = hash(integer_list)
txt = str(tupleN_hash) + "=!" +  str(integer_list_hash)

print(txt)