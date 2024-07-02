create or replace table github_demo.github_schema.example_table_downstream
as (

select example_column from github_demo.github_schema.example_table

union all

select 2 as example_column

);