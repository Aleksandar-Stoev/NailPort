from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NailPort.accounts'

    def ready(self):
        import NailPort.accounts.signals  # така се активират
