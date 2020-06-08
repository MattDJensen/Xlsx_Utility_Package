## Xlsx filetype utility functions

#### Autofit_Columns: Autofit all columns from dataframe written to xlsxfile with xlsxwriter
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
from mj.xlsxutility import autofit_columns

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
writer = pd.excelwriter("some_path",engine='xlsxwriter')
df.to_excel(writer)
autofit_columns(df,writer.sheets['Sheet1'],index=False)

```