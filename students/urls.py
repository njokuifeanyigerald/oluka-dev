from django.urls import path
from students import views as student_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', student_views.dashboard_view,name='dashboard'),
    path('enroll/', student_views.enroll_view,name='enroll'),
    path('crash-course/', student_views.crash_course_view,name='crash_course'),
    path('full-course/', student_views.full_course_view,name='full_course'),
    path('student-profile/', student_views.student_profile_view,name='student_profile'),    
    path('upload-waec/', student_views.upload_waec_view,name='upload_waec'),    
    path('upload-jamb/', student_views.upload_jamb_view,name='upload_jamb'),    
    path('upload-guardian/', student_views.upload_guardian_view,name='upload_guardian'),    
    # path('login/', student_views.login_view,name='login'),    
    path('grade/', student_views.grade_view,name='grade'),    
    path('profile/', student_views.profile_view,name='profile'),     
    # path('register/', student_views.register_view,name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)