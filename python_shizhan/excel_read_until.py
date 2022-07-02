import os
import xlrd2
from python_shizhan.excel_info import CaseInfo
from python_shizhan.log_utils import log_pri


class ReadExcel:
    def __init__(self,file_path):
        self.file_path=file_path

    def read_excel(self):
        case_info = []
        try:
            workbook = xlrd2.open_workbook(self.file_path)
            log_pri.info('创建workbook成功')
        except FileNotFoundError as e:
            print('未知文件')
            current_path = os.path.dirname(__file__)
            self.file_path = os.path.join(current_path, '../test_case/test_data.xlsx')
            workbook = xlrd2.open_workbook(self.file_path)
            log_pri.error('文件未找到，使用默认文件路径')
        sheet1 = workbook.sheet_by_index(0)
        for i in range(1, sheet1.nrows):
            case_info_list = []
            for j in range(sheet1.ncols):
                case_info_list.append(sheet1.cell_value(i, j))
                # print(case_info_list)
            case_info.append(case_info_list)
        # except IndexError as e:
        #     print('表格下标越界')
        # except Exception as e:
        #     print('未知错误，原因'+ str(e))
        return case_info


    def read_excel_cls(self):
        workbook = xlrd2.open_workbook(self.file_path)
        sheet1 = workbook.sheet_by_index(0)
        case_infos = []
        for i in range(1, sheet1.nrows):
            # for j in range(sheet1.ncols):
            case_id= sheet1.cell_value(i,0)
            # print('case_id'+str(case_id))
            case_name=sheet1.cell_value(i,1)
            module=sheet1.cell_value(i,2)
            pri=sheet1.cell_value(i,3)
            case_stpe=sheet1.cell_value(i,4)
            expect_result=sheet1.cell_value(i,5)
            case_info=CaseInfo(case_id,case_name,module,pri,case_stpe,expect_result)
            case_infos.append(case_info)

        return case_infos


