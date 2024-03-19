from django.shortcuts import render, redirect
from .forms import ReportForm, HomenurseForm, AmbulanceForm, FeedbackForm


#report an abandoned individual
def report_abandoned_individual(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_success') 
    else:
        form = ReportForm()
    return render(request, 'report.html', {'form': form})

def report_success(request):
    return render(request, 'report_success.html')


#register for home nurse
def homenurse_registration(request):
    if request.method == 'POST':
        form = HomenurseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reg_success')
    else:
        form = HomenurseForm()
    return render(request, 'homenurse_reg.html', {'form': form})
    
def registration_success(request):
    return render(request, 'reg_success.html')


#ambulance service
def ambulance_service(request):
    if request.method == "POST":
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('amb_success')
    else:
        form = AmbulanceForm()
    return render(request, 'ambulance_service.html', {'form': form})

def ambulance_success(request):
    return render(request, 'amb_success.html')

#feedback
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def Activities(request):
    return render(request, 'activities.html')