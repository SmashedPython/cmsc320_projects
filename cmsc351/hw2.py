def getMaxRequests(weight, value, capacity):
    n = len(value)
    # Create a list of tuples (value, weight, value/weight, index)
    items = [(value[i], weight[i], value[i] / weight[i], i) for i in range(n)]
    items.sort(key=lambda x: x[2], reverse=True)

    max_value = 0

    for item in items:
        if capacity == 0:
            break
        elif item[1] <= capacity:
            
            max_value += item[0]
            capacity -= item[1]
        else:
            max_value += item[0] * (capacity / item[1])
            capacity = 0

    return max_value

print(getMaxRequests([1,2,2,3,4],[13,6,15,5,8],7))