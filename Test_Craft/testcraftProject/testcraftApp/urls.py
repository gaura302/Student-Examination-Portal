from django.urls import path 
from . import views
urlpatterns = [
         path('', views.Home),
                    # For Question
    path('givemequestioncurd/', views.Give_Me_Questioncurd_Page),
    path('giveaddquestion/' , views.Give_Me_AddQuestion_Page),
    path('giveviewquestion/' , views.Give_Me_ViewQuestion_Page),
    path('giveupdatequestion/' , views.Give_Me_UpdateQuestion_Page),
    path('givedeletequestion/' , views.Give_Me_DeleteQuestion_Page),
    path('givemeshowallquestion/', views.Give_Me_ShowAllQuestion_Page),
    path('addquestion/', views.AddQuestions),
    path('viewquestion/', views.View_Question),
    path('updatequestion/', views.UpdateQuestion),
    path('deletequestion/',views.DeleteQuestion),
    path('viewquestionupdate/', views.View_Question_Update),
    path('viewquestiondelete/', views.View_Question_Delete),
                # for Student
   path('givemeragister/', views.GiveMeRagisterPage),
   path('ragister/', views.Ragister),
   path('givemelogin/', views.GiveMeLoginPage),
   path('login/', views.Login),
   path('givemeusercurd/' , views.GiveMeUserCurdPage),
   path('adduser/', views.AddUser),
   path('showuser/', views.ShowUser),
   path('updateuser/', views.UpdateUser),
   path('deleteuser/', views.DeleteUser),
   path('showalluser/', views.GiveMeShowAllPage),
   path('deleteusershowall/', views.DeleteUserForShowAllPage),
   path('starttest/' , views.StartTest),
   path('nextquestion/', views.NextQuestion),
   path('previousquestion/', views.PreviousQuestion),
   path('endtest/', views.EndTest),
   path('showallresult/', views.SHowallresult),
   path('logoutuser/', views.LogoutUser),
   path('logoutuser1/', views.LogoutUser1),

]