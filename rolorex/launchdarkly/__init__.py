import os

import ldclient

ldclient.set_sdk_key(os.environ.get("LD_SDK_KEY"))
ld = ldclient.get()

any_user = {
    "key": "any"
}
