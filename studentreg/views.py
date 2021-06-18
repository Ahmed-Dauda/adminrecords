from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from studentreg.models import Salat, Dining, Lightout, Prep, Hygiene

from studentreg.forms import Salatform, Diningform, Lightoutform, Prepform, Hygieneform

from .filters import Salatfilter
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .permission import user_perm, group_perm
# Create your views here.

@group_perm
@user_perm
def home(request):

    activities = Salat.objects.order_by('-pub_date')

    myfilter = Salatfilter(request.GET, queryset= activities)
    activities = myfilter.qs
   

    context = {
        'activities': activities,
        'myfilter':myfilter
       
        
    }
    return render(request, 'studentreg/home.html', context)


def edit_view(request, post_id):
    post_id = Salat.objects.get(pk = post_id)

    activities = Salat.objects.all()

    form = Salatform(instance=post_id)
    if request.method == 'POST':
        form = Salatform(request.POST, request.FILES, instance=post_id)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {
        'form': form
       
       
    }
    return render(request, 'studentreg/edit.html', context)

def delete_view(request, delete_id):
    delete_id = Salat.objects.get(pk = delete_id)
  
    
    if request.method == 'POST':
        delete_id.delete()
        return redirect('home')
        
    context = {
        'item': delete_id
       
    }
    return render(request, 'studentreg/delete.html', context)





def prep_view(request):

    activities = Salat.objects.order_by('-pub_date')
    #activities = Salat.objects.filter(pk='-pub_date')

    myfilter = Salatfilter(request.GET, queryset= activities)
    activities = myfilter.qs
   
    context = {
        'activities': activities,
        'myfilter':myfilter  
    }
    
    return render(request, 'studentreg/prep.html', context)



def editprep_view(request, post_id):
    post_id = Prep.objects.get(pk = post_id)
  
    form = Prepform(instance=post_id)
    if request.method == 'POST':
        form = Prepform(request.POST, request.FILES, instance=post_id)
        if form.is_valid():
            form.save()
            return redirect('edit')
        
    context = {
        'form': form
       
    }
    return render(request, 'studentreg/edit_prep.html', context)


def deleteprep_view(request, delete_id):
    deleteprep_id = Prep.objects.get(pk = delete_id)
  
    
    if request.method == 'POST':
        deleteprep_id.delete()
        return redirect('lightout')
        
    context = {
        'item': deleteprep_id
       
    }
    return render(request, 'studentreg/deleteprep.html', context)
  


def signin_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
         form = AuthenticationForm(data = request.POST)
         if form.is_valid():
             user = form.get_user()
             if user is not None:
                 login(request, user)
                 return redirect ('home')


    else:
        form  = AuthenticationForm()

        context = {
        'form': form
        }
        return render(request, 'studentreg/signin.html', context)



  
def add_view(request):

    form = Salatform()
    activities = Salat.objects.order_by('-pub_date')
    if request.method == 'POST':
        form = Salatform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
            #m = form.changed_data.get('names')
    

    context = {
        'activities': activities,
        'form':form
    }
    return render(request, 'studentreg/add.html', context)



# def editall_view(request, post_id):
#     post_id = Salat.objects.get(pk = post_id)
#     activities = Salat.objects.all()
#     form = Salatform()
#     if request.method == 'POST':
#         form = Salatform(request.POST, request.FILES, instance=post_id)
#         if form.is_valid():
#             form.save()
#             return render(request, 'studentreg/editall.html', context)
        
#     context = {
#         'form': form,
#         'activities':activities
       
#     }
#     return render(request, 'studentreg/editall.html', context)


# def generatepdf(request):
#      Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()

#      Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)

#      Draw things on the PDF. Here's where the PDF generation happens.
#      See the ReportLab documentation for the full list of functionality.
#     activities = Salat.objects.all()
    
#     myfilter = Salatfilter(request.GET, queryset= activities)
#     activities = myfilter.qs
 

  
#     for n in activities:

#         p.drawString(500,750,  n.names)

   

#     p.drawString(500,750, n)

#     p.line(480,747,580,747)

#     p.drawString(275,725,'AMOUNT OWED:')
#     p.drawString(500,725,"$1,000.00")
#     p.line(378,723,580,723)

#     p.drawString(30,703,'RECEIVED BY:')
#     p.line(120,700,580,700)
#     p.drawString(120,703,"JOHN DOE")

#     Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     FileResponse sets the Content-Disposition header so that browsers
#     present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')




# def get(request):
#     template = get_template('studentreg/invoice.html')
#     activities = Salat.objects.order_by('-pub_date')

#     myfilter = Salatfilter(request.GET, queryset= activities)
#     activities = myfilter.qs
 

#     context = {
#         'activities': activities,
#         'myfilter':myfilter
#     }
#     html = template.render(context)
#     pdf = render_to_pdf('studentreg/invoice.html', context)
#     if pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "Invoice_%s.pdf" %("12341231")
#         content = "inline; filename='%s'" %(filename)
#         download = request.GET.get("download")
#         if download:
#             content = "attachment; filename='%s'" %(filename)
#         response['Content-Disposition'] = content
#         return response
#     return HttpResponse("Not found")

from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .utils import render_to_pdf

# def render_to_pdf(template_src, context_dict={}):
# 	template = get_template(template_src)
# 	html  = template.render(context_dict)
# 	result = BytesIO()
# 	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
# 	if not pdf.err:
# 		return HttpResponse(result.getvalue(), content_type='application/pdf')
# 	return None


data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

#Opens up page as PDF

def generatepdf(request):
    
   
    activities = Salat.objects.order_by('-pub_date')

    myfilter = Salatfilter(request.GET, queryset= activities)
    activities = myfilter.qs
   

    context = {
        'activities': activities,
        'myfilter':myfilter  
    }

   
    pdf = render_to_pdf('studentreg/prep.html', context)
	        
    return HttpResponse(pdf, content_type='application/pdf')


def generate(request):

    pdf = render_to_pdf('studentreg/edit.html')       
    return HttpResponse(pdf, content_type='application/pdf')

# download by id


from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def salat_render_pfd(request, *args, **kwargs):
    
    #return HttpResponse('testing my project')
    #activities = Salat.objects.order_by('-pub_date')
    pk = kwargs.get('pk')
    post = get_list_or_404(Salat, pk = pk)
    template_path = 'studentreg/pdf_id.html'
    context = {
        'activities':post
        #'activities':activities
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
def render_pdf_view_id(request):
    #activities = Salat.objects.order_by('-pub_date')
    #pk = kwargs.get('pk')
    #posts = get_object_or_404(Salat, pk=pk)
    template_path = 'studentreg/pdf_id.html'
    context = {
        'myvar': 'posts'
        #'activities':activities
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
