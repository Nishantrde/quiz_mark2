from django.db import models
from django import forms

class Team(models.Model):
    team_name = models.CharField(max_length = 15)
    team_id = models.IntegerField(default= 0)
    qualified = models.BooleanField(default = True)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.team_name

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'team_id', 'qualified', 'score']

class Quset(models.Model):
    quest_name = models.CharField(max_length = 20)
    ans = models.CharField(default= '', max_length = 25)
    round = models.CharField(default= '', max_length = 25)
    quest_type = models.CharField(default= '', max_length = 25)
    
    def __str__(self):
        return self.quest_name

class Team_list(models.Model):
    team = models.CharField(default= '', max_length = 25)

    def __str__(self):
        return self.team

class Rounds(models.Model):
    round_name = models.CharField(max_length = 20)
    round_id = models.IntegerField(default= 0)
    points = models.IntegerField(default = 0)
    negative_mark = models.IntegerField(default = 0)
    pass_mark = models.IntegerField(default = 0)

    def __str__(self):
        return self.round_name


