# https://ipinfo.io/developers/

import ipinfo
import json

handler = ipinfo.getHandlerLite(access_token='498bf80487bcbb')

details = handler.getDetails("103.168.172.52")

print(json.dumps(details.all))
