#!/usr/bin/python3
import json
import sys


def parse_report(report_file):
    with open(report_file, 'r') as fh:
        report = json.load(fh)

    print('## Nox\n')
    for session in report['sessions']:
        # looks weird, but is literally how Nox creates a "friendly name"
        # for a session
        name = session['signatures'][0] \
            if session['signatures'] else session['name']

        result = session['result']
        if result == 'success':
            mark = 'heavy_check_mark'
        elif result == 'skipped':
            mark = 'large_blue_circle'
        else:
            mark = 'heavy_multiplication_x'

        print(f'* {name}: {result} :{mark}:')


if __name__ == '__main__':
    parse_report(sys.argv[1])
