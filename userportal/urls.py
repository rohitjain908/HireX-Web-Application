from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
  path('userprofile/',views.user_profile,name="user_profile"),
  path('userregistration/',views.user_registration,name="user_registration"),
  path('UploadResume/',views.upload_resume,name="upload_resume"),
  path('StartQuiz/',views.start_quiz,name="start_quiz"),
  path('start/',views.start,name="start"),
  path('start/end_quiz/',views.end_quiz,name="end_quiz"),
  path('result',views.result,name="result"),
  path('user_analysis/',views.user_analysis,name="user_analysis")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

