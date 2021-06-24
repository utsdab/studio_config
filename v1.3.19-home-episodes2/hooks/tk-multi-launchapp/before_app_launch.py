# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Before App Launch Hook

This hook is executed prior to application launch and is useful if you need
to set environment variables or run scripts as part of the app initialization.

example.....
import os
import tank

class BeforeAppLaunch(tank.Hook):

    def execute(self, app_path, app_args, version, engine_name, **kwargs):

        if engine_name == "tk-maya":
            os.environ["MY_CUSTOM_MAYA_ENV_VAR"] = "Some Maya specific setting"

"""



import os
import sys

import tank

import sgtk
logger = sgtk.LogManager.get_logger(__name__)
logger.info("Before App Launch Hook DAB")


class BeforeAppLaunch(tank.Hook):
    """
    Hook to set up the system prior to app launch.
    """
    
    def execute(self, app_path, app_args, version, engine_name, **kwargs):
        """
        The execute functon of the hook will be called prior to starting the required application        
        
        :param app_path: (str) The path of the application executable
        :param app_args: (str) Any arguments the application may require
        :param version: (str) version of the application being run if set in the
            "versions" settings of the Launcher instance, otherwise None
        :param engine_name (str) The name of the engine associated with the
            software about to be launched.

        """
#         logger.info("Before App Launch Hook")
		
        # accessing the current context (current shot, etc)
        # can be done via the parent object
        #
        # > multi_launchapp = self.parent
        # > current_entity = multi_launchapp.context.entity
        
        # you can set environment variables like this:
        # os.environ["MY_SETTING"] = "foo bar"
        
        _db   ="/Volumes/dabrender"
        _dbdev="/Users/Shared/UTS_Dev/gitRepositories/utsdab_repos"


        ENV={
            "DABRENDER"         : "{}".format(_db),\
            "DABWORK"           : "{}/work".format(_db),\
            "DABUSR"            : "{}/usr".format(_dbdev),\
            "DABASSETS"         : "{}/assets".format(_db),\
            "DABSWW"            : "{}/sww".format(_dbdev),\
            "DABETC"            : "{}/etc".format(_dbdev),\
            "DABPREFS"          : "{}/prefs".format(_db),\
            "DABUSERPREFS"      : "{}/prefs/user_prefs".format(_db),\
            "CONFIG"            : "{}/prefs/user_prefs/{}/config".format(_db,os.environ["USER"]),\
            "RMAN_VERSION"      : "21.6",\
            "MAYA_VERSION"      : "2018",\
            "TRACTOR_VERSION"   : "2.2",\
            "SHOTGUNENV_SOURCE" : "before_app_launch",\
            "SHOTGUNENV_USER"   : "{}".format(os.environ["USER"])
        }


        for key in ENV.keys():
            os.environ[key] = ENV[key]
            tank.util.append_path_to_env_var(key, ENV[key])


        # if you are using a shared hook to cover multiple applications,
        # you can use the engine setting to figure out which application
        # is currently being launched:
        #
        multi_launchapp = self.parent
        logger.info("{}".format(engine_name))


        if engine_name == "tk-maya" &&  sys.platform == "darwin":
            ###############################  ONLY INTERESTED IN OSX
            logger.info("running tk-maya on darwin")
            ENV_MAYA={\
            "MAYA_APP_DIR"         : "{}/mayaprefs".format(os.environ["CONFIG"]),\
            "RMANTREE"             : "/Applications/Pixar/RenderManProServer-{}".format(os.environ["RMAN_VERSION"]),\
            "RMSTREE"              : "/Applications/Pixar/RenderManForMaya-{}-maya{}".format(os.environ["RMAN_VERSION"],os.environ["MAYA_VERSION"]),\
            "RMS_SCRIPT_PATHS"     : "{}/etc/pixar/config".format(_dbdev),\
            "RDIR"                 : "{}/etc/pixar/config".format(_dbdev),\
            "SHOTGUNENV_MAYAONLY"  : "before_app_launch"
            }

            for key in ENV_MAYA.keys():
                os.environ[key] = ENV_MAYA[key]
                tank.util.prepend_path_to_env_var(key, ENV_MAYA[key])

            ##################################    ONLY INTERESTED IN OSX
            ENV_NUKE={\
            "RMANTREE"            : "/Applications/Pixar/RenderManProServer-{}".format(os.environ["RMAN_VERSION"]),\
            "SHOTGUNENV_NUKEONLY" : "before_app_launch"
            }

            for key in ENV_NUKE.keys():
                os.environ[key] = ENV_NUKE[key]
                tank.util.append_path_to_env_var(key, ENV_NUKE[key])

            # If there is a Task in the context, set its status to 'ip'

        if self.parent.context.task:
            task_id = self.parent.context.task['id']
            data = {
                'sg_status_list':'ip'
            }
            self.parent.shotgun.update("Task", task_id, data)





