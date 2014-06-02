#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unisport.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unibet.settings")
>>>>>>> 11a138d8bd8f3db99059a41adc16b714ed3293cf

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
