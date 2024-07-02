create or replace table github_demo.github_schema.example_table_third
as (

select example_column from github_demo.github_schema.example_table_downstream

union all

select 3 as example_column;

);