import xadmin
from users.models import User
from clubs.models import Institute
from clubs.models import Club
from clubs.models import Notification
from clubs.models import UserClub


class InstituteAdmin(object):

    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10


class ClubAdmin(object):

    list_display = ['name', 'create_time', 'brief', 'type', 'level']
    search_fields = ['name', 'create_time', 'brief', 'type', 'level']
    list_filter = ['name', 'create_time', 'brief', 'type', 'level']
    list_per_page = 10
    date_hierarchy = 'create_time'
    style_fields = {'description': 'ueditor'}


class NotificationAdmin(object):

    list_display = ['club', 'title', 'content', 'publish_date']
    search_fields = ['club', 'title', 'content', 'publish_date']
    list_filter = ['club', 'title', 'content', 'publish_date']
    list_per_page = 10
    date_hierarchy = 'publish_date'
    style_fields = {'content': 'ueditor'}


class UserClubAdmin(object):

    list_display = ['user', 'club']
    search_fields = ['user', 'club']
    list_filter = ['user__username', 'club__name']
    list_per_page = 10


xadmin.site.register(Institute, InstituteAdmin)
xadmin.site.register(Club, ClubAdmin)
xadmin.site.register(Notification, NotificationAdmin)
xadmin.site.register(UserClub, UserClubAdmin)
