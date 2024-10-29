-- Joining the table using (id) and find the count of the datas from the query output

SELECT COUNT(*)
FROM districts
FULL JOIN expenditures ON districts.id = expenditures.id
FULL JOIN graduation_rates ON districts.id = graduation_rates.id
FULL JOIN schools ON districts.id = schools.id
FULL JOIN staff_evaluations ON districts.id = staff_evaluations.id;
