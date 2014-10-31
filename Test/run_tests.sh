#!/bin/bash

PID=$$

cd ../Phase2/Web
./udeltio.py 8080 1>&2 2>/dev/null &

sleep 1

cd ../../Test/Dredd
../../Phase2/Web/node_modules/dredd/bin/dredd ../../apiary.apib http://localhost:8080 --hookfiles hooks/* --sorted --reporter markdown --output ../dredd_report.md >/dev/null
RET=$?

sleep 1

if [ $RET == 0 ]
then
	echo "All tests passed"
else
	echo "Some tests failed. Please check dredd_report.md"
fi

kill -TERM -- -$PID
