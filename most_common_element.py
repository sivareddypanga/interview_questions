from collections import Counter
my_list = ["siva", "reddy","sai","siva","sai","sai", "kranthi","reddy","siva", "kranthi","sai", "siva"]


my_c = Counter(my_list)
print my_c.most_common()[0][0]
print my_c.items()