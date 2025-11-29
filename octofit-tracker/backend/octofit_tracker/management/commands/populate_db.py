from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all users
        User.objects.all().delete()

        # Create Marvel and DC teams
        Team = self.get_team_model()
        Team.objects.all().delete()
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        users = [
            {'email': 'tony@marvel.com', 'username': 'IronMan', 'team': marvel},
            {'email': 'steve@marvel.com', 'username': 'CaptainAmerica', 'team': marvel},
            {'email': 'bruce@marvel.com', 'username': 'Hulk', 'team': marvel},
            {'email': 'clark@dc.com', 'username': 'Superman', 'team': dc},
            {'email': 'bruce@dc.com', 'username': 'Batman', 'team': dc},
            {'email': 'diana@dc.com', 'username': 'WonderWoman', 'team': dc},
        ]
        for u in users:
            User.objects.create_user(email=u['email'], username=u['username'], password='password', team=u['team'])

        # Create activities, leaderboard, workouts collections as needed
        # ... (implement as you define models)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

    def get_team_model(self):
        from octofit_tracker.models import Team
        return Team
