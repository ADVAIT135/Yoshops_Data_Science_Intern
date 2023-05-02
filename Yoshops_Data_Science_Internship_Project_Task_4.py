import urllib.request
from urllib.parse import urljoin
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq


def user_input_choice_1():
    item_name = []
    item_name_no_image = []
    site = []
    site_no_image = []
    no_image = []
    description = []
    url_1 = "https://yoshops.com"
    uClient_1 = uReq(url_1)
    page_html_1 = uClient_1.read()

    soup = BeautifulSoup(page_html_1, "html.parser")
    containers = soup.findAll("div", {"class": "col-sm-3 col-xs-6"})

    for container in containers:
        item_name.append(container.div.a.span.text)

        site_link = "https://yoshops.com" + container.div.a.span.get('href')
        site.append(site_link)

        image_link = container.div.a.div.div.img['src']

        if (
                image_link == "//onlinestore.wsimg.com/assets/noimage/product-5fec99477aebb10bac85d82665ec1497de4536cda3279e59089555c45cf589fa.png"):
            item_name_no_image.append(container.div.a.span.text)
            site_no_image.append(site_link)
            no_image.append(image_link)
            url_2 = "https://yoshops.com" + container.div.a.span.get('href')
            uClient_2 = uReq(url_2)
            page_html_2 = uClient_2.read()
            soup = BeautifulSoup(page_html_2, "html.parser")
            product_details = soup.findAll("div", {"class": "single-product-description"})
            item_details = []
            for details in product_details:
                item_details.append(details.text)
            description.append(item_details)
    df_no_image = pd.DataFrame(list(zip(item_name_no_image, site_no_image, no_image, description)),
                               columns=['Product Name', 'Site Link', 'Image Link', 'Product Description'])

    # creating excel writer object
    product_file = pd.ExcelWriter('yoshops-products-with-no-image-for-the-entire-yoshops-site.xlsx')
    # write dataframe to excel

    df_no_image.to_excel(product_file)

    # save the excel
    product_file._save()


def user_input_choice_2():
    item_name = []
    item_name_no_image = []
    site = []
    site_no_image = []
    no_image = []
    description = []
    url_1 = input("Enter the site url : ")
    uClient_1 = uReq(url_1)
    page_html_1 = uClient_1.read()

    soup = BeautifulSoup(page_html_1, "html.parser")
    containers = soup.findAll("div", {"class": "col-sm-3 col-xs-6"})

    for container in containers:
        item_name.append(container.div.a.span.text)

        site_link = "https://yoshops.com" + container.div.a.span.get('href')
        site.append(site_link)

        image_link = container.div.a.div.div.img['src']

        if (
                image_link == "//onlinestore.wsimg.com/assets/noimage/product-5fec99477aebb10bac85d82665ec1497de4536cda3279e59089555c45cf589fa.png"):
            item_name_no_image.append(container.div.a.span.text)
            site_no_image.append(site_link)
            no_image.append(image_link)
            url_2 = "https://yoshops.com" + container.div.a.span.get('href')
            uClient_2 = uReq(url_2)
            page_html_2 = uClient_2.read()
            soup = BeautifulSoup(page_html_2, "html.parser")
            product_details = soup.findAll("div", {"class": "single-product-description"})
            item_details = []
            for details in product_details:
                item_details.append(details.text)
            description.append(item_details)
    df_no_image = pd.DataFrame(list(zip(item_name_no_image, site_no_image, no_image, description)),
                               columns=['Product Name', 'Site Link', 'Image Link', 'Product Description'])

    # creating excel writer object
    product_file = pd.ExcelWriter('yoshops-products-with-no-image-for-the-given-url.xlsx')
    # write dataframe to excel

    df_no_image.to_excel(product_file)

    # save the excel
    product_file._save()

def yoshops_data_science_internship_project_task_4():
    print("Welcome to Yoshops.com")
    print("\n\nPlease select the correct option to find the details of products which don't have an image thumbnail")
    print("\n\nEnter 1 for Input value  = Yoshops.com")
    print("\n\nEnter 2 for Input value= Any main categories and sub categories Link")
    choice = int(input("\n\nEnter your choice from the given available options : "))
    print("\n\nYou have select option ", choice)
    def no_image_thumbnail(choice):
        if choice == 1:
            user_input_choice_1()
        elif choice == 2:
            user_input_choice_2()
        else:
            print("\n\nYou have entered a false choice. Please go through the available options and try again")
    no_image_thumbnail(choice)
    input("Excel File Generated Successfully Enter 0 to Exit: ")

yoshops_data_science_internship_project_task_4()
