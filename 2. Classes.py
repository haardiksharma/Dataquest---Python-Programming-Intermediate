## 2. Defining the Dataset Class ##

class Dataset:
    type = "csv"
    
    
dataset = Dataset()
print(dataset.type)

## 3. Passing Additional Arguments to the Initializer ##

# Default display code
class Dataset:
    def __init__(self,data):
        self.type = "csv"
        
        f = open("nfl.csv", 'r')
        self.data = data

f = open("nfl.csv")
nfl_data =  list(csv.reader(f))

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data 

## 4. Adding Additional Behavior ##

"""
As you can see from this example, the benefit of having the self variable is that we can reference it from any instance method we define. Also, using self, you can call the print_data() method within other instance methods by calling self.print_data().
"""
# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data
        
    def print_data(self,num_rows): 
        """ it is important to pass 'self' object as a parameter becuase otherwise              self object will not be identified in the function scope, which is             important inorder to reference other objects."""

        print(self.data [0:num_rows])

# Create an instance of the Dataset class and initialize with the nfl_data.
nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data(5)

## 5. Enhancing the Initializer ##

"""
#Inital Approach
class Dataset:
    def __init__(self, data):
        self.data = data 
    
    def extract_header(self):
        self.header = self.data[0]
        self.data = self.data[1:]
        
        spec = []
        spec.append(self.header)
        spec.append(self.data)
        return spec
    
nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.extract_header()
nfl_header[0]    
    

This works well but there is a problem. Let's say the user keeps calling the extract_header() method continuously. Well, then the second time this is called the correct header will be overwritten and the next row will be set as the header. What we want is to extract the header once and only once in our class.

The best place to do that is to set it in the initializer! Because this method will only get called once on instantiation we know that the header will also only be set once. By setting the header within the initializer, the user doesn't have to worry about calling the method after creating the object and this promotes a better user experience.
"""
        
class Dataset:
    def __init__(self, data): # Enhancing the initializer
        self.header = data[0] 
        self.data = data[1:len(data)]
       
        
nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header
nfl_header

## 6. Grabbing Column Data ##

# Add a method named column that takes in a label argument, finds the index of the header, and returns a list of the column data.
## If the label is not in the header, you should return None.

"""
#Raw Function - straight outta mind:
def column(label):
    indx = -1
    cnt = 0
    clmdata = []
    for i in nfl_data[0]:
        if label == nfl_data[0][cnt]:
            indx = cnt
        cnt += 1
            
    if indx == -1:
        return "None"
    else:
        for elmnt in nfl_data[1:]:
            clmdata.append(elmnt[indx])
        return clmdata
    
year_column = column('year')
year_column[0:5]


"""



# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    # Add your method here.
    
    def column(self,label):
        indx = -1
        clmdata = []
        for idx,value in enumerate (self.header):
            if label == value:
                indx = idx
        
        if indx == -1:
            return None
    
        else:
            for elmnt in self.data:
                clmdata.append(elmnt[indx])
            return clmdata

            
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')



## 7. Count Unique Method ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    # Add your method here.
    
    def column(self,label):
        indx = -1
        clmdata = []
        for idx,value in enumerate (self.header):
            if label == value:
                indx = idx
        
        if indx == -1:
            return None
    
        else:
            for elmnt in self.data:
                clmdata.append(elmnt[indx])
            return clmdata
    
   
    """
    Add a method to the Dataset class called count_unique() that takes in a label arguments.
    
   -- To return a unique set of items from a list, we can use the set() function. The set() function returns only the unique elements in a list:
        weeks = [1,1,1,1,1,2,2,2,2]
        unique_weeks = set(weeks)
        print(unique_weeks)
        >> {1,2}
        print(type(unique_weeks))
        >> set
The resulting object is a set object and while values in a set aren't indexable (unique_weeks[0] will result in an error), the number of values in a set is maintained and updated within the set object. This means that we can use the len() function with set objects:
        print(len(unique_weeks))
        >> 2
    """
    def count_unique(self,label):
        data = self.column(label)
        return len(set(data))
        
        

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')
total_years

## 8. Make Objects Human Readable ##

"""
Add a method to the Dataset class called __str__()
Convert the first 10 rows of self.data to a string and set it as the return value.


   # raw approach
    def drv(self):
        top5 = self.data[0:5]
        strtop = []
        for i in top5:
            strtop.append(str(i))
        return strtop

nfl_dataset = Dataset(nfl_data)
drv = nfl_dataset.drv()
print(drv) #trying to understand the different 
drv

"""


class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
         
    def __str__(self):
        top10 = self.data[0:10]
        strtop = str(top10)
        return strtop

           
    def column(self,label):
        indx = -1
        clmdata = []
        for idx,value in enumerate (self.header):
            if label == value:
                indx = idx
        
        if indx == -1:
            return None
    
        else:
            for elmnt in self.data:
                clmdata.append(elmnt[indx])
            return clmdata
    
    
    def count_unique(self,label):
        data = self.column(label)
        return len(set(data))

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)
nfl_dataset
 
