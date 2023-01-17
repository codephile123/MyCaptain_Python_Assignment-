import operator
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

    cd = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    for i in cd:
        print(i[0], '=', i[1], end='  ')
most_frequent('mississippi')
