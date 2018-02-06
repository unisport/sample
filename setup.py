#!/usr/bin/env python3
import os
import shutil

if not os.path.exists("/www/"):
    os.mkdir("/www/")

if os.path.exists("/etc/nginx"):
    shutil.copy("nginx.conf", "/etc/nginx")
