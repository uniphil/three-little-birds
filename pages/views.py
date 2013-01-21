from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    feature = {
        'title': 'Singing Their Minds on Social and Political Issues',
        'img': {
            'src': 'https://s3.amazonaws.com/three-little-birds/IMG_20130119_092429.jpg?AWSAccessKeyId=ASIAJCGNDLJWAJ47RCEQ&Expires=1358781552&Signature=dC2rTaRDZB7%2BaH6zee5Wbryxgow%3D&x-amz-security-token=AQoDYXdzEHgakAI81hIl2FruQ3H0Q27n5Nh8z4AUm0y4GtagTr15P4gAypEjFQp%2BssTD6BqKRo2KfNejlBdiQiPNyZdb/H45IftwH1vRqV57qAD3WkgL78RMaxApUXk9y%2Bkc1UMbVpaI61W5wCsFmFlZITtRpkwW6tkIqeDyaW1PHaWpgXOoNKz15NacIxDy7kmwyEj7xUhDZl1fd7MxyBo4G8FRp9VIE1fUW7yfF0UoNSTKaan/qFuZE9nE7HX5fjEzCqI%2BkrDRzKqxdQ6kKO%2BOcYezMcHGGEFWyo%2B1FIa2I00FioITm/r3WIoWUw72IDOOdqyhzvV8Ouy/8SUdgmJcZuPYg2MmRl%2BM4BBoa2HKvmGBZe7NbJEyXSCYs/WHBQ%3D%3D',
            'alt': 'Octocats!',
            'title': 'Octocats!',
        },
        'content': 'Three Little Birds is a fusion of three distinct women who candidly sing their minds on social and political issues. Drawing upon a variety of musical influences; their songs combine everything from Balkan styled harmonies within reggae beats to country-flavoured melodies amidst Tin-Pan Eran arrangements.',       
    }
    return render_to_response('home.html', {
        'feature': feature,
    })
