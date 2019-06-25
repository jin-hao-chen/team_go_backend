import xadmin
from clubs.models import Institute
from clubs.models import Club
from clubs.models import Notification


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


class NotificationAdmin(object):

    list_display = ['title', 'content', 'publish_date']
    search_fields = ['title', 'content', 'publish_date']
    list_filter = ['title', 'content', 'publish_date']
    list_per_page = 10
    date_hierarchy = 'publish_date'


xadmin.site.register(Institute, InstituteAdmin)
xadmin.site.register(Club, ClubAdmin)
xadmin.site.register(Notification, NotificationAdmin)
