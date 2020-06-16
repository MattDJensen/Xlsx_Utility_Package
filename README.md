## Xlsx filetype utility functions

#### autofit_columns: Autofit all columns from dataframe written to xlsxfile with xlsxwriter
```python
def autofit_columns(dataframe, worksheet, padding=1.1, index=True):
    """

    :param dataframe: Base dataframe written to xlsx workbook
    :param worksheet: Sheet in xlsx workbook to be formatted
    :param padding: Optional, padding amount
    :param index:  Optional, Index true/false in dataframe. Defaults true, use false for non-indexed dataframe outputs. 
    :return: formatted worksheet
    """

```

##### Example Call
```python
import pandas as pd
import numpy as np
from xlsxutility import autofit_columns

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
writer = pd.excelwriter("some_path",engine='xlsxwriter')
df.to_excel(writer)
autofit_columns(df,writer.sheets['Sheet1'],index=False)

```

#### align_cells: Horizontally or vertically align all cells in given dataframe. 
#### Note - If using in conjunction with autofit_columns this must be called first, or the default width (1) will overwrite. 
```python
def align_cells(dataframe,workbook,worksheet, align='center'):
    """

    :param dataframe: Reference Dataset, Pandas Dataframe
    :type dataframe: Pandas Dataframe
    :param workbook: Xlsxwriter workbook
    :param worksheet: Xlsxwriter worksheet (must be within workbook)
    :param align (optional):Defaults to horizontal center.  Alignment types Horizontal: (left / center/ right / fill / justify / center_across / distributed) or Vertical: (top, vcenter, bottom, vjustify, vdistributed)
    """

```

##### Example Call
```python
import pandas as pd
import numpy as np
from xlsxutility import align_cells

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
writer = pd.excelwriter("some_path",sheet_name='Example',engine='xlsxwriter')
df.to_excel(writer)
align_cells(df,writer,writer.sheets['Example'],'center')

```