import django
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

# Create Users
def create_users():
    users = []
    for username in ['alice', 'bob', 'carol']:
        user, _ = User.objects.get_or_create(username=username)
        users.append(user)
    return users

# Create Teams
def create_teams(users):
    team1, _ = Team.objects.get_or_create(name='Team Alpha')
    team2, _ = Team.objects.get_or_create(name='Team Beta')
    team1.members.set(users[:2])
    team2.members.set(users[1:])
    return [team1, team2]

# Create Activities
def create_activities(users):
    Activity.objects.get_or_create(user=users[0], activity_type='run', duration=30, date=date(2024, 1, 1))
    Activity.objects.get_or_create(user=users[1], activity_type='bike', duration=45, date=date(2024, 1, 2))
    Activity.objects.get_or_create(user=users[2], activity_type='swim', duration=20, date=date(2024, 1, 3))

# Create Workouts
def create_workouts(users):
    w1, _ = Workout.objects.get_or_create(name='Pushups', description='Do 20 pushups')
    w2, _ = Workout.objects.get_or_create(name='Situps', description='Do 30 situps')
    w1.suggested_for.set([users[0], users[1]])
    w2.suggested_for.set([users[2]])
    return [w1, w2]

# Create Leaderboards
def create_leaderboards(teams):
    Leaderboard.objects.get_or_create(team=teams[0], score=150)
    Leaderboard.objects.get_or_create(team=teams[1], score=120)

def main():
    users = create_users()
    teams = create_teams(users)
    create_activities(users)
    create_workouts(users)
    create_leaderboards(teams)
    print('Test data created successfully.')

if __name__ == '__main__':
    main()
