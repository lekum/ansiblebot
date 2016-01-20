import logging
import os

BACKEND = 'Slack'
BOT_IDENTITY = {
     'token': os.getenv("SLACK_API_TOKEN"),
}
CHATROOM_FN = 'ansiblebot'
BOT_DATA_DIR = 'data'
BOT_EXTRA_PLUGIN_DIR = 'plugins'
BOT_LOG_FILE = "/".join((BOT_DATA_DIR, 'err.log'))
BOT_LOG_LEVEL = logging.INFO


BOT_ADMINS = ('gbin@localhost',)
CHATROOM_PRESENCE = ('example',)
BOT_PREFIX = '!'
DIVERT_TO_PRIVATE = ()
CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}
BOT_LOG_SENTRY = False
SENTRY_DSN = ''
SENTRY_LOGLEVEL = BOT_LOG_LEVEL
BOT_ASYNC = True
