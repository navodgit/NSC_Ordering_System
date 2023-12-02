from django.http import HttpResponse
from django.template import loader


def NSC(request):
  template = loader.get_template('myrest.html')
  return HttpResponse(template.render())

