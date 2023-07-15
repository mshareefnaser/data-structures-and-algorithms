from hashtable import HashTable 

def left_joins(hash1, hash2):
    joined = []

    for key in hash1.keys():
        vals = []
        vals.append(key)
        vals.append(hash1[key])

        if key in hash2:
            vals.append(hash2[key])
        else:
            vals.append('NONE')

        joined.append(vals)

    print(joined)
    return joined


