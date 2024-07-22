from django.shortcuts import render, redirect
from .models import *
import random

def index(request):

    return render(request, "index.html")

def round1(request):
    if request.method == "POST":
        if request.POST.get("inpt") == "ans1":
            info = {'msg':request.POST.get('inf'),"team":request.POST.get('team'), "btn":"Next", "inf":"qes2", "type":request.POST.get('type'), "inpt":"qes2"}
            return render(request, "round1_ans.html", info)

        if request.POST.get("inpt") == "qes2":
            team = request.POST.get('team')

            if request.POST.get('right') == "on":
                tm = Team.objects.get(team_name = team)
                tm.score += Rounds.objects.get(round_id = 0).points
                tm.save()
            
            elif request.POST.get('wrong') == "on":
                tm = Team.objects.get(team_name = team)
                tm.score -= Rounds.objects.get(round_id = 0).negative_mark
                tm.save()
            
            elif request.POST.get('pass') == "on":
                tm = Team.objects.get(team_name = team)
                tm.score -= Rounds.objects.get(round_id = 0).pass_mark
                tm.save()
            
            theme = request.POST.get("type")
            qes = Quset.objects.filter(quest_type = theme)[1]
            info = {"msg":qes, "team":team, "inf":qes.ans, "btn":"Ans", "inpt":"ans2", "type":qes.quest_type}
            return render(request, "round1_quest.html", info)

        if request.POST.get("inpt") == "ans2":
            info = {'msg':request.POST.get('inf'), "team":request.POST.get('team'), "btn":"Next", "inf":"ret", "type":request.POST.get('type'), "inpt":"ret"}
            return render(request, "round1_ans.html", info)
        
        if request.POST.get("inpt") == "ret":
            team = request.POST.get('team')

            if request.POST.get('right') == "on":
                tm = Team.objects.get(team_name = team)
                tm.score += Rounds.objects.get(round_id = 0).points
                tm.save()
            
            elif request.POST.get('wrong') == "on":
                tm = Team.objects.get(team_name = team)
                tm.score -= Rounds.objects.get(round_id = 0).negative_mark
                tm.save()
            
            elif request.POST.get('pass') == "on":
                tm = Team.objects.get(team_name = team)
                tm.score -= Rounds.objects.get(round_id = 0).pass_mark
                tm.save()
            return redirect("/r1")
        

        else:
            team_lst = Team_list.objects.get(id = 1002)
            tm = team_lst.team[0]
            team_lst.team = team_lst.team[1:]
            team_lst.save()
            team = Team.objects.get(team_id = tm)
            theme = request.POST.get("theme")
            qes = Quset.objects.filter(quest_type = theme)[0]
            info = {"msg":qes, "team":team, "inf":qes.ans, "btn":"Ans", "inpt":"ans1", "type":qes.quest_type}
            return render(request, "round1_quest.html", info)
    
    
    return render(request, "round1.html")

def leaderboard(request):
    info = {"teams":Team.objects.all()}
    return render(request, "leaderboard.html", info)

def suffel(request):
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(my_list)
    st = ""
    for i in my_list:
        st += str(i)
    lst = Team_list.objects.get(id = 1002)
    lst.team = st
    lst.save()
    return redirect("/")

def mk_list(request):
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(my_list)
    st = ""
    for i in my_list:
        st += str(i)
    lst = Team_list(team = st, id  = 1002)
    lst.save()
    return redirect("/")


def make_teams(request):
    for i in range(11):
        tm = Team(team_name = f"team{i}", team_id = i)
        tm.save()
    return redirect("/")

def make_quest(request):
    j = 0
    k = 0
    for i in range(21):
        if k == 2:
            j += 1
            k = 0
        quest = Quset(quest_name = f"ans this question {i}", ans = "No Answer", round = "round1", quest_type = f"type{j}")
        quest.save()
        k += 1
        
    return redirect("/")

