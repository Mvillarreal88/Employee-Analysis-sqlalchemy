# sqlalchemy-challenge

### Precipitation Analysis:

![Screenshot 2021-12-15 185042](https://user-images.githubusercontent.com/81705144/146287837-37ec69a7-a35a-40a4-b969-28d6b00521e5.png)

• We start by finding the most recent date in the data set.

• Using this date, we retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 

• We selected only the date and prcp values.

• Then load the query results into a Pandas DataFrame and set the index to the date column.

• Sort the DataFrame values by date.

• Plot the results using the DataFrame plot method.

• Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis


• Design a query to calculate the total number of stations in the dataset.

• Design a query to find the most active stations (i.e. which stations have the most rows?).

• Design a query to retrieve the last 12 months of temperature observation data (TOBS).


### Climate App

We then design a Flask API based on the data and queries that were ran in the Analysis. This will allow the user to acquire the below information:

• The Home page that will list the available routes

• Precipitation data by stations

• Input dates to get precipitation information. 

![Screenshot 2021-12-15 185056](https://user-images.githubusercontent.com/81705144/146287850-48af80df-49e6-489e-8b46-9927f6130487.png)

>- Matthew Villarreal
