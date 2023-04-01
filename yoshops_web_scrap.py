#NAME : ADVAIT GURUNATH CHAVAN, Yoshops Data Science Internship Project Task 1: Webscrapping Yoshops.com
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

print("Welcome to Yoshops.com")
print("\n\nPlease select the correct option finding the number of products on any webpage of Yoshops.com")
print("\n\nEnter 1 if your product lies into the main category of yoshops.com")
print(
    "\n\nEnter 2 if your product lies into the sub-category of some main category of yoshops.com \nlike (main_cat>sub_cat)")
print(
    "\n\nEnter 3 if your product lies into sub-category of a sub-category of some main category of yoshops.com \nlike (main_cat>sub_cat>sub_sub_cat)")

choice = int(input("\n\nEnter your choice from the given available options : "))
print("\n\nYou have select option ", choice)


def yoshops_product_count(choice):
    if choice == 1:
        url = input("\n\nEnter the url of the webpage of main category of Yoshops.com : ")
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        x = []
        y = []
        for i in soup.find_all('div', class_='product-thumb-inner'):
            x.append(i)
        for j in x:
            y.append(j.find_all('img'))
        for i in soup.find_all('ol'):
            b = i.find_all('li')
        c = []
        for i in b[1]:
            c.append(i)
        print("The number of products in the given url are : ", len(y), "\nThey belong to the category of", c[0],
              "under Yoshops.com")
        print("The number of products available under ", c[0], " are ", len(y))

    elif choice == 2:
        sub_url = input("\n\nEnter the url of the webpage of subcategory under some main category of Yoshops.com : ")
        response = requests.get(sub_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        x = []
        y = []
        for i in soup.find_all('div', class_='product-thumb-inner'):
            x.append(i)
        for j in x:
            y.append(j.find_all('img'))
        for i in soup.find_all('ol'):
            b = i.find_all('li')
        c = []
        for i in b[2]:
            c.append(i)
        for i in soup.find_all('ol'):
            d = i.find_all('a')
        e = []
        for i in d[1]:
            e.append(i)
        print("The number of products in the given url are : ", len(y), "\nThey belong to the Subcategory of", c[0],
              "under Yoshops.com")
        print("The number of products available under ", e[0], ">", c[0], " are ", len(y))

    elif choice == 3:
        sub_sub_url = input(
            "\n\nEnter the url of the webpage of subcategory under some subcategory under some main category of Yoshops.com : ")
        response = requests.get(sub_sub_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        x = []
        y = []
        for i in soup.find_all('div', class_='product-thumb-inner'):
            x.append(i)
        for j in x:
            y.append(j.find_all('img'))
        for i in soup.find_all('ol'):
            b = i.find_all('li')
        c = []
        for i in b[3]:
            c.append(i)
        for i in soup.find_all('ol'):
            d = i.find_all('a')
        e = []
        for i in d[2]:
            e.append(i)
        f = []
        for i in d[1]:
            f.append(i)
        print("The number of products in the given url are : ", len(y), "\nThey belong to the Sub - Subcategory of",
              c[0], "\nwhich is a Subcategory of", e[0], "\nwhich in turn is a sub category of", f[0],
              "which is category available under Yoshops.com")
        print("The number of products available under ", f[0], ">", e[0], ">", c[0], " are ", len(y))

    else:
        print("\n\nYou have entered a false choice. Please go through the available options and try again")


yoshops_product_count(choice)
input("enter 0 to exit : ")