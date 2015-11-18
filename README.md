# shop-scraper
Scrapes specific shops for their data and displays them as an aggregate for the user

# Currently working features:
- Classes created for different types of RW&Co items and pages (Once this works for RW&Co I will add other retailers)
- Selenium scrolling down works to trigger infinite scroll to get entire DOM
- Given HTML, parser can identify different item's links

# Currently working on:
- Parsing all the HTML with BeautifulSoup, to populate classes (will add in DB later)

# Next steps:
- Adding more retailers
- Integrating with web:
  - Set up database for scraped data
  - Set up time at night to scrape, every 24 hours
  - Set up front-end to display scraped data nicely and allow users to customize data they want
  - Set up relationship between DB and front end
  - Deployment!
