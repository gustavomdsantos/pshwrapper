#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PSH Wrapper – Run any Windows PowerShell command in Python scripts.
# Author: Gustavo Moraes <gustavosotnas1@gmail.com>
# MIT License – Copyright (c) 2018 Gustavo Moraes

import base64, subprocess

class PowerShellWrapper:
	def __encodeCommand__(self, commandString):
		commandInBase64 = base64.b64encode(commandString.encode('utf-16le'))
		return commandInBase64.decode("utf-8")

	def run(self, command):
		encodedCommand = self.__encodeCommand__(command)
		input = 'PowerShell -encodedCommand "'+ encodedCommand + '"'
		output = subprocess.run(input, shell=True)
		return output
