from django.urls import path
from frontend import views as frontend_views

urlpatterns = [
    path('', frontend_views.frontend_view,name='Home'),
    path('hardware/', frontend_views.hardware_view, name='hardware'),
    path('health/', frontend_views.health_view, name='health'),
    path('software/', frontend_views.software_view, name='software'),
    path('network/', frontend_views.network_view, name='network'),
    path('psp/', frontend_views.psp_view, name='psp'),
    path('cec/', frontend_views.cec_view, name='cec'),
    path('alumni/', frontend_views.alumni_view, name='alumni'),
    path('accomodation/', frontend_views.accomodation_view, name='accomodation'),
    path('engagement/', frontend_views.engagement_view, name='engagement'),
    path('exams/', frontend_views.exam_view, name='exam'),
    path('404/', frontend_views.error_404_view, name='404')
    # path('crash-course/', student_views.crash_course_view,name='crash_course'),
    # path('full-course/', student_views.full_course_view,name='full_course'),
    # path('student-profile/', student_views.student_profile_view,name='student_profile'),    
    # path('upload-waec/', student_views.upload_waec_view,name='upload_waec'),    
    # path('upload-jamb/', student_views.upload_jamb_view,name='upload_jamb'),    
    # path('upload-guardian/', student_views.upload_guardian_view,name='upload_guardian'),    
    # path('login/', student_views.login_view,name='login'),    
    # path('grade/', student_views.grade_view,name='grade'),    
    # path('profile/', student_views.profile_view,name='profile'), 
]