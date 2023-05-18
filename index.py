marks=[12,22,34,55]
stri="task"
num=1
dic={}
for i in marks:
  stri+=str(num)
  dic[stri]=i
  stri="task"
  num+=1
size=len(marks)
sum=0
for i in dic.values():
  sum+=i
avg=sum/size
dic["average"]=avg
print(dic)    