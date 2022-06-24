# THIS MODULE DOES THE ACTUAL DATA COMPARISON. #
from filewrite import FileWrite


class Compare:
    def __init__(self, lista, listb):
        self.table_ext = lista
        self.table_int = listb
        self.table_diff = []

    def compare_table(self):
        file = FileWrite()
        ext_only_data = []
        int_only_data = []
        variance_data = []

        # TODO A LIST OF ALL THE PRIMARY KEYS IS RETRIEVED FROM BOTH TABLES.
        product_id_list_ext = [self.table_ext[index][1] for index in range(0, len(self.table_ext))]
        product_id_list_int = [self.table_int[index][1] for index in range(0, len(self.table_int))]

        # TODO : PRODUCT IDS  OF ROWS PRESENT ONLY IN EXTERNAL TABLE IS OBTAINED
        present_in_ext_only = set(product_id_list_ext) - set(product_id_list_int)

        # TODO : FOR DATA PRESENT IN EXTERNAL PRODUCT TABLE AND NOT IN INTERNAL PRODUCT TABLE
        #  A FLAG 'EXT_ONLY'
        #  IS APPENDED TO EACH ROW AND FILE_WRITE METHOD IS CALLED
        for item in present_in_ext_only:
            for entry in self.table_ext:
                if entry[1] == int(item):
                    flag = 'EXT_ONLY'
                    ext_only_data.append([flag, entry])
        print(ext_only_data)
        file.write_file_firsttime(ext_only_data)

        # TODO : PRODUCT IDS  OF ROWS PRESENT ONLY IN INTERNAL TABLE IS OBTAINED
        present_in_int_only = set(product_id_list_int) - set(product_id_list_ext)

        # TODO : FOR DATA PRESENT IN INTERNAL PRODUCT TABLE AND NOT IN EXTERNAL PRODUCT TABLE
        #  A FLAG 'INT_ONLY'
        #  IS APPENDED AND FILE_WRITE METHOD IS CALLED

        for item in present_in_int_only:
            for entry in self.table_int:
                if entry[1] == int(item):
                    flag = 'INT_ONLY'
                    int_only_data.append([flag, entry])
        print(int_only_data)
        file.write_file(int_only_data)

        # TODO : PRODUCT IDS  OF ROWS PRESENT IN BOTH THE TABLES ARE OBTAINED
        present_in_both = set(product_id_list_ext) & set(product_id_list_int)

        # TODO : FOR DATA PRESENT IN BOTH INTERNAL PRODUCT TABLE AND EXTERNAL PRODUCT TABLE BUT WITH DATA VARIATIONS
        #  A FLAG 'VARIANCE'
        #  IS APPENDED AND FILE_WRITE METHOD IS CALLED

        for item in present_in_both:
            for dataA, dataB in zip(self.table_ext, self.table_int):
                if dataA[1] == item & dataB[1] == item:
                    if dataA != dataB:
                        print(f'Mismatch found in product ID {item}!')
                        flag = 'VARIANCE'
                        variance_data.append([flag, dataA])
        print(variance_data)
        file.write_file(variance_data)
