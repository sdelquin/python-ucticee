import re
from pathlib import Path

import settings
import yaml


def read_testbench(filepath: str = settings.TESTBENCH):
    return yaml.load(Path(filepath).read_text(), Loader=yaml.FullLoader)


def parse_exception(exception_message):
    if m := re.search(r'\w+Error:.*', exception_message):
        exception_type = m.group()
        if m := re.search(r'line \d+', exception_message):
            exception_at = m.group()
            exception_summary = f'{exception_type} ({exception_at})'
        else:
            exception_summary = exception_type
    else:
        exception_summary = 'Exception'
    return exception_summary
