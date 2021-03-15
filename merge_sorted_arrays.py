odd = [1,3,5,7,9]
even = [2,4,6,8]

odd_count = 0
even_count = 0

merged_sorted_array = []

while odd_count < len(odd) and even_count < len(even):
    if odd[odd_count] < even[even_count]:
        merged_sorted_array.append(odd[odd_count])
        odd_count = odd_count + 1
    else:
        merged_sorted_array.append(even[even_count])
        even_count = even_count + 1

merged_sorted_array = merged_sorted_array + odd[odd_count:] + even[even_count:]

print(merged_sorted_array)
