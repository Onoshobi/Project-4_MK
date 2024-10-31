# Project_4_Group_5

![image](https://github.com/user-attachments/assets/89e01c71-358e-4214-be72-02ad85cd6564)


# Project proposal

The gym chain One Fitness is in the process of developing a customer interaction strategy driven by analytical data. One of the most significant challenges that gyms and similar services encounter is customer churn. But how can you determine if a customer has disengaged? You can calculate churn by tracking those who cancel their accounts or fail to renew their memberships. However, sometimes it’s not immediately clear that a client has left; they may quietly withdraw their engagement.

Churn indicators can differ across industries. For example, if a customer rarely makes a purchase from an online store but does so consistently, they cannot be considered lost. Conversely, if a user has not accessed a platform that offers daily updates for two weeks, that’s a cause for concern; they may have lost interest and moved on.

For a gym, it is reasonable to conclude that a customer has left if they haven’t visited in a month. While it’s possible they are on vacation and will return, this is not the usual scenario. Typically, if a customer joins, attends a few times, and then disappears, they are unlikely to return.

To combat churn, Model Fitness has digitized several customer profiles. Your task is to analyze this data and develop a customer retention strategy.

You should:
 - Learn to predict the probability of churn (for the upcoming month) for each customer
 - Draw up typical user portraits: select the most outstanding groups and describe their main features
 - Analyze the factors that impact churn most
 - Draw basic conclusions and develop recommendations on how to improve customer service:
   
      - Identify target groups
   
      - Suggest measures to cut churn
   
      - Describe any other patterns you see with respect to interaction with customers

# **Info / Credits:**

**Team**
 - [Evgeniia Kozodeeva](https://github.com/EvgeniiaKei)
 - [Hung Lim(Hansen)](https://github.com/HansLimq)
 - [Mark Krishna](
 - [Han Wang]()
 - [Jiahuib Du(Mary)]( https://github.com/JiahuiDu1015/Project_4_Group_5)



# Data

   https://www.kaggle.com/datasets/ellanihill/model-fitness-customer-churn

# Navigation
gym_churning_colab - jupyter notebook file, created in Google Colab, that contains the queries.

**Tools**

- Jupyter Notebook
- Python Pandas
- Python Matplotlib

# Environment for Google Colab
 - The model utilises data retrieved from Spark
check SPARK_VERSION (spark_version = 'spark-3.5.3')
 - Install needed packages pip install
       - python
       - scikit-learn
       - pandas
       - numpy
       - sklearn
       - flask
       - hvplot
       - dask[dataframe]
       - lazypredict
# Machine Learning Models   

**Model 1: LazyPredict**

strong predictive capability across multiple classifiers, particularly favoring the XGBClassifier for its overall performance. 
However, the final choice of the model should also consider the specific needs of the application, such as speed and interpretability.

![image](https://github.com/user-attachments/assets/e7aef466-916e-42e5-852c-aa83deddc8f3)



**Model 2: AdaBoostClassifier**
Model Strengths: With high precision and recall, AdaBoost classifier is effective at identifying customers likely to churn and is also reliable in minimizing misclassification of loyal customers.
Areas for Improvement: False negatives (missed churners) indicate the model may overlook some customers who are at risk of leaving. Consider additional techniques like hyperparameter tuning, ensemble methods with different configurations, or gathering more features if reducing false negatives is a priority.

![image](https://github.com/user-attachments/assets/f33b2bcf-6294-41c2-8fe2-a60f92df6605)

**Logistic regression**
This section demonstrates setting up a logistic regression model for a binary classification problem and using stratified data splitting to handle class imbalance. Stratification helps maintain the original class proportions in both training and test sets, ensuring the model is trained and tested fairly across the classes.

We compare our result with Random Forest

![image](https://github.com/user-attachments/assets/42cf9bd3-839d-48d4-a71d-0ed8cdbc404e)


**Model 3: Random Forest Classifier (optimal)**

High precision roc_au 97.4%. we want to find out the feature importance (features of why people stay), better than ada because Ada is only good if the relatonship between the churn and feature is straighforward but RF can handle more complex relatonships because we are dealing with human behaviours which is complex

<img width="307" alt="image" src="https://github.com/user-attachments/assets/d62c51a0-6755-459a-8a5c-ca89872a2a23">



# Clustering - unsupervised learning 

As we can see from the dendrogram, the system allows us to divide clients into 3 clusters. The result shows in the next slide the churn rate for each of the four identified customer clusters. The churn_rate column shows the proportion of customers in each cluster who churned.  Cluster 2 has the highest churn rate at 64%,  Clusters 1 and 3 have significantly lower churn rates at 13%. Cluster 0 has the lowest churn rate. This information can be used to identify which clusters are at higher risk of churning and may require additional attention and retention strategies.
Here are the general characteristics of customers who are more likely to churn: most of them have a lifetime below three months, visit less than twice a week, get lower promo_friends, the average additional extra charge below 125 USD, and they still have remaining contract period for about four months.
Overall, the user clustering model provides a valuable tool for the gym to better understand and serve its customers. It can help to improve retention rates, increase revenue, and build a stronger brand reputation.

![image](https://github.com/user-attachments/assets/0fb0f3ab-4114-4125-897c-7fc9aaf72925) / ![image](https://github.com/user-attachments/assets/b3a2bd84-63a6-49ff-99f7-1c0f26408a24)


# Testing Model - Random Forest

**Front-End**
 - Flask Web Application
 - HTML
 - Javascript
 - CSS

![image](https://github.com/user-attachments/assets/91494d3c-da48-4b09-81ca-cf0f2e350c6a)


# Group Presentation

[Presentation]([Slides group 5 .pptx](https://github.com/JiahuiDu1015/Project_4_Group_5/blob/main/Slides%20group%205%20.pptx))

# Conclusion

In our analysis of client attendance at the gym, we aimed to identify key factors contributing to client churn and develop an effective predictive model. After evaluating various modeling approaches, we concluded that the Random Forest model provided the best results for predicting churn.

The Random Forest algorithm excels in handling the complex interactions and nonlinear relationships often present in client behavior data. By leveraging multiple decision trees, this model effectively reduces overfitting and enhances the accuracy of predictions. Our analysis revealed significant predictors of churn, such as attendance frequency, membership duration, and engagement with gym services.

Implementing this model allows us to proactively identify at-risk clients and tailor retention strategies accordingly. By focusing on the specific needs and behaviors of these clients, we can improve customer satisfaction, enhance loyalty, and ultimately reduce churn rates.

Moving forward, we recommend continuous monitoring and refining of the model to adapt to changing client dynamics and incorporate additional data sources as they become available. Overall, the insights gained from this project not only highlight the effectiveness of the Random Forest model but also provide a solid foundation for data-driven decision-making in our client retention strategies.

# Recommendations


•   In future we will use CRM System to create more features so we can predict our model better  and analyze comprehensive data on client interactions, preferences, and feedback. This system can help create additional features that provide deeper insights into factors influencing churn. Key data points to consider include communication history, client satisfaction scores, and service usage patterns.

•   Maintain discussions with membership team on what the key features are for members to churn.   

•   Staff Training: Provide training for staff on the importance of data-driven decisions and how to interpret model outputs. Educating the team on churn predictors will empower them to implement proactive engagement strategies.
