# ================
#  TEST LETTINGS
# ================
import pytest

from .models import Letting, Address
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestLettingAndAddress:
    def test_display_lettings_index_page(self):
        client = Client()
        path = reverse('lettings:index')
        response = client.get(path)
        content = response.content.decode()
        expected_content = "<h1>Lettings</h1>"

        assert expected_content in content
        assert response.status_code == 200

    def test_display_letting_detail_page(self):
        client = Client()
        address = Address.objects.create(
            number='7217',
            street='Bedford Street',
            city='Brunswick',
            state='GA',
            zip_code='31525',
            country_iso_code='USA'
        )
        Letting.objects.create(
            title='Joshua Tree Green Haus /w Hot Tub',
            address=address
        )
        path = reverse('lettings:detail', kwargs={'letting_id': 1})
        response = client.get(path)
        content = response.content.decode()
        expected_content = "<h1>Joshua Tree Green Haus /w Hot Tub</h1>"

        assert expected_content in content
        assert response.status_code == 200
