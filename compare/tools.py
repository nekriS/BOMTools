import Levenshtein
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
        table = pd.read_excel(file_name, usecols=f"{column}", skiprows=skip_row).dropna()
        if columns_name != []:
            table.columns = columns_name
        return table
    except:
        print("ERROR")

def compare(first_table, second_table):

    common = pd.merge(first_table, second_table, how='inner')
    #print(common)

    merged = pd.merge(first_table, second_table, how='outer', indicator=True)

    only_first = merged[merged['_merge'] == 'left_only'].drop('_merge', axis=1)
    only_second = merged[merged['_merge'] == 'right_only'].drop('_merge', axis=1)
                      
    print(only_first)
    print(only_second)

    quantity_changed = []
    spelling_changed = []
    q_s_changed = []

    add_first = only_first.copy()
    add_second = only_second.copy()

    column_names = only_first.columns

    for index, row in only_first.iterrows():
        row_count = row[column_names[0]]
        row_pn = row[column_names[1]]

        [status, target] = find_line_in_table([row_count, row_pn], only_second)
        match status:
            case "quantity changed":
                quantity_changed.append([row_count, row_pn, target[0], target[1]])
            case "spelling changed":
                spelling_changed.append([row_count, row_pn, target[0], target[1]])
            case "spelling and quantity changed":
                q_s_changed.append([row_count, row_pn, target[0], target[1]])
            case _:
                continue

        add_first = add_first[add_first[add_first.columns[1]] != row_pn]
        add_second = add_second[add_second[add_second.columns[1]] != target[1]]


    df_quantity_changed = pd.DataFrame(quantity_changed, columns=column_names.to_list()*2)
    df_spelling_changed = pd.DataFrame(spelling_changed, columns=column_names.to_list()*2)
    df_q_s_changed = pd.DataFrame(q_s_changed, columns=column_names.to_list()*2)
    print(add_first)
    print(add_second)

    return [common, df_quantity_changed, df_spelling_changed, df_q_s_changed, add_first, add_second]

def compare_the_lines(str1, str2):

    Levenshtein_c = 1 - Levenshtein.distance(str1, str2) / max(len(str1), len(str2))
    
    if str1 == str2:
        return 'equal'
    elif Levenshtein_c >= 0.9:
        return 'similar'
    else:
        return 'not equal'
    

def find_line_in_table(line, table):

    columns = table.columns

    line_count = line[0]
    line_pn = line[1]

    for index, row in table.iterrows():
        row_count = row[columns[0]]
        row_pn = row[columns[1]]

        match compare_the_lines(line_pn, row_pn):
            case 'equal':
                if row_count != line_count:
                    return 'quantity changed', [row_count, row_pn]
            case 'similar':
                if row_count == line_count:
                    return 'spelling changed', [row_count, row_pn]
                else:
                    return 'spelling and quantity changed', [row_count, row_pn]
            case _:
                continue

        print(row_count, row_pn)

    return "", []

if __name__ == "__main__":
    
    first_file_name = "CS_Trans2_TEST_SP_1.xlsx"
    first_file_count_column = "B"
    first_file_pn_column = "D"
    first_file_skip_row = 8

    first_table = get_table(first_file_name, f"{first_file_count_column}, {first_file_pn_column}", first_file_skip_row, ["count", "pn"])

    second_file_name = "CS_Trans2_TEST_SP_2.xlsx"
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

