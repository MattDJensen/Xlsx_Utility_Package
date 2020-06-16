def align_cells(dataframe,workbook,worksheet, align='center'):
    """

    :param dataframe: Reference Dataset, Pandas Dataframe
    :type dataframe: Pandas Dataframe
    :param workbook: Xlsxwriter workbook
    :param worksheet: Xlsxwriter worksheet (must be within workbook)
    :param align: Alignment type Horizontal: (left / center/ right / fill / justify / center_across / distributed) or Vertical: (top, vcenter, bottom, vjustify, vdistributed)
    """
    cell_format = workbook.add_format()
    cell_format.set_align(align)
    worksheet.set_column(first_col=0, last_col=(len(dataframe.columns) + 1), width=1, cell_format=cell_format)
