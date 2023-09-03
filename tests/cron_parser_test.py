import pytest
from cron_parser.cron_expression import CronExpression
from cron_parser.cron_field import CronField

@pytest.fixture
def valid_cron_expression():
    return "*/15 0 1,15 * 1-5 /usr/bin/find"

@pytest.fixture
def invalid_cron_expression():
    return "*-/15 0 1,15 * 1-5 /usr/bin/find extra_field"

def test_cron_field_parse_valid():
    field = CronField("*/15", "minute")
    field.parse()
    assert field.values == [0, 15, 30, 45]

def test_cron_field_parse_range():
    field = CronField("1-5", "hour")
    field.parse()
    assert field.values == [1, 2, 3, 4, 5]

def test_cron_field_parse_list():
    field = CronField("1,2,3", "day of month")
    field.parse()
    assert field.values == [1, 2, 3]

def test_cron_field_parse_step():
    field = CronField("*/2", "month")
    field.parse()
    assert field.values == [1, 3, 5, 7, 9, 11]

def test_cron_field_parse_invalid():
    field = CronField("*/15,1-8", "day of week")
    with pytest.raises(ValueError):
        field.parse()

def test_cron_expression_parse_valid(valid_cron_expression):
    expression = CronExpression(valid_cron_expression)
    expression.parse()
    assert len(expression.fields) == 5

def test_cron_expression_parse_invalid(invalid_cron_expression):
    expression = CronExpression(invalid_cron_expression)
    with pytest.raises(ValueError):
        expression.parse()

def test_cron_expression_format_table(valid_cron_expression):
    expression = CronExpression(valid_cron_expression)
    expression.parse()
    table = expression.format_as_table()
    expected_table = """minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find"""
    print(table)
    print(expected_table)
    assert table == expected_table
