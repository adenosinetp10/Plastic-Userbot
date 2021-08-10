from os.path import dirname, basename, isfile
from glob import glob
from plastic import logger

def modules_list():
    module_path = glob(dirname(__file__)+"/*.py")
    #print(module_path)
    all_modules = [basename(mdl)[:-3] for mdl in module_path if isfile(mdl) and mdl.endswith(".py") and not mdl.endswith("__init__.py")]
    return all_modules



MODULES = sorted(modules_list())
__all__ = MODULES + ["MODULES"]
#print(MODULES)
for i in MODULES:
    logger.info(f"Modules loaded : {i}")