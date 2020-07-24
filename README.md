[![Build Status](https://travis-ci.org/freddorn/coolpets.svg?branch=master)](https://travis-ci.org/freddorn/coolpets)

#   [Coolpets](https://coolpets.herokuapp.com/)

Welcome to Cool Pets, your number one source for all things pet related.
We're dedicated to giving you the very best pet products, with a focus on dogs.
We now serve customers all across the USA and are thrilled that we're able to turn
our passion into offering our pet supplies to you, on our website. 


---
 
## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
    - [**Database**](#database)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
    - [**Automated Testing**](#automated-testing)
    - [**Manual Testing**](#manual-testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

---
 
## UX


### User Stories

As a user, I want to be able to _____________:

- Create an account
- Log into the site
- Log out of the site
- Have a profile page
- Edit and update my profile information on my profile page
- To find the product I am looking for, easily
- Have information given to me that is presented easily to navigate and absorb
- Have the ability to search for the products I am interested in
- Have the website being easy to navigate on any device
- Learn about the business and what they offer
- View the full details of my purchase
- View images of the product, I am considering purchasing
- Know the stock level of an item, I am considering purchasing
- See a summary of my order, on each page of the checkout process
- Be able to look up information on past orders
- Request cancellation on an order that hasn't been processed yet
- Be charged securely for my purchase
- See the checkout progress of my purchase
- Be able to contact the company via a contact form
- Have feedback from the website to inform me when my forms have been entered correctly, or to inform me of an error and how to correct it


### Design

#### Framework

Frameworks used in the project are:

- [BootstrapCDN](https://www.bootstrapcdn.com/)
    - Used to simplify the building of a responsive website.
- [Django](https://www.djangoproject.com/)
    - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [jQuery](https://jquery.com/)
    - To simplify DOM manipulation.

#### Color Scheme

The site uses easy to look at, contrasting colors. A chateau green #28a745 navbar, eclipse #373737 footer, red icons and blue buttons of varying shades.

#### Typography

The Google font [Roboto](https://fonts.google.com/specimen/Roboto) has been used for titles and main headings.

### Wireframes

These can be found using [this link](https://github.com/freddorn/coolpets/tree/master/design/wireframes).

##### back to [top](#table-of-contents)

---
 


## Features
 
### Existing Features

**Navbar**

The options that a user will see displayed in the navbar are dependant on whether or not they are logged in.
- Users that are not logged in will see:
    - Home
    - Shop
    - About
    - Contact
    - Register
    - Login

- Users that are signed into the site will see:
    - Home
    - Shop
    - About
    - Contact
    - Account
    - Logout

- The navbar also features:
    - The Coolpets logo
    - Search Icon
    - Shopping Cart Icon
      -Shopping Cart Counter

- On medium and smaller screen sizes:
    - The logo remains on the left side of the navbar
    - The shopping cart icon and counter is in the center of the navbar
    - A hamburger icon appears on the right side of the navbar, that contains all navigation items and the search icon

**Footer**
  - Product categories are listed on the left side
  - Popular links are listed on the right side
  - The copyright date is set with javascript to the current year

**Home Page**

**Shop Page**

**Search Page**

**Product Listing Page**

**About Page**

**Contact Page**

**Register Page**

**Login Page**

**Account Page**

**Logout Page**

**Cart Page**

**Checkout Pages**

### Features Left to Implement

**Delete Account**
**Email Confirmation after placing order**
**Password Reset**
**Saving customer's Shipping and Payment Information**
  - These features will be implemented at a future date, due to time constraints


###Database

**Users**

The Users model used is the standard one provided by `django.contrib.auth.models`


**Products**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Title | title | max_length=100 | CharField
Shop category | category | choices=CATEGORY_CHOICES | CharField
Image 1 | product_image1 |  | ImageField
Image 2 | product_image2 | blank=True, null=True | ImageField
Image 3 | product_image3 | blank=True, null=True | ImageField
Image 4 | product_image4 | blank=True, null=True | ImageField
Image 5 | product_image5 | blank=True, null=True | ImageField
Description | description |  | TextField
Price | price | max_digits=6, decimal_places=2 | DecimalField
Tags | tags | max_length=300 | CharField
Stock qty | num_in_stock | validators=[MaxValueValidator(100)] | PositiveSmallIntegerField
Featured | featured | default=False | BooleanField

**Shipping**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Country | country | max_length=50 | CharField
Shipping Price | shipping_price | max_digits=6, decimal_places=2 | DecimalField
Shipping Time | shipping_time | max_length=150, default="1 week" | CharField

**Order**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | customer | on_delete=models.PROTECT | ForeignKey to User
Full Name | full_name | max_length=150 | CharField
Address line 1 | address_line_1 | max_length=150 | CharField
Address line 2 | address_line_2 | max_length=150, blank=True | CharField
Town / City | town_or_city | max_length=150 | CharField
State | state | max_length=150, blank=True | CharField
Postcode | postcode | max_length=10 | CharField
Country | country | on_delete=models.PROTECT | ForeignKey to ShippingDestination
Date ordered | date_ordered | default=datetime.date.today | DateField
Paid | paid | default=False | BooleanField
Shipped | shipped | default=False | BooleanField

**Order Items**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order | order | on_delete=models.CASCADE | ForeignKey to Order
Product | product | on_delete=models.PROTECT | ForeignKey to Product
Quantity | quantity | | PositiveSmallIntegerField

##### back to [top](#table-of-contents)

---


## Technologies Used




## Testing



## Deployment



## Credits

### Content

- The text and descriptions of the merchandise, were obtained from [Amazon](https://www.amazon.com/) and [Chewy](https://www.chewy.com/)


### Media

- The image of the three dogs on the Main page was taken by myself.
- The images on the About and Contact pages, were obtained from [Pxhere](https://pxhere.com/en/)
- All category and product images, were obtained from [Amazon](https://www.amazon.com/) and [Chewy](https://www.chewy.com/)



### Acknowledgements

- I received inspiration for this project from [Chewy](https://www.chewy.com/) pet supplies.
- The Slack community, where I have learned a great deal, reading through many posts.
- My mentor Sebastian Immel.
- W3SCHOOLS website for easy explanation of the code.
- Stack Overflow, a good source of knowledge.
- My database structure was inspired by [Anna Greaves](https://github.com/AJGreaves) from her milestone project The House of Mouse.
  