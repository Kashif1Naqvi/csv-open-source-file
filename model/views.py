import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Profile
# Create your views here.
# one parameter named request
def profile(request):
    # declaring template
    template = "model/profile.html"
    data = Profile.objects.all()
    
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
            'profiles': data
        }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            name=column[0],
            job_title=column[1],
            department=column[2],
            full_or_part_time=column[3],
            salary_or_hourly=column[4],
            typical_hours=column[5],
            annual_salary=column[6],
            hourly_rate =column[7],
        )
    context = {}
    
    
    return render(request, template, context)