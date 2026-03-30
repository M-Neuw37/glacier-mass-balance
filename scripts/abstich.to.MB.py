def abstich_to_mass_balance (filepath):
    
    """
    **TODO** 
    Change column names to make them make more sense. (start_season_ab & end_season_ab)
    ********
    
    The purpose of this function is to take a csv file that has columns that store the previous years abstich and the current years abstich.
    
    Abstich (Upstick) is the length of the ablation stake remaining above the ice surface after installation. It can also 
    be the distace from the top of the stake to the ice surface, this would result in a negative value for the absitch. 
    
    To calculate the actual ablation the initial abstich (abstich measured when the stake was installed at the start of the season)
    is subtracted from the final measurement at the end of the season (top of the stake to the ice surface).
    
    Formula:
    Actual Melt = Final Stake Exposure - Initial Abstich
    
    Example:
    At the start of the season 6m stake is drilled 5.9m into the ice, therefore there is 0.1m (10cm) of abstich and at the end season
    the stake is 3m above the ice. Using the formula above helps to get the acutual ice melt at the location, which would be 2.9m (3.0(Final Stake Exposure) - 0.1(Initial Abstich)).
    
    -------------
    
    The small and basic function works as follows.
    
    The input csv is has two columns, one for the previous years abstich and one for the current years abstich.
    Example:
        Stake  Prev.Yr.Abstich(cm)  Curr.Yr.Abstich(cm)
           1                   33                  676
           2                   -4                  508
           3                   40                  463
           4                  137                  305
           
    To get the ice melted, the previous year abstich has to be taken away from the current year and the output from this 
    is stored in a new column ('ice_metled').
    
    A final is created which stores the point (or stake) mass balance by multiplying the value in the 'ice_melted' column by the 
    density of ice (0.9). An example output of this column can be seen below:
        Stake  stake_mass_balance
           1              -5.787
           2              -4.608
           3              -3.807
           4              -1.512
    """
    
    abstich = pd.read_csv(filepath)
    
    #abstich.head()
    
    #print(abstich.columns)
    
    abstich['ice_melted'] = abstich['Prev.Yr.Abstich(cm)'] - abstich['Curr.Yr.Abstich(cm)']
    
    # get the mass balance for the stake by multiplying by the density of ice and then divide by 100 to change
    # into meter water equivilent
    
    abstich['stake_mass_balance'] = abstich['ice_melted'] * 0.9 / 100
    
    return abstich

results = abstich_to_mass_balance('data/abstich.test.csv') 
print(results[['Stake', 'stake_mass_balance']])
