def ordinal_encoding(data1):
    category_value = {}
    encoded__data = []
    current_value = 0
    for i in sorted(data1):
        if i not in category_value:
            category_value[i] = current_value
            current_value += 1
        encoded__data.append(category_value[i])

    return encoded__data, category_value



data = ['good',"better",'best','poor','poor']
print(ordinal_encoding(data))


#ONEHOT ENCODING



import numpy as np
def onehot(data1):
    unique_categories = np.unique(data1)

    category_to_index = {category: i for i, category in enumerate(unique_categories)}

    one_hot_encoded = np.zeros((data1.shape[0], len(unique_categories)), dtype=int)

    for i, category in enumerate(data1):
        one_hot_encoded[i, category_to_index[category]] = 1

    return one_hot_encoded, category_to_index

data = np.array(['A', 'B', 'C', 'D', 'E', 'F'])

encoded_data, encoding_map = onehot(data)

print("Original Data:", data)
print("One-Hot Encoded Data:\n", encoded_data)
print("Encoding Map:", encoding_map)
