import json
import os
import uuid

import docdb
import platform

print("Python == ", platform.python_version())

os.environ["DOCDB_HOST"] = 'https://mmffcoqaidb.documents.azure.com:443/'
os.environ["DOCDB_KEY"] = 'epU95lw68ON0azev8K3eXK5ZPfqdRmSKP32sjwBMBuHqbmr6v5lnMSlr8rrmUCdtTwBQMRtCOMw1oMicQNvzbA=='

# request body (POST requests) is stored in a file
# and the file path is exposed as an environment variable
with open(os.environ["REQ"]) as req:
    details = json.loads(req.read())


# note that there's no init for functions, so this will be
# executed everytime the function is triggered :(
# see https://github.com/Azure/azure-webjobs-sdk-script/issues/586
repository = docdb.Repository(os.environ["DOCDB_HOST"], os.environ["DOCDB_KEY"])

print(details)
print(uuid.uuid4())
# using email as partition key, so ensure that it exists,
# even if it's made up :)

#if not details.has_key("email"):
#    details["email"] = "%s@outlook.com" % uuid.uuid4()

print ("Storing the contact details in Azure Document DB")
doc = repository.insert(details)
print ("Repository returned %s" % doc)
