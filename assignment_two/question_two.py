class IncompleteDataError(Exception):
    pass
def read_ledger(lines):
    for line in lines:
        if line.strip() == "":
            raise IncompleteDataError("Empty line found in ledger")
        yield line
        ledger_data = [
            "2026-01-01, Sales, 500",
            "2026-01-02, Expenses, 200",
            "",
            "2026-01-03, Sales, 300"
        ]

        gen = read_ledger(ledger_data)

        while True:
            try:
                entry = next(gen)
                print("Processing:", entry)

            except IncompleteDataError as e:
                print("Warning:", e)
                print("Skipping bad record and continuing...")
                continue

            except StopIteration:
                print("Finished reading ledger.")
                break