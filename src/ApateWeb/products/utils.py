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

def generate_select_page(total, current):
    if total < 5:
        ls = []
        for i in range(1, total + 1):
            ls.append([i, i])
        return ls
    if current < 5:
        return [[1, 1],
                [2, 2],
                [3, 3],
                [4, 4],
                ['>', 5]]
    elif current >= 5 and current < total:
        return [['<', current - 1],
                [current - 2, current - 2],
                [current - 1, current - 1],
                [current, current],
                ['>', current + 1]]
    elif current == total:
        return [['<', current - 4],
                [current - 3, current - 3],
                [current - 2, current - 2],
                [current - 1, current - 1],
                [current, current]]
    
            
        
    
