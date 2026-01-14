def create_book_catalog(borrowed_books):
    borrowed_num = {}
    for book in borrowed_books:
        borrowed_num[book[0]] = book[1]
        return borrowed_num
def audit_returns(catalog, returned_isbns):
    catalog_set = set(catalog)
    returned_isbns_set = set(returned_isbns)
    overdue_books = catalog_set - returned_isbns_set
    unknown_returns = returned_isbns_set - catalog_set
    return overdue_books, unknown_returns
def format_overdue_report(catalog, overdue_isbns):
    missing = sorted([title for isbn,title in catalog.items() if isbn not in overdue_isbns ])
    for title in missing:
        for isbn, title_all in catalog.items():
            if title != title:
                continue
                print(f"MISSING: {title} (ISBN: {isbn})")
    
borrowed = [
    (1001, "The Great Gatsby", "John"),
    (1002, "1984", "Sarah"),
    (1003, "Python 101", "Mike")
]

returned = [1003, 1001, 9999]

catalog = create_book_catalog(borrowed)
overdue_isbns = audit_returns(catalog, returned)
format_overdue_report(catalog, overdue_isbns)










