from django.views.generic import TemplateView


class GroupWall(TemplateView):
    template_name = 'scrap_group/group_wall.html'

    def get_context_data(self, **kwargs):
        context = super(GroupWall, self).get_context_data(**kwargs)

        context['posts'] = []

        return context
