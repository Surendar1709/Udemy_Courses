'break continue pass'
# break 
for i in range(0,10):
    if i==5:
        break
    else:
        print(i)

print()
print()
#continue
for i in range(0,20):
    if i%2!=0:
        continue
    else:
        print(i)

#pass 
for i in range(0,10):
    if i%2!=0:
        pass # just pass dont do anything 
    print(i)

#nested  for loop

#sample table upto 10 
for i in range(1,11):
    for j in range(1,11):
        print(f"i{i},j{j}={i*j}")

#calcualte the sum of  natural no using for loop
print("using the for loop")
num=11
sum=0
for i in range(0,num):
    sum=sum+i
    print("after every iteration ",sum)

print(sum)

print("using the while loop ")

# using  the whille loop 
num=10
sum=0
count=1
while count<=num:
    sum+=count
    count+=1
print("sum of the natural no is ",sum)

print("prime number between 1 to 100")

for i in range(1,101):
    for j in range(2,i):
        if i%j==0:
           break
    else:
        print(i ,"is prime no ")    

print("using while loop ")

num=1
while num<=100:
    i=2
    while i<=num:
        if num%i==0:
            break
        i+=1
    else:
        print(num,"is prime")
    num+=1

str="hello how  are you "
words=str.split()
for word in words:
    print(word[-1],end=" ")

print()
# list 
double=[x**x for x in range(4)]
print(double)

list =["Apple","mango","Banan","orage","pomogranite","pineapple"]
print(list)
list.append("grapes")
print(list)
list.extend(["cherry","dragonfruit"])
print(list)
list.insert(2,"watermelon")
print(list)
list.remove("cherry")
print(list)
p=list.pop()
print(p)
print(list)
list.sort 
print("sorted list")
print(list)
list.reverse()
print(list)

# reversing the list without usin the inbuild function 

print("reversing the list without usin the inbuild function ")
start=0
end=-1
while start<end:
    temp=list[start]
    list[start]=list[end]
    list[end]=temp
    start+=1
    end-=1

print(list)
num=[1,2,3,4,5,6,7,8,9,10]
print(num[2:5])
print(num[:5])
print(num[5:])
print(num[::2])
print(num[::-1])

# iterating throgh the loop 
for f in list:
    print(f)

#iterating with index no also 

for index ,f in enumerate(list):
    print(index,f)

for i, n in enumerate(num):
    print(i,n)

#list compretion

l=[]
for i in range(51):
    if i%2==0:
        l.append(i)
print(l)

ln=[]
for i in range(10):
    i=i**2
    if i%2==0:
        ln.append(i)
print(ln)

# basic syntax is for list compresheion list =[expression for item in iterable]
                                        #list list =[expression for  item in iterable condition]

# using the list compreshion 
lst=[i**2 for i in range(10) if i%2==0]
print(lst)

# nested list compreshion 

l1=[1,2,3,4]
l2=["a","b","c","d"]
pair=[[i,j] for i in l1 for j in l2]
print(pair)

#list  comprehsion with function call 

words=["hello","hi","welcome","join","wakeup"]
lenth=[len(w) for w in words]
print(lenth)

str1="hello welcome to the pune city"
str=str1.split()

print(str1[::-1])
l=[len(word) for word in str1]
print(l)
s=0
for i in l:
    s=s+i
print(s)


## set in python 
# unordered collection of uniques element  represent using the curly braces 

my_set=set()
print(type(my_set))
setn={1,2,3,4,5,5,5,6,7,8}
print(setn)
setn.add(9)
print(set)
# list to set
set_new=[90,490,322,445,6,7,7,56]
new=set(set_new)
print(new)
print(type(new))

new.add(555)
# 555 added to the set
print(new)
#555 remove from the set 
new.remove(555)
print(new)
new.discard(555) #----> wont return error if element is not present 
print()
re=new.pop()
print(re)
print(new)

new.clear() # to remove the all the element 
print(new)

# set membership test check the  particular  elemtn is member  or not of the set 
set2={1,2,3,4,5,6,7}
print(3 in set2)
print(10 in set2 )

