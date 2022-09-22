from django.shortcuts import render
from scoreboard.models import User, Size, Score
from django.template.defaulttags import register


@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

def users(request):
    users = User.objects.all()
    sizes = Size.objects.all()

    for size in sizes:
        for user in users:
            if "score" not in user.__dict__.keys():
                user.score= {}
            print(Score.objects.filter(user=user, width=size.width, height=size.height,
                                                      count_mine=size.count_mine).order_by('time'))
            score = Score.objects.filter(user=user, width=size.width, height=size.height,
                                                      count_mine=size.count_mine).order_by('time')
            if score:
                user.score[size.name] = score[0]

    return render(request, "users.html", {"users": users, "sizes": sizes})
