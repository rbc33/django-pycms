from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = "procces tailwind classes to output.css"

    def handle(self, *args, **kwargs):

        subprocess.run(
            [
                "tailwinds-macos-3.4.1",
                "-i",
                "./api/static/style.css",
                "-o",
                "./api/static/output.css",
                "-m",
            ]
        )