#mathametical operation in set 
s1={1,2,3,4,5}
s2={5,6,7,8,9}

#union
union=s1.union(s2)
print(union)
#intersection
intersection=s1.intersection(s2)
print(intersection)

s1.intersection_update(s2) # update the set with comman element 
print("update the set with comman element")
print(s1)

# diffrence

ss1={1,2,3,4,5,6,7,8}
ss2={6,7,8,9,10,11,12,13}
print(ss1.difference(ss2)) # return the unique elements 
print(ss1)

# in two set common elements will be romved uniquese  element in the both set will be present  in symmetric diffrenence
print(ss1.symmetric_difference(ss2))

#subset 
print(ss1.issubset(ss2))
#super set 
print(ss1.issuperset(ss2))

#count the uniques words in the text 
text="this is python  sets to  Totorial  videos about sets"
words=text.split()
unique=set(words)
print(len(unique))

# Dictinary unordered collection of key:value pairs 
bio_data={"name":"Marco","age":30,"mobile":9344470438}
print(bio_data)


#accessing the element of the Dictonary

print(bio_data["mobile"])
#accessing the element of the Dictonary using the get() method 
print(bio_data.get("age"))
print(bio_data.get("Gender"))
print(bio_data.get("Gender","not availble"))

# modify the  element of the dictornay ,add ,update,delete 
bio_data["age"]=30 #update
bio_data["address"]="Nilgiris ooty Tamil Nadu " # add
del bio_data["name"]
print(bio_data)

# dict methods 

print(bio_data.keys())
print(bio_data.values())
print(bio_data.items())

#copy 
student={"name":"Vijay","Age":18,"Dept":"cse"}
print(student)
student_copy=student
student_copy["name"]="Ajith"
print(student)
print(student_copy)


#copy 
student1={"name":"Vijay","Age":18,"Dept":"cse"}
print(student1)
student_copy1=student.copy()
student_copy1["name"]="Ajith"
student_copy1["Dept"]="EEE"
print(student1)
print(student_copy1)

# iterating  through the  Dict

for key in  student_copy1.keys():
    print(key)
print()
for value in student_copy1.values():
    print(value)
print()
for item in student_copy1.items():
    print(item)
print()

for key,value in student_copy1.items():
    print(f"{key}:{value}")

# nested Dict 
database={"stu1":{"name":"surendar","Age":25,"Dept":"Ai"},
          "stu2":{"name":"peter","Age":30,"Dept":"web"},
          "stu3":{"name":"Dominic","Age":30,"Dept":"python"}}
print(database["stu1"]["name"])

for key,values in database.items():
    print(key,values)

for studentid ,studentinfo in database.items():
    print(studentid)
    for key,value in studentinfo.items():
        print(f"{key}:{value}")
    print()

# dict comphression 
squre={x:x**2 for x in range(6)}
print(squre)

print("Even Squre ")
evenS={x:x**2 for x in range(10) if x%2==0}
print(evenS)
print("odd Squre ")
odds={x:x**2 for x in range(10) if x%2!=0}
print(odds)

# count the Frquency of the no using dict

numbers=[1,2,2,2,3,3,3,3,4,4,4,5,5]

frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1

print(frequency)


t="apple banana apple orange banana apple Mango pineapple orange  Mango"
t1=t.split()
f={}
for words in t1:
    if words in f:
        f[words]+=1
    else:
        f[words]=1
print(f)

# merge dict 
d1={"A":1,"B":2}
d2={"C":3,"D":4}
merge={**d1,**d2}
print(merge)

# tuples  similar to  list  ordeted   collection of immutable elements 
t=()
print(type(t))

t1=[20,'hello',3.5]
t2=tuple(t1)
print(type(t2))
T=(1,2,3,4,5,6,7,8,9,10)
for index, i in enumerate(T):
    print(index,i)
