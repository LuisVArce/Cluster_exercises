Regression_Project
Project Goals and Description:
Talk about Zillow. Our goal will be focused on the 2017 data for single household homes in three Carlifonia Counties- Orange, L.A. and Ventura. We will construct an additional new machine learning regression model to complement the current one in production with the ultimate purpose of predicting key drivers for home values for single family properties in the counties above. The approach here is adapting newer insight into keys driver features.

Initial Hypothesis/Questions
Is there a correlation between home value and:-

A home's square feet? Number of bedrooms? Number of bathrooms?

The Project Plan Structure
This projects follows Data Science Pipeline. Should you wish to recreate the project, follow the following general steps:

(1). Planning
Define goals, understand the stakeholders and or audience, brain-storm to arrive at the MVP, define end product and purpose. Finally deliver report through presentation.

(2). Acquisition
Create a connection with CodeUp Online SQL through conn.py module. Call the conn.py function with the acquire.py function. Save a cached copy of the .csv file in local machine. Import this module and other required python libraries into the main zillow_workspace.ipynb file

(3). Preparation
Create a module called prepare.py to hold all functions required to prepare the data for exploration including: - Remove duplicates, empty spaces, encode data, drop unnecessary columns and data outliers, rename columns. - Split the data into train, validate and test sets in ratios: 56% : 24% : 20% respectively.

(4). Exploration
With cleaned data prepared, ensure no data leakage and use train subset. Utilize the initial questions to guide the project explorations. Create visualizations to explain the relationships observed. Perform statistical test to infer key driveres through feature engineering. Document takeaways that guide the project to modeling.

(5). Modeling
Utilize python Sklearn libraries to create, fit and test models in the zillow workspace.ipynb file Predict the target variables Evaluate the results on the in-sample predictions Select the best model, and use on test subsets for out-of-sample observations.

(6). Delivery
A final report with summarized results is saved in the zillow_report workbook. Deliverables include a 5 minute presentation through Zoom with the audience of Zillow Data Science Team. The key drivers for home values clearly explained and best performing model presented with charts. Deployment of the entire code and workbooks in public Data Scientist GitHub Account without sensitive database access information through .gitignore.py. Create this** ReadMe.md file with all steps required to reproduce this test.

Appendix
Data Dictionary

Columns and Description

bedroom_count: The number of bedrooms
bath_count: The number of bathrooms
finished_sq_feet: Square footage of property
home_value: Property tax value dollar amount
year_built: The year a home was built
fips: a location identifier All converted to floats
To Reconstruct this Project
You'll require own env.py file to store query connection credentials(access rights to CodeUp SQL is required). Read this ReadMe.md file fully and make necessary files Set up .gitignore file and ignore env.py, *.csv files Create and Repository directory on GitHub.com Follow instructions above and run the final zillow_workspace report. Modeling Perform Linear Regression, LassoLars and Tweedie Regression (GLM). Determine best model for prediction of home value.

Key Findings
. finished_sq_feet is the key driver for home_value followed by bath_room count, and lastly bedroom_count? In varying the features, Linear progression model seem to perform better than Polynomial regression.

Future Study on Unseen Data
With more time, create new unseen features that will predict home_value Heat map shows very strong correlation between bath_room count and finished_sq_feet. How are these features affecting the home_value?
