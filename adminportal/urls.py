from django.urls import path

from . import views

urlpatterns=[
  path('',views.admin_index,name="admin_index"),
  path('admin_login/',views.admin_login,name="admin_login"),
  path('admin_logout/',views.admin_logout,name="admin_logout"),
  path('add_question/',views.add_question,name="add_question"),
  path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
  path('questions/<str:Tag>',views.view_questions,name="view_questions"),
  path('questions/edit/<int:pos>',views.edit_question,name="edit_question"),
  path('questions/delete/<int:pos>',views.delete_question,name="delete_question"),
  path('register_admin',views.register_admin,name="register_admin"),
  path('eligible_candidates',views.eligible_candidates,name="eligible_candidates"),
  path('eligible_criteria',views.eligible_criteria,name="eligible_criteria")

]
