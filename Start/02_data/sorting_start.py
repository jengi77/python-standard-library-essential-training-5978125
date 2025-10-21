# using the built-in sorted function to sort data content

test_scores = [82, 67, 94, 73, 79, 86, 58, 91, 89, 71, 88, 77, 84]
test_names = ["Bob", "Doug", "Jane", "Sue", "Ted", "Craig", "Melanie"]

# TODO: perform a simple sort using sorted()
sorted_scores = sorted(test_scores)
print(sorted_scores)

# TODO: explicitly declare a sort order - ascending and descending
sorted_scores = sorted(test_scores, reverse=True)
print(sorted_scores)

# TODO: sorting works on strings, too
sorted_names = sorted(test_names, reverse=True)
print(sorted_names)