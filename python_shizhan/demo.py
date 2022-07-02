import os
from python_shizhan.excel_read_until import ReadExcel
from python_shizhan.conf_until import ReadConf

if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    read_confpath=ReadConf()
    print(read_confpath.read('mail','username'))
    excel_path = os.path.join(current_path, read_confpath.get_excelpath)
    print(excel_path)
    read_excel1=ReadExcel(excel_path)
    cases=read_excel1.read_excel()
    print(cases)
    # print(cases)
    # cases1=read_excel1.read_excel_cls()
    # print(cases1[3].case_name)