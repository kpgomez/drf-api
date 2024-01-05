# from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Toy


class ToyTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        test_user1.save()

        test_toy = Toy.objects.create(
            title="rake",
            purchaser=test_user1,
            description="Better for collecting leaves than a shovel.",
        )
        test_toy.save()

    def test_toys_model(self):
        toy = Toy.objects.get(id=1)
        actual_purchaser = str(toy.purchaser)
        actual_title = str(toy.title)
        actual_description = str(toy.description)
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_title, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_toy_list(self):
        url = reverse("toy_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        toys = response.data
        self.assertEqual(len(toys), 1)
        self.assertEqual(toys[0]["title"], "rake")

    def test_get_toy_by_id(self):
        url = reverse("toy_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        toy = response.data
        self.assertEqual(toy["title"], "rake")

    def test_create_toy(self):
        url = reverse("toy_list")
        data = {"purchaser": 1, "title": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        toys = Toy.objects.all()
        self.assertEqual(len(toys), 2)
        self.assertEqual(Toy.objects.get(id=2).title, "spoon")

    def test_update_toy(self):
        url = reverse("toy_detail", args=(1,))
        data = {
            "purchaser": 1,
            "title": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        toy = Toy.objects.get(id=1)
        self.assertEqual(toy.title, data["title"])
        self.assertEqual(toy.purchaser.id, data["purchaser"])
        self.assertEqual(toy.description, data["description"])

    def test_delete_toy(self):
        url = reverse("toy_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        toys = Toy.objects.all()
        self.assertEqual(len(toys), 0)
