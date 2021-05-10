import json_log_formatter
import logging
from django.utils.timezone import now
from django.conf import settings


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord):
        context = extra
        django = {
            'app': getattr(settings,'APP_ID','DefaultApp'), #settings.APP_ID,
            'name': record.name,
            'filename': record.filename,
            'funcName': record.funcName,
            'lineno': record.lineno,
            'msecs': record.msecs,
        }
        if record.exc_info:
            django['exc_info'] = self.formatException(record.exc_info)

        return {
            'message': message,
            'timestamp': now(),
            'level': record.levelname,
            'context': context,
            'django': django
        }