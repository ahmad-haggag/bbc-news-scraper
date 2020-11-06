BBC News Scraping Application

This project provides the following features 
    1. Crawling articles on a BBC news website
    2. Extracting article relevant information  e.g (article text, author, headline, article url , summary , keywords)
    3. Storing article data in hosted Mongo database for subsequent search and retrieval.
    4. Searching capability for previous stored articles by attributes like ( keyword)
  




Project Structure

The project consists of 2 main subdirectory

    1. scraper 
    • contains scrapy project structure for scraping BBC website news 
    2. api
    • contains REST api for accessing articles stored in mongoDB
