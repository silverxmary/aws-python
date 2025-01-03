# Working with Numeric Data Types

Lab overview
Python makes it easier to do math. In fact, Python is a popular language among data scientists, who must analyze large amounts of data. In this lab, you will explore the basic data types that are used to store numeric values.

In this lab, you will:

Use the Python shell
Use the int data type
Use the float data type
Use the complex data type
Use the bool data type

Exercise 1: Using the Python shell
In the terminal tab, a Python shell can be started by entering the following command:

python3
The Python shell should look similar to the following example.

Python 3.6.12 (default, Aug 31 2020, 18:56:18)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>                                                
The three greater-than symbols (>>>) represent the prompt where the user can enter Python commands. In the following activities, you will practice using the Python shell by issuing some numeric commands.

Adding
Enter the following input:

2 + 2
Press ENTER.

Confirm that you get 4 as output.

Subtracting
Enter the following input

4 - 2
Press ENTER.

Confirm that you get 2 as output.

Multiplying
To multiply, you use the * symbol:

Enter the following input:

2 + 2
Press ENTER.

Confirm that you get 4 as output.

Dividing
To divide, use the / symbol:

Enter the following input:

4 / 2
Press ENTER.

Confirm that you get 2.0 as output.

Exiting the Python shell
To exit the Python shell, enter the following command:

quit()
Exercise 2: Introducing the int data type
To learn more about data types, you will use some built-in functions. A function is a piece of reusable code with a name. You use a function by:

Calling by its name
Including a list of one or more inputs called arguments, which are enclosed in parentheses
Python has several built-in functions that you can use to help you write more useful programs.

A collection of functions is called a library. Python’s collection of built-in functions is called the Python Standard Library.

Editing a Python file
Instead of entering commands one by one in the Python shell, you will edit a text file that contains a sequence of commands:

From the navigation pane of the IDE, choose the file that you created in the previous Creating your Python exercise file section.

In the file, enter the following code:

print("Python has three numeric types: int, float, and complex")
To save the file, choose File > Save.

At the top of the IDE window, choose Run (the Play button).

In the bottom (console) pane of the IDE, confirm that the program prints the message: Python has three numeric types: int, float, and complex

Note: You might need to scroll up to see the console output.

In the terminal tab, you can also run the program by entering the following command, where <lab-python-file-name> is the name of the file that you created for this lab:

python3 <lab-python-file-name>.py
Confirm that the text you wrote is written to standard output.

~ $ python3 <lab-python-file-name>.py                          
Python has three numeric types: int, float, and complex      
Creating a variable
A variable is like a labeled box that stores information. You can change the contents of the box, but the label stays the same. In this activity, you will use the variable name myValue, but will store different data types in that labeled box.

Return to the Python file and on a new line, enter the following code:

myValue=1
Use the print() function to write the value of the variable to the shell. In the context of programming, writing means to add information to the shell.

print(myValue)
To get the data type of the variable, use the type() built-in function:

print(type(myValue))
To combine numbers and text, use the str() built-in function, which converts an argument into a collection of letters called a string. In this instance, you are converting the int (integer) data type into the string data type:

print(str(myValue) + " is of the data type " + str(type(myValue)))
Save the file.

To run the file, choose Run.

In the bottom pane of the IDE, confirm that you have the following output:

Python has three numeric types: int, float, and complex              
1                                                            
<class 'int'>                                                
1 is of the data type <class 'int'>                              
~ $
Note: You might need to scroll up to see the output.

Exercise 3: Introducing the float data type
The int data type only stores whole numbers. If you want to store a number with a decimal, like 3.14, you need a new data type called a float.

Return to the Python file and on a new line, enter the following code:

myValue=3.14
To write the value of the variable to the shell, use the print() function:

print(myValue)
Get the data type of the variable by using the type() built-in function:

print(type(myValue))
To combine numbers and text, use the str() built-in function:

print(str(myValue) + " is of the data type " + str(type(myValue)))
Save the file.

To run the file, choose Run.

In the bottom pane of the IDE, confirm that you see the following output:

Python has three numeric types: int, float, and complex              
1                                                            
<class 'int'>                                                
1 is of the data type <class 'int'>                              
3.14                                                         
<class 'float'>                                              
3.14 is of the data type <class 'float'>                         
~ $ 
Note: Recall that you might need to scroll up to see the output.

Exercise 4: Introducing the complex data type
In advanced math, an imaginary number is a complex number that can be written as a real number that is multiplied by the imaginary unit i. This complex data type is complicated because it must represent a letter and a number, such as 5j.

Return to the Python file and enter the following code:

myValue=5j
Write the value of the variable with the print() function:

print(myValue)
Get the data type of the variable with the type() function:

print(type(myValue))
To combine numbers and text, use the str() built-in function:

print(str(myValue) + " is of the data type " + str(type(myValue)))
Save the file.

To run the file, choose Run.

In the bottom pane of the IDE, confirm that you have the following output:

Python has three numeric types: int, float, and complex              
1                                                            
<class 'int'>                                                
1 is of the data type <class 'int'>                              
3.14                                                         
<class 'float'>                                              
3.14 is of the data type <class 'float'>                         
5j                                                           
<class 'complex'>                                            
5j is of the data type <class 'complex'>                         
~ $ 
Note: Recall that you might need to scroll up to see the output.

Exercise 5: Introducing the bool data type
The bool (Boolean) data type comprises the permanent names True and False, which are represented by the numerals 1 and 0, where 1 = True and 0 = False. The bool data type is implemented as a subset of int and is not considered a real data type. However, in some programming languages, it is implemented as a different data type. These exercises call the Python bool a fake data type.

Return to your text file, and enter the following code:

myValue=True
Write the value of the variable to the shell by using the print() function:

print(myValue)
Get the data type of the variable by using the type() built-in function:

print(type(myValue))
To combine numbers and text, use the str() built-in function:

print(str(myValue) + " is of the data type " + str(type(myValue)))
Save the file.

Choose Run (the Play button).

In the bottom pane of the IDE, confirm that it displays the correct output.

Return to your .py file and enter the following code:

myValue=False
Use the print() function to write the value of the variable to the shell:

print(myValue)
To get the data type of the variable, use the type() built-in function:

print(type(myValue))
To combine numbers and text, use the str() built-in function:

print(str(myValue) + " is of the data type " + str(type(myValue)))
Save the file.

Choose Run (the Play button).

In the bottom pane of the IDE, confirm that you have the following output:

Python has three numeric types: int, float, and complex              
1                                                            
<class 'int'>                                                
1 is of the data type <class 'int'>                              
3.14                                                         
<class 'float'>                                              
3.14 is of the data type <class 'float'>                         
5j                                                           
<class 'complex'>                                            
5j is of the data type <class 'complex'>                         
True                                                         
<class 'bool'>                                               
True is of the data type <class 'bool'>
False                                                         
<class 'bool'>                                               
False is of the data type <class 'bool'>                           
~ $
Congratulations! You have learned about Python’s three numeric data types: int, float, and complex. Additionally, you were introduced to the Python fake data type that is called bool. Note that bool is actually the numerals 0 and 1, which represent the values of True and False.___

End Lab
 Congratulations! You have completed the lab.

Choose  End Lab at the top of this page, and then select Yes to confirm that you want to end the lab.

A panel indicates that DELETE has been initiated... You may close this message box now.

A message Ended AWS Lab Successfully is briefly displayed, indicating that the lab has ended