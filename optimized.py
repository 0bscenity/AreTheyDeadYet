import requests
import bs4
from bs4 import BeautifulSoup

def is_person_dead(url, name):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            death_occurrences = soup.body.find_all(
                string=lambda string: "dead" in string.lower() or "death" in string.lower()
            )
            if death_occurrences:
                print(f"{name}_dead")
                return True
            else:
                print(f"{name}_not_dead️")
                return False
        else:
            print(
                f"Failed to retrieve the webpage. Check if you're connected to the internet. Status code: {response.status_code}"
            )

    except Exception as e:
        print(f"An error occurred: {e}")

# Define the URLs for each person
netscrape = "https://www.famousbirthdays.com/people/dennis-prager.html"
pragerscrape = "https://www.famousbirthdays.com/people/dennis-prager.html"
dickscrape = 'https://www.famousbirthdays.com/people/benjamin-netanyahu.html'
bushscrape = 'https://www.famousbirthdays.com/people/george-w-bush.html'
hkscrape = "https://www.famousbirthdays.com/people/henry-kissinger.html"
jpscrape = "https://www.famousbirthdays.com/people/jordan-peterson.html"

# Check if each person is dead or not
is_person_dead(netscrape, "bn")
is_person_dead(pragerscrape, "dp")
is_person_dead(dickscrape, "dick")
is_person_dead(bushscrape, "bushjr")
is_person_dead(hkscrape, "hk")
is_person_dead(jpscrape, "jp")
