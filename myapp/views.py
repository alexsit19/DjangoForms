from django.shortcuts import render
from django.views import View
from .forms import IncrementForm
from .models import Hours
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

class FormShow(View):
    def get(self, request):

        current_hours = Hours.objects.all()
        #print(current_hours[len(current_hours) -1].total_hours)
        form = IncrementForm(initial={'number' : 1})
        current_hours = current_hours[len(current_hours) -1].total_hours
        context = {
            'form' : form,
            'hours' : current_hours
            #'Hours': current_hours,
        }


        return render(request, 'base.html', context)

class FormProcessing(View):
    def post(self, request):
        form = IncrementForm(self.request.POST)
        if form.is_valid():
            current_hours = Hours.objects.all()
            current_hours = current_hours[len(current_hours) - 1].total_hours
            data = form.cleaned_data['number']
            current_hours += int(data)
            hours = Hours(name='DevHours', total_hours=current_hours)
            hours.save()



        return HttpResponseRedirect('/index/formshow')
