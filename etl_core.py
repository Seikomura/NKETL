import pdfplumber


def extract_tables_from_pdf(pdf_path, target_headers):
    data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if (
                    table
                    and [c.strip() if c is not None else "" for c in table[0][: len(target_headers)]]
                    == target_headers
                ):
                    for row in table[1:]:
                        row_dict = {
                            header: value
                            for header, value in zip(
                                target_headers, row[: len(target_headers)]
                            )
                        }
                        data.append(row_dict)
    return data
