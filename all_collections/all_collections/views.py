from django.shortcuts import render
from django.template import loader
# Define the home view
def main(request):
    template = loader.get_template('main.html')
    return render(request, 'main.html')