import userportal
from django.shortcuts import render
from userportal.models import Analysis, UserData,Resume
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from pyresparser import ResumeParser
from adminportal.models import Add_Question
import random,datetime

from json import dumps
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def user_profile(request):
  if request.method=="POST":
    user_id=request.user
    first_name=request.POST["first_name"]
    last_name=request.POST["last_name"]
    email=request.POST["email"]
    stream=request.POST["stream"]
    graduation_year=request.POST["graduation"]
    dob=request.POST["dob"]


    UserData.objects.create(
      user_id=request.user,
      first_name=first_name,
      last_name=last_name,
      email=email,
      stream=stream,
      graduation_year=graduation_year,
      dob=dob
    )
  user_id=User.objects.get(id=request.user.id)
  # print(5)
  if UserData.objects.filter(user_id=user_id).exists():
    # print(5)
    user=UserData.objects.filter(user_id=user_id)[0]
    return render(request,'userportal/userprofile.html',{
      "message":False,
      "user":user
    })
  return render(request,'userportal/userprofile.html',{
    "message":True,
    "user":""
  })


def user_registration(request):
  return render(request,'userportal/userregistration.html')

def upload_resume(request):
  context={}
  if request.method=="POST":
    upload_file=request.FILES["document"]

    Resume.objects.create(
      user_id=request.user,
      resume=upload_file
    )
    #uploaded file have several properties like name,url,size
    fs=FileSystemStorage()
    name=fs.save(upload_file.name,upload_file)
    #url=fs.url(name)
    #print(url)
    context['url']=fs.url(name)
    data=ResumeParser('media/rohit-resume1_1UoHbvM.pdf').get_extracted_data()
    print(data['skills'])

  return render(request,'userportal/UploadResume.html',context)



def start_quiz(request):
  # user =request.user
  # print(user.username)
  # resume=Resume.objects.filter(user_id=request.user)[0]
  # print(resume.resume.url)
  # url=resume.resume.url
  # url=url[1:]
  # print(url)
  # data=ResumeParser(url).get_extracted_data()
  # # print(data)
  # skills=data["skills"]
  # for i in range(len(skills)):
  #   skills[i]=skills[i].upper()
  # print(data['skills'])
  # avaliable_questions=[]
  # for question in Add_Question.objects.all():
  #   tag=question.Tag.upper()
  #   if tag in skills:
  #     avaliable_questions.append(question)

  # number_of_questions=5
  
  # quiz_questions=[]
  # for i in range(number_of_questions):
  #   r=random.randint(0,len(avaliable_questions)-1)
  #   print(r)
  #   quiz_questions.append(avaliable_questions[r])

  # print(len(avaliable_questions))
  




  return render(request,'userportal/StartQuiz.html')

def start(request):
  user =request.user
  #print(user.username)
  resume=Resume.objects.filter(user_id=request.user)[0]
  #print(resume.resume.url)
  url=resume.resume.url
  url=url[1:]
  #print(url)
  data=ResumeParser(url).get_extracted_data()
  # print(data)
  skills=data["skills"]
  for i in range(len(skills)):
    skills[i]=skills[i].upper()
  #print(data['skills'])
  avaliable_questions=[]
  for question in Add_Question.objects.all():
    tag=question.Tag.upper()
    if tag in skills:
      avaliable_questions.append(question)


  number_of_questions=4
  if request.session.get("number_of_questions"):
    number_of_questions=request.session.get("number_of_questions")


  random.shuffle(avaliable_questions)
  quiz_questions=[]
  for i in range(number_of_questions):
    #r=random.randint(0,len(avaliable_questions)-1)
    #print(r)
    quiz_questions.append(avaliable_questions[i])

  #print(len(avaliable_questions))
  request.session["max_score"]=number_of_questions*10

  ques=serializers.serialize("json", quiz_questions)
  questionsJson = dumps(ques)




  return render(request,'quiz/start.html',{
    'questionsData': questionsJson,
    'number_of_questions':number_of_questions
    })

def end_quiz(request):
  return render(request,'userportal/end_quiz.html')

def result(request):
  user=request.user
  #score=request.POST.get('points')
  score=request.POST['points']
  max_score=request.session["max_score"]
  print(score)
  print(int(score))
  #print(int(score))
  print(max_score)
  percentage=float((int(score)/max_score))*100
  status="Not Eligible"
  date=datetime.date.today()
  if percentage>=75:
    status="Eligible"
  Analysis.objects.create(
    user_id=user,
    score=score,
    max_score=max_score,
    precentage=percentage,
    status=status,
    date=date
  )

  return render(request,'userportal/end_quiz.html')

def user_analysis(request):
  user_id=request.user
  quiz_results=[]
  for obj in Analysis.objects.all():
    if obj.user_id==user_id:
      quiz_results.append(obj)
  


  return render(request,'userportal/user_analysis.html',{
    'quiz_results':quiz_results
  })



