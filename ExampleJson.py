#
# JSON processing
#

import json
import base64

# data = "{\"bucket\": \"pgs-git-datalake-nonprod-eur4-orca-compiled\"," \
#        "\"name\": \"HYP/HYP_OrcaCompiled_2021-08-31_12-00.json\"}"

data = {
       "bucket": "pgs-git-datalake-nonprod-eur4-orca-compiled",
       "name": "HYP/HYP_OrcaCompiled_2021-08-31_12-00.json"
}


json_data = json.dumps(data)

json_encoded = json_data.encode('utf-8')

print(f'json_encoded: {json_encoded}')