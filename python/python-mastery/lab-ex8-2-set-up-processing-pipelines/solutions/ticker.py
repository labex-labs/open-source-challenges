# ticker.py
from structure import Structure


class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()


if __name__ == "__main__":
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter("text")

    lines = follow("/home/labex/project/stocklog.csv")
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ["name", "price", "change"], formatter)
