#!/bin/bash
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 2.1
# of the License.
#
# Copyright(c) 2023 Huawei Device Co., Ltd.

set -e
cd $1
if [ -d "re2-2021-11-01" ];then
    rm -rf re2-2021-11-01
fi
tar zxvf re2-2021-11-01.tar.gz
exit 0