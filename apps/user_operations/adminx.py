import xadmin
from users.models import User
from user_operations.models import Apply
from user_operations.models import Follow


class ApplyAdmin(object):

    list_display = ['user', 'club', 'department_name']
    search_fields = ['user', 'club', 'department_name']
    list_filter = ['user__username', 'club__name', 'department_name']
    list_per_page = 10

    # def get_username(self, apply):
    #     name = map(lambda x: User.objects.filter(id=x.user_id).username, apply.objects.all())
    #     return name
    #
    # def get_club_name(self, apply):
    #     name = map(lambda x: User.objects.filter(id=x.club_id), apply.objects.all())
    #     return name


class FollowAdmin(object):

    list_display = ['get_username', 'get_club_name']
    search_fields = ['get_username', 'get_username']
    list_filter = ['user__username', 'club__name']
    list_per_page = 10

    def get_username(self, apply):
        name = map(lambda x: User.objects.filter(id=x.user_id).username, apply.objects.all())
        return name

    def get_club_name(self, apply):
        name = map(lambda x: User.objects.filter(id=x.club_id), apply.objects.all())
        return name


xadmin.site.register(Apply, ApplyAdmin)
xadmin.site.register(Follow, FollowAdmin)