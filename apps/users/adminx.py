import xadmin
from xadmin import views
from users.models import User
from users.models import Teacher


class BaseSetting(object):

    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):

    site_title = '社团 GO'
    site_footer = 'http://www.busix.com'
    menu_style = 'accordion'


class UserAdmin(object):

    list_display = ['username', 'nickname', 'mobile', 'institute', 'admission_time',
                    'introduction', 'clubs', 'is_admin']
    search_fields = ['username', 'nickname', 'mobile', 'institute',
                     'admission_time', 'introduction', 'clubs', 'is_admin']
    list_filter = ['username', 'nickname', 'mobile', 'institute',
                   'admission_time', 'introduction', 'clubs', 'is_admin']
    list_per_page = 10
    date_hierarchy = 'admission_time'
    style_fields = {'introduction': 'ueditor'}


class TeacherAdmin(object):

    list_display = ['username', 'nickname', 'mobile']
    search_fields = ['username', 'nickname', 'mobile']
    list_filter = ['username', 'nickname', 'mobile']
    list_per_page = 10


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
