release: python manage.py migrate
web: daphne ideahubio.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker channels --settings=ideahubio.settings -v2