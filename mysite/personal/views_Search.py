# This code is to be added on the in the views.py in the function
# that takes the request from the page
# we will have a models.py for this site where we will hold the 
# information about the authors, content and the title
# this is using that information as basis for the searching query
# this code imports high level packages from django website and can search 
# using titles, content or the authors

# https://docs.djangoproject.com/en/1.11/topics/db/queries/ 
# this website will give you the query format


from django.db.models import Q

query = request.GET.get("q")
if query:
	queryset_list = queryset_list.filter(
			Q(title__icontains = query)	|
			Q(content__icontains = query)|
			Q(author__first_name__icontains = query) |
			Q(author__last_name__icontains = query)
			).distinct()