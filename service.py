import os
import traceback

import xbmc
import xbmcaddon
import xbmcvfs

__addon__ = xbmcaddon.Addon()
__addondir__ = __addon__.getAddonInfo('profile')
__cwd__ = __addon__.getAddonInfo('path')
__resource__ = os.path.join(__cwd__, 'resources', 'lib')
sys.path.append (xbmcvfs.translatePath( os.path.join( os.getcwd(), 'resources', 'lib' ) ))

sys.path.append(__resource__)

from resources.lib.service_entry import Service
from tools import xbmclog
#from resources.lib.ga_client import GoogleAnalytics

#DELAY = int(Settings.getSetting('startup_delay') or 0)

DELAY = 0

if __name__ == "__main__":
    xbmclog("======== STARTED ========")

    try:
        service = Service()
        abort = False
        if DELAY and xbmc.Monitor().waitForAbort(DELAY):
            raise RuntimeError("Abort event while waiting to start Emby for kodi")
            abort = True
        # Start the service
        if abort == False:
            service.service_entry_point()

    except Exception as error:
        # Display the *original* exception
        traceback.print_exc()

        xbmclog("Forcing shutdown")
        service.shutdown()

    xbmclog("======== STOPPED ========")
