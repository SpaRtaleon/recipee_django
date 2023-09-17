

from django.contrib.auth.models import User

user = User.objects.create_user('sparta','spartaleon4@gmail.com','$parta')
user.save()