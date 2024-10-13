from django.shortcuts import render

# Existing home view
def home(request):
    return render(request, 'home.html')

# New view for /test
def test_dash(request):
    return render(request, 'test_dash.html')
