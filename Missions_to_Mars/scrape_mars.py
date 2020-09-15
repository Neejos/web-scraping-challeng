from selenium import webdriver
from bs4 import BeautifulSoup as bs
    
import time
import pandas as pd

import requests
import pymongo 
    
driver=webdriver.Firefox(executable_path='C:\webdrivers2\geckodriver.exe')




def scrape():
   

    #Step1: extract the News-Title and the News
     #driver to access the url
    url="https://mars.nasa.gov/news/"
    driver.get(url) 
        #access the slide class which has the div elements that contain both the title and the news
    info=driver.find_element_by_class_name("slide")
    soup=bs(info.get_attribute("innerHTML"))
    soup

    News_Title=soup.find('div',class_="content_title").text
    News=soup.find('div',class_="article_teaser_body").text
    print(f'''News Title:{News_Title}
    News:{News}''') 

    # Step 2: extract the featured image url
        #driver access the url and .click function is used to click the buttonon the main page to go the page that has the full image.
    driver.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
    url=driver.find_element_by_class_name("carousel_item").get_attribute("style")
    featured_image_url=url.replace('background-image: url("/','https://www.jpl.nasa.gov/').replace('");','')
# featured_image_url
# url
# driver.find_element_by_id("full_image").click()



#             #image url is saved in a variable
# o=driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/a[3]").click

#     print(Featured_image_url)

    # Step 3:extract the table element from the below url
        #  by using read_html pandas function and assign the table theat u need to the  variable Mars

    df=pd.read_html("https://space-facts.com/mars/")
    Mars=df[0]
     # Rename columns.
    Mars.columns = ['Description', 'Data']
    # Mars.set_index('Description',inplace=True)
    # print(Mars)
                # then converted to html table string variable 'html'and cleaned to final_html to be used later.
    final_html=Mars.replace('\n','')
    html=final_html.to_html(index=False).replace('\n','')


    image={}
    Image_list=[]
    for i in range(1,5,1):
        driver.get("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
        url1=driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[{i}]/div/a/h3').click()
        open=driver.find_element_by_id("wide-image-toggle").click()
        image_url= driver.find_element_by_class_name('wide-image').get_attribute('src')
        image_title=driver.find_element_by_tag_name('h2').text
        image={'img_url':image_url,'title':image_title}
        Image_list.append(image)

    driver.quit()
    

    scrape_mars={}
    
    scrape_mars["News_title"]=News_Title
    scrape_mars["News"]=News
    scrape_mars["Featured_image_url"]=featured_image_url
     
    scrape_mars["html_table"]=html
    scrape_mars["Hemisphere_image_urls"]=Image_list
        
    return scrape_mars

#scrape()
# def load():
     
#     # Initialize PyMongo to work with MongoDBs
#     conn = 'mongodb://localhost:27017'
#     client = pymongo.MongoClient(conn)

#     # Define database and collection
#     db = client.Mars_db
#     collection = db.items

#     data=scrape()
    
#     collection.insert_one(data)
#     return









