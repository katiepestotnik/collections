from django.shortcuts import render
# Define the home view
def main(request):
  return render(request, 'main.html')