def concatenate_feature_labels(feature, label):
    return [[merge[0][0], merge[0][1], merge[1]] for merge in zip(feature, label)]


x = [[0.2, 0.3], [0.5, 0.4], [0.1, 0.2], [0.2, 0.2], [0.4, 0.5], [0.5, 0.5]]
y = [1, 2, 1, 1, 2, 2]
dataset = concatenate_feature_labels(x, y)
print(dataset)