print(T[::])
print(T[::-1])
print(T[5:])
print(T[::2])
print(T[-1:-5:-1])
# tuple concadination 
Tuple1=(1,2,3,4,2)
Tuple2=("A","B","C","D")
con=Tuple1+Tuple2
print(con)
#Tuple methods 
print("2 is present ",Tuple1.count(2),"time")
print(Tuple2.index("B"))
# packing elements in tuple 
pack=1,"software",2.5,True
print(pack)
print(type(pack))

# unpacking in tuple
a,b,c,d=pack
print(a)
print(b)
print(c)
print(d)
#unpacking with star 
ff=(10,20,30,40,50,607,80,89)
first,*middle,star=ff
print(first)
print(middle)
print(star)
# nested list 
nested_list = [
    [1, 2, 3],
    ["apple", "banana", "cherry"],
    [True, False, True]
]

for item in nested_list:
    print(item)
    print()
    for i in item:
        print(i)

print(nested_list[1][1]) # tp pick Banana 
nested_tuple = (
    (1, 2, 3),
    ("apple", "banana", "cherry"),
    (True, False)
)

# ACCESING Elemtents in the tuple nested tuple
print(nested_tuple[1][2]) # to pickl cherrey

# list with real word example  simple to do list 
to_do_list=["Jokking","eating_Break_fast","postletter","paythe_bill"]
print(to_do_list)
# add two more task to list 
to_do_list.append("have launch")
print(to_do_list)
# removeing the completed task 
to_do_list.remove("eating_Break_fast")
to_do_list.remove("Jokking")
# Add remainder
if "paythe_bill" in to_do_list:
    print("Dont forgot to pay the Bill ")
    to_do_list.remove("paythe_bill")

#remaingn task in the list 

print(to_do_list)

# managing the student Grades 
from math import* 
grades=[85,92,75,88,95]

# adding the new grade
grades.append(70)
print(85+92+75+88+95+70)
# Find the average grade 
sum_l=0 
for g in grades:
    sum_l+=g
print(sum_l)
ave_grade= sum_l /len(grades)
print(ave_grade)
print(min(grades),"is the minimum Grade")
print(max(grades),"is the maximun Grade")

# collecting  user Feed back
feed_back=["Excellent","Good","Great","Average","notgood","Bad","very good","outstanding"]
print(feed_back)
feed_back.append("not satified with service")

postive=[1 for f  in feed_back if "great" in f.lower() or "outstanding" in f.lower()]
print("postive feed back",postive)
negative=[1 for f in feed_back if "bad" in f.lower() or "not" in f.lower()]
print("negative Feed back",negative)


# function
"Function is the block of code  that perform the certain task  help to reuse the code organizing the code  improve the readbiltiy"

# def function_name(para):
#     "Doc string to tell the what the function is does"
#     return statement

# Basic addtion functin 
def add(a,b):
    c=a+b
    return c

r=add(50,30)
print(r)

# sub 
def sub(a,b):
    return a-b
r=sub(20,5)
print(r)
# default argrment 

def greet(name="Guest"):
    print(f'hello {name} welcome the class')

greet("Ramesh")
greet()
# postional argument 
# keyword length postitional argument 
def print_arg(*args):
    for item in args:
        print(item)
print_arg(1,2,3,4,5,6,7,8,9,"hi","hello")
# keyword arguemtnt 

