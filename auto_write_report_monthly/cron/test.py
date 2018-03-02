#coding=utf-8
#！/usr/bin/env python3


import docx

doc = docx.Document()


table = doc.add_table(rows=4, cols=1, style='Table Grid')  # 创建带边框的表格
table.style.font.size = 120000

cells = table.rows[0].cells
cells[0].text = '巡检记录： 已检 \n设备型号： Cisco 4506 \n设备描述：多层交换机 '

    # for j in range(1):
    #     cells[j].text = str(val * 10)
    #     val += 1

doc.save('tmp1.docx')