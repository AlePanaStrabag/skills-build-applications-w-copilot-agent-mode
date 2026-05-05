from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connessione a MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Cancella dati esistenti
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Crea indice unico su email
        db.users.create_index('email', unique=True)

        # Dati di esempio
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Batman", "email": "batman@dc.com", "team": "dc"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
        ]
        teams = [
            {"name": "marvel", "members": ["ironman@marvel.com", "cap@marvel.com"]},
            {"name": "dc", "members": ["batman@dc.com", "wonderwoman@dc.com"]},
        ]
        activities = [
            {"user_email": "ironman@marvel.com", "activity": "run", "distance": 5},
            {"user_email": "batman@dc.com", "activity": "cycle", "distance": 10},
        ]
        leaderboard = [
            {"team": "marvel", "points": 100},
            {"team": "dc", "points": 90},
        ]
        workouts = [
            {"name": "Pushups", "difficulty": "easy"},
            {"name": "Squats", "difficulty": "medium"},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Database octofit_db popolato con dati di esempio!'))
