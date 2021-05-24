# CULLEN WENZLICK
# MAY 24TH COHORT
######################
print("PYTHON AS A CALCULATOR")
print("PART 1\n")

print(2+2)
print(50 - 5*6)
print((50 - 5*6) / 4)
print(8/5)

######  CALCLUATOR #######
print("\nCALCULATOR")
print("PART 2\n")

print(17 / 3)
print(17 // 3)
print(17 % 3)
print(5 * 3 + 2)
print(5**2)
print(2**7)

print("\nCALCULATOR")
print("PART 3\n")

width = 20
height = 5 * 9
print(width * height)
print(4 * 3.75 - 1)

#####    STRINGS #######
print("\nSTRINGS")
print("PART 1\n")

print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"Yes," he said.')
print("\"Yes,\" he said.")
print('"Isn\'t," she said.')

print("\nSTRINGS")
print("PART 2 - Concatenation\n")

prefix = "Py"
print(prefix + "thon123")

print("\nSTRINGS")
print("PART 3 - index position\n")

word = "Python"
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])

print("\nSTRINGS")
print("PART 4 - slicing\n")

print(word[0:2])
print(word[2:5])
print(word[:2] + word[2:])
print(word[:4] + word[4:])
print(word[:2])
print(word[4:])
print(word[-2:])

#####   LISTS #######
print("\nLISTS")
print("PART 1\n")

squares = [1,4,9,16,25]
print(squares)

print("\nLISTS")
print("PART 2 - index/slicing\n")

print(squares[0])
print(squares[-1])
print(squares[-3:])

print("\nLISTS")
print("PART 3 - concatenation\n")

print(squares + [36,49,64,81,100])

print("\nLISTS")
print("PART 4 - mutating list\n")

cubes = [1,8,27,65,125]
print(cubes)
print(4**3)
print(str(cubes[3]) + " is incorrect. Let's fix that.")
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7**3)
print(cubes)

print("\nLISTS")
print("PART 5 - slicing list\n")

letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)

print("replacing some values")

letters[2:5] = ["C", "D", "E"]
print(letters)

print("remove them")

letters[2:5] = []
print(letters)

print("clear the list by replacing all the elements with an empty list")

letters[:] = []
print(letters)

print("len() also applies to lists")

letters = ["a", "b", "c", "d"]
print(len(letters))