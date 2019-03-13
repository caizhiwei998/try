1.
SELECT
year_and_moth,
count_per_month,
(
SELECT
SUM(count_per_month)
FROM
test_table AS test_table_1
WHERE
test_table_1.year_and_moth <= test_table_2.year_and_moth
) AS total_by_month
FROM
test_table AS test_table_2


2.
SET @csum := 0;
SELECT 日期, 净利润, (@csum := @csum + 净利润) AS 累计利润
FROM daily_pnl_view;
