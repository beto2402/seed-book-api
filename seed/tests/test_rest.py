"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from rest_framework import status
from rest_framework.test import APITestCase

from seed.tests.util_test import fill_test_database

class TestRest(APITestCase):
    def setUp(self):
        fill_test_database()
    
    def test_get_comments(self):
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_comment(self):
        response = self.client.get('/api/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_comment(self):
        data = {
            "content": "",
            "created_by_id":  1,
            "post_id":  1,
        }
        response = self.client.post('/api/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_comment(self):
        data = {
            "content": "",
            "created_by_id":  1,
            "post_id":  1,
        }
        response = self.client.put('/api/comments/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_comment(self):
        response = self.client.delete('/api/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_post(self):
        response = self.client.get('/api/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_post(self):
        data = {
            "content": "",
            "picture_id": 1,
            "created_by_id":  1,
            "liked_by_ids": [1],
        }
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_post(self):
        data = {
            "content": "",
            "picture_id": 1,
            "created_by_id":  1,
            "liked_by_ids": [1],
        }
        response = self.client.put('/api/posts/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_post(self):
        response = self.client.delete('/api/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_user(self):
        response = self.client.get('/api/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_user(self):
        data = {
            "username": "email_1@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "email": "email_1@test.com",
            "password": "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
            "is_active": False,
            "profile_image_id": 1,
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_user(self):
        data = {
            "username": "email_1@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "email": "email_1@test.com",
            "password": "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
            "is_active": False,
            "profile_image_id": 1,
        }
        response = self.client.put('/api/users/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_user(self):
        response = self.client.delete('/api/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)