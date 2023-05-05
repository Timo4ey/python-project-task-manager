from django.test import TestCase, Client
from django.urls import reverse

ru_headers = {"Accept-Language": "ru"}
en_headers = {"Accept-Language": "en"}


class MainTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.main_url = reverse('main')

    def test_main_page_status(self):
        response = self.client.get(self.main_url)
        self.assertEquals(response.status_code, 200)

    def test_ru_content(self):
        response = self.client.get(self.main_url, headers=ru_headers)
        self.assertIn("Привет от Хекслета!", str(response._container[0].decode('utf-8')))
        self.assertEquals(response.headers.get("Content-Language"), "ru")

    def test_en_content(self):
        response = self.client.get(self.main_url, headers=en_headers)
        self.assertIn("Hello from Hexlet", str(response._container[0].decode('utf-8')))
        self.assertEquals(response.headers.get("Content-Language"), "en-us")


class Login(TestCase):

    def setUp(self):
        self.client = Client()
        self.main_url = reverse('login')

    def test_main_page_status(self):
        response = self.client.get(self.main_url)
        self.assertEquals(response.status_code, 200)

    def test_ru_content(self):
        response = self.client.get(self.main_url, headers=ru_headers)
        self.assertIn('<h1 class="my-4">Вход</h1>', str(response._container[0].decode('utf-8')))
        self.assertIn('<label for="id_for_username">Имя пользователя</label>',
                      str(response._container[0].decode('utf-8')))
        self.assertIn('<label for="id_for_password">Пароль</label>', str(response._container[0].decode('utf-8')))
        self.assertIn('<input class="btn btn-primary" type="submit" value="Войти">',
                      str(response._container[0].decode('utf-8')))
        self.assertEquals(response.headers.get("Content-Language"), "ru")

    def test_en_content(self):
        response = self.client.get(self.main_url, headers=en_headers)
        self.assertIn('<h1 class="my-4">Login</h1>', str(response._container[0].decode('utf-8')))
        self.assertIn('<label for="id_for_username">Username</label>',
                      str(response._container[0].decode('utf-8')))
        self.assertIn('<label for="id_for_password">Password</label>', str(response._container[0].decode('utf-8')))
        self.assertIn('<input class="btn btn-primary" type="submit" value="Login">',
                      str(response._container[0].decode('utf-8')))
        self.assertEquals(response.headers.get("Content-Language"), "en-us")


class Registration(TestCase):

    def setUp(self):
        self.client = Client()
        self.main_url = reverse('create_user')

    def test_main_page_status(self):
        response = self.client.get(self.main_url)
        self.assertEquals(response.status_code, 200)

    def test_ruPlease_content(self):
        response = self.client.get(self.main_url, headers=ru_headers)
        self.assertIn('<h1 class="my-4">Регистрация</h1>', str(response._container[0].decode('utf-8')))

        self.assertIn('<label for="id_first_name">Имя</label>',
                      str(response._container[0].decode('utf-8')))

        self.assertIn('<label for="id_last_name">Фамилия</label>',
                      str(response._container[0].decode('utf-8')))

        self.assertIn('<label for="id_password1">Пароль</label>', str(response._container[0].decode('utf-8')))
        self.assertIn('<label for="id_password2">Подтверждение пароля</label>', str(response._container[0].decode('utf-8')))

        self.assertIn('<input class="btn btn-primary" type="submit" value="Зарегистрировать">',
                      str(response._container[0].decode('utf-8')))

        self.assertEquals(response.headers.get("Content-Language"), "ru")

    def test_en_content(self):
        response = self.client.get(self.main_url, headers=en_headers)
        self.assertIn('<h1 class="my-4">Registration</h1>', str(response._container[0].decode('utf-8')))

        self.assertIn('<label for="id_username">Username</label>',
                      str(response._container[0].decode('utf-8')))

        self.assertIn('<label for="id_last_name">Last name</label>',
                      str(response._container[0].decode('utf-8')))

        self.assertIn('<label for="id_password1">Password</label>', str(response._container[0].decode('utf-8')))

        self.assertIn('<label for="id_password2">Password confirmation</label>', str(response._container[0].decode('utf-8')))

        self.assertIn('<input class="btn btn-primary" type="submit" value="Registrate">',
                      str(response._container[0].decode('utf-8')))

        self.assertEquals(response.headers.get("Content-Language"), "en-us")
