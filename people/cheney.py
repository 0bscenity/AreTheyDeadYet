#bush vp dick cheney
import requests
from bs4 import BeautifulSoup


def is_person_dead(url):
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


url_to_scrape = "https://www.famousbirthdays.com/people/dick-cheney.html"
is_person_dead(url_to_scrape)
