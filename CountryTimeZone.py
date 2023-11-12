

import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "https://www.timeanddate.com/worldclock/germany/berlin"
url2 = "https://www.timeanddate.com/worldclock/usa/san-francisco"
url3 = "https://www.timeanddate.com/worldclock/japan/tokyo"



def info_Berlin():
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Locate the element containing time
        clock_element = soup.find("span", {"id": "ct"})
    
        # Extract time text
        time_element = clock_element.get_text()


        # Locate the element containing the date 
        cal_element = soup.find("span", {"id": "ctdat"})
        
        # Extract the date text
        date_element = cal_element.get_text()


        #Locate the element containing the weather
        weather_element  = soup.find("div", {"id": "wt-tp"})

        #Extract the weather element
        weather_element2= weather_element.get_text()

        # Print the result
        print("Date and Time in Berlin:", time_element," || ", date_element, " || ", weather_element2)
    
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)


info_Berlin()



def info_SanFrancisco():
    # Send an HTTP GET request to the URL   
    response = requests.get(url2)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Locate the element containing time
        clock_element = soup.find("span", {"id": "ct"})
    
        # Extract time text
        time_element = clock_element.get_text()


        # Locate the element containing the date 
        cal_element = soup.find("span", {"id": "ctdat"})
        
        # Extract the date text
        date_element = cal_element.get_text()

        #Locate the element containing the weather
        weather_element  = soup.find("div", {"id": "wt-tp"})

        #Extract the weather element
        weather_element2= weather_element.get_text()

        # Print the result
        print("Date and Time in San Francisco:", time_element," || ", date_element, " || ", weather_element2)
    
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)


info_SanFrancisco()


def info_Tokyo():
    # Send an HTTP GET request to the URL   
    response = requests.get(url3)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Locate the element containing time
        clock_element = soup.find("span", {"id": "ct"})
    
        # Extract time text
        time_element = clock_element.get_text()


        # Locate the element containing the date 
        cal_element = soup.find("span", {"id": "ctdat"})
        
        # Extract the date text
        date_element = cal_element.get_text()

        #Locate the element containing the weather
        weather_element  = soup.find("div", {"id": "wt-tp"})

        #Extract the weather element
        weather_element2= weather_element.get_text()

        # Print the result
        print("Date and Time in Tokyo:", time_element," || ", date_element, " || ", weather_element2)
    
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

info_Tokyo()


def infoCountry():
    print("Test")


def get_date_and_time(city, country):
    # Format the city and country in the URL
    url = f"https://www.timeanddate.com/worldclock/{country.lower()}/{city.lower()}"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Locate the element containing the date and time
        clock_element = soup.find("span", {"id": "ct"})

        # Extract the date and time text
        date_and_time = clock_element.get_text()

         # Locate the element containing the date 
        cal_element = soup.find("span", {"id": "ctdat"})
        
        # Extract the date text
        date_element = cal_element.get_text()

        #Locate the element containing the weather
        weather_element  = soup.find("div", {"id": "wt-tp"})

        #Extract the weather element
        weather_element2= weather_element.get_text()

        return date_and_time, date_element, weather_element2
    else:
        return f"Failed to retrieve the web page for {city}, {country}. Status code: {response.status_code}"

# Get user input for the city and country
city_input = input("Enter a city: ").strip()
country_input = input("Enter the country: ").strip()

# Call the function and print the result
result = get_date_and_time(city_input, country_input)

print(f"Date and Time in {city_input.capitalize()}, {country_input.capitalize()}: {result}")









