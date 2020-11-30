from django.contrib import admin
from .models import Student,Guardian, Admission,JambUpload,StudentMessages,WAEC

admin.site.register(Student)
admin.site.register(Guardian)
admin.site.register(Admission)
admin.site.register(JambUpload)
admin.site.register(WAEC)
admin.site.register(StudentMessages)