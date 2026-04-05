The app is launched by putting `streamlit run main.py` into the terminal
in the relevant file directory. 

Upload a CSV file to streamlit to calculate the stake mass balance. 

The CSV file has to have a column called `Stake` (for the stake number) and
`IceMelted (m)` (for the measured amount of ice melted at the stake).

| Stake | IceMelted (m) |
|----------|----------|
| 1        | -6.43   |
| 2        | -5.12   |

      
The values in `IceMelted (m)` are multiplied by the density of ice 0.9 (900kgm−3) and 
are then printed into a new column called `stake.mb(m w.e)`.

| Stake | IceMelted (m) | stake.mb(m w.e) |
|----------|----------| ------------------|
| 1        | -6.43   | -5.787 |
| 2        | -5.12   | -4.608 |

Below the new CSV file there is an interative bar chart for visualising the data.
