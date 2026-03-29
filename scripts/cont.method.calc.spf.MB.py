def contour_method_basic(filepath):
    
    """
    This function 'contour_method_basic' takes in a csv file that has two columns. The first one (MB) in the mass balance band
    for the glacier that the mass balance is being calculated for and the second one (Area) is the area of glacier within the 
    mass balance band. This was calculated by counting the number of squares on milimetere paper in the mass balance band
    and multiplying it by 25 (e.g. 35 * 25 = 875).

    The volume is calculated by multiplying the mass balance band and the area and then the sum of the volume is divided by
    the sum of the area to get the specific mass balance. The volume is a fictitious unit.

    Example csv input:
         MB  Area
        -5.5  1375
        -4.5   400
        -3.5   275
        -2.5   250
        -1.5   875
        
    Example calculation:
        -5.5 * 1375

    csv output:
          MB  Area  Volume
        -5.5  1375 -7562.5
        -4.5   400 -1800.0
        -3.5   275  -962.5
        -2.5   250  -625.0
        -1.5   875 -1312.5
        -0.5  1425  -712.5
         0.5  1000   500.0  
         
    The volume sum is the divided by the area sum to get the specific glacier mass balance. See below:
        Volume sum = -12475.0
        Area sum = 5600
        
        -12475.0 / 5600 = -2.228
        
    final function output:
    'The specific mass balance is -2.228 m.w.e.'   
    """
    
    cont_test = pd.read_csv(filepath)
    
    cont_test['Volume'] = cont_test['MB'] * cont_test['Area']
    
    cont_test.head()
    
    cont_test['Area'].sum()
    
    specf_MB = cont_test['Volume'].sum() / cont_test['Area'].sum()
    
    print(f"The specific mass balance is {specf_MB:.3f} m.w.e.")
