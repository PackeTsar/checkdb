import os
import re
from datetime import datetime
from zoneinfo import ZoneInfo
from home.models import Record


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def create_record(time, ip, port, protocol):
    timestamp = datetime.strptime(time, DATETIME_FORMAT).replace(
        tzinfo=ZoneInfo('America/Los_Angeles'))
    if ':' in ip:
        address_family = 'ipv6'
    else:
        address_family = 'ipv4'
    return Record.objects.create(
        timestamp=timestamp,
        ip=ip,
        port=int(port),
        protocol=protocol,
        address_family=address_family,
    )


def process_line(line):
    try:
        split = line.split(': ')
        timestamp = split[0]
        match = re.search(r'(\S+) \((\d+)\) \((\S+)\)', split[2])
        ip = match[1]
        port = match[2]
        protocol = match[3]
        record = create_record(timestamp, ip, port, protocol)
        print(record)
    except Exception as e:
        print(f'ERROR IN WITH LINE: {line}')
        print(e)


def process_file(filepath):
    print(f'Processing File {filepath}')
    f = open(filepath)
    lines = f.readlines()
    f.close()
    for line in lines:
        process_line(line)


def list_files(dir):
    return os.listdir(dir)
