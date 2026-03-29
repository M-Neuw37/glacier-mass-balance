def single_stake_MB():
    
    """
    Calculates the mass balance of one stake based.
    
    Input the amount ice melted at the stake in meters (e.g. -6.43). This value is then multiplyed by the density of ice (0.9)
    and then printed to 3 deccimal places. 
    """
    
    ice_density = 0.9

    #TODO - input the ice metled at the stake
    ice_melted = float(input('Enter the amount of ice melted (m): '))
    
    mass_balance = ice_melted * ice_density
    
    print(f'The mass balance for the stake was {mass_balance:.3f}m w.e')
    
single_stake_MB()
