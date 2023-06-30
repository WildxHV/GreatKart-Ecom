
# SnapStyle E-commerce Website

SnapStyle is an e-commerce website that allows users to shop for clothing and accessories online. This repository contains the source code and necessary files for the SnapStyle website.



## Demo

Go to the webpage - [Live Link](http://hvss.pythonanywhere.com/)


## Features
- User registration and authentication
- Product browsing and search 
- Product categories and filtering
- Shopping cart functionality
- Secure payment processing
- Order management
- User reviews and ratings
- User profile management
- Admin panel for managing products, categories, and orders - Responsive design for optimal viewing on different devices 


## Technologies
The SnapStyle website is built using the following technologies and frameworks:

- Django: a high-level Python web framework
- HTML, CSS, and JavaScript: for front-end development
- Bootstrap: a popular CSS framework for responsive design
- SQLite: a lightweight and easy-to-use database
- Paypal: for secure payment processing
- Python libraries and packages: Django Rest Framework, Pillow, and others


## Installation

To install and run the SnapStyle website locally, follow these steps:
 1. Clone this repository to your local machine:

```bash
  git clone https://github.com/WildxHV/SnapStyle.git
```
 2. Navigate to the project directory:
```bash
  cd SnapStyle
```      
 3. Create a virtual environment:
```bash
  python -m venv venv
```      
 4. Activate the virtual environment:
  - For Windows:
   ```bash
     venv\Scripts\activate
   ```      
  - For macOS/Linux:
   ```bash
     source venv/bin/activate
   ```      
 5. Install the required dependencies:
```bash
  pip install -r requirements.txt
```      
 6. Set up the database:
```bash
  python manage.py makemigrations
  python manage.py migrate
```      
 7. Configure the necessary environment variables:

   - Create a .env file in the project directory.

   - Add the following variables to the .env file:
```bash
  SECRET_KEY=django_app_secret_key
  DEBUG=True
  EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
  EMAIL_HOST=smtp.gmail.com
  EMAIL_PORT=587
  EMAIL_HOST_USER=your_email_id
  EMAIL_HOST_PASSWORD=your_email_host_pass
  EMAIL_USE_TLS= True
```      
 8. Run the development server:
 ```bash
  python manage.py runserver
```

 9. Open your web browser and visit http://localhost:8000 to access the SnapStyle website.
## Contributing

Contributions to the SnapStyle project are welcome! If you find any bugs, have suggestions for improvements

