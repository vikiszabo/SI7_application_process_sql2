




'''Requirements
Root root [/]:

It shows a list of links which are pointing to specific roots. See the roots below. 

    Mentors and schools page [/mentors]
    On this page you should show the result of a query that returns the name of the mentors plus the name and country of the school (joining with the schools table) ordered by the mentors id column (columns: mentors.first_name, mentors.last_name, schools.name, schools.country). 

    All school page [/all-school]
    On this page you should show the result of a query that returns the name of the mentors plus the name and country of the school (joining with the schools table) ordered by the mentors id column.
    BUT include all the schools, even if there's no mentor yet (in that cell, "No data" should be displayed)!
    columns: mentors.first_name, mentors.last_name, schools.name, schools.country

    Mentors by country page [/mentors-by-country]
    On this page you should show the result of a query that returns the number of the mentors per country ordered by the name of the countries
    columns: country, count

    Contacts page [/contacts]
    On this page you should show the result of a query that returns the name of the school plus the name of contact person at the school (from the mentors table) ordered by the name of the school
    columns: schools.name, mentors.first_name, mentors.last_name

    Applicants page [/applicants]
    On this page you should show the result of a query that returns the first name and the code of the applicants plus the creation_date of the application (joining with the applicants_mentors table) ordered by the creation_date in descending order
    BUT only for applications later than 2016-01-01
    columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date

    Applicants and mentors page [/applicants-and-mentors]
    On this page you should show the result of a query that returns the first name and the code of the applicants plus the name of the assigned mentor (joining through the applicants_mentors table) ordered by the applicants id column
    Show all the applicants, even if they have no assigned mentor in the database!
    In this case use the string "No data" instead of the mentor name.
    columns: applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name

Use proper HTML elements to represent the data on the query related pages.

Do not forget to commit frequently after you finish a certain feature e.g.: a whole page.'''