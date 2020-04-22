from django.contrib.admin.apps import AdminConfig


class RolorexAdminConfig(AdminConfig):
    default_site = 'rolorex.admin.RolorexAdminSite'
