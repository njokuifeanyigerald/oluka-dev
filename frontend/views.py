from django.shortcuts import render


# Test if the page returned is the index page

# Create your views here.
def frontend_view(request):
    context = {
        'title': 'Oluaka Institute | Home'
    }
    return render(request, 'frontend/index.html', context)

def hardware_view(request):
    context = {
        'title': 'Oluaka Institute | Hardware Lab'
    }
    return render(request, 'frontend/hardware.html', context)

def health_view(request):
    context = {
        'title': 'Oluaka Institute | Student Health'
    }
    return render(request, 'frontend/health.html', context)

def software_view(request):
    context = {
        'title' : 'Oluaka Institute | Software Lab'
    }
    return render(request, 'frontend/software.html', context)

def network_view(request):
    context = {
        'title': 'Oluaka Institute | Network Lab'
    }
    return render(request, 'frontend/network.html', context)

def psp_view(request):
    context = {
        'title' : 'Oluaka Institute | Students Peer Support'
    }
    return render(request, 'frontend/psp.html', context)

def cec_view(request):
    context = {
        'title': 'Oluaka Institute | Continuing Education'
    }
    return render(request, 'frontend/cec.html', context)

def alumni_view(request):
    context = {
        'title': 'Oluaka Institute | Alumni Community'
    }
    return render(request, 'frontend/alumni.html', context)

def accomodation_view(request):
    context = {
        'title': 'Oluaka Institute | Accomodation Plan'
    }
    return render(request, 'frontend/accomodation.html', context)

def engagement_view(request):
    context = {
        'title': "Oluaka Institute | Student's Engagement"
    }
    return render(request, 'frontend/engagement.html', context)

def exam_view(request):
    context = {
        'title' : 'Examnination & Assessment'
    }
    return render(request, 'frontend/exams.html', context)

def error_404_view(request):
    context = {
        'title' : 'Page not Found'
    }
    return render(request, 'frontend/404.html', context)