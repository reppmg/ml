n, m, k = list(map(int, str(input()).split(" ")))
classes = list(map(int, str(input()).split(" ")))
new_ar = list(zip(classes, [i for i in range(len(classes))]))
new_ar.sort()
answer = []
for i in range(0, k):
    answer.append([])
i = 0
for (cls, index) in new_ar:
    answer[i % k].append(index)
    i += 1
for line in answer:
    print(len(line), end=" ")
    for index in line:
        print(index + 1, end=" ")
    print()
