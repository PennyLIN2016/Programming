# PASSED 35.23%

delete  t1 from Person t1 inner join Person t2 where t1.Id > t2.Id and t1.Email = t2.Email;
select * from Person;

