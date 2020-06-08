import pandas as pd
import xlsxwriter


def autofit_columns(dataframe, worksheet, padding=1.1, index=True):
    """ Autofit all columns in xlsxwriter worksheet based on length of values in dataframe column.

    :param dataframe: Base dataframe written to xlsx workbook
    :param worksheet: Sheet in xlsx workbook to be formatted
    :param padding: Optional, padding amount
    :param index:  Optional, Index true/false in dataframe. defaults to True
    :return: formatted worksheet
    """
    def get_col_widths(dataframe, padding, index):
        """

        :param dataframe: Base dataframe written to xlsx workbook
        :param padding: Optional, padding amount
        :param index:  Optional, Index true/false in dataframe. defaults to True
        :return: Column width for formatting
        """
        max_width_idx = []
        if index and isinstance(dataframe.index, pd.MultiIndex):
            # Index name lengths
            max_width_idx = [len(v) for v in dataframe.index.names]

            # Index value lengths
            for column, content in enumerate(dataframe.index.levels):
                max_width_idx[column] = max(max_width_idx[column],
                                            max([len(str(v)) for v in content.values]))
        elif index:
            max_width_idx = [
                max([len(str(s))
                     for s in dataframe.index.values] + [len(str(dataframe.index.name))])
            ]

        if isinstance(dataframe.columns, pd.MultiIndex):
            # Take care of columns - headers first.
            max_width_column = [0] * len(dataframe.columns.get_level_values(0))
            for level in range(len(dataframe.columns.levels)):
                values = dataframe.columns.get_level_values(level).values
                max_width_column = [
                    max(v1, len(str(v2))) for v1, v2 in zip(max_width_column, values)
                ]

            # Now content.
            for idx, col in enumerate(dataframe.columns):
                max_width_column[idx] = max(max_width_column[idx],
                                            max([len(str(v)) for v in dataframe[col].values]))

        else:
            max_width_column = [
                max([len(str(s)) for s in dataframe[col].values] + [len(col)])
                for col in dataframe.columns
            ]

        return [round(v * padding) for v in max_width_idx + max_width_column]

    for i, width in enumerate(get_col_widths(dataframe, padding, index)):
        worksheet.set_column(i, i, width)
