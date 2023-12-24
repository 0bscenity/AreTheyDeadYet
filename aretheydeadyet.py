#combined everyone
# -*- coding: utf-8 -*-
#
#  aretheydeadyet.py
#  
#  Copyright 2023  <0bscenity>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import requests
import bs4
from bs4 import BeautifulSoup



def is_dp_dead(url):
	try:
		response = requests.get(url)

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, "html.parser")
			death_occurrences = soup.body.find_all(
				string=lambda string: "dead" in string.lower() or "death" in string.lower()
			)
			if death_occurrences:
				print("dp_dead")
			else:
				print("dp_not_dead️")
		else:
			print(
				f"Failed to retrieve the webpage. Check if your connected to the internet. Status code: {response.status_code}"
			)

	except Exception as e:
		print(f"An error occurred: {e}")

def is_hk_dead(url):
	try:
		response = requests.get(url)

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, "html.parser")
			death_occurrences = soup.body.find_all(
				string=lambda string: "dead" in string.lower() or "death" in string.lower()
			)
			if death_occurrences:
				print("hk_dead")
			else:
				print("hk_not_dead️")
		else:
			print(
				f"Failed to retrieve the webpage. Check if your connected to the internet. Status code: {response.status_code}"
			)

	except Exception as e:
		print(f"An error occurred: {e}")

def is_jp_dead(url):
	try:
		response = requests.get(url)

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, "html.parser")
			death_occurrences = soup.body.find_all(
				string=lambda string: "dead" in string.lower() or "death" in string.lower()
			)
			if death_occurrences:
				print("jp_dead")
			else:
				print("jp_not_dead️")
		else:
			print(
				f"Failed to retrieve the webpage. Check if your connected to the internet. Status code: {response.status_code}"
			)

	except Exception as e:
		print(f"An error occurred: {e}")
		
def is_bn_dead(url):
	try:
		response = requests.get(url)

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, "html.parser")
			death_occurrences = soup.body.find_all(
				string=lambda string: "dead" in string.lower() or "death" in string.lower()
			)
			if death_occurrences:
				print("bn_dead")
			else:
				print("bn_not_dead️")
		else:
			print(
				f"Failed to retrieve the webpage. Check if your connected to the internet. Status code: {response.status_code}"
			)

	except Exception as e:
		print(f"An error occurred: {e}")

def is_dick_dead(url):
	try:
		response = requests.get(url)

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, "html.parser")
			death_occurrences = soup.body.find_all(
				string=lambda string: "dead" in string.lower() or "death" in string.lower()
			)
			if death_occurrences:
				print("dick_dead")
			else:
				print("dick_not_dead️")
		else:
			print(
				f"Failed to retrieve the webpage. Check if your connected to the internet. Status code: {response.status_code}"
			)

	except Exception as e:
		print(f"An error occurred: {e}")

def is_bushjr_dead(url):
	try:
		response = requests.get(url)

		if response.status_code == 200:
			soup = BeautifulSoup(response.text, "html.parser")
			death_occurrences = soup.body.find_all(
				string=lambda string: "dead" in string.lower() or "death" in string.lower()
			)
			if death_occurrences:
				print("bush_dead")
			else:
				print("bush_not_dead️")
		else:
			print(
				f"Failed to retrieve the webpage. Check if your connected to the internet. Status code: {response.status_code}"
			)

	except Exception as e:
		print(f"An error occurred: {e}")

netscrape = "https://www.famousbirthdays.com/people/dennis-prager.html"
is_bn_dead(netscrape)

pragerscrape = "https://www.famousbirthdays.com/people/dennis-prager.html"
is_dp_dead(pragerscrape)

dickscrape = 'https://www.famousbirthdays.com/people/benjamin-netanyahu.html'
is_dick_dead(dickscrape)

bushscrape = 'https://www.famousbirthdays.com/people/george-w-bush.html'
is_bushjr_dead(bushscrape)

hkscrape = "https://www.famousbirthdays.com/people/henry-kissinger.html"
is_hk_dead(hkscrape)

jpscrape = "https://www.famousbirthdays.com/people/jordan-peterson.html"
is_jp_dead(jpscrape)


