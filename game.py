from prod_list import get_prod_list
import pickle
import os


def get_phase1_output(num):
    # phase1: get products which are ambiguous (must have multiple factor pairs)
    init_prod_dict = get_prod_list(num)
    phase1_prod_dict = dict()
    for key,val in init_prod_dict.items():
        print(key, "and", val)
        if len(val)>1:
            new_val = set()
            for pair in val:
                if pair[0] < num and pair[1] < num:
                    new_val.add(pair)
            if len(new_val) > 1:
                phase1_prod_dict[key] = new_val
                print("added",key)

    print (phase1_prod_dict.keys())
    return init_prod_dict, phase1_prod_dict


# Phase 2: get possible sums based on phase1
def get_phase2_output(phase1_prod_dict):
    phase2_sums_reduced = []
    for sum1 in range(2,2001):
        sum_is_candidate = True
        for num1 in range(1,sum1):
            num2 = sum1 - num1
            prod = num1*num2
            if prod not in phase1_prod_dict.keys():
                sum_is_candidate = False
                break
        if sum_is_candidate:
            phase2_sums_reduced.append(sum1)

    with open("phase2_sums.pkl","wb") as fil:
        pickle.dump(phase2_sums_reduced,fil)
    return phase2_sums_reduced


def get_phase3_output(phase1_prod_dict, phase2_sums):
    phase1_products_reduced = dict()
    for prod,pairs in phase1_prod_dict.items():
        temp_set_for_pairs = set()
        for pair in pairs:
            temp_sum = sum(pair)
            if temp_sum in phase2_sums:
                temp_set_for_pairs.add(pair)
        if len(temp_set_for_pairs) == 1:
            phase1_products_reduced[prod] = temp_set_for_pairs

    with open("phase3_products.pkl","wb") as fil:
        pickle.dump(phase1_products_reduced,fil)
    return phase1_products_reduced


# Phase 4: get possible sums based on phase3
def get_phase4_output(phase3_prod_dict, phase2_sums):
    phase4_sums_dict = dict()
    for sum1 in phase2_sums:
        temp_prod_set = set()
        for num1 in range(1,int(sum1/2)+1):
            num2 = sum1 - num1
            prod = num1 * num2
            if prod in phase3_prod_dict.keys():
                temp_prod_set.add((num1,num2))
        if len(temp_prod_set) == 1:
            phase4_sums_dict[sum1] = temp_prod_set

    with open("phase4_sums.pkl","wb") as fil:
        pickle.dump(phase4_sums_dict,fil)
    return phase4_sums_dict

# REDO REDO REDO REDO REDO REDO REDO REDO REDO REDO REDO REDO REDO REDO
def get_phase5_output(phase4_sums):
    phase5_diff_dict = dict()
    for pair_temp in phase4_sums.values():
        pair = pair_temp.pop()
        if abs(pair[0]-pair[1]) not in phase5_diff_dict.keys():
            phase5_diff_dict[abs(pair[0]-pair[1])] = set((pair,))
        else:
            temp_set = phase5_diff_dict[abs(pair[0] - pair[1])]
            temp_set.add(pair)
            phase5_diff_dict[abs(pair[0] - pair[1])] = temp_set

    with open("phase5_diff.pkl","wb") as fil:
        pickle.dump(phase5_diff_dict,fil)
    return phase5_diff_dict

if __name__ == "__main__":

    if not os.path.exists("initial_products.pkl"):
        init_prod_dict, phase1_prod_dict= get_phase1_output(1001)
        # with open("initial_products.pkl","wb") as fil:
        #     pickle.dump(init_prod_dict,fil)
        # with open("phase1_products.pkl", "wb") as fil:
        #     pickle.dump(phase1_prod_dict,fil)
    else:
        with open("phase1_products.pkl", "rb") as fil:
            phase1_prod_dict = pickle.load(fil)

    if not os.path.exists("phase2_sums.pkl"):
        phase2_sums = get_phase2_output(phase1_prod_dict)
    else:
        with open("phase2_sums.pkl","rb") as fil:
            phase2_sums = pickle.load(fil)
        print(phase2_sums)

    if not os.path.exists("phase3_products.pkl"):
        phase3_products = get_phase3_output(phase1_prod_dict, phase2_sums)
    else:
        with open("phase3_products.pkl","rb") as fil:
            phase3_products = pickle.load(fil)
        print(phase3_products)

    if not os.path.exists("phase4_sums.pkl"):
        phase4_sums = get_phase4_output(phase3_products,phase2_sums)
    else:
        with open("phase4_sums.pkl", "rb") as fil:
            phase4_sums = pickle.load(fil)
        print(phase4_sums)

    if not os.path.exists("phase5_diff.pkl"):
        phase5_diff = get_phase5_output(phase4_sums)
    else:
        with open("phase5_diff.pkl", "rb") as fil:
            phase5_diff = pickle.load(fil)
        print(phase5_diff)