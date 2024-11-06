# Phoenix Valent
    # U3L3
        # Perform black magic and witchcraft commonly known as "merge-sort"


# ≽^•⩊•^≼ Good luck cat thinks I should get a good grade!


def mergeSort(list):
    # list.sort()
    # return list
    #  maybe in a better world...
	
	if len(list) == 1:
		return list
    
	midpoint = int(len(list)/2)
	left = list[:midpoint]
	right = list[midpoint:]

	newLeft = mergeSort(left)
	newRight = mergeSort(right)

	newList = []

	while len(newLeft) > 0 and len(newRight) > 0:

		if newLeft[0] > newRight[0]:
			newList.append(newRight[0])
			newRight.pop(0)

		elif newLeft[0] < newRight[0]:
			newList.append(newLeft[0])
			newLeft.pop(0)

		else:
			newList.append(newLeft[0])
			newLeft.pop(0)
			newList.append(newRight[0])
			newRight.pop(0)

	if len(newLeft) > 0:
		for i in newLeft:
			newList.append(i)
	else:
		for i in newRight:
			newList.append(i)

	return newList

def main():
	nums1 = [6, 2, 5, 8, 3, 4, 8]
	nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
	nums3 = [8, 2, 6, 0, 1, 3]


	for i in [nums1, nums2, nums3]:
		print(f"\nOriginal: {i}")
		newList = mergeSort(i)
		print(f"Sorted: {newList}\n")

if __name__ == "__main__":
	main()