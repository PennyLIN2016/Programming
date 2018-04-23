select a.Name as Employee From Employee a, Employee b
where a.Salary > b.Salary and a.Managerid = b.id