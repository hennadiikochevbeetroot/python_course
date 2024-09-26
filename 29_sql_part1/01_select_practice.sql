-- comment
-- comment 2
-- DQL - Data Query Language - SELECT == select
-- python - imperative language - how do we want
-- sql - declarative language - what do we want
-- varchar - character varying
-- select description from categories where category_name = 'Seafood';
-- int, smallint, bigint, boolean (true, false), varchar(3), text, date, timestamp
-- python None == sql NULL null
-- AND, OR, NOT
select * from customers where contact_title <> 'Owner' and country = 'Mexico' limit 500;

-- select column_name1, column_name2
-- from table_name
-- where column3 > 5
-- order by column4
-- limit 1