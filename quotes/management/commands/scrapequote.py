from django.core.management.base import BaseCommand
from requests.api import options
from quotes.models import Quote
from bs4 import BeautifulSoup
import requests
import random

class Command(BaseCommand):
    help = 'Scrapes n quotes from Goodreads by category and saves them to the database'

    def add_arguments(self, parser) -> None:
        parser.add_argument('category', type = str)
        parser.add_argument('n', type = int)

    def handle(self, *args, **options):
        category = options['category']
        number = options['n']
        html = requests.get(f"https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q={category}&commit=Search").content
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all("div", class_ = "quoteDetails")
        authors = []
        quotes = []
        for result in results:
            quote = result.find("div", class_ = "quoteText")
            quotes.append(quote.text.split("\n")[1].strip("\n “”"))
            author = quote.find("span", class_ = "authorOrTitle")
            authors.append(author.text.strip("\n ,"))

        for quote, author in zip(quotes[:number], authors[:number]):
            quote_obj = Quote(quote = f"{quote}", author = author, rating = random.choice([1, 2, 3, 4, 5]))
            quote_obj.save()
