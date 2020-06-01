def fanc(filename):
    n = 0
    m = 0
    l = 0
    res = 0
    try:
        f = open(filename, "r")
    except:
        print('cant open file')
    seq = [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in
           s4.split('\t') if s5 != '']
    print(seq)
    if len(seq) < 3:
        print('not enough numbers')
    for x in seq:
        if (l == 0):
            m = int(x)
        elif (l == 1):
            n = int(x)
        else:
            if (int(x) > min(m, n)) and (int(x) < max(n, m)):
                res += 1
        l += 1
    f.close()
    return res


print(fanc("data.txt"))
