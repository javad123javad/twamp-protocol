"""
This setup.py script is used to update the version of a ROS package.
We use semantic_release for the actual logic of updating the version based on the GIT commit messages.

NOTE: There is a __version__ string in this file. You should start by setting this to "0.0.0".

USAGE:
This script should be run twice:
1) Look at the git commits and increment the version: python3 setup.py version
2) Update the package.xml file with the new __version__ value: python3 setup.py
"""
import xml.etree.ElementTree as ET
import logging
import logging.config
import sys

logger = logging.getLogger(__name__)

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "class": "logging.StreamHandler",
            },
            # "fileInfo": {
            #     "level": "INFO",
            #     "class": "logging.handlers.RotatingFileHandler",
            #     "filename": os.path.join(LOG_ROOT, "info.log"),
            #     "maxBytes": 1024*1024*15,  # 15 MB
            #     "backupCount": 20,
            # },
        },
        "loggers": {"": {"handlers": ["default"], "level": "DEBUG", "propagate": True}},
    }
)

# This is version tag that we keep track of using semantic versioning
__version__ = "0.2.2"

try:
    from semantic_release import setup_hook
    logger.info(f"Version pre-hook: {__version__}")

    # TODO: Don't allow this to exit!
    # We currently have to run this twice to also update the package.xml file!
    setup_hook(sys.argv)

    logger.info(f"Version post-hook: {__version__}")
except Exception as e:
    logger.exception(f"Error :{e}")
# Update the version tag inside the package.xml file
file_name = "package.xml"
try:
    tree = ET.parse(file_name)
    root = tree.getroot()
    version_element = root.find("version").text
    logger.info(f"Version in package.xml is {version_element}")
    if(version_element != __version__):
        root.find("version").text = __version__
        logger.info(
            f'Updating version in {file_name} to {root.find("version").text}')
        tree.write(file_name)
except Exception as e:
    logger.exception(f"Error :{e}")