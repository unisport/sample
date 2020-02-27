#!/bin/sh

dockerize -wait tcp://$DB_HOSTNAME:5432 -timeout 10s
if [ "$NO_MIGRATE" != "1" ]; then
    python3 manage.py migrate
    echo "=== MIGRATION COMPLETE ==="
fi

echo "=== LOADING DJANGO APP === "

exec "$@"
