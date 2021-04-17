"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from graphene_django.utils.testing import GraphQLTestCase

from seed.tests.util_test import fill_test_database

class TestGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        fill_test_database()
    
    def test_query_comments(self):
        response_01 = self.query(
            '''
            {
                comments(query: "id=1", orderBy: "id", limit: 1){
                    id
                    content
                    createdBy {
                      id
                    }
                    post {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["comments"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                comments{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["comments"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                commentPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    comments { id }
                }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["commentPagination"]["totalPages"], 1)
            self.assertEqual(res_03["commentPagination"]["totalCount"], 1)
            self.assertEqual(res_03["commentPagination"]["comments"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                commentCount(query: "id=1"){ count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["commentCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                commentCount { count }
            }
            ''')
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["commentCount"]["count"], 1)

    def test_query_comment(self):
        response = self.query(
            '''
            {
                comment(id: 1){
                    id
                    content
                    createdBy {
                      id
                    }
                    post {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["comment"]["id"], 1)
    
    def test_save_comment(self):
        response = self.query(
            '''
            mutation {
                saveComment(
                    content: "",
                    createdBy:  1,
                    post:  1,
                ) {
                    comment {
                        id
                        content
                        createdBy {
                          id
                        }
                        post {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveComment"]["comment"]["id"], 2)
    
    def test_set_comment(self):
        response = self.query(
            '''
            mutation {
                setComment(id:1
                    content: "",
                    createdBy:  1,
                    post:  1,

                ) {
                    comment {
                        id
                        content
                        createdBy {
                          id
                        }
                        post {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setComment"]["comment"]["id"], 1)
    
    def test_delete_comment(self):
        response = self.query(
            '''
            mutation {
                deleteComment(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteComment"]["id"], 1)

    def test_query_posts(self):
        response_01 = self.query(
            '''
            {
                posts(query: "id=1", orderBy: "id", limit: 1){
                    id
                    content
                    picture {
                      id
                    }
                    createdBy {
                      id
                    }
                    likedBy {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["posts"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                posts{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["posts"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                postPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    posts { id }
                }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["postPagination"]["totalPages"], 1)
            self.assertEqual(res_03["postPagination"]["totalCount"], 1)
            self.assertEqual(res_03["postPagination"]["posts"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                postCount(query: "id=1"){ count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["postCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                postCount { count }
            }
            ''')
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["postCount"]["count"], 1)

    def test_query_post(self):
        response = self.query(
            '''
            {
                post(id: 1){
                    id
                    content
                    picture {
                      id
                    }
                    createdBy {
                      id
                    }
                    likedBy {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["post"]["id"], 1)
    
    def test_save_post(self):
        response = self.query(
            '''
            mutation {
                savePost(
                    content: "",
                    picture: 1,
                    createdBy:  1,
                    likedBy: [1],
                ) {
                    post {
                        id
                        content
                        picture {
                          id
                        }
                        createdBy {
                          id
                        }
                        likedBy {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["savePost"]["post"]["id"], 2)
    
    def test_set_post(self):
        response = self.query(
            '''
            mutation {
                setPost(id:1
                    content: "",
                    picture: 1,
                    createdBy:  1,
                    likedBy: [1],

                ) {
                    post {
                        id
                        content
                        picture {
                          id
                        }
                        createdBy {
                          id
                        }
                        likedBy {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setPost"]["post"]["id"], 1)
    
    def test_delete_post(self):
        response = self.query(
            '''
            mutation {
                deletePost(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deletePost"]["id"], 1)

    def test_query_users(self):
        response_01 = self.query(
            '''
            {
                users(query: "id=1", orderBy: "id", limit: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    profileImage {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["users"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                users{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["users"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                userPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    users { id }
                }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["userPagination"]["totalPages"], 1)
            self.assertEqual(res_03["userPagination"]["totalCount"], 1)
            self.assertEqual(res_03["userPagination"]["users"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                userCount(query: "id=1"){ count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["userCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                userCount { count }
            }
            ''')
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["userCount"]["count"], 1)

    def test_query_user(self):
        response = self.query(
            '''
            {
                user(id: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    profileImage {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["user"]["id"], 1)
    
    def test_save_user(self):
        response = self.query(
            '''
            mutation {
                saveUser(
                    username: "email@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                    profileImage: 1,
                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                        profileImage {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveUser"]["user"]["id"], 2)
    
    def test_set_user(self):
        response = self.query(
            '''
            mutation {
                setUser(id:1
                    username: "email_1@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email_1@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                    profileImage: 1,

                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                        profileImage {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setUser"]["user"]["id"], 1)
    
    def test_delete_user(self):
        response = self.query(
            '''
            mutation {
                deleteUser(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteUser"]["id"], 1)