select DISTINCT a.Email from Person a, Person b
where a.id != b.id and a.Email = b.Email