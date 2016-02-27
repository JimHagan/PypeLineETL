from __future__ import absolute_import

from datetime import timedelta
from tasks import NIGHTLY_REFRESH_SCHEDULE


CELERY_ALWAYS_EAGER = False
CELERY_IGNORE_RESULT = False

BROKER_URL = "redis://localhost:6379/0"

CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

CELERY_IMPORTS = (
    'tasks',
)

CELERYD_POOL = "eventlet"


# For production configuration
# set this to NIGHTLY_REFRESH_SCHEDULE
CELERYBEAT_SCHEDULE = {}


CELERY_TIMEZONE = 'UTC'
