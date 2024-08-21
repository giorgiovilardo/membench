run-flask:
  python -m memray run -m gunicorn -w 4 -b 0.0.0.0:8000 src.pypro.flask:app

run-falcon-sync:
  python -m memray run -m gunicorn -w 4 -b 0.0.0.0:8000 src.pypro.falcon_sync:app

run-falcon-async:
  python -m memray run -m uvicorn --port 8000 --workers 4 --log-level critical src.pypro.falcon_async:app

run-fastapi:
  python -m memray run -m uvicorn --port 8000 --workers 4 --log-level critical src.pypro.fastapi:app

run-litestar:
  python -m memray run -m uvicorn --port 8000 --workers 4 --log-level critical src.pypro.litestar:app

run-wsgi:
  python -m memray run -m gunicorn -w 4 -b 0.0.0.0:8000 src.pypro.wsgi:app

locust:
  locust -f locustfile.py --headless -u 100 -r 20 -t 1m --host http://127.0.0.1:8000
