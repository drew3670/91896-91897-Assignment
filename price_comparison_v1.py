def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"


# Program main heading
print(make_statement("Welcome to Planty Plants ", "🌸"))
print()
