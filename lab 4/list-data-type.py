# define a list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# change the value in a list
myFruitList[2] = "orange"
print(myFruitList)

# Exercise 2: Introducing the tuple data type
# The tuple is like a list, but it can't be changed. 
# A data type that can't be changed after it's created is said to be immutable.
# To define a tuple, you use parentheses instead of brackets ([]).
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


# define a dictionary / map
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#accesing a dictionary by name 
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])


favorite_book = {
 "title": "Harry Potter",
 "pages": 223,
 "price": 19.99,
 "is_hardcover": True
 }

## Working with Numbers
#Calculate the total cost of all books
favorite_book = {
 "title": "Harry Potter",
 "pages": 223,
 "price": 19.99,
 "is_hardcover": True
 }

print (favorite_book)

sentence = ["a", "b", "c"]
print(sentence)
sentence.reverse()
print(sentence)