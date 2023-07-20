from django.shortcuts import render
from . models import place,team
def demo(request):
   obj=place.objects.all()
   obj2=team.objects.all()
   return render(request,'index.html',{'objkey':obj, 'obj2key':obj2})
