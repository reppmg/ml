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


def f_score(recall, precision):
    if recall == 0 or precision == 0:
        return 0
    return 2 * recall * precision / (recall + precision)


def recall(tp, fn):
    if tp == 0:
        return 0
    return tp/(tp+fn)


def precision(tp, fp):
    if tp == 0:
        return 0
    return tp/(tp+fp)


def divide_or_zero(numerator, denominator):
    if numerator == 0:
        return 0
    return numerator / denominator


k = int(str(input()))
classes = []
for i in range(k):
    classes.append(list(map(int, str(input()).split(" "))))
All = sum(map(lambda x: sum(x), classes))
C = list(map(lambda x: sum(x), classes))
fps = list(map(lambda x: fp(classes, x), range(k)))
tps = list(map(lambda x: tp(classes, x), range(k)))
fns = list(map(lambda x: fn(classes, x), range(k)))
recalls = list(map(lambda x: recall(tps[x], fns[x]), range(k)))
precisions = list(map(lambda x: precision(tps[x], fps[x]), range(k)))
f_scores = list(map(lambda x: f_score(recalls[x], precisions[x]), range(k)))
f_micro = divide_or_zero(sum(map(lambda x: f_scores[x] * C[x], range(k))), All)
p_w = divide_or_zero(sum(map(lambda x: C[x] * precision(tps[x], fps[x]), range(k))), All)
r_w = divide_or_zero(sum(tps), All)
f_macro = f_score(r_w, p_w)
print(f_macro)
print(f_micro)