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
    - [**Languages**](#languages)
    - [**Libraries**](#libraries)
    - [**Databases**](#databases)
    - [**Tools**](#tools)

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
  1. At the top of the page is an image of three dogs.
  2. The title of the page and a brief introduction. 
  3. A Learn More link, that leads to the About page.
  4. Category images, where the first two are larger images and underneath those with four smaller images.
  5. Featured Listings with four images, each from a different category.
  6. A Browse More link, that leads to the All Products page.
  
**Product Page**
  1. With the Shop links in the navbar, View All will show all products.
  2. All categories of products are in a dropdown menu of the navbar that will show all the products of a certain category.
  3. When viewing All Products, all links to each category are at the top of the page.
  4. On the All Products page, there is a sorting capability to sort each listing by Featured, Price high to low, or Price low to high.
  5. At the top of the page, are bread crumbs that show which page you are viewing.
  6. If more than 12 listings are shown, pagination buttons will be shown at the bottom of the page.

**Search Page**
  1. Similar to the All Products page with the same category links and bread crumbs.
  2. A search field to enter your search criteria.
  3. All matching listings will be displayed, or a message stating that no items were found in the search.

**Product Listing Page**
  1. Has bread crumbs as the other pages have.
  2. The title of the product is shown.
  3. There are five images of each product, with the thumbnail images to the right of a larger image of which image is currently selected.
  4. The price is shown, along with a dropdown menu to select your quantity and an Add To Cart button.
  5. A description of the product.
  6. A You Might Also Like section, shows more similiar products, that a customer could add on to the order.
  7. A Browse More link, to the category of the product that is currently being shown.

**About Page**
  1. At the top of the page is an image of two dogs.
  2. The name of the company and a  paragraph describing the company.
  3. A Visit Shop link that leads to the All Products page.

**Contact Page**
  1. At the top of the page, is another image of two dogs.
  2. A contact form for contacting the company.
  3. The form has a field for Name, Email and Message.

**Register Page**
  1. Uses the same image, that the Account page uses.
  2. A form with fields for username, email, password and password confirmation.
  3. A description of which characters are accepted in creating your password.

**Login Page**
  1. Uses the same image, that the Account page uses.
  2. A log in form of the username and password.
  3. Form validation is used and informs the user that they are logged in, or that either the username or password are incorrect.

**Account Page**
  1. At the top of the page, is an image of three dogs.
  2. The user's profile information is shown and can be updated.
  3. All of the user's previous orders as well as the order's details are shown.

**Logout Page**
  1. Uses the same image, that the Account page uses.
  2. Advises that You have successfully logged out.
  3. Has a link to Log in again.

**Cart Page**
  1. Has the name of the product or products.
  2. Shows the product prices and quantities.
  3. Lists the subtotal of the order.

**Checkout Information Page**
  1. The customer enters their shipping information into a form.
  2. The price, quantity and subtotal information from the cart page is shown.

**Checkout Shipping Page**
  1. The customer's shipping information is shown.
  2. The user selects their shipping method, which currently only has one choice.
  3. The order summary with the total amount is shown.

**Checkout Payment Page**
  1. The customer's shipping information is shown.
  2. The order summary with the total amount is shown.
  3. A Continue To Payment link leads to a Stripe generated payment page.

**Stripe Payment Page**
  1. The order total amount is shown on this payment page hosted by Stripe.
  2. All card information is entered and processed by Stripe.

**Checkout Confirmation Page**
  1. An Order Confirmed message is shown.
  2. The customer's name and shipping information is shown.
  3. Links are present to the Account and Contact pages.

### Features Left to Implement

1. Delete Account
2. Email Confirmation after placing order
3. Password Reset
4. Saving customer's Shipping and Payment Information
  - These features will be implemented at a future date, due to time constraints


### Database

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

### Languages
* HTML 
* CSS 
* Javascript
* Python

### Libraries
- [Bootstrap](https://www.bootstrapcdn.com/) Simplifies the website structure and easily makes it responsive.
- [JQuery](https://jquery.com) Simpifies DOM manipulation.
- [Google Fonts](https://fonts.google.com/) Styling the website fonts.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) Provides icons for the website.

### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Tools
- [Gitpod](https://https://www.gitpod.io/) IDE used to develop the project. 
- [Django](https://www.djangoproject.com/) Python web framework.
- [Stripe](https://stripe.com) Platform for accepting secure payments.
- [Travis](https://travis-ci.org/) Continuous Integration testing.
- [AWS S3](https://aws.amazon.com/) Storage for the profuct images in the database.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) Allows the web app to serve its own static files.
- [Obfuscator](https://obfuscator.io/) Used to conceal the stripe public key.
- [Imgbb](https://imgbb.com) Storage for static page images.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) For handling version control.
- [GitHub](https://github.com/) For remotely storing and sharing project code.
- [Heroku](https://www.heroku.com/) Was used to deploy the project.
- [Email JS](https://www.emailjs.com/) Send email directly from your client-side Javascript code without server-side code.
 


##### back to [top](#table-of-contents)

---


## Testing

### Automated Testing
- [Travis](https://travis-ci.org/) was used throughout the unit testing of this project to provide continuous integration with the deployed site.
  - In the heroku deployment settings, it will only allow deployment, when Travis CI has passed the latest push to the master branch on GitHub.

- Unittests in combination with the coverage.py testing tool.


### Manual Testing
- All python pages are mostly PEP8 compliant, with four instances of the `line too long` error.
  - Disregarded the message as I could not find an alernative format for each instance.

- The W3C Jigsaw validator does not recognize root variables, and therefore passes **Parse Errors**.

- When validating Javascript, the following errors appeared as the validator could not recognize JQuery or Stripe:
  - '$' is not defined.
  - "STRIPE" is not defined.

- All images are displaying properly.

- Links and URLs are working correctly.

- The Responsiveness of the site is good at all screen sizes.

- All pages are rendering as expected.

- The back-end functionality is working as expected.

- Stripe payments is operating properly.

### Validators
* [AutoPrefixer](https://autoprefixer.github.io/)
    - To make sure the css code is valid for all browsers.

* [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
    - To check the the validity of the CSS code. 
    
* [W3C Markup Validation](https://validator.w3.org/)
    - To check the the validity of the HTML code. 

* [Javascript Syntax Validator](https://esprima.org/demo/validate.html)
    - Checks for javascript mistakes and errors.
    
* [JS Hint](https://jshint.com/)
    - Validates javascript and checks for errors.

### Compatibility

To ensure a broad range of users can successfully use the site, I tested different browsers in both desktop and mobile configuration, for appearance and responsiveness.

- **Chrome**
  - Tested Good 
- **Edge** 
  - Tested Good
- **Firefox**
  - Tested Good
- **Safari** 
  - Tested Fair
- **Opera** 
  - Tested Good

#### Bugs Fixed

I originally had each python test in the test directory of each app. It was causing Travis CI to have a Failed Build error. The tests were moved to a 
Tests directory, at the root level, to prevent this problem.



## Deployment

### Local Deployment

Before you are able to deploy and run this application locally, you must have the following installed on your system:

- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- An IDE of your choice, such as [Gitpod](https://https://www.gitpod.io/).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.

Also it would be beneficial to have free accounts set up for the following services:
- AWS S3
- Stripe
- Emailjs

Next, perform the following steps:

Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:
    - `git clone https://github.com/freddorn/coolpets.git`.
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `.env` file containing the following environmental variables:
    - ***STRIPE_PUBLISHABLE*** - Used solely to identify your account with Stripe; it isn't secret.
    - ***STRIPE_SECRET*** -  Can perform any API request to Stripe without restriction.
    - ***STRIPE_CANCEL_URL***
    - ***STRIPE_SUCCESS_URL***
    - ***SECRET_KEY*** - Standard secret key, any value.
    - ***HOSTNAME***
    - ***AWS_ACCESS_KEY_ID*** - AWS user credentials.
    - ***AWS_SECRET_ACCESS_KEY*** - AWS S3 credentials.
    - ***AWS_STORAGE_BUCKET_NAME***
    - ***DATABASE_URL*** - Remote PostgreSQL database link if using a remote database.



- Install all requirements from the requirements.txt file using this command:
    - `pip3 install -r requirements.txt`

- At the terminal prompt, type ```python3 manage.py runserver```. Django should now start running a development server from 'http://127.0.0.1:8000'. 

    Running the project for the first time will cause Django to create a SQLite3 database named ```db.sqlite3```. Type the following command into the terminal to create the database schema:
    - `python3 manage.py migrate`

    Django will then migrate the files contained in the migrations folder to create a database schema.


### Remote Deployment

To implement this project on Heroku, the following must be completed:

1. Create the **requirements.txt** file so Heroku knows what dependencies are needed, with the command `pip3 freeze > requirements.txt`
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
3. Sign up for or log into your Heroku account, create your project app, and click the **Deploy** tab. Select *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as in the local deployment above.
5. In the **Resources** tab, go to the Add-ons section and add the Heroku Postgres add-on. Choose the *Hobby* level when prompted. This will give you a remote database to use for your project. The database URI will be located in the Config Vars in the **Settings** tab.
6. The app will now be deployed and built by Heroku and will be ready to run.
7. Alter your project's ```settings.py``` file to connect to the remote database using the ```dj_database_url``` Python package.
8. Follow the steps in the Local Deployments section above to migrate your schema to the remote database.

##### back to [top](#table-of-contents)

---


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
- My three dogs Bo, Chloie and Lena, who gave me the idea for this project. 