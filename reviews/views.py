from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Review


from .forms import ReviewForm
from .models import Review
# Create your views here.
# View via class
class ReviewView(CreateView):
    #When inheriting from FormView
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    # When inheriting from basic View
    """def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid(): 
            form.save()         
            return HttpResponseRedirect("/thank-you")    

        return render(request, "reviews/review.html", {
            "form": form
        })    """

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    # get context data is used to overwrite some returned data, or to add more. Works with every view. 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # A way to filter displayed data.
    """def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data"""


class DeailView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review



        
# view via function
'''def review(request):  
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            """review = Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], 
            rating=form.cleaned_data['rating'])
            review.save()"""    # This is valid, mandatory only when models and forms are separate. 
            form.save()         # Possible only when forms are created by Django via ModelForm 
            return HttpResponseRedirect("/thank-you")
     
    else:        
        form = ReviewForm()

    
    return render(request, "reviews/review.html", {
            "form": form
        })
'''

