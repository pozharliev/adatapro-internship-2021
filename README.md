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
<p><strong> Introducing our solution - a scraper with a site to display its results.</strong></p>
<hr>
<h1>🎥 Interface</h1>
<img src = "interface.gif">
<h1><a href = "#">Our Documentation</h1>
<h1>⌨️ How it works</h1>
<p>Our work can be split into 4 different parts</p>
<ol>
<li>The Site (Our Front-end)</li>
<ul>
<li></li>
</ul>
<li>The Django Application (Our Back-end)</li>
<ul>
<li>Our Back-end is entirely written on <img src="https://emoji.gg/assets/emoji/py.png" width="18px" height="18px" alt="py">  Django. </li>
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
