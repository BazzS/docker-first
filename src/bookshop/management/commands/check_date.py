from django.core.management.base import BaseCommand, CommandError
from bookshop.models import Event
from logging import getLogger
from django.core.mail import send_mail

logger = getLogger('django')

class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.warning('works')
