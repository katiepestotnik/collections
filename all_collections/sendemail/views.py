from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import environ
import os
env = environ.Env()


def contactView(request):
  if request.method == "GET":
      form = ContactForm()
  else:
      form = ContactForm(request.POST)
      if form.is_valid():
          subject = form.cleaned_data["subject"]
          print(subject)
          from_email = form.cleaned_data["from_email"]
          message = form.cleaned_data['message']
          try:
            EmailMessage(subject, message, from_email, to=['katie.pestotnik@gmail.com']).send()
              # send_mail(subject, message, from_email, [env('DEFAULT_FROM_EMAIL')])
          except BadHeaderError:
              return HttpResponse("Invalid header found.")
          return redirect("success")
  return render(request, "email.html", {"form": form})

def successView(request):
  return HttpResponse("Success! Thank you for your message.")
