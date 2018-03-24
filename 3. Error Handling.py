## 2. Sets ##

"""
Formal introductio to set
A set behaves very similarly to a list. However, if you add an element to a set that it already contains, the set will ignore it. Also, the items in a set are unordered, while each item in a list has an index.

You can add items to a set using the add() method:
    unique_animals.add("Tiger")
Finally, you can remove items from a set with the remove() method:
    unique_animals.remove("Dog")
If we want to convert a set to a list, we can use the list() method:
    list(unique_animals)
"""
gender = []
for i in legislators:
    gender.append(i[3])

gender = set(gender)    
print(gender)    

## 3. Exploring the Dataset ##

#Extract the party column from legislators and convert it to a set. Assign the result to party.

party = []
for i in legislators:
    
    party.append(i[len(i)-1])
                   
party = set(party)

#Print out party and inspect the values.
print(party)
#Print count of unique parties.
print(len(party))

#Print out legislators and inspect the data.
print(legislators)

## 4. Missing Values ##

"""
Missing values are very common in real world data analysis, since the people compiling the datasets often don't have full information.

You can use one of the following strategies to address missing data:

    Remove any rows that contain missing data.
    Populate the empty fields with a specified value.
    Populate the empty fields with a calculated value.
    Use analysis techniques that work with missing data.
  
  
Here's how we could replace any missing values in the party column with the string No Party:

rows = [
    ["Bassett", "Richard", "1745-04-02", "M", "sen", "DE", "Anti-Administration"],
    ["Bland", "Theodorick", "1742-03-21", "", "rep", "VA", ""]]
    
for row in rows:
    if row[6] == "":
        row[6] = "No Party"
"""

#Replace any missing values in the gender column of legislators with the string M.
for i in legislators:
    if i[3] == "":
        i[3] = "M"
legislators[:10]
    
    

## 5. Parsing Birth Years ##

"""
As you may have noticed, the birthday column has the format 1820-01-02, which is hard to work with. However, it's common to reformat values to simplify them. In this case, we can split the date into its component parts:


date = "1820-01-02"
parts = date.split("-")
print(parts)
"""
birth_years = []
for i in legislators:
    bdate = []
    bdate = i[2].split("-")
    birth_years.append(bdate[0])
    

birth_years[:10]

## 6. Try/except Blocks ##

"""
If you surround the code that causes an error with a try/except block, the error will be handled, and the code will continue to run:
try:
    int('')
except Exception:
    print("There was an error")
In the example above, the Python interpreter will try to run int(''), and generate a ValueError. Instead of stopping the code from executing, it will be handled by the except statement, which will print the message There was an error. The Python interpreter will continue to run any lines of code that come after the except statement.

"""
try:
    float("hello")
except:
    print("Error converting to float.")











## 7. Exception Instances ##

"""
-Write a statement that attempts to convert an empty string to an integer, and wrap it in a try/except block.
-Capture the Exception instance.
-Print the type of the Exception instance.
-Convert the Exception instance to a string and print it out.
"""

try:
    int(" ")
except Exception as excp:
    print(excp)
    print(type(excp))
    print(str(excp))
    

## 8. The Pass Keyword ##

"""
Python statement that ends in a colon (:) needs to have an indented body below it.
we can't just leave out the print statement to avoid printing lots of errors messages.
Instead, we can use the pass keyword to avoid generating an error and keep the code running:

        try:
            int('')
        except Exception:
            pass
            
While the pass keyword doesn't actually do anything, it's a valid statement body. It offers a solution when we don't want an error to stop code execution, but also don't want to do anything in the except statement body.

"""

"""
Excercies- Loop through each element in birth_years.
Assign the element to year.
Try to convert year to an integer using the int() function.
Wrap the conversion in a try/except block.
Use the pass keyword in the except statement body.
Append year to converted_years.
"""

converted_years = []
for i in birth_years:
    year = i
    try:
        year= int(year)
    except:
        pass
    converted_years.append(year)
    
converted_years[:5]





