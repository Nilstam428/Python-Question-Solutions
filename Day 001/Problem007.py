# Q delete a character by its position


# 1. string = immutable ( not change )
# can replace with white space but can't delete that character/placeholder

# str = input("enter something :")
# pos = int(input("enter position :"))
# char = str[pos - 1]
# print(str.replace(char, ""))


# pos->3 index->2
# nilesh  => 3 -> l = char = ""
name = 'ramesh'
name = name.replace(name[2], "")
print(name)