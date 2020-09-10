# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.

## ACM-Research-Coding-Challenge
I used K-means clustering - within the sum of squared to check for the optimal number of clustes. 
For more accuracy, you can go further by using Gap-stat and Silhouette and then comparing the answers gotten from the plotted graphs

References
[1] Open Data Science(2018) "Unsupervised Learning, Evaluating Clusters" les at Meduim.com
Available:https://medium.com/@ODSC/unsupervised-learning-evaluating-clusters-bd47eed175ce (Accessed: September 8, 2020).
[2] Kindson the Tech Pro(2019) "How to perform K means clustering" les at youtube.com
Available:https://www.youtube.com/watch?v=fl0PH6uQDIw&ab_channel=KindsonTheTechPro(Accessed: September 9,2020)
[3] DecisionForest(2020) "How to choose the Right Number of clusters|Elbow Method explained|kmeans clustering" les at youtube.com
Available:https://www.youtube.com/watch?v=qs8nfzUsW5U&ab_channel=DecisionForest(Accessed September 7,2020)
[4] C.N.Van,(2018) "How to Determine the Optimal Number Of Clusters for K-Means" les at Youtube.com
Available:https://www.youtube.com/watch?v=imtvI5CQLm4&ab_channel=ChucNguyenVan(Accessed September 8, 2020)

