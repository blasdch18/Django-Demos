from django.views import View
from .models import Company
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
class CompanyListView(View):
    def get(self, request):
        #get
        if('name' in request.GET):
            clist = Company.objects.filter(name__contains=request.GET['name'])
        else:    
            clist = Company.objects.all()
        return JsonResponse(list(clist.values()),safe=False)

    
class CompanyDetailView(View):
    def get(self, request, pk):
        #get
        company = Company.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company))

