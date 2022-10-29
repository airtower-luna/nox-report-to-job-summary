#!/usr/bin/python3
import json


def parse_report(report_file, title):
    with open(report_file, 'r') as fh:
        report = json.load(fh)

    print(f'## {title}\n')
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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--report', required=True,
                        help='the Nox JSON report to parse')
    parser.add_argument('-t', '--title', default='Nox',
                        help='title for the generated summary section')
    args = parser.parse_args()
    parse_report(args.report, args.title)
