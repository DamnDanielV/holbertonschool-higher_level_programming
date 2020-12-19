#!/bin/bash
# displays all HTTP methods the server will accept
curl -I "$1" 2>&1 | grep Allow | cut -d ' ' -f2-
