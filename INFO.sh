#!/bin/bash
# Copyright (c) 2000-2020 Synology Inc. All rights reserved.

source /pkgscripts/include/pkg_util.sh

package="KakuTPCServer"
version="1.0.0-0001"
displayname="KaKu TPC-300 REST server"
os_min_ver="7.0-40000"
maintainer="Marijn Suijten"
arch="$(pkg_get_platform)"
description="Control individual KaKu lights through the TPC-300, exposed as a REST service"
dsmuidir="ui"
[ "$(caller)" != "0 NULL" ] && return 0
pkg_dump_info
