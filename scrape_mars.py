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
nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(nasa_url)

# Create BeautifulSoup object'
news_soup = bs(browser.html, 'html.parser')
news_soup

# Retrieve the parent divs for all articles
nasa_results = news_soup.find('div', class_='image_and_description_container')
# nasa_results
#For testing to see if an element is printing: browser.is_element_present_by_text(text = "For Insight, Dust", wait_time=2)

# Store title and text results into variables
title = nasa_results.find('h3').get_text()
print(title)

text = nasa_results.find(class_='article_teaser_body' ).get_text()
print(text)

# Part 2 - JPL Mars Space Images - Featured Image

# Visit url
chrome_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **chrome_path)
jpg_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(jpg_url)

jpg_soup = bs(browser.html, 'html.parser')
jpg_soup

# Locate the "full_image" button and click
full_image_button = browser.find_by_id('full_image')
full_image_button.click

# Locate the "more info" button and click
browser.is_element_present_by_text('more info', wait_time=1)
more_info_element = browser.find_link_by_partial_text('more info')

# Parse
image_soup = bs(browser.html, 'html.parser')

img_url = image_soup.select_one('figure.lede a img').get('src')
try:
        img_url = img.get('src')
    except AttributeError:
        return None
img_url

# Use the previously-defined url to create new url
img_url = f'https://www.jpl.nasa.gov{img_url}'
img_url

# Part 3 - Mars Weather

# Visit url
chrome_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **chrome_path)
weather_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(weather_url)

# Parse
weather_soup = bs(browser.html, 'html.parser')

# Retrieve the results
weather_tweet = weather_soup.find('div', 
                                       attrs={
                                           "class": "tweet", 
                                            "data-name": "Mars Weather"
                                        })
print(weather_tweet)

# Locate the tweet text
mars_weather = weather_tweet.find('p', 'tweet-text').get_text()
mars_weather

# Part 4 - Mars Facts 

# Define url
mars_url = 'https://space-facts.com/mars/'

# Web scrape using Pandas
mars_tables = pd.read_html(mars_url)
mars_tables

# Part 5 - Mars Hemispheres

# Visit url
chrome_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **chrome_path)
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)

hemisphere_soup = bs(browser.html, 'html.parser')

# Retrieve the results by looping thorugh the data
hemisphere_dictionary = []


hemisphere_results = broswer.find_by_css('a.product-item h3')

for result in range(len(hemisphere_results)):
    hemisphere = {}
    
    browser.find_by_css('a.product-item h3')[item].click()
        
    hemisphere_sample = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = hemisphere_sample['href']
    
#     Obtain title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    hemisphere_results.append(hemisphere)
    
broswer.back()