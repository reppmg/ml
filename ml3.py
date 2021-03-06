# CART on the Bank Note dataset
from random import seed
from random import randrange
from csv import reader


# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


# Split a dataset based on an attribute and an attribute value
def split_average(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


# Calculate the Gini index for a split dataset
def gini_index(groups, class_values):
    gini = 0.0
    for class_value in class_values:
        for group in groups:
            size = len(group)
            if size == 0:
                gini += 1.0
                continue
            proportion = [row[-1] for row in group].count(class_value) / float(size)
            gini += (proportion * (1.0 - proportion))
    return gini


# Select the best split point for a dataset
def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0]) - 1):
        slice = list(set(row[index] for row in dataset))
        mx = max(slice)
        mn = min(slice)
        threshold = (mx + mn) / 2
        groups = test_split(index, threshold, dataset)
        gini = gini_index(groups, class_values)
        if gini < b_score:
            b_index, b_value, b_score, b_groups = index, threshold, gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}


# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)


# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del (node['groups'])
    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    # check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)
    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)


# Build a decision tree
def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root


def print_tree(node, node_number, lines):
    left, right = node['left'], node['right']
    lines.append("Q {} {} {}".format(node['index'] + 1, node['value'], node_number + 1))
    left_size = 1
    if isinstance(left, int):
        lines.append("C {}".format(left))
    else:
        left_size = print_tree(left, node_number + 1, lines)
    lines[node_number - 1] += " {}".format(node_number + left_size + 1)
    right_size = 1
    if isinstance(right, int):
        lines.append("C {}".format(right))
    else:
        right_size = print_tree(right, node_number + 1 + left_size, lines)
    return left_size + right_size + 1


first_string = list(map(int, str(input()).split(" ")))
feature_count = first_string[0]
classes = first_string[1]
max_depth = first_string[2]
min_size = 0
n = int(str(input()))
dataset = list()
for i in range(n):
    dataset.append(list(map(int, str(input()).split(" "))))

tree = build_tree(dataset, max_depth, min_size)
# print(tree)
tree_text = list()
indx = print_tree(tree, 1, tree_text)
# tree_text[0] += " {}".format(indx)
print(len(tree_text))
for i in tree_text:
    print(i)
