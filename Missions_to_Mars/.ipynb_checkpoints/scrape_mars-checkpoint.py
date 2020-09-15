from selenium import webdriver
from bs4 import BeautifulSoup as bs
    
import time
import pandas as pd

import requests
    
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

        
    driver.find_element_by_id("full_image").click()
            #image url is saved in a variable
    Featured_image_url=driver.find_element_by_class_name("fancybox-image").get_attribute("src")
    print(Featured_image_url)

    # Step 3:extract the table element from the below url
        #  by using read_html pandas function and assign the table theat u need to the  variable Mars

    df=pd.read_html("https://space-facts.com/mars/")
    Mars=df[0]
    Mars.rename({0:"Description",1:"Mars"},axis=1,inplace=True)
    Mars.set_index('Description',inplace=True)
            # then converted to html table string variable 'html'and cleaned to final_html to be used later.
    final_html=Mars.replace('\n','')
    html=final_html.to_html()
    print(html)
    





    for i in range(1,5,1):
    driver.get("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    url1=driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[{i}]/div/a/h3').click()
    open=driver.find_element_by_id("wide-image-toggle").click()
    image_url= driver.find_element_by_class_name('wide-image').get_attribute('src')
    image_title=driver.find_element_by_tag_name('h2').text
    #image_title=driver.find_element_by_css_selector(section[class='block metadata']).find_element_by_tag_name('h2').text
    #driver.findElement(By.cssSelector("section[class='block metadata']")).find_element_by_tag_name('h2').text

#     image_title=driver.find_element_by_css_selection('section.metadata').find_element_by_tag_name('h2').text
#     print(image_url,image_title)
    image.append({'img_url':img_url1,'title':img_title1})
     

    scrape_mars={}
    
    scrape_mars["News_title"]=News_Title
    scrape_mars["News"]=News
    # scrape_mars["Featured_image_url"]=Featured_image_url
        
    scrape_mars["html_table"]=final_html
    scrape_mars["Hemisphere_image_urls"]=image
        
    return scrape_mars











