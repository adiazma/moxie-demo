# CHECK SRC FOLDER 
import sys, os, warnings, json
sys.path.insert(0, f'{os.path.dirname(os.path.abspath(__file__))}/src/')

from importlib import import_module
from projects.base_project import BaseProject

warnings.filterwarnings('ignore')

def lambda_handler(event={}, context={}):
    project = os.environ.get('PROJECT')
    if project is None:
        raise ValueError('Invalid selected project')

    params = {**event, 'proxy': False}
    print(f'Event received: {json.dumps(params)}')
    method = params.get('function', 'run')
    if params.get('project'):
        project = params.get('project')

    _import = ''.join([a.capitalize() for a in project.split('_')])
    _class: BaseProject = getattr(import_module(f'projects.{project.lower()}.model'), _import)(**params)
    return getattr(_class, method)(**params)