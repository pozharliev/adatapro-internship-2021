<p align = "center">
  
<img src="https://i.imgur.com/fKw1JHJ.png">
  
 </p>
<h1 align="center">Team Red</h1>

<p align = "center">
   <img src = "https://img.shields.io/github/languages/count/ABPozharliev19/adatapro-internship-2021?style=for-the-badge">
   <img src = "https://img.shields.io/github/contributors/ABPozharliev19/adatapro-internship-2021?style=for-the-badge">
   <img src = "https://img.shields.io/github/repo-size/ABPozharliev19/adatapro-internship-2021?style=for-the-badge">
   <img src = "https://img.shields.io/github/last-commit/ABPozharliev19/adatapro-internship-2021?style=for-the-badge">
   <img src = "https://img.shields.io/github/languages/top/ABPozharliev19/adatapro-internship-2021?style=for-the-badge">
 </p>
  
<hr>
<br>
    <p align="center"><strong><big>Site, which shows information about the current scraping status.</big></strong></p>
<br>
<hr>

<h1>💻 About  </h1>
<p align="center"> <strong>Our project consists of a site that aims to help its users by providing them with up-to-date information on the availability of the PlayStation 5. The information is retrieved automatically through crawling. Once a day, registered users are sent an email with information about an available PS5, and users can set up the system to receive information only from the places they are interested in.</strong></p>
<hr>

<h1>🎥 Interface</h1>

<img src = "interface.gif">

<h1><a href = "#">Our Documentation</h1>
  
<h1>⌨️ How it works</h1>
  
<p>Our work can be split into 4 different parts</p>
  
<ol>
  
<li>The Site (Our Front-end)</li>
<ul>
  <li>Home - gives basic information about the site.</li>
  <li>Information - gives more information about the site and how to use the functions of the site.</li>
  <li>Registration and login - to create an account and log in.</li>
  <li>Account - to control user settings and functions. </li>
</ul>
  
<li>The Django Application (Our Back-end)</li>
  
<ul>
<li>Our Back-end is entirely written on <img src="https://emoji.gg/assets/emoji/py.png" width="18px" height="18px" alt="py">  Django. </li>
<li>It is centered around views, which are in different 📁 folders.</li>
<li>It can be started by the 📁 <code> manage.py</code> script. </li>
<li> You can find in the in 📁 API/ folder. </li>
<li>It is hosted on <code> localhost</code> on port 8000, although you can change it.</li>
</ul>
  
<li>📊 The Database </li>
<ul>
  
<li>We are using <img src="https://i.imgur.com/o8ZCuYn.png" width="16px" height="16px" alt="mariadb"> MariaDB because of its worldwide popularity and its simplicity.</li>
<li>We have a few of tables, but the main ones are the <strong>auth_user</strong>, <strong>accountview_profilepreferences</strong> and <strong> historyview_historyscraping</strong>. </li>
  
<ul>
    <li> The <strong>auth_user</strong> stores all ®️ registered accounts.</li>
    <li> The <strong>accountview_profilepreferences</strong> stores all the profile preferences related to which sites you want to see. </li>
    <li> The <strong>historyview_historyscraping</strong> stores all the information from the scrapers.</li>
</ul>
  
<li>All of the tables are generated from <img src="https://emoji.gg/assets/emoji/py.png" width="18px" height="18px" alt="py"> Django models. </li>
</ul>
  
<li>The Scraper</li>
</ol>
<h1>⛏️ Installation</h1>
<h2>Step 1: Clone the repository</h2>
<code>
git clone https://github.com/ABPozharliev19/adatapro-internship-2021.git
</code>
<br>
<code>
cd adatapro-internship-2021/
</code>
<h2>Step 2: Install dependencies </h2>
<h3>You can do this by either using pipenv:</h3>
<code>
pip3 install pipenv # Install pipenv with pip
</code>
<br>
<code>
pipenv shell # Activate the environment 
</code>
<br>
<code>
pipenv install # Install all dependencies in the Pipfile.lock file
</code>
<h3>Or by using pip:</h3>
<code>
pip3 install -r requirements.txt # Install all dependencies in the requirements.txt file
</code>
<h2>Step 3: Rename env.example to .env</h2>
<h2>Step 4: Change the information in the .env file</h2>
<code>
SECRET_KEY = 'Your django secret key'
</code>
<br>
<code>
DB_NAME = 'Your database name'
</code>
<br>
<code>
DB_USER = 'Your database user'
</code>
<br>
<code>
DB_PASSWORD = 'Your database password'
</code>
<br>
<code>
DB_HOST = 'Your host'
</code>
<br>
<code>
DB_PORT = 3306 # The port you want to use
</code>
<br>
<code>
EMAIL_HOST_USER = 'Your email username' # Should be gmail
</code>
<br>
<code>
EMAIL_HOST_PASSWORD = 'Your email password'
</code>

<h2>Step 5: Make the migrations and migrate the models</h2>
<code>
python manage.py makemigrations
</code>
<br>
<code>
python manage.py migrate
</code>
<h2>Step 6: Run the server</h2>
<code>
python manage.py runserver
</code>
<h3>Or specify the port for the server</h3>
<code>
python manage.py runserver PORT
</code>
<h2>Step 7: Go to localhost and use the site!</h2>