def print_details(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")
print_details(name="sun",age="450",add="Galaxy center point")

print("keyword and postitional argmentts")

def function1(*args,**kwargs):
    for p in args:
        print(f"postitional args{p}")
    for k,v in kwargs.items():
        print(f"keywordargments   {k} : {v}")

function1(1,2,3,4,5,6,7,8,9,"hi","hello",name="moon ",age="300",add="milkyway")

#return,multple values in the function 
def mul(a,b):
    return f" mul of {a}:{b}",a*b
result=mul(4,5)
print(result)

#simple function 
def cover_temp(temp,unit):
    " convert the tempearut between  celius to fraghet  "
    if unit.lower()=="c":
        return temp *(9/5)+32 # celcius to Framhent 
    elif unit.lower()=="f":
        return temp *(5/9)-32 # frament to celsis 
    else:
        return None
    
print(cover_temp(45,'F'))
print(cover_temp(45,'c'))

# password strenth checker 
def is_strong(password):
    if len(password)<8:
        return False
    elif not any( char.isdigit() for char in password):
        return False
    elif not any( char.islower() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char in "!@#$%^&*()" for char in password):
        return False
    return True

result=is_strong("Aandd$123")
print(result)

# Calcualting the total cost the item in the cart 

def price_calcualte(cart):
    total_price=0
    for item in cart:
        total_price+=item["price"]*item["Quantity"]
    return total_price

cart=[{"name":"Apple","price":50,"Quantity":5},
      {"name":"Banana","price":30,"Quantity":3},
      {"name":"Mango","price":50,"Quantity":4},
      ]
total=price_calcualte(cart)
print(total)

# to check pallindrom 

def palindrom(var):
    orginal=var
    if var[::-1]!=orginal:
        return False
    else:
        return True

result=palindrom("aba")
print(result)
result=palindrom("racecars")
print(result)


def is_pallindorm(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
    
print(is_pallindorm("a man a plan a canal panama"))
print(is_pallindorm("hello"))

#Factroal of the no 

def fact(num):
    if num==0:
        return 1
    return num * fact(num-1)
f=fact(5)
print(f)

def Word_Frequency(filepath):
    word_f={}
    with open(filepath,'r') as file :
        for line in file:
            words=line.split()
            for word in words:
                word=word.strip()
                if word in word_f:
                    word_f[word]+=1
                else:
                    word_f[word]=1
        return word_f
filepath=r"C:\Users\surendar.s\Music\python_leanring\Udemy_Courses\sample.txt"
result=Word_Frequency(filepath)
print(result)
 
# Validated  email address  
import re 
def emailvalid(email):
    pattern=r'^[A-Za-z0-9._+-]+@[a-zA-z0-9]+\.[a-zA-z0-9-.]+$'
    return re.match(pattern,email) is not None
print("Validationg email")
print(emailvalid("surendarinbox@gamil.com"))

print(emailvalid("ssssooy"))

# lamda functin  
"small ananomous function with the lambda keyword can  have  any no of arguments and single expressin "
#syntax
# lamda argurments: expression 
additon=lambda x,y,z:x+y+z
print(type(additon))
print(additon(30,32,8))

#map function is inbuld function that apply give function to the all the items in the iterables like list tuple 
nums=[1,2,3,4,5]
squere=tuple(map(lambda x:x**2,nums))
print(squere)

def square(num):
    return num*num

print(square(5))
nums=[1,2,3,4,5,6,7,8,9,10]
sq=tuple(map(square,nums))
print(sq)

# map with multiple iterables 
m1=[1,2,3]
m2=[4,5,6]
ml=tuple(map(lambda x,y:x+y,m1,m2))
print(ml)

#conver list of string into  the num 

li=["1",'2','3','4','5']
no_list=tuple(map(int,li))
print(no_list)

# convert list to lower to upper of list of strings 
# lower=["apple","Banana","cherry"]
# uppper=tuple(map(str.upper(),lower))
# print(uppper)
def get_name(person):
    return person["name"]
people=[{"name":"surendar","age":30},{"name":"gokul","age":45}]

nnn=tuple(map(get_name,people))
print(nnn)

# filter function  used to filter the item from the squance  with ceratin condtion 

# fileter with lamda function 
commontuple=[1,2,3,4,5,6,78,8.90,10]
filter_list=tuple(filter(lambda x:x>5 ,commontuple))
print("values filtered from the list",filter_list)

# filter with multiple conditon 

even_and_greaterthan5=tuple(filter(lambda x:x>5 and x%2==0,commontuple))
print(even_and_greaterthan5)
# apply filter in dict 
people = [
    {"name": "surendar", "age": 20},
    {"name": "gokul", "age": 45},
    {"name": "arun", "age": 30},
    {"name": "meena", "age": 27},
    {"name": "karthik", "age": 22},
    {"name": "priya", "age": 35}
]


dict_filter=tuple(filter(lambda x :x["age"]>25,people))
print(dict_filter)

