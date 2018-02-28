from django.shortcuts import render
def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact NewsRank, please email me.',
                                                             'Freshworks.help@gmail.com'
                                                            ]})
                                                          

def googleSearch(request):
    return render(request, 'personal/googleSearch.html')
