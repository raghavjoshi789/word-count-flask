# word-count-flask

- ## Working
    - ### Frontend
        - It takes ***url*** of any site form input.
        - Dislaying counts of words. 
    - ### Backend
        - In backend it scrape words from url and using ***requests*** and ***BeautifulSoup*** packages.
        - Then using ***nltk-punkt*** tokenizer it tokenize the words ( converting to single words) and filter ***stop words*** ( e.g. If,then,i,me etc. ) using list of ***stop words*** from ***nltk-corpora***.
        - Then using ***collections.Counter*** it gets count of indivisual words  

- ## Its simple word count web app created by flask it is good for getting familiar with :-  
    1. Project structure 
    2. Flask app configuration
    3. Database Creation, Integration, Migration
    4. Heroku deployement

- ## Setup instructions :-
  
    1. Setup __virtual environment__ It is not necessary for app to work but __recommended__ to keep your system clean. <br>
    e.g. `python -m venv <environment directory name>` ***venv*** package is required for these to work
  
    2. Setup environment variables used by Application.
        - __APP_SETTING__ : It tells flaks app to which configuration should be applied from  _config.py_.
        - __DATABASE_URL__ : It is required for connecting to database and App will look for it in _config.py_ file.
        - __SECRET_KEY__ : we don't have use for it now but it is good practice to define it early on, It is used for signing session cookies in flask 
        - __FLASK_ENV__ : these tells flask which mode should run It should be defined early to avoid unexpected behaviour it also activate __DEBUG MODE__ in flask  <br>
      <br>
     e.g. For Windows `set <VARIABLE_NAME>=<VARIABLE_VALUE>`
      
  3. Installing requirements from _requirements.txt_. <br>
  e.g. `python -m pip install -r requirements.txt`
