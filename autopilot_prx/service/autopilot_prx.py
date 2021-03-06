#!/usr/bin/env python
"""
  ___________________________________________________
 |  _____                       _____ _ _       _    |
 | |  __ \                     |  __ (_) |     | |   |
 | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
 | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
 | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
 | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
 |                   __/ |                           |
 |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
 |___________________________________________________|
  
 Autopilot State Proxy

 Copyright (C) 2015 Integrated Communication Systems Group, TU Ilmenau

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details. """


from scl import SCL_Proxy
from scl import SCL_Reader, scl_get_socket
from misc import daemonize
from pp_prio import PP_PRIO_3
from scheduler import sched_set_prio
from time import sleep

def main(name):
   #sched_set_prio(PP_PRIO_3)

   ap_state = SCL_Reader('ap_state', 'sub', 'standing')
   ap_status = scl_get_socket('ap_status', 'pub')
   prev_state = 'standing'

   while True:
       sleep(0.1)
       if ap_state.data:
           ap_status.send(ap_state.data)
           prev_state = ap_state.data
       else:
           ap_status.send(prev_state)

daemonize('autopilot_prx', main)
