# Steps:
# 1. Manually download Strava user data and store file in desired location.
# 2. Create new geodatabase for file storage of polylines.
# 3. Point to .GPX files in script ((Input_GPX_File))
# 4. Run 'GPX to Feature Class' tool
####   syntax: 
####       GPXtoFeatures_conversion (Input_GPX_File, Output_Feature_class)
#5. Feature class to geodatabase
#6. Repeat script through list of rides.

import arcpy
import os

try:
	arcpy.env.workspace = r"D://PT/BusStops"
	arcpy.env.overwriteOutput = True

	# Create new geodatabase to store created polylines.
	arcpy.CreateFileGDB_management("D:/MSGT/Data/PythonBook/Exercise06/Results", "Routes.gdb")
	
	
	
	# Iterate over files in folder to convert GPX file to Feature Class and then copy to Geodatabase
	
	path = 'rides/'
	folder = os.listdir(path)
	for Input_GPX_File in folder:
		arcpy.GPXtoFeatures_conversion(Input_GPX_File, Output_Feature_class)
		arcpy.CopyFeatures_management(Output_Feature_class, "Routes.gdb/" + Output_Feature_class.basename)
	

		
		




# Catch errors.
except:
	print(arcpy.GetMessages())
