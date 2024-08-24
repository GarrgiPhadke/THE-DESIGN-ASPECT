from django.shortcuts import render
from contact.models import Contact

def contact(request):
    if request.method=='POST':
        
        name = request.POST['name']
        email = request.POST['email']
        phone= request.POST['phone']
        location= request.POST['location']
        message = request.POST['message']
        print(name,email,message)
        ins = Contact(name=name, email=email, phone=phone, location=location, message=message)
        ins.save()
        print("the database has written to the db")
    # Handle form submission or other logic if needed
    return render(request, 'contact.html')



