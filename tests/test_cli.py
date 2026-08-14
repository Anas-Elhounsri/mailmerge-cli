from mailmerge.cli import render_rows


def test_render(tmp_path):
    tpl = tmp_path / "t.j2"
    tpl.write_text("Hello {{ name }}")
    data = tmp_path / "d.csv"
    data.write_text("name\nAda\n")
    rows = list(render_rows(tpl, data))
    assert rows[0][1] == "Hello Ada"
