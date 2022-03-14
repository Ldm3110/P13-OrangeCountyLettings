# ================
#  TEST PROFILES
# ================
import pytest
from django.contrib.auth.models import User

from .models import Profile
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestProfiles:

    def test_display_profiles_index_page(self):
        client = Client()
        path = reverse('profiles:index')
        response = client.get(path)
        content = response.content.decode()
        expected_content = "<h1>Profiles</h1>"

        assert expected_content in content
        assert response.status_code == 200

    def test_display_profile_detail_page(self):
        client = Client()
        user = User.objects.create(
            username='AirWow',
            first_name='Ada',
            last_name='Paul',
            email='flocation.vam4@glendenningflowerdesign.com',
        )
        Profile.objects.create(
            user=user,
            favorite_city='Budapest',
        )
        path = reverse('profiles:detail', kwargs={'username': 'AirWow'})
        response = client.get(path)
        content = response.content.decode()
        expected_content = "<h1>AirWow</h1>"

        assert expected_content in content
        assert response.status_code == 200
