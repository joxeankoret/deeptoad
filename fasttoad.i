%include "carrays.i"

/*
This file is part of DeepToad
Copyright (C) 2009, Joxean Koret

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Speed improvements by Avira Operations Gmbh, Thorsten Sick, thorsten.sick@avira.com
*/

%module fasttoad_wrap

%{
#include <fasttoad.h>
%}

%apply (char *STRING, int LENGTH) { (unsigned char *data, int size) };

extern unsigned char modsum(unsigned char * data, int size);
