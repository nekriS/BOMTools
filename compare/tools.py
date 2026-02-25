
import pandas as pd

class options():
    def __init__(self):
        pass

    def add_option(self, option):
        setattr(self, get_var_name(option), option)

def get_var_name(var):
    for name, value in locals().items():
        if value is var:
            return name
    return None

def get_table(file_name, column, skip_row, columns_name=[]):

    try:
        table = pd.read_excel(file_name, usecols=f"{column}", skiprows=skip_row)
        if columns_name != []:
            table.columns = columns_name
        return table
    except:
        print("ERROR")
    

def find_common_rows(df1, df2, ignore_index=True, ignore_column_order=True):
    """
    Возвращает строки, которые присутствуют в обоих DataFrame.

    Параметры:
        df1 (pd.DataFrame): Первый DataFrame.
        df2 (pd.DataFrame): Второй DataFrame.
        ignore_index (bool): Игнорировать индексы при сравнении (по умолчанию True).
        ignore_column_order (bool): Игнорировать порядок столбцов (по умолчанию True).

    Возвращает:
        pd.DataFrame: DataFrame с общими строками.
    """
    # Копируем DataFrame, чтобы не изменять оригиналы
    d1 = df1.copy()
    d2 = df2.copy()

    # При необходимости приводим столбцы к одному порядку
    if ignore_column_order:
        common_cols = sorted(set(d1.columns) & set(d2.columns))
        if not common_cols:
            return pd.DataFrame()  # Нет общих столбцов
        d1 = d1[common_cols]
        d2 = d2[common_cols]

    # Сбрасываем индексы, если нужно
    if ignore_index:
        d1 = d1.reset_index(drop=True)
        d2 = d2.reset_index(drop=True)

    # Находим общие строки через inner merge
    common = pd.merge(d1, d2, how='inner')

    return common

def compare(first_table, second_table):

    print(find_common_rows(first_table, second_table))
    pass

if __name__ == "__main__":
    
    first_file_name = "cubesat_sp_1.xlsx"
    first_file_count_column = "B"
    first_file_pn_column = "D"
    first_file_skip_row = 8

    first_table = get_table(first_file_name, f"{first_file_count_column}, {first_file_pn_column}", first_file_skip_row, ["count", "pn"])

    second_file_name = "cubesat_sp_1.xlsx"
    second_file_count_column = "B"
    second_file_pn_column = "D"
    second_file_skip_row = 8

    second_table = get_table(second_file_name, f"{second_file_count_column}, {second_file_pn_column}", second_file_skip_row, ["count", "pn"])

    compare(first_table, second_table)

    # options_list = options()
    # options_list.add_option(first_file_column)
    # options_list.add_option(first_file_skip_row)
    # options_list.add_option(second_file_column)
    # options_list.add_option(second_file_skip_row)
    
    # compare(first_file_name, second_file_name, options_list)

