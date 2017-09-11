import multiprocessing

pythonpath = "/home/mikhail/Documents/webenv/web/ask"
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
