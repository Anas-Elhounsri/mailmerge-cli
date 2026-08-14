import argparse
import csv
import pathlib

from jinja2 import Template


def render_rows(template_path, csv_path):
    template = Template(pathlib.Path(template_path).read_text())
    with open(csv_path, newline="") as fh:
        for row in csv.DictReader(fh):
            yield row, template.render(**row)


def main():
    parser = argparse.ArgumentParser(prog="mailmerge")
    parser.add_argument("--template", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--out", default="out")
    args = parser.parse_args()

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for i, (row, html) in enumerate(render_rows(args.template, args.data), start=1):
        (out / f"letter-{i:03d}.html").write_text(html)
    print(f"wrote {i} letters to {out}")


if __name__ == "__main__":
    main()
