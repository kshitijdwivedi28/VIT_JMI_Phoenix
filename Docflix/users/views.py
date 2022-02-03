from pydoc import doc
import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fpdf import FPDF

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    dict={"Key":"yes"}
    naam = None
    mail = None
    ph = None
    dt = None
    dept = None
    doct = None
    mes = None
    res=request.POST
    result = request.POST
    for i in result:
        print("Hello")
        print(naam)
        if naam ==None:
            dict["Key"]="no"
        if i=='name':
            naam=res[i]
        if i=='email':
            mail=res[i]
        if i=='phone':
            ph=res[i]
        if i=='date':
            dt=res[i]
        if i=='department':
            dept=res[i]
        if i=='doctor':
            doct=res[i]
        if i=='message':
            mes=res[i]
    print(res)
    print(dict)
    if(naam is not None and mail is not None):
        pdf = FPDF()  
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = "DocFlix-eAppointment", ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "________________________________________________________________________________________________________________________",ln = 2, align = 'L')
        pdf.cell(200, 10, txt = "________________________________________________________________________________________________________________________",ln = 3, align = 'L')
        pdf.cell(200, 10, txt = "Name : "+naam,ln = 4, align = 'L')
        pdf.cell(200, 10, txt = "Email : "+mail,ln = 5, align = 'L')
        pdf.cell(200, 10, txt = "Contact No : "+ph,ln = 6, align = 'L')
        pdf.cell(200, 10, txt = "Date : "+dt,ln = 7, align = 'L')
        pdf.cell(200, 10, txt = "Department : "+dept,ln = 8, align = 'L')
        pdf.cell(200, 10, txt = "Doctor : "+doct,ln = 9, align = 'L')
        pdf.cell(200, 10, txt = "Message : "+mes,ln = 10, align = 'L')
        f = open("demofile2.txt", "r")
        str=f.readlines()
        print(str)
        str1 = "" 
        for ele in str: 
            str1 += ele  
        pdf.cell(200, 10, txt = "Symptoms: "+str1,ln =11, align = 'L')
        f.close()
        pdf.cell(200, 10, txt = "",ln = 12, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 13, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 14, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 15, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 16, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 16, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 16, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 16, align = 'L')
        pdf.cell(200, 10, txt = "You will be contacted soon regarding timings soon.",ln = 17, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 18, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 19, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 20, align = 'L')
        pdf.cell(200, 10, txt = "Thank you for choosing us.",ln = 15, align = 'C')
        pdf.cell(200, 10, txt = "Team Phoneix",ln = 16, align = 'C')
        pdf.output("Docflix.pdf")
        dict['Key']="no"
        print("Downloaded Successfully") 
    return render(request,'users/response.html',dict)

#def response(request):
#    res=request.POST
#    print(res)
#   return render(request,'users/response.html')
