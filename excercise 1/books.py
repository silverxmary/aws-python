# Part 1: Numbers
books_owned = 5              # Integer
book_price = 24.99          # Float
total_pages = 1250          # Integer

# Part 2: Strings
book_name = "Alice in Wonderland"
author_name = "Lewis Carroll"
# Part 3: Collections
my_books = ["Harry Potter", "Percy Jackson", "Charlotte's Web"]
book_categories = ("Fantasy", "Adventure", "Mystery")
favorite_book = {
 "title": "Harry Potter",
 "pages": 223,
 "price": 19.99,
 "is_hardcover": True
 }

## Working with Numbers
#Calculate the total cost of all books
total_cost_of_boks = book_price * books_owned
print("Total cost of books:", total_cost_of_boks)

#Calculate the average pages per book
average_pages = total_pages / books_owned
print("averages pages:", average_pages)


## Working with Strings
#If each book takes 3 days to read, calculate how many days to read all books
days = 3
days_to_read_books = books_owned * days
print("it will take to read all books: ", average_pages, " Days")
#Create a full_title by combining book_name and author_name with " - " between them
full_title = book_name +" - "+ author_name
print("full title of book: ", full_title)

#Convert book_name to all uppercase letters
book_name_upper = book_name.upper()
print(book_name_upper)

#Count how many letters 'a' appear in book_name
count = 0;     
for i in range(0, len(book_name_upper)):  
    if(book_name[i] == 'A'):  
        count = count + 1; 
         
print("has the letter a ", count, " times")
#Convert author_name to all lowercase letters
book_name_lower = book_name.lower()
print(book_name_lower)

## Working with Collections
#Add "The Hobbit" to the my_books list
print(my_books)

my_books.append("The hobbit")

print(my_books)
#Print the second category from book_categories
print(book_categories[1])

#Add a new "year" key to favorite_book with the value 1997

#Print the first book and last book from my_books

#Create a new list called book_prices with these prices: 19.99, 24.99, 12.50, 34.99, 9.99

#Calculate the average price if all books in book_prices had a 20% discount 2
