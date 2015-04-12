import sys
from .apps_settings import *
from .common import *

try:
    from .local import *

    invalid_key = '123456789_123456789_123456789_123456789_123456789_'

    if SECRET_KEY == invalid_key and sys.argv[1] != 'generate_secret_key':
        print ("Please, fill 'SECRET_KEY' setting in 'conf/settings/local.py' file\n"
               "Generate it by running command\n"
               "$ python manage.py generate_secret_key")

        import sys
        sys.exit(1)

except ImportError:
    print ("Please, provide your local configuration for this project.\n"
           "You need to create 'conf/settings/local.py' with your local settings.")
    import sys
    sys.exit(1)
