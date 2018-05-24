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



try:
	arcpy.env.workspace = r"D://PT/BusStops"
	arcpy.env.overwriteOutput = True

	for files in folder:
		
 

	# Create new geodatabase to store created polylines.
	arcpy.CreateFileGDB_management("D:/MSGT/Data/PythonBook/Exercise06/Results", "Routes.gdb")


	# Convert GPX file to Feature Class and then copy to Geodatabase
	arcpy.GPXtoFeatures_conversion('c:\\GPX_Files\\Hike.gpx', 'c:\\gisData\\Hike.shp')
	arcpy.CopyFeatures_management(ride, "D:/MSGT/Data/PythonBook/Exercise06/Results/NMpoly.gdb/" + ridedesc.basename)




# Catch errors.
except:
	print(arcpy.GetMessages())
