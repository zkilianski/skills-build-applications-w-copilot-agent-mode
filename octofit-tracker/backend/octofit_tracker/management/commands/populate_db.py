from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import MongoClient

# Sample data for superheroes, teams, activities, leaderboard, and workouts
def get_sample_data():
    users = [
        {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
        {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
        {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
        {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
        {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
        {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
    ]
    teams = [
        {"name": "Marvel", "description": "Marvel superheroes team"},
        {"name": "DC", "description": "DC superheroes team"},
    ]
    activities = [
        {"user_email": "superman@dc.com", "activity": "Flying", "duration": 60},
        {"user_email": "batman@dc.com", "activity": "Martial Arts", "duration": 45},
        {"user_email": "ironman@marvel.com", "activity": "Suit Training", "duration": 30},
    ]
    leaderboard = [
        {"user_email": "superman@dc.com", "points": 1000},
        {"user_email": "ironman@marvel.com", "points": 950},
    ]
    workouts = [
        {"name": "Strength Training", "description": "General superhero strength workout"},
        {"name": "Agility Drills", "description": "Improve agility and reflexes"},
    ]
    return users, teams, activities, leaderboard, workouts

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        users, teams, activities, leaderboard, workouts = get_sample_data()

        # Insert sample data
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        # Ensure unique index on email for users
        db.users.create_index("email", unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
