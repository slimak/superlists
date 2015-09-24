#!/usr/bin/python3

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		# uzytkownik uruchamia przegladarke i wpisuje adres

		self.browser.get('http://localhost:8000')

		# sprawdzamy tytul strony i naglowek czy zawiera 'To-Do'

		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# uzytkownik moze od razu wpisac pierwsza rzecz do zrobienia

		# wpisuje 'kupic piora na przynete wedkarska'

		# po nacisnieciu 'enter' strona uaktualnia sie i wyswietla pierwszy element

		# wciaz istnieje mozliwosc wpisania kolejnej rzeczy do zrobienia
		# wpisuje 'uzyc pior i zrobic przynete' naciska przycisk save

		# strona uaktualnia sie i mamy juz dwa elementy

		# sprawdzamy czy lista zostanie zapisana i czy wyswietli sie po wpisaniu spreparowanego adresu url

		# uzytkownik zamyka przegladarke

if __name__ == '__main__':
	unittest.main(warnings='ignore')