from django.http import HttpResponse

from .models import Word

def index(request):
    word_list = Word.objects.all()
    output = ', '.join([w.value for w in word_list])

    return HttpResponse("Hello, world. You're at the polls index. here are the words: {}".format(output))


def detail(request, word_id):
    return HttpResponse("You're looking at word %s." % word_id)


def results(request, word_id):
    response = "You're looking at the results of word %s."
    return HttpResponse(response % word_id)


def vote(request, word_id):
    return HttpResponse("You're voting on word %s." % word_id)
