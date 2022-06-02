# pages/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Client, Document
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'docgener/index.html'
    context_object_name = 'latest_client_list'

    def get_queryset(self):
        """Return the last five first clients"""
        return Client.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Client
    template_name = 'docgener/detail.html'


class ResultsView(generic.DetailView):
    model = Client
    template_name = 'docgener/results.html'


def vote(request, question_id):
    client = get_object_or_404(Client, pk=question_id)
    try:
        selected_documents = client.document_set.get(pk=request.POST['document'])
    except (KeyError, Document.DoesNotExist):
        return render(request, 'docgener/detail.html',
                      {
                          'client': client,
                          'error_message': "You didn't select a choice",
                      })
    else:
        selected_documents.cost += 1
        selected_documents.save()
        return HttpResponseRedirect(reverse('docgener:results', args=(client.id,)))