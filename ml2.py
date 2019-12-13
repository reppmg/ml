def tp(classes, i):
    return classes[i][i]


def fp(classes, i):
    positive = list(map(lambda x: x[i], classes))
    positive.pop(i)
    return sum(positive)


def fn(classes, i):
    false = list(classes[i])
    false.pop(i)
    return sum(false)


def f_score(x, recalls, precisions):
    if recalls[x] == 0 or precisions[x] == 0:
        return 0
    return 2 * recalls[x] * precisions[x] / (recalls[x] + precisions[x])


k = int(str(input()))
classes = []
for i in range(k):
    classes.append(list(map(int, str(input()).split(" "))))
All = sum(map(lambda x: sum(x), classes))
C = list(map(lambda x: sum(x), classes))
fps = list(map(lambda x: fp(classes, x), range(k)))
tps = list(map(lambda x: tp(classes, x), range(k)))
fns = list(map(lambda x: fn(classes, x), range(k)))
recalls = list(map(lambda x: tps[x] / (tps[x] + fns[x]), range(k)))
precisions = list(map(lambda x: tps[x] / (tps[x] + fps[x]), range(k)))
f_scores = list(map(lambda x: f_score(x, recalls, precisions), range(k)))
f_micro = sum(map(lambda x: f_scores[x] * C[x], range(k))) / All
p_w = sum(map(lambda x: tps[x] * C[x] / (tps[x] + fps[x]), range(k))) / All
r_w = sum(tps) / All
f_macro = 2 * p_w * r_w / (p_w + r_w)
print(f_macro)
print(f_micro)