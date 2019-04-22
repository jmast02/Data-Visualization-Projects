from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    '''return the 2 digit country code'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #if the country isnt found return none
    return None

