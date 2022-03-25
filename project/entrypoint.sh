#!/bin/sh

echo "Waiting for postgres..."

# * Loop until connection to web-db on
# port 5432 [tcp/postgresql] succeeds
while ! nc -z web-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"