#!/usr/bin/env python

"""
Automatically generate redirect pages.

"""

import os
import sys
import argparse
import glob

REDIRECT_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf8">
    <meta http-equiv="refresh" content="0; url={DOMAIN}/{SLUG}">
    <link rel="canonical" href="{DOMAIN}/{SLUG}">
    <title>This page has moved</title>
</head>
<body>
    <p>This page has moved. Redirecting you to <a href="{DOMAIN}/{SLUG}">{DOMAIN}/{SLUG}</a>&hellip;</p>
</body>
</html>

"""

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "source",
        action="store",
        nargs=1,
        )
    p.add_argument(
        "dest",
        action="store",
        nargs=1,
        )
    p.add_argument(
        "domain",
        action="store",
        nargs=1,
        )
    args = p.parse_args()

    source = args.source[0].rstrip('/')
    dest = args.dest[0].rstrip('/')
    domain = args.domain[0].rstrip('/')
    if not domain.startswith('http'):
        p.error("The domain should start with https://")

    for path in glob.glob(source + '/**.html', recursive=True):
        if '.git' in path:
            continue
        file = path[len(source) + 1:]
        newpath = os.path.join(dest, file)
        os.makedirs(os.path.split(newpath)[0], exist_ok=True)
        # It must always be /, even on Windows
        redirect = '/'.join(file.split(os.path.sep))
        with open(os.path.join(newpath), 'w') as f:
            f.write(REDIRECT_TEMPLATE.format(DOMAIN=domain, SLUG=redirect))

if __name__ == '__main__':
    sys.exit(main())
