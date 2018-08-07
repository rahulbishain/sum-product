count = 0


def get_binary_indices(n):
    global count
    # print("n=",n)
    binary_indices = []
    if n == 1:
        binary_indices.append([0])
        binary_indices.append([1])
        return binary_indices
    if n>1:
        new_index_pre0,new_index_pre1 = [],[]
        for curr_list in get_binary_indices(n-1):
            count +=1
            temp_list0 = curr_list.copy()
            temp_list1 = curr_list.copy()
            temp_list0.insert(0, 0)
            temp_list1.insert(0, 1)
            new_index_pre0.append(temp_list0)
            new_index_pre1.append(temp_list1)
        return new_index_pre0+new_index_pre1


if __name__ == "__main__":
    print(get_binary_indices(6))
    print(count)