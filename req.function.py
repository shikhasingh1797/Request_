import requests
import json
from pprint import pprint
def first ():
    global load2
    data1=requests.get("http://saral.navgurukul.org/api/courses")
    data_load = json.loads(data1.text)
    with open ("courses_function.json","w") as file:
        json.dump(data_load,file,indent=4)
    data_get = data_load["availableCourses"]
    data1=open("courses_function.json","r")
    data=data1.read()
    load2=json.loads(data)
    i=1
    while i<len(load2["availableCourses"]):        
        x=(load2["availableCourses"][i]["name"])
        print(i,x)
        i=i+1       
def topic():
    global id
    select_course=int(input("Enter topic num="))
    j=0
    while j<len(load2["availableCourses"]):
        if select_course==j:
            topic1=("name-", load2["availableCourses"][j]["name"],"id-", load2["availableCourses"][j]["id"])
            id=load2["availableCourses"][j]["id"]
            print(id)
        j=j+1
    return topic1
first()
def second():
    global z
    call_second=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")
    y= json.loads(call_second.text)
    with open ("second_API_function.json","w") as json_file:
        json.dump(y,json_file,indent=4)
    call_third=requests.get("http://saral.navgurukul.org/api/courses/"+str(id)+"/exercises")
    print(call_third)
    z=json.loads(call_third.text)
    with open ("third_API_function.json","w") as my_file:
        json.dump(z,my_file,indent=4)
second()
def third():
    read_json=open("third_API_function.json","r")
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
def main():
    first()
    print(topic())
    second()
    third()
main()