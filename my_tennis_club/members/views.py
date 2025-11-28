from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  mymembers = Member.objects.all().values()
  column_firstname = Member.objects.values_list('firstname')
  records_laura = Member.objects.filter(firstname='Laura').values()
  genero_and_name = Member.objects.filter(genero='Mujer', firstname='Laura').values()
  name_or_name = Member.objects.filter(Q(firstname='Laura') | Q(firstname='Valery')).values()
  start_lyrics = Member.objects.filter(firstname__startswith='L').values()
  end_lyrics = Member.objects.filter(firstname__endswith='a').values()
  contains_lyrics = Member.objects.filter(firstname__contains='ra').values()
  rangge_lyrics = Member.objects.filter(firstname__range=['G', 'L']).values()
  inn_names = Member.objects.filter(firstname__in=['Carlos','Laura', 'Valery']).values()
  end_and_start = Member.objects.filter(firstname__startswith='L', firstname__endswith='a').values()
  order_by_asc = Member.objects.all().order_by('firstname').values()
  order_by_desc = Member.objects.all().order_by('-firstname').values()
  
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
     'mymembers': mymembers,
     'column_firstname': column_firstname,
     'records_laura': records_laura,
     'genero_and_name': genero_and_name,
     'name_or_name': name_or_name,
     'start_lyrics': start_lyrics,
     'end_lyrics': end_lyrics,
     'contains_lyrics': contains_lyrics,
     'rangge_lyrics': rangge_lyrics,
     'inn_names': inn_names,
     'end_and_start': end_and_start,
     'order_by_asc' : order_by_asc,
     'order_by_desc' : order_by_desc,
  }
  return HttpResponse(template.render(context, request))