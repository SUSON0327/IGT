from django.test import TestCase
from igensys.views import MainPage
from .models import Haveyour_say
'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	# def test_responding_post_request(self): 
	# 	resp = self.client.post('/', data={'name' :'newName',
	# 		'email': 'newEmail', 
	# 		'experience': 'newExperience'})
	# 	self.assertIn('newName', resp.content.decode())
	# 	self.assertTemplateUsed(resp, 'mainpage.html')
	def test_save_POST_request(self):
		response = self.client.post('/', {'name': 'Suson',
			'email': 'sharmielsuson2000@gmail.com', 
			'experience': 'Great Experience!'})
		self.assertEqual(Haveyour_say.objects.count(), 1)
		newData = Haveyour_say.objects.first()
		self.assertEqual(newData.YourName, 'Suson')
		self.assertEqual(newData.YourEmail, 'sharmielsuson2000@gmail.com')
		self.assertEqual(newData.YourExperience, 'Great Experience!')
	def test_save_POST_redirect(self):
		response = self.client.post('/', {'name': 'Suson',
			'email': 'sharmielsuson2000@gmail.com', 
			'experience': 'Great Experience!'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], '/')
	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Haveyour_say.objects.count(), 0)

class ORMTEST(TestCase):
    def test_saving_retriv(self):
        
        Guest1 = Haveyour_say()
        Guest1.YourName = 'Suson'
        Guest1.YourEmail= 'sharmielsuson2000@gmail.com'
        Guest1.YourExperience= 'Great Experience!'
        Guest1.save()

        Guest2 = Haveyour_say()
        Guest2.YourName = 'Velasquez'
        Guest2.YourEmail= 'emvelasquez@gmail.com'
        Guest2.YourExperience= 'Nice information!'
        Guest2.save()

        Guest = Haveyour_say.objects.all()
        self.assertEqual(Guest.count(), 2)

        Guest1 = Guest[0]
        Guest2 = Guest[1]

        self.assertEqual(Guest1.YourName, 'Suson')
        self.assertEqual(Guest1.YourEmail, 'sharmielsuson2000@gmail.com')
        self.assertEqual(Guest1.YourExperience, 'Great Experience!')
        self.assertEqual(Guest2.YourName, 'Velasquez')
        self.assertEqual(Guest2.YourEmail, 'emvelasquez@gmail.com')
        self.assertEqual(Guest2.YourExperience, 'Nice information!')

    def test_template_display_list(self):
    	Haveyour_say.objects.create(YourName="Travis", YourEmail='travis@gmail.com',
    		YourExperience='Great!' )
    	Haveyour_say.objects.create(YourName="Kylie", YourEmail='kyliejenner@gmail.com',
    		YourExperience='Amazing!')
    	resp = self.client.get('/')
    	self.assertIn('Entry 1: Travis, travis@gmail.com, Great!', resp.content.decode())
    	self.assertIn('Entry 2: Kylie, kyliejenner@gmail.com, Amazing!', resp.content.decode())