from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username='testuser')
        self.assertEqual(user.username, 'testuser')

    def test_team_creation(self):
        user = User.objects.create(username='testuser')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertIn(user, team.members.all())

    def test_activity_creation(self):
        user = User.objects.create(username='testuser')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'run')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')
