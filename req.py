import requests
import json
from pprint import pprint
r=requests.get("http://saral.navgurukul.org/api/courses")
a = json.loads(r.text)
with open ("courses.json","w") as file:
    json.dump(a,file,indent=4)
data_get = a["availableCourses"]
r=open("courses.json","r")
data=r.read()
b=json.loads(data)
i=1
while i<len(b["availableCourses"]):
    
    x=(b["availableCourses"][i]["name"])
    print(i,x)
    i=i+1
select_course=int(input("Enter a num="))
j=0
while j<len(b["availableCourses"]):
    if select_course==j:
        print("name-", b["availableCourses"][j]["name"],"id-", b["availableCourses"][j]["id"])
        id=b["availableCourses"][j]["id"]
        print(id)
    j=j+1
call_second=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")
y= json.loads(call_second.text)
with open ("second_API.json","w") as json_file:
    json.dump(y,json_file,indent=4)

call_third=requests.get("http://saral.navgurukul.org/api/courses/"+str(id)+"/exercises")

z=json.loads(call_third.text)

with open ("third_API.json","w") as my_file:
    json.dump(z,my_file,indent=4)
read_json=open("third_API.json","r")
read=read_json.read()
j=0
emp_str="  "
count=0
lis=[]
while j<len(z["data"]):
    print(j+1,z["data"][j]["name"])

    if z["data"][j]["childExercises"]==[]:
        print(emp_str,z["data"][j]["slug"])
        lis.append(z["data"][j]["slug"])

    else:
        m=0
        while m<len(z["data"][j]["childExercises"]):
            print("  ",m+1,z["data"][j]["childExercises"][m]["name"])
            m=m+1
    j=j+1
content=int(input("Enter content number="))
call_fourth=("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=request_using-json")
call_fourth=call_fourth.replace("request_using-json",(lis[content-1]))

call_fourth=call_fourth.replace("75",str(id))
print(call_fourth)
call=requests.get(call_fourth)
print(call.text)

user=input("Enter previous or next=")
if user=="n":
    call_fourth=("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=request_using-json")
    call_fourth=call_fourth.replace("request_using-json",(lis[content-1+1]))

    call_fourth=call_fourth.replace("75",str(id))
    print(call_fourth)
    call=requests.get(call_fourth)
    print(call.text)
else:
    call_fourth=("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=request_using-json")
    call_fourth=call_fourth.replace("request_using-json",(lis[content-2]))

    call_fourth=call_fourth.replace("75",str(id))
    print(call_fourth)
    call=requests.get(call_fourth)
    print(call.text)