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