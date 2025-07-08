def cal_sal(base,bonus=.1):
    '''
    Calculates the total salary based on the base salary and bonus salary
    '''
    #this is a docstring which is helpful for other coders who want to know about this function, they just need to pass the function name to help :)
    return base*(1+bonus)

def cal_bon(total,base):
    return (total - base)/base
