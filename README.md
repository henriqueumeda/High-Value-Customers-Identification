# Insiders - All In One Place

This is the repo of the Insiders project from the All In One Place company.
 
# Project
- In this project, I defined the best customers, from the All In One Place company, eligible to be part of a loyalty program, called Insiders.
- From the database of the company, I structured, cleaned and analysed the datasets using pandas and numpy, created charts that generated insights with matplotlib and seaborn, clustered the customers with K-Means algorithm into 3 groups:
   - Normal Customers (red)
   - High Value Customers (yellow - included in Insiders)
   - Highest Value Customers (orange - included in Insiders)

<p align="center">
  <img  src="images/kmeans.png">
</p>

- An API was created using Flask and Heroku. The following url can be accessed in order to use the API: https://insiders.herokuapp.com/predict

# Repository
- csv - The folder with all csv files used
- images - The folder with all images files used in this repo
- model - The folder with all models used to build the API


# Stack 
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-Learn
- Flask
- Heroku
