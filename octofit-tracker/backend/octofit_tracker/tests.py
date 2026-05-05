from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', members=['a@a.com'])
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='a@a.com', activity='run', distance=5)
        self.assertEqual(activity.activity, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='marvel', points=100)
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', difficulty='easy')
        self.assertEqual(workout.difficulty, 'easy')
