# mailmerge-cli

Command-line mail merge for small research offices: takes a Jinja2 template and
a CSV of recipients and produces one PDF per row.

## Install

```
pip install -r requirements.txt
python -m mailmerge --template letter.html.j2 --data recipients.csv --out out/
```

## Status

Used internally for workshop certificates and reviewer invitation letters.
