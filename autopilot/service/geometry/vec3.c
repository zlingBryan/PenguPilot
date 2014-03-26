/*___________________________________________________
 |  _____                       _____ _ _       _    |
 | |  __ \                     |  __ (_) |     | |   |
 | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
 | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
 | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
 | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
 |                   __/ |                           |
 |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
 |___________________________________________________|
  
 3D Vector Implementation

 Copyright (C) 2014 Tobias Simon, Ilmenau University of Technology

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details. */


#include <string.h>
#include <math.h>

#include <util.h>
#include "vec3.h"


void vec3_copy(vec3_t *vo, const vec3_t *vi)
{
   memcpy(vo, vi, sizeof(vec3_t));   
}


void vec3_mul_scalar(vec3_t *out, const vec3_t *in, const float scalar)
{
   FOR_N(i, 3)
      out->vec[i] = in->vec[i] * scalar;
}


float vec3_len(const vec3_t *in)
{
   float sum = 0.0f;
   FOR_N(i, 3)
      sum += in->vec[i] * in->vec[i];
   return sqrt(sum);
}

