import sys
import json
from typing import Dict, List

class ReportView():

    def __init__(self):
        self.values: Dict = None
        self.tests: Dict = None

    def read_json_files(self, filepath_to_values: str, filepath_to_tests: str) -> None:
        with open(filepath_to_values) as file:
            json_file = json.load(file)
            result_values = json_file['values']

        self.values = {result['id']:result['value'] for result in result_values}

        with open(filepath_to_tests) as file:
            json_file = json.load(file)
            self.tests = json_file['tests']

    def merge_values_to_tests(self) -> None:
        item_stack = [*self.tests]
        while item_stack:
            item = item_stack.pop()

            if item['id'] in self.values:
                item['value'] = self.values[item['id']]

            if 'values' in item:
                item_stack += item['values']

    def write_report_as_json(self, filepath_to_report) -> None:
        with open(filepath_to_report, 'w') as file:
            json.dump({'tests':self.tests}, file, indent=4)

if __name__ == '__main__':
    report = ReportView()
    report.read_json_files(*sys.argv[1:3])
    report.merge_values_to_tests()
    report.write_report_as_json(sys.argv[3])