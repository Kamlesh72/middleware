import time
import logging
import os

from procrastinate_worker import app, flask_app

logger = logging.getLogger(__name__)

class ProcrastinateWebhookQueueService:
    @staticmethod
    @app.task(queue="webhookQueue")
    def enqueue_webhook():
        pid = os.getpid()
        logger.info(f"Worker with pid {pid} started")
        time.sleep(10)
        logger.info(f"Task completed for Worker with pid {pid}")
