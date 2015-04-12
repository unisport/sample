name = '{{ GUNICORN_NAME }}'
bind = "127.0.0.1:{{ GUNICORN_PORT }}"
workers = '{{ GUNICORN_WORKERS }}'
max_requests = 1000
timeout = 300
log_level = 'error'
