from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice


# function-based view
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")

    context = {
        "latest_question_list": latest_question_list,
        "titulo": "Curso de Python"
        }

    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # get_object_or_404 retorna um objeto caso exista. Se não exisitr gera um erro 404
    question = get_object_or_404(Question, pk=question_id)
    # primary key -> chave primária
    # question = Question.object.get(pk=question_id)

    context = {"question": question}
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "Você não escolheu uma opção para votar."
        }
        return render(request, "polls/detail.html", context)

    else:
        # Incrementamos a quantidade de votos da opção selecionada em 1
        selected_choice.votes += 1

        # Salvamos (atualizamos) o objeto com a nova quantidade de votos
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))