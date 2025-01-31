# Technical Assessment - Solution Document
### Nuno Pedrosa
 
This document presents an overview and the final conclusions of the work.
The study focused on analyzing churn prediction in an internet shipment reselling company. In this context, churn refers to customers who cease doing business with the company.

The process began with data preprocessing, following these steps: Replacing NaN values with 0, encoding categorical variables, splitting the data into training and testing sets, standardizing the data, performing feature selection (through direct analysis and feature correlation). The initial dataset consisted of 1000 rows and 51 columns. After preprocessing, the number of features/columns was reduced to 22.

Next, a more focused Exploratory Data Analysis (EDA) was conducted, although this topic was also addressed in other sections throughout the work.

We then moved on to building predictive models. The first approach was to determine which of the following models performed best in a superficial analysis: Neural Networks, XGBoost, Random Forest, Logistic Regression, Gaussian Naive Bayes, K-Nearest Neighbors, and Support Vector Machine. The best-performing model was XGBoost. Next, a grid search was performed with XGBoost to find the best hyperparameters for our model, yielding the following results during training:
- Accuracy: 0.89 (std 0.02)
- Precision: 0.91 (std 0.02)
- Recall: 0.86 (std 0.04)
- F1-score: 0.88 (std 0.02)

Next, the performance on the test set was evaluated. It was possible to obtain an ROC curve with an area of 0.98, a false positive rate of 0.08, and a true positive rate of 0.93. The model achieved an accuracy of 0.93, with both precision and recall around 0.93 for both classes (0 and 1). These results are quite good. We were able to achieve a very strong prediction with these test data, and I hope these results will hold when the model is applied in real-world scenarios.

Next, we moved on to explaining the behavior of the model's features. The gain represents the average gain across all splits where the feature is used. The most important features in terms of gain were:
- year_plat_cntry_aov: 3.62
- max_days_btwn_sales: 3.28
- avg_sales_per_day: 3.10
- avg_days_btwn_sales: 3.03
These features were the most influential in the model's performance.

Upon analyzing the SHAP plot, we observed that the features most influencing the results are, in order: year_plat_cntry_aov, max_days_btwn_sales, avg_sales_per_day, avg_days_btwn_sales and longevity.
Among these, higher values for year_plat_cntry_aov, max_days_btwn_sales, avg_sales_per_day, and avg_days_btwn_sales are associated with a higher likelihood of churn. This makes sense, as consumers who take longer to make subsequent purchases are likely to show less interest in the company. Conversely, when these values are lower, the probability of churn decreases. The longevity variable behaves oppositely, indicating that the longer a customer has been engaged with the company's products, the less likely they are to churn.

Finally, I saved the model as a package.

Here’s the breakdown of the time spent on each section: First, selecting the dataset took a bit of time. I wanted a churn dataset, but it also had to meet the given constraints, so it took some time to find the right one. For Task 1 and Task 2, the process was relatively quick. Task 1 took about 1 hour, and Task 2 took around 2 hours, considering the time spent on decisions regarding how to proceed. For Task 3, Part 1, it took less than 1 hour. Task 3, Part 2 was the most time-consuming section, taking an entire afternoon and a bit more, over 4 hours. Finally, Task 4 took about 1 hour and 30 minutes, including time spent on research.

We will now move on to the design considerations:

One of the first decisions was that, in the orginal dataset, the status column is directly calculated by the churn_factor column (where a factor greater than 4 is considered churn). The churn factor is calculated by dividing the recency by the frequency columns. Our goal was to predict future churn status without considering the last item bought. Because we wanted to predict churn based on relative customer habits, rather than relying on a predetermined approach where metrics are calculated based on the last item purchased. As a result, some columns related to the last item bought were eliminated. Using data from the last item bought could be interesting in a later approach.

Another thing to consider in the future could be to eliminate individuals who already have a very high churn factor and consider only those with a lower churn factor. However, it's important to note that doing this would result in a imbalanced dataset, and we would need to take the necessary precautions to address this issue.

Another thing is that this data is very interesting for a deeper data exploration, which would be future work.

Lastly, this model includes information about countries and platforms. In the case of company expansion, these features would need to be reconsidered. However, based on our studies, they do not seem to be highly influential in the predictions. In that case, they could probably be eliminated without much loss of predictive power, at least in the current countries and markets.

Thank you for the time spent reviewing my work!


