from django.test import TestCase, Client
from django.urls import reverse
from search_app.models import Data
import json

class TestSearchApi(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_method(self):
        # Create some test data in the database (if needed)
        # You can create Data objects using Data.objects.create()
        print(print(Data.objects.all()))
        # Define your test data
        test_data = {
            'drawing_number': '10674-S',
            'descr': ''
        }
        # print(reverse('search'))
        # Make a GET request to your API endpoint
        
        response = self.client.post(reverse('search'), data=json.dumps(test_data), content_type='application/json')
        print('RESPONCE', end= ' ')
        print(response.content.decode('utf-8'))
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)