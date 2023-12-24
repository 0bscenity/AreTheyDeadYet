#combined everyone test v1
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
				print("dead")
			else:
				print("not_dead️")
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
				print("dead")
			else:
				print("not_dead️")
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


