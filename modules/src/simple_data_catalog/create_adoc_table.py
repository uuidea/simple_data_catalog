def create_adoc_table(entries: list, num_cols: int) -> str:
    """
    Creates an AsciiDoc table string from a list of entries.

    Args:
        entries (list): A list of data entries to include in the table.
        num_cols (int): The desired number of columns in the table.

    Returns:
        str: An AsciiDoc table string. Returns "table dimensions inconsistent" if the number of entries is not divisible by the number of columns.
    """
    if len(entries) % num_cols != 0:
        return "table dimensions inconsistent"

    table_str = ""
    col_specs = "[cols=" + '"' + ",".join(["1"] * num_cols) + '"]\n'
    header = "|=== \n"

    table_str += col_specs + header

    for entry in entries:
        table_str = table_str + "a| " + str(entry) + "\n"  # a is to support lists

    table_str = table_str + "|=== \n\n"
    return table_str
