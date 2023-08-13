#!/bin/bash

for filename in *MOV
do
	# Use the original file as the reference to set the time for the related derived/converted files.
	# E.g., set timestamps for `FILE230805-173217-003647.MOV.mkv` from file `FILE230805-173217-003647.MOV`.
	touch --no-create --reference=$filename $filename?*
done