from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'clients'

    def ready(self):
        import clients.signals