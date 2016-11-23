from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

import vk

from scrap_group.models import UserIds


class GroupWall(TemplateView):
    template_name = 'scrap_group/group_wall.html'

    def get_context_data(self, **kwargs):
        context = super(GroupWall, self).get_context_data(**kwargs)

        session = vk.Session()
        api = vk.API(session)
        user = api.users.get(user_ids=1)

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
        print(uid)

        user = api.users.get(user_ids=uid)

        context['user_details'] = user

        return context
