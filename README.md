[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<div id="top"></div>

<div align="center">
  <a href="https://github.com/vsuraj25">
    <img src="https://img.icons8.com/external-dreamcreateicons-flat-dreamcreateicons/64/null/external-fire-weather-dreamcreateicons-flat-dreamcreateicons.png" alt="Logo" width="80" height="80"/> 
  </a>

    
<h3 align="center">Forest Fire Prediction</h3>

 <p align="center">
    Machine Learning Project
    <br />
    <a href="https://github.com/vsuraj25"><strong>Explore my Repositories. »</strong></a>
    <br />
    <br />
    <a href="#intro">Introduction</a>
    ·
    <a href="#data"> Data Information</a>
    ·
    <a href="#contact">Contact</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## **About The Project**
* This project aims to predict forest fire using best machine learning models. Regression and Classification both streams Supervised learning is portrayed in this project. The dataset used in this project is taken from UCI Machine Learning Repository - Algerian Forest Fire Dataset. Both Single input and Bulk input prediction can be exceuted.

## **Deployed app**
[![App Screenshot](https://user-images.githubusercontent.com/55409076/205337765-74845c49-de33-4f9d-943c-c7d80c35ccf6.PNG)](https://web-production-ae1b.up.railway.app/)

[LINK TO HEROKU APP](https://web-production-ae1b.up.railway.app/)

<!-- GETTING STARTED -->
<div id="intro"></div>

## **Introduction**
*  In this project, i have worked on solving Regression and Classification both with a usecase of predicting the Forest Fire Weather index and Forest Fire possibility.The dataset used in this project is taken from UCI Machine Learning Repository - Algerian Forest Fire Dataset. MongoDB database is used to store the dataset. EDA and Model Building both could be found in the repo. Logging is maintained accordingly.
  
 
<div id="data"></div>
<!-- USAGE EXAMPLES -->

## **Dataset Information**

* Download the original dataset here : 
  [Algerian Forest Fire Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00547/Algerian_forest_fires_dataset_UPDATE.csv)

 
* The dataset includes 244 instances that regroup a data of two regions of Algeria,namely the Bejaia region located in the northeast of Algeria and the Sidi Bel-abbes region located in the northwest of Algeria.

* The period of data is from June 2012 to September 2012.

* The dataset includes 11 attribues and 1 output attribue (class)

* The 244 instances have been classified into 'fire' (138 classes) and 'not fire' (106 classes) classes.

* **Attribute Information**

1. `Date` : (DD/MM/YYYY) Day, month ('june' to 'september'), year (2012) Weather data observations
2. `Temp` : temperature noon (temperature max) in Celsius degrees: 22 to 42
3. `RH` : Relative Humidity in %: 21 to 90
4. `Ws` :Wind speed in km/h: 6 to 29
5. `Rain`: total day in mm: 0 to 16.8 FWI Components
6. `Fine`: Fuel Moisture Code (FFMC) index from the FWI system: 28.6 to 92.5
7. `Duff Moisture Code (DMC)`: index from the FWI system: 1.1 to 65.9
8. `Drought Code (DC)`: index from the FWI system: 7 to 220.4
9. `Initial Spread Index (ISI)`: index from the FWI system: 0 to 18.5
10. `Buildup Index (BUI)`: index from the FWI system: 1.1 to 68
11. `Fire Weather Index (FWI)`:  Index: 0 to 31.1
12. `Classes`: two classes, namely 'fire' and â€œnot 'not fire'

<p align="right">(<a href="#top">back to top</a>)</p> 

<!-- USAGE EXAMPLES -->
## Steps

* Installing Python, PyCharm, Monogodb, Git to Computer.
* Creating Flask app by importing `Flask` module.
* Download the source dataset from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++#).
* For Classification algorithm decided to predict the features `Classes` from the dataset which is Binary classification `(fire, not fire)`.
* For Regression Problem algorithm decided to predict the feature `FWI` (Fire weather Index) which is 90%+ correlated to Classes Feature.

### Loading CSV and Inserting to DB
* The Downloaded CSV file is loaded as pandas Dataframe using Pandas Library.
* Pandas Dataframe is converted to Dict .
* Mongodb Altas is used as DB here, with `pymongo library` mongodb is connected to python.
* Database and collections created via python and the list of dictionaries is uploaded using `collection.insert_many` method.

<p align="right">(<a href="#top">back to top</a>)</p> 

### EDA
* In this step, we will apply Exploratory Data Analysis (EDA) to extract insights from the data set to know which features have contributed more in predicting Forest fire by performing Data Analysis using Pandas and Data visualization using Matplotlib & Seaborn. 
* It is always a good practice to understand the data first and try to gather as many insights from it.

### Model Building 
* For Regression Problem algorithm decided to predict the feature `FWI` (Fire weather Index) which is 90%+ correlated to Classes Feature.
* Models used : **Linear regression, Lasso Regression, Ridge Regression, Random forest, Decision tree, K-Nearest Neighbour regressor, Support Vector Regressor.**
* For Classification algorithm decided to predict the features `Classes` from the dataset which is Binary classification `(fire, not fire)`.
* Models used : **Logistic Regression, Decision Tree, Random Forest, XGboost, K-Nearest Neighbour.**

### Model Selection
* HyperParameter Tuning Randomized Gridsearch CV is done for top 2 models for both Regression and Classification.
* For Classification `Stratified Kfold Cross-Validation metrics` is used based best Mean CV Accuracy Model is used for Model Deployment.
* For Regression `R2 score metrics` is used to select best model The R2 score is one of the performance evaluation measures for regression-based machine learning models.

### Flask
* Importing the Flask module and creating a Flask web server from the Flask module.
* Create an object **app** in flask class with `__name__` which represents current app.py file.
* Create `/` route to render default page html.
* `/predict_api` route for api testing using `Postman`
* Create a route `/predict` `/predictR` to get user input for Classification and Regression respectively. 
* Run the flask app with `app.run()` code.

### Heroku Deployment
* Create new repo in Github and push all the data using `Git`.
* Install Heroku CLI and login using `heroku login` and setup the app in Heroku Web.
* Connect with app `heroku git:remote -a appname`
* Push to Heroku using `git push heroku main`

## **Requirements**
* Python 3.7
* Numpy
* Pandas
* Flask
* Checkout requirements.txt for more information.

### **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)


### **Tools used**
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

<!-- CONTACT -->
<div id="contact"></div>

## **Contact**
[![Suraj Verma | LinkedIn](https://img.shields.io/badge/Suraj_Verma-eeeeee?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=0A66C2)][reach_linkedin]
[![Suraj Verma | G Mail](https://img.shields.io/badge/sv255255-eeeeee?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=EA4335)][reach_gmail]
[![Suraj Verma | G Mail](https://img.shields.io/badge/My_Portfolio-eeeeee?style=for-the-badge)][reach_gmail]

[reach_linkedin]: https://www.linkedin.com/in/suraj-verma-982b31157/
[reach_gmail]: mailto:sv255255@gmail.com?subject=Github


<p align="right">(<a href="#top">back to top</a>)</p>



