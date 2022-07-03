from data import load_data
from core import dominate, check
from queue import PriorityQueue
import time
import argparse


class modified_tuple(object):

    def __init__(self, _tuple):
        self._tuple = _tuple

    def __lt__(self, that):
        return self._tuple[1] < that._tuple[1]
        # return sum(self._tuple) < sum(that._tuple)


def SFS(data):
    q = PriorityQueue()
    for x in data:
        q.put(x)

    result = [q.get()]
    while not q.empty():
        insert_cur = True
        data_cur = q.get()
        j = 0
        while j < len(result):
            if dominate(data_cur, result[j]):
                result.pop(j)
            elif dominate(result[j], data_cur):
                insert_cur = False
                break
            else:
                j = j + 1
        if insert_cur:
            result.append(data_cur)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    data = load_data('data/qws_normal.txt')
    tic = time.time()
    result = SFS(data)
    toc = time.time()
    assert check(result, data)
    print('SFS algorithm costs: {:.4}s'.format(toc - tic))