import xadmin
from xadmin import views


class BaseSetting(object):

    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):

    site_title = '社团 GO'
    site_footer = 'http://www.busix.com'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
