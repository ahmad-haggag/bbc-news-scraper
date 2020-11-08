# BBC News Scraping Application
Collect and store BBC News Website article

# Description
    1. Crawl articles on a BBC news website
    2. Cleanse the articles to obtain only relevant information to the news story e.g (article text, author, headline, article url , summary , keywords)
    3. Store the data in a hosted Mongo database (MongoDB Atlas)) for subsequent search and retrieval.
    4. Provide the following search API to the content in the mongo database
        * retrieve all BBC news articles in the database
        * search the article by headline keyword (case insensitive)
        * search the articles' text by keyword (full text search)
        
# Project Structure
    1. scraper :  scrapy project structure for scraping BBC website news
    2. api : contains REST api for accessing articles stored in mongoDB
    
    
    
# Usage
   * Set DEPTH_LIMIT in scraper `settings.py` file  (for testing purpose I have set it = 2)
   
   * Run BBC News Scraper via the following command 
   ```
         scrapy crawl bbc  
   ```

   * Run BBC New Search API via the following command from `api` directory
   ```
        python search.py
   ```

   * Retrieve all BBC news articles in the database use `<ROOT URL>/bbc-news/api/_all` for example `http://127.0.0.1:5000/bbc-news/api/_all`
   
   
   * Search the article by headline keyword use `<ROOT URL>/bbc-news/api/headline/{keyword}` for example `http://127.0.0.1:5000/bbc-news/api/headline/election`
     
     
   * Search the articles' text by keyword use `<ROOT URL>/bbc-news/api/text?q={keyword}` for example `http://127.0.0.1:5000/bbc-news/api/text?q=covid`
  


    
      

