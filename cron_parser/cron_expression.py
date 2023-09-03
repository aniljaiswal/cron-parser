from cron_parser.constants import FIELD_NAMES
from cron_parser.cron_field import CronField


class CronExpression:
    def __init__(self, expression: str):
        self.expression = expression
        self.fields = []
        self.command = None

    def parse(self):
        # Divide on space with 5 splits since there will
        # always be 6 parts to the supplied expression
        field_strings = self.expression.split(' ', 5)

        self.command = field_strings[-1]
        for i, field_str in enumerate(field_strings[:-1]):
            field_name = FIELD_NAMES[i]
            cron_field = CronField(field_str, field_name)
            cron_field.parse()
            self.fields.append(cron_field)
        return self

    def format_as_table(self):
        table = []
        for field in self.fields:
            table.append(f"{field.field_name:<14}{' '.join(map(str, field.values))}")

        # Append the command at last
        table.append(f"{'command':<14}{self.command}")

        return "\n".join(table)
