#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PSH Wrapper – Run any Windows PowerShell command in Python scripts.
# Author: Gustavo Moraes <gustavosotnas1@gmail.com>
# MIT License – Copyright (c) 2018 Gustavo Moraes

import base64, subprocess

class PowerShellWrapper:
	def __encodeCommand__(self, commandString):
		input = 'PowerShell -Command "& {$command = {'+ commandString +'}; $bytes = [System.Text.Encoding]::Unicode.GetBytes($command); $encodedCommand = [Convert]::ToBase64String($bytes); echo $encodedCommand}"'
		output = subprocess.run(input, shell=True, stdout=subprocess.PIPE)
		return output.stdout.decode("utf-8").strip()

	def run(self, command):
		encodedCommand = self.__encodeCommand__(command)
		input = 'PowerShell -encodedCommand "'+ encodedCommand + '"'
		output = subprocess.run(input, shell=True)
		return output
