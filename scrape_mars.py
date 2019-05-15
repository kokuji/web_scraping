# Import dependencies
import pandas as pd
import numpy as np
import os
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser

# Step 1 - NASA Mars News
chrome_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **chrome_path)

# URL of page to be scraped
def mars_news(browser):
    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(nasa_url)
    
    # Create BeautifulSoup object'
    news_soup = bs(browser.html, 'html.parser')
#     news_soup

# Retrieve the parent divs for all articles
    try:
        nasa_results = news_soup.find('div', class_='image_and_description_container')
# nasa_results
#For testing to see if an element is printing: browser.is_element_present_by_text(text = "For Insight, Dust", wait_time=2)

# Store title and text results into variables
        news_title = nasa_results.find('h3').get_text()
#     print(title)
        news_text = nasa_results.find(class_='article_teaser_body' ).get_text()
#     print(text)
    except AttributeError:
        return None, None
    return news_title, news_text


# Part 2 - JPL Mars Space Images - Featured Image


def featured_image(browser):
    jpg_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpg_url)
    
    # Locate the "full_image" button and click
    full_image_button = browser.find_by_id('full_image')
    full_image_button.click
    #For testing to see if an element is printing: browser.is_element_present_by_text(text = "For Insight, Dust", wait_time=2)
    
    # Locate the "more info" button and click
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_element = browser.find_link_by_partial_text('more info')
    more_info_element.click()
    
    jpg_soup = bs(browser.html, 'html.parser')
#     jpg_soup
    
    jpg_url = jpg_soup.select_one('figure.lede a img').get('src')
    try:
        image_url = img.get('src')
    except AttributeError:
        return None
    
    image_url = f'https://www.jpl.nasa.gov{jpg_url}'
    return image_url

# Part 3 - Mars Weather

def weather_twitter(browser):
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    
    # Parse
    weather_soup = bs(browser.html, 'html.parser')
    
    weather_tweet = weather_soup.find('div', 
                                       attrs={
                                           "class": "tweet", 
                                            "data-name": "Mars Weather"
#     print(weather_tweet)
    # Locate the tweet text
    mars_weather = weather_tweet.find('p', 'tweet-text').get_text()
    return mars_weather

# Part 4 - Mars Facts 
mars_url = 'https://space-facts.com/mars/'

def mars_facts():
# Define url
    try:
    # Web scrape using Pandas
        mars_tables = pd.read_html(mars_url)
#         mars_tables
    except BaseException:
        return None
    mars_tables.columns = ['description', 'value']
    mars_tables.set_index('description', inplace=True)

# Part 5 - Mars Hemispheres

# Visit url

def hemisphere(browser):
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
# Retrieve the results by looping thorugh the data
    hemisphere_dictionary = []
    
    hemisphere_results = browser.find_by_css('a.product-item h3')

    for result in range(len(hemisphere_results)):
        hemisphere = {}
    
        browser.find_by_css('a.product-item h3')[item].click()
        
        hemisphere_sample = browser.find_link_by_text('Sample').first
        hemisphere['img_url'] = hemisphere_sample['href']
    
#     Obtain title
        hemisphere['title'] = browser.find_by_css('h2.title').text
    
        hemisphere_dictionary.append(hemisphere)
    
        browser.back()
    
    return hemisphere_dictionary

def hemisphere_scrape(html_text):
    hemisphere_soup = bs(html_text, 'html.parser')

    try: 
        hemisphere_title = hemisphere_soup.find('h2', class_="title").get_text()
        hemisphere_sample_soup = hemisphere_soup.find('a', text="Sample").get('href')
    except AttributeError:
        hemisphere_title = None
        hemisphere_sample_soup = None 
    hemisphere = {
        "title": title_element,
        "img_url": hemisphere_sample_soup
    }
    return hemisphere


def scrape_all():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    news_title, news_text = mars_news(browser)
    jpg_url = featured_image(browser)
    mars_weather = twitter_weather(browser)
    hemisphere_dictionary = hemisphere(browser)
    facts = mars_facts()
    timestamp = dt.datetime.now()

    data = {
        "news_title": news_title,
        "news_paragraph": news_text,
        "featured_image": jpg_url,
        "hemispheres": hemisphere_dictionary,
        "weather": mars_weather,
        "facts": facts,
        "last_modified": timestamp
    }
    browser.quit()
    return data 


if __name__ == "__main__":
    print(scrape_all())
