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




def gradient_descent(x,y):
    m=b=0
    learning_rate=0.001
    iterations=1000
    n=len(x)
    for i in range(iterations):
        y_predicted=m*x+b
        cost=(1/n)*sum([val**2 for val in(y-y_predicted)])
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum(y-y_predicted)

        m-=learning_rate*md
        b-=learning_rate*bd

        print("m:",m,"b:",b,"iterations:",i,"cost:",cost)

x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
gradient_descent(x,y)
    

    return one_hot_encoded, category_to_index

data = np.array(['A', 'B', 'C', 'D', 'E', 'F'])

encoded_data, encoding_map = onehot(data)

print("Original Data:", data)
print("One-Hot Encoded Data:\n", encoded_data)
print("Encoding Map:", encoding_map)
