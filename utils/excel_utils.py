from openpyxl import load_workbook


def get_categories_from_excel(file_path):
    workbook = load_workbook(file_path)
    sheet = workbook.active

    categories = []

    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, values_only=True):
        category_name = row[0]
        if category_name:
            categories.append(category_name)

    workbook.close()
    return categories


def get_products_from_excel(file_path):
    workbook = load_workbook(file_path)
    sheet = workbook.active

    products = []

    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, values_only=True):
        product = {
            "category": row[0],
            "name": row[1],
            "price": row[2],
            "unit": row[3],
            "description": row[4],
            "is_hidden": row[5],
            "position": row[6],
        }

        if product["name"] is not None:
            products.append(product)

    print("TOTAL PRODUCTS:", len(products))

    workbook.close()
    return products

def get_unit_from_excel(file_path):
    workbook = load_workbook(file_path)
    sheet = workbook.active

    units = []

    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, values_only=True):
        unit = {
            "unit_name" : row[0],
            "unit_code" : row[1],
            "unit_ratio" : row[2],
            "unit_description" : row[3]
        }

        if unit["unit_name"] is not None:
            units.append(unit)

    print("TOTAL PRODUCTS:", len(units))

    workbook.close()
    return units
