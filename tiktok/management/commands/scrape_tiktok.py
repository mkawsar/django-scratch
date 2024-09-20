from typing import Any
from tiktok.scraper import scrape_tiktok_videos
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **kwargs):
        usernames = ['senorita_toe']
        for uname in usernames:
            scrape_tiktok_videos (uname)
