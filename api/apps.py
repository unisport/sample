from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        """Run when app has been loaded."""
        from api.importer import import_unisport_data

        import_unisport_data()
