from django.shortcuts import render

# Create your views here.
def home_view(request):
    """
    A functional based view for the home page
    """

    return render(request, "index.html")
