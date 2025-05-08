def find_min_index(arr, start, end):
    min_idx = start
    for i in range(start + 1, end):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def swap_elements(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def greedy_selection_sort(arr):
    length = len(arr)
    step = 1
    for i in range(length):
        min_index = find_min_index(arr, i, length)
        swap_elements(arr, i, min_index)
        print(f"Step {step}: {arr}")
        step += 1

def print_array_state(title, array):
    print(f"{title}: {array}")

def main():
    input_array = [64, 25, 12, 22, 11, 90, 45, 33, 5, 17]
    print_array_state("Original Array", input_array)
    greedy_selection_sort(input_array)
    print_array_state("Sorted Array", input_array)

if __name__ == "__main__":
    main()




o/p


Original Array: [64, 25, 12, 22, 11, 90, 45, 33, 5, 17]
Step 1: [5, 25, 12, 22, 11, 90, 45, 33, 64, 17]
Step 2: [5, 11, 12, 22, 25, 90, 45, 33, 64, 17]
Step 3: [5, 11, 12, 22, 25, 90, 45, 33, 64, 17]
Step 4: [5, 11, 12, 17, 25, 90, 45, 33, 64, 22]
Step 5: [5, 11, 12, 17, 22, 90, 45, 33, 64, 25]
Step 6: [5, 11, 12, 17, 22, 25, 45, 33, 64, 90]
Step 7: [5, 11, 12, 17, 22, 25, 33, 45, 64, 90]
Step 8: [5, 11, 12, 17, 22, 25, 33, 45, 64, 90]
Step 9: [5, 11, 12, 17, 22, 25, 33, 45, 64, 90]
Step 10: [5, 11, 12, 17, 22, 25, 33, 45, 64, 90]
Sorted Array: [5, 11, 12, 17, 22, 25, 33, 45, 64, 90]


