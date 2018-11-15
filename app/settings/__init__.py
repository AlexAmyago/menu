import os

if os.getenv('ENV') == 'local':
    from .local import *
elif os.getenv('ENV') == 'production':
    from .production import *
