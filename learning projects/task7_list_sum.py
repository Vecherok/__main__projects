def list_sum(l):
    sum = 0
    for i in l:
        sum += list_sum(i) if isinstance(i,list) else i     
    return sum


l = [1,2,[[3,[4,[[5],6]],[7]],8],9]

print(list_sum(l))

