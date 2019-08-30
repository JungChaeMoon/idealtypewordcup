from django.shortcuts import render,reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CandidateForm
from .models import Contest, Candidate
import json
import random


def worldcup_view(request, *args, **kwargs):

    contest_list = Contest.objects.all()
    context = {'contest_list': contest_list}
    return render(request, 'worldcup/worldcup.html', context)


def start(request, contest_id):

    contest = get_object_or_404(Contest, pk=contest_id)
    item_list = contest.candidate_set.all().order_by('?').all()
    #context = {'item_list': item_list, 'contest': contest}
    list = []
    for a in contest.candidate_set.all().order_by('?'):

        dic = {'pk': a.id, 'title': a.title, 'photo': a.photo.url}
        list.append(dic)

    new_item_list = json.dumps(list, ensure_ascii=False)
    count = contest.candidate_set.all().count()
    context = {'new_item_list': new_item_list, 'contest_id': contest_id, 'count' : count}
    return render(request, 'worldcup/start.html', context)


def make_contest(request, *args, **kwargs):

    contest = Contest.objects.all()
    context = {'contest': contest}

    return render(request, 'worldcup/makecontest.html', context)


def middle(request, *args, **kwargs):

    contest = Contest()
    contest.worldcup_name = request.POST.get('contest', '')
    contest.save()
    key = Contest.objects.latest('id').id
    new_contest = get_object_or_404(Contest, pk=key)

    return HttpResponseRedirect(reverse('worldcup:make_worldcup', args=(new_contest.id,)))


def make_worldcup(request, contest_id):


    contest = get_object_or_404(Contest, pk=contest_id)
    form = CandidateForm()
    context = {'form': form, 'contest': contest}
    return render(request, 'worldcup/makeworldcup.html', context)


def upload_file(request, contest_id):

    contest = get_object_or_404(Contest, pk=contest_id)
    data = request.POST.copy()
    dict(data)
    data['contest'] = contest_id

    if request.method == 'POST':

        form = CandidateForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('worldcup:make_worldcup', args=(contest_id,)))
    else:
        form = CandidateForm()

    context = {'form': form, 'contest': contest}
    return render(request, 'worldcup/makeworldcup.html', context)


def make_quit(request, pk):

    contest = get_object_or_404(Contest, pk=pk)

    data = request.GET.get('pk', '')
    new_data = int(data, base=10)
    item = contest.candidate_set.filter(pk=new_data-1)

    context = {'item': item, 'data': data}

    return render(request,'worldcup/final.html',context)