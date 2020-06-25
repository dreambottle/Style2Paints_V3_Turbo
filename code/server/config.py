import configparser

# get ini config parser
ini_config = configparser.ConfigParser()


device_A = '/gpu:0'
device_B = '/gpu:0'
multiple_process = True
debugging = False


# load "zoom factor" from ini config file
def get_sketch_resolution_factor():
    ini_path = 'config.ini'
    ini_config.read(ini_path) # read ini config
    resolution_factor = ini_config.getfloat('general','sketch_zoom_factor')
    return resolution_factor