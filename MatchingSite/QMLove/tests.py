from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse
from .forms import UserForm, ProfileForm
from .views import register
from . import models

'''
The class RegisterForms tests that
the forms contain the fields they are
expected to include.
'''
class RegisterForms(TestCase):
    # tests the first form
    # which is the UserForm
    def test_userForm_has_fields(self):
        form = UserForm()
        expected = ['username', 'password', 'first_name', 'last_name']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

    # tests the second form
    # which is ProfileFOrm
    def test_profileForm_has_fields(self):
        form = ProfileForm()
        expected = ['image', 'email', 'gender', 'dob', 'hobby']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

'''
The class RegisterTests tests the actual
registering process.
'''
class RegisterTests(TestCase):
    # set up the url that will be used in the tests below
    # reverse gets the url of the registration page
    # self.response stores the response returned by the server
    def setUp(self):
        url = reverse('QMLove:register')
        self.response = self.client.get(url)

    # the method tests that the response code is 200
    # which means the page can be retrieved
    def test_register_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    # it tests that the register url renders the
    # proper view, which is register
    def test_register_url_resolves_register_view(self):
        view = resolve('/register/')
        self.assertEquals(view.func, register)

    # checks that the registration page contains
    # the UserForm
    def test_register_contains_userForm(self):
        response_userForm = self.response.context.get('userForm')
        self.assertIsInstance(response_userForm, UserForm)

    # checks that the registration page contains
    # the ProfileForm
    def test_register_contains_profileForm(self):
        response_profileForm = self.response.context.get('profileForm')
        self.assertIsInstance(response_profileForm, ProfileForm)

    # tests that the registration response contains
    # csrf token
    def test_register_contains_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    # test the registration inputs
    # it should be 14 inputs because the hobbies' checkboxes
    # are counted as separate inputs
    def test_forms_inputs(self):
        self.assertContains(self.response, '<input', 14)
        self.assertContains(self.response, 'type="text"', 4)
        self.assertContains(self.response, 'type="file"', 1)
        self.assertContains(self.response, 'type="checkbox"', 6)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="submit"', 1)
        self.assertContains(self.response, 'type="password"', 1)

'''
This class tests a successful registration.
'''
class RegistrationSuccessful(TestCase):
    def setUp(self):
        url = reverse('QMLove:register')

        self.uForm = UserForm({
            'username': 'testuser',
            'password': 'testuserpassword',
            'first_name': 'testtt',
            'last_name': 'userrr'
        })
        self.pForm = ProfileForm({
            'image': '',
            'email': 'testuser@gmail.com',
            'gender': 'Male',
            'dob': '10/10/1996',
            'hobby': 'Fishing'
        })

        # there is a many-to-many relationship between Profile and Hobby
        # thus, the tests do not have access to the real database to retrieve the hobbies
        # in order to simulate a successful registration, the line below creates an identic hobby to the one from the real database
        # then the id of the hobby created below is passed to the hobby field in self.client.post
        hobby = models.Hobby.objects.create(name='Fishing')

        # dummy data is passed as a POST request
        # not saved to the database
        self.response = self.client.post(url, {
            'username': 'testuser',
            'password': 'testuserpassword',
            'first_name': 'testtt',
            'last_name': 'userrr',
            'image': '',
            'email': 'testuser@gmail.com',
            'gender': 'M',
            'dob': '10/10/1996',
            'hobby': hobby.id
        })

        self.home_url = reverse('QMLove:index')

    # Test both the forms with valid data
    # The tests should pass
    def test_valid_data(self):
        self.assertTrue(self.uForm)
        self.assertTrue(self.pForm)

    # checks if valid form submission redirects the user to the home page
    def test_successful_registration_redirection(self):
        self.assertRedirects(self.response, self.home_url)

    # check if the User, Profile and Hobby have been created
    # if yes, it returns true
    def test_objects_are_created(self):
        self.assertTrue(models.User.objects.exists())
        self.assertTrue(models.Profile.objects.exists())
        self.assertTrue(models.Hobby.objects.exists())

    # creates a new request to the home page
    # the home page sends a response when making a request
    # that response context should have a field called user inside its context
    # after a successful registration
    def test_user_login(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

    # it tests that the user is redirected back to the homepage
    # after it logs out
    def test_user_logout(self):
        response = self.client.get('/logout/')
        self.assertRedirects(response, self.home_url)

'''
This class tests an unsuccessful registration.
'''
class RegistrationUnsuccessful(TestCase):
    # send a POST request with empty data
    def setUp(self):
        url = reverse('QMLove:register')
        self.response = self.client.post(url, {})

    # unsuccessful form submission should return to the same page
    # which is represented by the status code 200
    def test_register_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    # check if the UserForm has any errors
    def test_userForm_error(self):
        userForm = self.response.context.get('userForm')
        self.assertTrue(userForm.errors)

    # check if the ProfileForm has any errors
    def test_profileForm_error(self):
        profileForm = self.response.context.get('profileForm')
        self.assertTrue(profileForm.errors)

    # tests that the user was not created
    def test_user_not_created(self):
        self.assertFalse(User.objects.exists())
