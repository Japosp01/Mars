# %%

# importing the power
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

#initialize splinter next

# %%


executable_path = {'executable_path': 'C:\Program Files\chromedriver.exe'}

browser = Browser('chrome', **executable_path, headless=False)

# %%
# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and 
#collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# %%
# mars news URL
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# %%


# BS object & parser
html = browser.html
mars_news_soup = BeautifulSoup(html, 'html.parser')

# %%

# get 1st title, it might work
first_title = mars_news_soup.find('div', class_='content_title').text
first_title

# %%
#lordy, it worked, now paragraph
first_paragraph = mars_news_soup.find('div', class_='article_teaser_body').text
first_paragraph

# %%


# %%
#I hate html but this is kind of cool
#
#* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign
#the url string to a variable called `featured_image_url`.

# %%
# jpl url

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars%27'
browser.visit(url)

# %%
browser.click_link_by_partial_text('FULL IMAGE')

# %%

# Go to 'more info'
browser.click_link_by_partial_text('more info')

# %%

# redirecting bs
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')

# %%


# get the URL for an incredibly attractive picture
feat_img_url = image_soup.find('figure', class_='lede').a['href']
feat_img_full_url = f'https://www.jpl.nasa.gov{feat_img_url}'
feat_img_full_url

# %%


# %%
# this got less cool quickly
#* Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) 
#and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather 
#report as a variable called `mars_weather`.

# %%
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

# %%
#more BS
html = browser.html
tweet_soup = BeautifulSoup(html, 'html.parser')

# %%
#put the weather somewhere. The tv show Mars on NatGeo is really good. No clue if it's renewed. The show leads me
#to believe it's cold and windy on Mars. We shall now find out.
mars_weather = tweet_soup.find('p', class_='TweetTextSize').text
mars_weather

# %%
#it is cold and windy and out there nobody can hear you scream
# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
#* Use Pandas to convert the data to a HTML table string.
#seems like that is in a lesson


# %%
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
tables

# %%


# %%
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
df = tables[0]
df.columns = ['Variable', 'Value']
df


# %%
#make a string. html.
html_table = df.to_html()
html_table

# %%
#get rid of \n crap
html_table.replace('\n', '')

# %%
#this doesn't quite work and neither does the image one in section 2
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# %%
#more BS
html = browser.html
astrogeology_soup = BeautifulSoup(html, 'html.parser')

# %%



#* You will need to click each of the links to the hemispheres in order to find the image url 
#to the full resolution image.

#* Save both the image url string for the full resolution hemisphere image, 
#and the Hemisphere title containing the hemisphere name. Use a Python dictionary
#to store the data using the keys `img_url` and `title`.

#* Append the dictionary with the image url string and the hemisphere title to a list. 
#This list will contain one dictionary for each hemisphere.

#that is a little confusing

# %%
#this might get the titles (h3s) and arrayify them
hemisphere_titles = []
links = astrogeology_soup.find_all('h3')

for x in links:
    hemisphere_titles.append(x.text)
    
hemisphere_titles
#worked when I bothered to spell astrogeology instead of astrology


# %%
#click, get images, yuck

# %%
hemisphere_image_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
    browser.find_by_css("a.product-item h3")[item].click()
    
    # Find Sample Image Anchor Tag & Extract <href>
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Append Hemisphere Object to List
    hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
    browser.back()

# %%
hemisphere_image_urls

# %%


# %%
