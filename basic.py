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

str="hello welcome to the pune city"
str=str.split()

print(str[::-1])
l=[len(word) for word in str]
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
print("Even Squre ")
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