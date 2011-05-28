'''
Created on May 28, 2011

@author: hongphi
'''

def generate_view(objs):
    objs_len = len(objs)
    lst = []
    row = objs_len >> 2
    for i in range(row):
        temp = []
        temp.append(objs[i << 2])
        temp.append(objs[(i << 2) + 1])
        temp.append(objs[(i << 2) + 2])
        temp.append(objs[(i << 2) + 3])
        lst.append(temp)

    if objs_len % 4 != 0:
        odd = objs_len % 4 - 1
        count = 0
        temp = []
        while odd >= count:
            temp.append(objs[(row << 2) + count])
            count += 1

        while len(temp) < 4:
            temp.append(None)

        lst.append(temp)

    return lst