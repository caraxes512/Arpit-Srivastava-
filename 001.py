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
def onehot_encode(data1):
    unique_categories = np.unique(data1)

    # Create a dictionary mapping categories to indices
    category_to_index = {category: i for i, category in enumerate(unique_categories)}

    # Create an empty one-hot encoded matrix (number of rows = len(data), number of columns = len(unique_categories))
    one_hot_encoded = np.zeros((data1.shape[0], len(unique_categories)), dtype=int)

    # Populate the one-hot encoded matrix
    for i, category in enumerate(data1):
        one_hot_encoded[i, category_to_index[category]] = 1

    return one_hot_encoded, category_to_index

data = np.array(['A', 'B', 'C', 'D', 'E', 'F'])

encoded_data, encoding_map = onehot_encode(data)

print("Original Data:", data)
print("One-Hot Encoded Data:\n", encoded_data)
print("Encoding Map:", encoding_map)
