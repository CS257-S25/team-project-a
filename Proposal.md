# Title
Analyzing Criminal Drug Abuse Treatment in Females
drug_abuse_treatment.py

# Dataset(s) summary
Our dataset provides statistics displaying the different frequencies at which
criminals of the female gender engaged in drug abuse or crime. It also asks
questions about their backgrounds.

For example, one variable asseses the rate at which subjects attended self-help
meetings over the course of 30 or 90 days prior to follow up. 

# Dataset(s) Metadata

Search terms and search tool we used to find this dataset
ICPSR: https://www.icpsr.umich.edu/web/pages/index.html 


URL -https://www.icpsr.umich.edu/web/ICPSR/studies/30842/summary 


Date Downloaded.
4/7/2025


Authorship
Carl Leukefeld, University of Kentucky. Center on Drug and Alcohol Research


Exact name of the dataset and version
Criminal Justice Drug Abuse Treatment Studies (CJ-DATS): Restructuring Risky Relationships-HIV (RRR-HIV), 2005-2008 [United States] (ICPSR 30842)
Version: V1


Geographic Coverage:
Rhode Island, Conneticut, Kentucky, Delaware


Location of dataset overview information:
https://www.icpsr.umich.edu/web/ICPSR/studies/30842/summary

Terms of Use
No restriction

Citation:
Leukefeld, Carl. Criminal Justice Drug Abuse Treatment Studies (CJ-DATS): Restructuring Risky Relationships-HIV (RRR-HIV), 2005-2008 [United States]. Inter-university Consortium for Political and Social Research [distributor], 2011-07-13. https://doi.org/10.3886/ICPSR30842.v1

# Potential User Interactions

User Story 1: A user wants to see the frequency at which subjects attended self-help meetings over the course of 30 or 90 days prior to follow up.

Acceptance Criteria:
* Expose a function or endpoint `get_meeting_counts(subject_id, days)` where `days ∈ {30, 90}`.  
* Output a table with columns:  
   - subject_id (integer)  
   - window_days (integer, either 30 or 90)  
   - meeting_count (integer ≥ 0)  
* For subject 42, if they attended 3 meetings in the 30 days prior and 7 meetings in the 90 days prior, the output would be: 
subject_id | window_days | meeting_count  
42         | 30          | 3  
42         | 90          | 7  

User Story 2: A user wants to see the frequency of a subject being arrested given a range of times committed selling drugs in the past 30 days.

Acceptance Criteria:
Able to see the relationship between a specific subject being arrested and the range of times they were commited selling drugs.
* Get a function get_arrest_vs_sales(subject_id, start_date, end_date) where end_date – start_date = 30 days.
* Output a table with columns:  
   - subject_id (integer)  
   - sales_count (integer ≥ 0)  
   - arrested (0 or 1)  
* For a subject selling 5 drugs between 2025-03-01 and 2025-03-31 and were arrested at least once, the output would be:  
subject_id | sales_count | arrested    
-----------|-------------|---------   
101        | 5           | 1  

User Story: A user wants to see if going to self help meeting increases the chance of employment.

Acceptance Criteria:
The terminal input returns a probability of a person being employed given that they went to a certain number of self help meetings. 