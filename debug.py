# CHECK SRC FOLDER 
import sys, os
sys.path.insert(0, f'{os.path.dirname(os.path.abspath(__file__))}/src/') 

from importlib import import_module
from projects.base_project import BaseProject
from datetime import datetime
import sys, json, os, argparse
from pathlib import Path

if len(sys.argv) <= 1:
    print('Unrecognized structure')
    exit(1)

# GET ARGS
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--project', required=True)
parser.add_argument('-f', '--function', required=False, default='run')
parser.add_argument('-c', '--config', required=False, default='config.json')
parser.add_argument('-p', '--proxy', required=False)
args = parser.parse_args(sys.argv[1:])
_proxy = args.proxy == 'true'

# CHECK PROXY
if _proxy:
    PROXY = 'http://localhost:8888'
    os.environ['http_proxy'] = PROXY
    os.environ['HTTP_PROXY'] = PROXY
    os.environ['https_proxy'] = PROXY
    os.environ['HTTPS_PROXY'] = PROXY

if args.project is None:
    raise ValueError('Invalid selected project')

if __name__ == '__main__':
    st = datetime.now()
    config_name = os.environ.get('CONFIG_FILE') or args.config
    params = {**json.loads(open(f'{Path(__file__).parent}/{config_name}', encoding='utf-8').read()), 'proxy': _proxy}
    _import = ''.join([a.capitalize() for a in args.project.split('_')])
    _class: BaseProject = getattr(import_module(f"projects.{args.project.lower()}.model"), _import)(**params)
    getattr(_class, args.function)(**params)
    print(f'Total time execution: {(datetime.now() - st).total_seconds()} seconds')