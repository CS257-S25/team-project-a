User Story 1: A user wants to see the frequency at which subjects attended self-help meetings over the course of 30 or 90 days prior to follow up.

Acceptance Criteria:
* Expose a function or endpoint `get_meeting_counts(subject_id, days)` where `days ∈ {30, 90}`.  
* Output a table with columns:  
   - subject_id (integer)  
   - window_days (integer, either 30 or 90)  
   - meeting_count (integer ≥ 0)  
* For subject 42, if they attended 3 meetings in the 30 days prior and 7 meetings in the 90 days prior, the output would be:  
|  -----------|------------|---------  |  
| subject_id | window_days | meeting_count  |  
|    42      |     30      |       3        |  
|    42      |     90      |       7        |  

User Story 2: A user wants to see the frequency of a subject being arrested given a range of times committed selling drugs in the past 30 days.

Acceptance Criteria:
Able to see the relationship between a specific subject being arrested and the range of times they were commited selling drugs.
* Get a function get_arrest_vs_sales(subject_id, start_date, end_date) where end_date – start_date = 30 days.
* Output a table with columns:  
   - subject_id (integer)  
   - sales_count (integer ≥ 0)  
   - arrested (0 or 1)  
* For a subject selling 5 drugs between 2025-03-01 and 2025-03-31 and were arrested at least once, the output would be:  
|  subject_id | sales_count | arrested  |  
|-------------|-------------|-----------|  
|  101        | 5           | 1         |  

## User Story 1: Meeting Info Page
### Story
As a public health researcher, our user wants to see the average number of self-help meetings attended and the attendance frequency so that I can quickly gauge overall participant engagement without manually calculating these data.

### Acceptance Criteria
The tab about self-help meeting will have a pre-calculated statistics for average meeting counts and average meeting attended in percentage. User should be able to navigate to the page by reading user guide.

## User Story 2: Arrests Page
### Story
As a criminology researcher, our user wants to be able to enter lower and upper bounds for drug sell arrest counts so that I can filter and visualize only the cases that fall within my specified range. Our users will get a clear idea of frequency of people involved in specific number of drug sales out of 500 sample.

### Acceptance Criteria
After following the user guide to reach this page, visitors can:
- Enter a minimum and maximum number of drug sales.
- Click Submit.
- See how many of the 500 survey participants reported making a number of drug sales within that range.

## User Story 3: Data Overview Graph
### Story
As a behavioral scientist, our user wants to view a graph correlating self-help meeting attendance with drug use’s effect on mental health so that she can assess whether increased meeting attendance is associated with improved mental health outcomes.

### Acceptance Criteria
After following the user guide to reach this page, visitors can:
View and understand a graph showing the correlation between mental health caused by drug intake and the number of self-help meeting attended.


## User Story 4: Drug Info Page
### Story
As a clinical researcher, our user wants to see the average response for drugs’ physical health impact and emotional health impact so that she can quickly compare drug effects on different health dimensions.

### Acceptance Criteria
The user should navigate to the page for drug intake feedback by reading the user guide. The user should see a pre-calculated average on people's physical and mental status affected by drugs

## User Story 5: Alcohol Info Page
### Story
As a public health administrator, our user wants to see the average response for alcohol's physical help impact and emotional health impact so that she can contrast these numbers directly against drug impact data.

### Acceptance Criteria
The user should navigate to the page for alcohol intake feedback by reading the user guide. The user should see a pre-calculated average on people's physical and mental status affected by alcohol.