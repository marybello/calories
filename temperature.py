from selectorlib import Extractor
import requests


class Temperature:
    """
    This class will get a temperature value from the 'timeanddate.com/weather' webpage
    """

    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def build_url(self):

        url = self.base_url + self.country + "/" + self.city
        return url

    def scrape(self):

        url = self.build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract(full_content)

        return  raw_content

    def get(self):

        scraped_content = self.scrape()
        return float(scraped_content['temp'].replace("\xa0°C", "").strip())


