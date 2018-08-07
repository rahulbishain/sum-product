from binary_indices import get_binary_indices


def get_partitions(num_list):
    indices = get_binary_indices(len(num_list))
    partition_list = []
    for index in indices:
        part0,part1 = [],[]
        counter = -1
        for val in index:
            counter+=1
            if val==0:
                part0.append(num_list[counter])
            else:
                part1.append(num_list[counter])
        part0 = tuple(part0)
        part1 = tuple(part1)
        # print(part0,part1)
        partition_list.append((part0,part1))
    # print("length = ",len(partition_list))
    return partition_list


if __name__ == "__main__":
    actual_list = [3,5,2]
    actual_list.sort()
    print(actual_list)
    k = get_partitions(actual_list)
    l = k[:int(len(k)/2)]
    print(l)
    print(len(k))