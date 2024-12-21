# Working with the String Data Type

Lab overview
In Python, a collection of letters and symbols is called a string. Strings are used often in Python for input and output.

In this lab, you will:

Write Python code that uses the string data type
Concatenate strings
Use the string to get input
Format strings for 


## Exercise 1: Introducing the string data type
A text file containing a logical sequence of commands is a script.

From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section.

In the file, enter the following code:

myString = "This is a string."
print(myString)
Save the file.

Run the file.

Confirm that the script runs correctly and that the output displays as you expect it to.

This is a string.
Extend the Python script by using the built-in function type() to get the data type of the variable. Enter the following code:

print(type(myString))
To convert the return value of type into a string, use the str() built-in function:

print(myString + " is of the data type " + str(type(myString)))
Save the file.

Run the file.

Confirm that the script runs correctly and that the output displays as you expect it to.

This is a string.
<class 'str'>
This is a string. is of the data type <class 'str'>

## Exercise 2: Working with string concatenation
String concatenation is the process of combining two strings into one string. You have actually been doing string concatenation since lab 1, but you didn’t call this process by that term. The plus sign (+) is used to concatenate strings. When the plus sign (+) is used with strings, it behaves differently than when you use it for numbers. In lab 1, you used the plus sign (+) to add numbers. Now, you will use the plus sign (+) to combine, or concatenate, strings.

Return to the Python script.

Create two strings and then concatenate them by entering the following code:

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
Save the file.

Run the file.

Confirm that the script runs correctly and that the output displays as you expect it to.

This is a string.                                            
<class 'str'>                                                
This is a string. is of the data type <class 'str'>
waterfall
​

## Exercise 3: Working with input strings
In coding, information that a user enters is known as input. You will use a built-in function named input() to get information from the user. The input() function will pause the code until a user enters a string and presses ENTER. Return to the Python script:

Enter the following code:

name = input("What is your name? ")
Use the print() function to write the value of the variable to the shell:

print(name)
Save the file.

Run the file.

Confirm that the script runs correctly and that the output displays as you expect it to.

This is a string.                                            
<class 'str'>                                                
This is a string. is of the data type <class 'str'>              
waterfall                                                    
What is your name? Maria                                     
Maria   
​

## Exercise 4: Formatting output strings
When your script wants to communicate information back to the user, it is called output. You have been using the print() function to write output to the shell. You will create a survey and output the information that it collects back to the user.

Return to the Python script and enter the following code:

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
You have been using the print() function with only one variable, but you can also use it with multiple variables to format a string. Enter the following code:

print("{}, you like a {} {}!".format(name,color,animal))
Save the file.

Run the file.

The Python shell has stopped and is waiting for your input.

Enter a name and press ENTER.

Next, you are asked for your favorite color. Enter a color and press ENTER.

Next, you are asked for your favorite animal. Enter an animal and press ENTER.

Finally, the script prints a formatted string to the user by using the three pieces of information that you provided. Confirm that the output in the shell looks like the following output.

This is a string.                                            
<class 'str'>                                                
This is a string. is of the data type <class 'str'>              
waterfall                                                    
What is your name? Maria                                     
Maria                                                        
What is your favorite color?  blue                           
What is your favorite animal?  dog                           
Maria, you like a blue dog!  
Note: The final print() statement uses the format() function. In the format() function, the opening and closing braces ({}) act as placeholders for the variables that will be passed to (that is, put between) the function's parentheses.

Congratulations! You have used Python to concatenate strings, take input from the user, and output a formatted string.

