from adminportal.models import Recruiter
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from adminportal.models import Recruiter,Add_Question
from collections import defaultdict
from userportal.models import Analysis,Resume,UserData

# Create your views here.

def admin_index(request):
  return HttpResponseRedirect(reverse("admin_login"))

def admin_login(request):
  if request.method=="POST":
    username=request.POST["username"]
    password=request.POST["password"]

    if Recruiter.objects.filter(username=username,password=password).exists():
      request.session["user"]=username
      return render(request,'adminportal/base_admin.html')
    else:
      return render(request,'adminportal/admin_login.html')


  return render(request,'adminportal/admin_login.html')

def admin_logout(request):
  return HttpResponseRedirect(reverse("admin_login"))

def add_question(request):
  if request.method=="POST":
    question=request.POST["question"]
    option_A=request.POST["option_A"]
    option_B=request.POST["option_B"]
    option_C=request.POST["option_C"]
    option_D=request.POST["option_D"]
    correct_answer=request.POST["correct_answer"]
    tag=request.POST["tag"]

    Add_Question.objects.create(
      Question=question,
      Option_A=option_A,
      Option_B=option_B,
      Option_C=option_C,
      Option_D=option_D,
      Correct_Answer=correct_answer,
      Tag=tag
    )




  return render(request,'adminportal/add_question.html')

def admin_dashboard(request):
  questions_dict=defaultdict(list)
  for question_object in Add_Question.objects.all():
    tag=question_object.Tag
    questions_dict[tag].append(question_object)
  # criteria=None
  # if request.session["criteria"]:
    criteria=request.session.get("criteria")

  return render(request,'adminportal/admin_dashboard.html',{
    "questions_dict":questions_dict.items(),
    "criteria":criteria
  })


def view_questions(request,Tag):
  questions=[]
  count=1
  for question_object in Add_Question.objects.all():
    tag=question_object.Tag
    if tag==Tag:
      l=[]
      l.append(question_object)
      l.append(count)
      questions.append(l)
    count=count+1

  objects=Add_Question.objects.all()
  print(objects[0])
  return render(request,'adminportal/show_questions.html',{
    "questions_list":questions
  })

def edit_question(request,pos):
  if request.method=="POST":
    question=request.POST["question"]
    option_A=request.POST["option_A"]
    option_B=request.POST["option_B"]
    option_C=request.POST["option_C"]
    option_D=request.POST["option_D"]
    correct_answer=request.POST["correct_answer"]
    tag=request.POST["tag"]

    Add_Question.objects.filter(id=pos).update(
    Question=question,
    Option_A=option_A,
    Option_B=option_B,
    Option_C=option_C,
    Option_D=option_D,
    Correct_Answer=correct_answer,
    Tag=tag
    )

    return redirect("view_questions", Tag=tag)

  # print(pos)
  object=Add_Question.objects.all()[pos-1]
  
  return render(request,'adminportal/edit_question.html',{
    "question":object,
    "pos":pos
  })

def delete_question(request,pos):
  # object
  instance=Add_Question.objects.get(id=pos)
  tag=instance.Tag
  instance.delete()
  return redirect("view_questions", Tag=tag)






def register_admin(request):
  if request.method=="POST":
    username=request.POST["username"]
    password=request.POST["password"]
    email=request.POST["email"]

    Recruiter.objects.create(
      username=username,
      password=password
    )

  return render(request,'adminportal/register_admin.html')

class info:
  def __init__(self,name,email,resume,graduation_year,percentage):
    self.name=name
    self.email=email
    self.resume=resume
    self.graduation_year=graduation_year
    self.percentage=percentage

def eligible_candidates(request):
  Eligible=[]
  criteria=75
  if request.session.get("criteria"):
    criteria=int(request.session.get("criteria"))
  print(criteria)
  for obj in Analysis.objects.all():
    if obj.precentage>=criteria:
      if obj.user_id in Eligible:
        continue
      else:
        Eligible.append(obj.user_id)
  
  temp=[]
  for user_id in Eligible:
    user=UserData.objects.filter(user_id=user_id)[0]
    name=user.first_name+" "+user.last_name
    email=user.email
    graduation_year=user.graduation_year
    user=Resume.objects.filter(user_id=user_id)[0]
    resume=user.resume
    all_obj=Analysis.objects.filter(user_id=user_id)
    percentage=0
    for obj in all_obj:
      if obj.precentage>=percentage:
        percentage=obj.precentage

    # print(name)
    # print(email)
    # print(graduation_year)
    # print(resume)

    obj=info(name,email,resume,graduation_year,percentage)
    temp.append(obj)
    # print(obj.name)
    # print(obj.email)
    # print(obj.graduation_year)
    # print(obj.resume)

  


  
  

  return render(request,'adminportal/eligible_candidates.html',{
    "Eligible":temp
  })


def eligible_criteria(request):
  if request.method=="POST":
    print()
    request.session["criteria"]=request.POST["criteria"]
    request.session["number_of_questions"]=request.POST["count_of_question"]


  return HttpResponseRedirect(reverse("admin_dashboard"))




  

  

  




