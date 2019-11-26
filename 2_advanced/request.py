'''
    Making HTTP requests to any number of services has become even more important with all of the networking and 
    cloud solutions out there. 

    Here ia simple example on how to use the requests library to make calls to a RESTful Web Service. 
    
    The service provides news stories and you can access the information with these links.
    
    To show you how this works, this will get the latest stories and print out
    1. What organziation published it
    2. The author
    3. The title

    This data is provided by : https://newsapi.org/
    Documentation: https://newsapi.org/docs/get-started

'''
import requests 
import json

# This is the country code, try de for German!
country_code = "us"
news_api_key = "4804eefdde4645309b2687aa495b590e"
service_url = "https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(country_code, news_api_key)

# Make a GET request
request_result = requests.get(url = service_url)

if request_result :
    # We have some result, so lets print a little bit out. Remember, we know what the 
    # backend code looks like so we know what to look for in the body. 
    print("CALL STATUS -", request_result.status_code)

    if(request_result.status_code == 200):
        result_body = json.loads(request_result.text)

        print("Status : ", result_body["status"])
        print("Article Count : ", result_body["totalResults"])
        for article in result_body["articles"]:
            print("Source : ", article["source"]["name"])
            print("Author : ", article["author"])
            print("Title  : ", article["title"])
            print("")







