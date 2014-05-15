""" 
Read the settings file from the appropriate place
"""
import yaml
import sys, os

__appname__ = "notoj"
__conffile__ = "notoj.yaml"

work_path = os.path.realpath(os.path.dirname(__file__))

is_BSD = sys.platform.find('bsd') != -1
is_Linux = sys.platform.startswith('linux')
is_Mac = sys.platform.startswith('darwin')
is_Windows = sys.platform.startswith('win')

# Prepare the paths given the system
paths = []

# Add current working directory
paths.append( os.path.join(os.getcwd(),__conffile__) )

# try to add the directory if we are testing
conf_path = os.path.realpath(os.path.join(work_path, "..", "conf"))
if os.path.exists(conf_path):
    paths.append(os.path.join(conf_path,__conffile__))

# add system dependent version of ~/.config/notoj/notoj.yaml
if is_Linux or is_BSD:
    paths.append( os.path.join( os.environ.get('XDG_CONFIG_HOME') or os.path.expanduser("~/.config"),
        __appname__, __conffile__))
elif is_Mac:
    paths.append(os.path.join(
        os.path.expanduser("~/Library/Application Support/"),
        __appname__, __conffile__))
elif is_Windows:
    paths.append(os.path.join(
        os.environ.get("APPDATA"), __appname__, __conffile__))

# add system dependent version of /etc/notoj/notoj.yaml
if is_Linux:
    paths.append(os.path.join("/etc", __appname__, __conffile__))
elif is_BSD:
    paths.append(os.path.join(
        sys.prefix, 'etc', __appname__, __conffile__))
elif is_Mac:
    paths.append(os.path.join(
        sys.prefix, 'etc', __appname__, __conffile__))

settings = {}

for path in paths:
    try:
        with open(path,'r') as f:
            settings.update( yaml.load(f) )
    except IOError:
        pass




