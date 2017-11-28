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
"""

import os
import sys
import tank

######################  set up logger
try:
    import sgtk
except Exception, err:
    print err
else:
    logger = sgtk.platform.get_logger(__name__)
#######################


#
class BeforeAppLaunch(tank.Hook):
    """
    Hook to set up the system prior to app launch.
    """

    def execute(self, app_path, app_args, version, **kwargs):
        """
        The execute functon of the hook will be called prior to starting the required application

        :param app_path: (str) The path of the application executable
        :param app_args: (str) Any arguments the application may require
        :param version: (str) version of the application being run if set in the "versions" settings
                              of the Launcher instance, otherwise None



        If you use environment variables in full paths, these will be automatically
        expanded. Note that on linux, they must be on the $ENV_VAR form and not on
        the ${ENV_VAR} form as this will confuse the include parser. Example:
        includes: ['$STUDIO_ROOT/foo/bar/hello.yml', '%STUDIO_ROOT%\foo\bar\hello.yml']

        """

        # accessing the current context (current shot, etc)
        # can be done via the parent object
        #
        # > multi_launchapp = self.parent
        # > current_entity = multi_launchapp.context.entity
        # you can set environment variables like this:
        # DABRENDER,DABWORK,DABUSR,DABASSETS,DABUSERPREFS ARE DEFINED EXTERNALLY

        _db   ="/Volumes/dabrender"
        _dbdev="/Users/Shared/UTS_Dev/gitRepositories/utsdab_repos"


        ENV={
            "DABRENDER"         : "{}".format(_db),\
            "DABWORK"           : "{}/work".format(_db),\
            "DABUSR"            : "{}/usr".format(_dbdev),\
            "DABASSETS"         : "{}/assets".format(_db),\
            "DABSWW"            : "{}/sww".format(_dbdev),\
            "DABETC"            : "{}/etc".format(_dbdev),\
            "DABUSERPREFS"      : "{}/work/user_prefs".format(_db),\
            "CONFIG"            : "{}/work/user_prefs/{}/config".format(_db,os.environ["USER"]),\
            "RMAN_VERSION"      : "21.5",\
            "MAYA_VERSION"      : "2017",\
            "XXX"               : "testing only",\
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

        if multi_launchapp.get_setting("engine") == "tk-maya":

            ###############################  ONLY INTERESTED IN OSX
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






