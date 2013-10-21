from django.shortcuts import render
from cd_library.models import CD

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            cds = CD.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'cds': cds, 'query':q})
    return render(request, 'search_form.html', {'errors': errors})
