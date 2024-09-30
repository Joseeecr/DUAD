def bubble_sort(list_to_sort):
	for outer_index in range(len(list_to_sort) - 1):
		has_made_changes = False
		for inner_index in range(len(list_to_sort) - 1 - outer_index):
			current_element = list_to_sort[inner_index]
			next_element = list_to_sort[inner_index + 1]
			if current_element > next_element:
				list_to_sort[inner_index] = next_element
				list_to_sort[inner_index + 1] = current_element
				has_made_changes = True
			print(f" {outer_index}, {inner_index} current element = {current_element} next element = {next_element}" )
		print(list_to_sort)
		if not has_made_changes:
			return
my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
my_list2 = [1,2,3,4,10,5,6,7,8,9]

bubble_sort(my_list2)

