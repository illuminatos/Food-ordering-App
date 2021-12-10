from rest_framework.decorators import api_view
from rest_framework import status
import json
from django.test import Client
from django.urls import reverse

client = Client()

@api_view(['POST'])
def get_post_puppies(request):
    def setup(self):
        self.valid_payload = {
            "items": [1]
        }
        self.invalid_payload = {
            "items": 1
        }

    def test_post_valid_order(self):
        response = client.post(
            reverse('order'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_order(self):
        response = client.post(
            reverse('order'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

