from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
import vk
from scrap_group.models import RequestHistory

from scrap_group.models import UserIds


class GroupWall(TemplateView):
    template_name = 'scrap_group/group_wall.html'

    def get_context_data(self, **kwargs):
        context = super(GroupWall, self).get_context_data(**kwargs)

        session = vk.Session()
        api = vk.API(session)
        user = api.users.get(user_ids=1, fields='sex,bdate,city')

        context['data'] = user

        return context


def user_id(request):
    if request.method == 'GET':
        return render(request, 'scrap_group/choose_user.html')

    if request.method == 'POST':
        uid = UserIds(user_id=request.POST['user_id'])
        uid.save()
        return redirect(reverse('user_details'))


class UserDetails(TemplateView):
    template_name = 'scrap_group/user_details.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetails, self).get_context_data(**kwargs)

        session = vk.Session()
        api = vk.API(session)

        uid = UserIds.objects.last().user_id

        user = api.users.get(user_ids=uid)

        friends_ids = api.friends.get(user_id=uid)
        friends = api.users.get(user_ids=friends_ids, fields='sex')
        men_count = 0
        women_count = 0
        dafaq_count = 0
        for friend in friends:
            if friend['sex'] == 1:
                women_count += 1
            elif friend['sex'] == 2:
                men_count += 1
            else:
                dafaq_count += 1
        context['user_details'] = user
        context['friends'] = friends
        context['men_count'] = men_count
        context['women_count'] = women_count

        # Wall last two posts (betsbyboss group)
        wall_posts = api.wall.get(domain='betsbyboss', count=1)

        return context


class SendMessagesOne(APIView):

    def get(self, request, format=None):
        application_id = 5743393
        redirect_url = 'http://yvdev.pythonanywhere.com/code'
        url = "https://oauth.vk.com/authorize?client_id=" + str(application_id) + \
              "&display=popup&redirect_uri=" + redirect_url + "&scope=friends&response_type=code&v=5.60"
        RequestHistory.objects.create(action="send_messages")
        return render(request, 'scrap_group/action.html', context={"url": url})


class SendMessagesTwo(APIView):
    def get(self, request, format=None):
        access_token = ''
        return Response('Your access token: ', access_token)


class SendMessagesThree(APIView):
    def get(self, request, format=None):
        access_token = ''
        return Response('Your access token: ', access_token)


class Code(View):
    def get (self,  request, format=None):
        print(request.GET)
        return redirect(reverse('send-messages-two'))
