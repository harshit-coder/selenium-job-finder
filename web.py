
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as soup

i=0
l=0
k=0
dataframe = pd.DataFrame(columns =["TITTLE"])
st = input("SEARCH")
for i in range(0,5,10):
    driver = webdriver.Chrome ( "./chromedriver" )
    driver.get ( "https://in.indeed.com/jobs?q=" + str ( st ) + "&l=India&start=" + str ( i ) )
    job_post = driver.find_elements_by_class_name ( 'result' )
    try:
        h = driver.find_element_by_css_selector('path[d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6-6-6z"]')
        for j in job_post :
            result = j.get_attribute( 'innerHTML' )
            sp = soup( result , 'html.parser' )

            try :
                job_tittle = sp.find ( "a" , class_ = "jobtitle" ).text
                print( job_tittle )
                l=l+1
            except :
                print( "none" )
                break

            dataframe=dataframe.append({'TITTLE':job_tittle},ignore_index = True)
    except:
        print("not found")
        for j in job_post :
            result = j.get_attribute( 'innerHTML' )
            sp = soup( result , 'html.parser' )

            try :
                job_tittle = sp.find ( "a" , class_ = "jobtitle" ).text
                print( job_tittle )
                k=k+1
            except :
                print( "none" )
                break
            dataframe=dataframe.append ( {'TITTLE' : job_tittle} , ignore_index = True )
        break
    driver.close()

sum =l+k
print(str(sum)+"post")
dataframe.to_excel("pharma1.xls", index = False)
