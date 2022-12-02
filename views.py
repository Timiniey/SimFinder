from django.shortcuts import render
import phonenumbers
from phonenumbers import carrier
from django.contrib import messages
def index(request):
    return render(request,"index.html")

def finder(request):
    try:
        if request.method=="POST":
            number=request.POST["number"]
            phonenumber=phonenumbers.parse(number)
            Carrier=carrier.name_for_number (phonenumber,"en")
            results={
                "Carrier":Carrier
        }
            print(results)
            return render (request, "index.html",results)
    except "NumberParseException":
            messages.info (request," The number is not in a valid format it should be in +country code +number")
    else:
        return render (request," index.html")
