# TODO- improve so that it can do this for multiple glaciers

import pandas as pd                                                                                   
import matplotlib.pyplot as plt 

def multiple_stakes_MB(filepath):
    
    """
    The multiple_stakes_MB function takes in a csv file which has the value of the ice melted at each stake 
    and calculates the specific mass balance for the stake by multiplying the value
    by the assumed density of ice (0.9 or  900kgm−3).
    
    csv input:
    Stake  IceMelted (m)
    1          -6.43
    2          -5.12
    3          -4.63
    4          -1.68    
    
    Example calculation:
        -6.43 * 0.9
        
    A new column is created (stake.mb(m w.e)) to store the value from the calculation. 
    
    csv output:
        Stake  IceMelted (m)  stake.mb(m w.e)
        1          -6.43           -5.787
        2          -5.12           -4.608
        3          -4.63           -4.167
        4          -1.68           -1.512 
        
    The data in the '(stake.mb(m w.e)' column is then plotted on a bar chart to visualise the data. 
    """
    
    df = pd.read_csv('data/basic.MB.calc.csv')
    
    df.head()
    
    print(df.columns)
    
    # add new column called 'stake.mb' to store the point mass balance
    df['stake.mb(m w.e)'] = df['IceMelted (m)'] * 0.9
    
    return df

MB_chart = multiple_stakes_MB('data/basic.MB.calc.csv')

# Create the bar chart to visualise the stake mass balance
plt.bar(MB_chart['Stake'], MB_chart['stake.mb(m w.e)'], color = 'red', edgecolor = 'k')

# Force the x-ticks to be exactly the stake numbers in the 'Stake' column
plt.xticks(MB_chart['Stake'])
plt.xlabel('Stake No.')
plt.ylabel('mass balance(m w.e.)')
plt.title('Stake mass balance')
plt.show()

multiple_stakes_MB('data/basic.MB.calc.csv')
