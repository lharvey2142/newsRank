from django.shortcuts import render
def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html')
    '''
    return render(request, 'personal/basic.html',{'content':['If you would like to contact NewsRank, please email me.',
                                                             'Freshworks.help@gmail.com', 
                                                             '<script type="text/javascript" src="http://assets.freshdesk.com/widget/freshwidget.js"></script><style type="text/css" media="screen, projection">@import url(http://assets.freshdesk.com/widget/freshwidget.css); </style> <iframe title="Feedback Form" class="freshwidget-embedded-form" id="freshwidget-embedded-form" src="https://demo-sandbox.freshdesk.com/widgets/feedback_widget/new?&widgetType=embedded&submitThanks=Thank+you+for+submitting+a+ticket+an+engineer+will+respond+to+you+promptly.%0D%0A&screenshot=No&captcha=yes" scrolling="no" height="500px" width="100%" frameborder="0" ></iframe>'
                                                            ]})
    '''                                                   

def googleSearch(request):
    return render(request, 'personal/googleSearch.html')
