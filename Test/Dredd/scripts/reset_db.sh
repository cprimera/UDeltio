#!/bin/bash

echo "Removing Tables..."
mysql -u udeltio --password=udeltio udeltio -e "drop table assigned_tags, post, subscribers, tag, token, client, user, board;"
cd ../../Phase3/Web
echo "Re-Creating Tables..."
echo "from udeltio import db; from models import *; from oauth2.o_models import *; db.create_all();" | python2
***REMOVED***
***REMOVED***
echo "Done"
