import sys
sys.path.insert(0, '/var/www')

activate_this = '/home/acenta/.local/share/virtualenvs/acenta-nguY8doA//bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))
	
from main import app as application