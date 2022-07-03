def dominate(x, y):
    flag = False
    for i in range(len(x)):
        flag = flag or (x[i] > y[i])
        if x[i] < y[i]:
            return False
    return flag


def check(result, data):
    for x in result:
        for y in data:
            if y in result:
                if dominate(x, y) or dominate(x, y):
                    return False
            else:
                if dominate(y, x):
                    return False
    print('Correctness Checked!')
    return True