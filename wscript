#! /usr/bin/env python
# encoding: utf-8
#
# Altruistic Control Systems
# Control Node base wscript
# Kenneth Wells, 2015

from waflib import Options, Logs
from waflib import Configure

def configure(conf):
    pass

def build(bld):
    bld(
        target='HmiCore',
        install_path='${PREFIX}/lib',
        features=['cxx', 'cxxshlib','package', 'qt5'],
        manifest='HmiCore.package',
        uselib=['QT5CORE','QT5GUI','QT5QUICK','QT5BASE','QT5OPENGL','QT5SVG'],
        defines='WAF=1'
        )
