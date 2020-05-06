import math as m



#weights
#values
#size
#k
#bn
#bw

#hash table
#hash table size
#opt values
#v&w tuples


def BinHash(capacity, weights, values, size):
    k = int(m.pow(2, size - 4))
    bn = int(m.ceil(m.log2(size + 1)))
    bw = int(m.ceil(m.log2(capacity+1)))

    opt_values = []
    HT_Size = 0
    HT = [[] for i in range(k)]

    v_w = []
    for i in range(len(weights)):
        v_w.append((values[i], weights[i]))

def h(i, j, bn, bw):
    ri = format(i, "b")
    rj = format(j, "b")

    while len(ri) < bn:
        ri = "0" + ri
    while len(rj) < bw:
        rj = "0" + rj

    rij = "0b" + "1" + ri + rj
    b2dec = int(rij, 2)

    return b2dec

def insert(i, j, num, k, HT, HT_Size, bn, bw):
    n = h(i, j, bn, bw)
    idx = n % k
    item = (num, n)
    HT[idx].append(item)
    HT_Size += 1

