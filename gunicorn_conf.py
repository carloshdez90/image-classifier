from multiprocessing import cpu_count

''' 
	Update paths to match with your file system
'''

# Socket Path
bind = 'unix:/home/deploy/imagenet21k/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/deploy/imagenet21k/logs/access_log.log'
errorlog = '/home/deploy/imagenet21k/logs/error_log.log'
