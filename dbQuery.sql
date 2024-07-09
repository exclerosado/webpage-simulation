SELECT 
    'landing_page' AS column_name, SUM(landing_page) AS total
FROM 
    web_page_logs
UNION
SELECT 
    'personal_data' AS column_name, SUM(personal_data) AS total
FROM 
    web_page_logs
UNION
SELECT 
    'address_data' AS column_name, SUM(address_data) AS total
FROM 
    web_page_logs
UNION
SELECT 
    'payment_data' AS column_name, SUM(payment_data) AS total
FROM 
    web_page_logs
UNION
SELECT 
    'confirmation' AS column_name, SUM(confirmation) AS total
FROM 
    web_page_logs;