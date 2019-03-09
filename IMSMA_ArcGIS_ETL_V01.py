# -*- coding: utf-8 -*-
"""---------------------------------------------------------------------------
# IMSMA_ArcGIS_ETL_V01.py
# Created on: 2017-11-09
# Created by: Gabriel ODUORI
# Technical Advisor
# Description: Translate IMSMA geoDB into a format ready to use with the online
# mapping tools/portal for UNMAS Project.
# ---------------------------------------------------------------------------
"""

import os
import csv
import xlrd
import arcpy


arcpy.env.workspace = os.path.join("ForPortal")

#Check if the IMSMA geodatabase is  present in the workspace.
#If the not the program will abort.

if arcpy.Exists("/ForPortal/00_RawIMSMA/IMSMA.gdb"):
    try:
        print "Checking and creating required folders"
        if not os.path.exists("/ForPortal/01_SHAPEFILE"):
            print "Creating 01_SHAPEFILE Folder...."
            os.makedirs("/ForPortal/01_SHAPEFILE")
        else:
            print "01_SHAPEFILE Folder already exists. Contents will be removed"


        HR_point = "00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_point"
        HR_polygon = "00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_polygon"
        H_point = "00_RawIMSMA/IMSMA.gdb/Hazards_point"
        H_polygon = "00_RawIMSMA/IMSMA.gdb/Hazards_polygon"
        v01_SHAPEFILE = "01_SHAPEFILE"
        
        """
        Checking if the output folder is empty before processing.
        If there are files available they will be deleted.
        """
        shapefilePath = "/ForPortal/01_SHAPEFILE"
        shapefileList = os.listdir(shapefilePath)
        if shapefileList!=[]:
            print "Removing 01_SHAPEFILE Folder contents..."
            print "++++++++++++++++++++++++++++++++++++++++++++++"
            for shapefile in shapefileList:
                print shapefile
                arcpy.Delete_management(shapefilePath+"/"+shapefile)
                


        print "++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "STAGE 1:"
        print "IMPORTING DATA FROM IMSMA.gdb"
        print "++++++++++++++++++++++++++++++++++++++++++++++++++"
        print ""
        print "Process: Hazard Reductions point"
        arcpy.FeatureClassToFeatureClass_conversion(HR_point, v01_SHAPEFILE, "Hazard_Reductions_point.shp", "Subtype = 'Benchmark' OR Subtype = 'Reference Point'", "ObjectUID \"ObjectUID\" true true false 40 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_point,ObjectUID,-1,-1;Subtype \"Subtype\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_point,Subtype,-1,-1;Type \"Type\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_point,Type,-1,-1;Status \"Status\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_point,Status,-1,-1", "")

        print "Process: Hazard Reductions Polygon"
        arcpy.FeatureClassToFeatureClass_conversion(HR_polygon, v01_SHAPEFILE, "Hazard_Reductions_polygon.shp", "", "ObjectUID \"ObjectUID\" true true false 40 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_polygon,ObjectUID,-1,-1;Subtype \"Subtype\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_polygon,Subtype,-1,-1;Type \"Type\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_polygon,Type,-1,-1;Status \"Status\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazard_Reductions_polygon,Status,-1,-1", "")

        print "Process: Hazards Point"
        arcpy.FeatureClassToFeatureClass_conversion(H_point, v01_SHAPEFILE, "Hazards_point.shp", "Subtype = 'Benchmark' OR Subtype = 'Reference Point'", "ObjectUID \"ObjectUID\" true true false 40 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazards_point,ObjectUID,-1,-1;Subtype \"Subtype\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazards_point,Subtype,-1,-1;Type \"Type\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazards_point,Type,-1,-1;Status \"Status\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazards_point,Status,-1,-1", "")

        print "Process: Hazards Polygon"
        arcpy.FeatureClassToFeatureClass_conversion(H_polygon, v01_SHAPEFILE, "Hazards_polygon.shp","", "ObjectUID \"ObjectUID\" true true false 40 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazards_polygon,ObjectUID,-1,-1;Subtype \"Subtype\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazards_polygon,Subtype,-1,-1;Type \"Type\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazards_polygon,Type,-1,-1;Status \"Status\" true true false 50 Text 0 0 ,First,#,00_RawIMSMA/IMSMA.gdb/Hazards_polygon,Status,-1,-1", "")

        print ""
        print "Import process completed succesfully"
        print""
        print "+++++++++++++++++++++++++++++++++++++++++"
        print "STAGE 2:"
        print "DATA MANAGEMENT"
        print "+++++++++++++++++++++++++++++++++++++++++"
        print ""


        print "Preparing Tabular data...."
        if not os.path.exists("/ForPortal/02_TABLES"):
            print "Creating 02_TABLE Folder..."
            os.makedirs("/ForPortal/02_TABLES")
            print "Folder 02_TABLES created"
        else:
            print "02_TABLES Folder already exists. Contents will be removed"

        tablesPath = "/ForPortal/02_TABLES"
        tablesleList = os.listdir(tablesPath)
        
        if tablesleList!=[]:
            print "Removing 02_TABLE Folder contents...."
            print "++++++++++++++++++++++++++++++++++++++"
            for table in tablesleList:
                print table
                os.remove(tablesPath+"/"+table)


        HAZARD_File = r'/ForPortal/00_RawIMSMA/HAZARD.xls'
        wb = xlrd.open_workbook(HAZARD_File)
        for name in wb.sheet_names():
            out = file('%s.csv'% name, 'wb')
            writer = csv.writer(out)
            sheet = wb.sheet_by_name(name)
            for row in xrange(sheet.nrows):
                writer.writerow([
                    sheet.cell_value(row,col)
                    for col in xrange(sheet.ncols)
                    ])

        inTables = ['/ForPortal/HR.csv',
                    '/ForPortal/HZ.csv']
        outLocation = '/ForPortal/02_TABLES/'

        arcpy.TableToDBASE_conversion(inTables,outLocation)

        print "Joining shapefies with related tables"

        """
        Checking if the output folder is empty before processing.
        If there are files available they will be deleted.
        """

        if not os.path.exists("/ForPortal/03_JOINED"):
            print "Creating 03_JOINED Folder..."
            os.makedirs("/ForPortal/03_JOINED")
        else:
            print "03_JOINED Folder already exists. Contents will be removed"


        joinedirPath = "/ForPortal/03_JOINED"
        joinedfileList = os.listdir(joinedirPath)
        if joinedfileList!=[]:
            print "Removing 03_JOINED Folder contents...."
            print "+++++++++++++++++++++++++++++++++++++++"
            for joinedShape in joinedfileList:
                print joinedShape
                os.remove(joinedirPath+"/"+joinedShape)

        print ""
        print "++++++++++++++++++++++++++++++++++++++++++"
        print "Destination Folder Cleaning Successful"
        print "++++++++++++++++++++++++++++++++++++++++++"
        print ""
        
        HZ_Polygon =r"/ForPortal/01_SHAPEFILE/Hazards_polygon.shp"
        HR_Polygon = r"/ForPortal/01_SHAPEFILE/Hazard_Reductions_polygon.shp"
        HZ_Point = r"/ForPortal/01_SHAPEFILE/Hazards_point.shp"
        HR_Point = r"/ForPortal/01_SHAPEFILE/Hazard_Reductions_point.shp"
        
        """
        Th DBF tables can be checked and updated on the fly to always have
        the most updated and correct file availabe for use.
        DBF are also more efficient for querying.
        """

        HZ_table = r"/ForPortal/02_TABLES/HZ.dbf"
        HR_table = r"/ForPortal/02_TABLES/HR.dbf"

        print "Joining data with GIS Reports tables"
        print ""

        print "Processing: Hazards Polygon"
        arcpy.MakeFeatureLayer_management(HZ_Polygon, "Hazards_polygon")
        arcpy.AddJoin_management("Hazards_polygon", "ObjectUID", HZ_table, "hazard_gui", "KEEP_COMMON")
        arcpy.FeatureClassToFeatureClass_conversion("Hazards_polygon","/ForPortal/03_JOINED","Hazards_polygon")

        print "Processing: Hazards Reductions Polygon"
        arcpy.MakeFeatureLayer_management(HR_Polygon, "Hazard_Reductions_polygon")
        arcpy.AddJoin_management("Hazard_Reductions_polygon", "ObjectUID", HR_table, "HazreducGU", "KEEP_COMMON")
        arcpy.FeatureClassToFeatureClass_conversion("Hazard_Reductions_polygon","/ForPortal/03_JOINED","Hazard_Reductions_polygon")

        print "Processing: Hazard Points"
        arcpy.MakeFeatureLayer_management(HZ_Point, "Hazards_point")
        arcpy.AddJoin_management("Hazards_point", "ObjectUID", HZ_table, "hazard_gui", "KEEP_COMMON")
        arcpy.FeatureClassToFeatureClass_conversion("Hazards_point","/ForPortal/03_JOINED","Hazards_point")

        print "Processing: Hazard Reduction Points"
        arcpy.MakeFeatureLayer_management(HR_Point, "Hazards_Reductions_point")
        arcpy.AddJoin_management("Hazards_Reductions_point", "ObjectUID", HR_table, "HazreducGU", "KEEP_COMMON")
        arcpy.FeatureClassToFeatureClass_conversion("Hazards_Reductions_point","/ForPortal/03_JOINED","Hazard_Reductions_point")


        print ""
        print "GIS Report table join process successful."
        print ""


        print ""
        print "++++++++++++++++++++++++++++++++++++++++"
        print "STAGE 3:"
        print "CREATE NEW FILE GEODATABASE"
        print "++++++++++++++++++++++++++++++++++++++++"
        print ""


        """
        Creating empty folder which will hold the geodatabase
        """


        if not os.path.exists("/ForPortal/04_GEODB"):
            print "Creating 04_GEODB Folder..."
            os.makedirs("/ForPortal/04_GEODB")

            print "GeoDB created"
        else:
            print "04_GEODB Folder already exists. Contents will be removed"

        """
        Checking if the output folder is empty before processing.
        If there are files available they will be deleted.
        """
        geodirPath = "/ForPortal/04_GEODB"
        geofileList = os.listdir(geodirPath)
        if geofileList!=[]:
            print "Removing 04_GEODB Folder contents..."
            print "+++++++++++++++++++++++++++++++++++++++"
            for geofileName in geofileList:
                print geofileName
                arcpy.Delete_management(geodirPath+"/"+geofileName)

        print ""
        print "++++++++++++++++++++++++++++++++++++++++++"
        print "Destination Folder Cleaning Successful"
        print "++++++++++++++++++++++++++++++++++++++++++"
        print ""

        print "Creating a new IMSMA_Server_Data.gdb..."

        arcpy.CreateFileGDB_management("/ForPortal/04_GEODB", "IMSMA_Server_Data.gdb","CURRENT")

        print "Geodatabase created successfully"


        """
        if arcpy.Exists("/ForPortal/04_GEODB/IMSMA_Server_Data.gdb"):
        arcpy.Delete_management("/ForPortal/04_GEODB/IMSMA_Server_Data.gdb")
        print "Geodatabase cleared..."
        """

        print "++++++++++++++++++++++++++++++++++++++++++"
        print "Moving features into the geoDB..."
        print "++++++++++++++++++++++++++++++++++++++++++"

        inFeatures = ["/ForPortal/03_JOINED/Hazards_point.shp",
                      "/ForPortal/03_JOINED/Hazards_polygon.shp",
                      "/ForPortal/03_JOINED/Hazard_Reductions_point.shp",
                      "/ForPortal/03_JOINED/Hazard_Reductions_polygon.shp"]

        arcpy.FeatureClassToGeodatabase_conversion(inFeatures, "/ForPortal/04_GEODB/IMSMA_Server_Data.gdb")


        print "Files moved to the geodatabase successfuly"


        print ""
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        print "STAGE 4:"
        print "VALIDATING TABULAR DATA IN THE GEODATABASE"
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        print ""

        Hazard_Reductions_polygon = "/ForPortal/04_GEODB/IMSMA_Server_Data.gdb/Hazard_Reductions_polygon"
        Hazard_Reductions_point = "/ForPortal/04_GEODB/IMSMA_Server_Data.gdb/Hazard_Reductions_point"
        Hazards_point = "/ForPortal/04_GEODB/IMSMA_Server_Data.gdb/Hazards_point"
        Hazards_polygon = "/ForPortal/04_GEODB/IMSMA_Server_Data.gdb/Hazards_polygon"


        print "UPDATING TABLES..."
        print ""      
    
        print "Updating Hazard Reductions Polygon table..."
        
        # Add new required fields
        arcpy.AddField_management(Hazard_Reductions_polygon, "HRStartDate", "DATE", "", "", "", "HR Start Date", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(Hazard_Reductions_polygon, "HREndDate", "DATE", "", "", "", "HR End Date", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(Hazard_Reductions_polygon, "TotalNoofDevices", "LONG", "8", "", "", "No of Devices found", "NULLABLE", "NON_REQUIRED", "")
     

        # Calculate values for the new fields
        arcpy.CalculateField_management(Hazard_Reductions_polygon, "HRStartDate", "!HR_HRStart!", "PYTHON_9.3", "")
        arcpy.CalculateField_management(Hazard_Reductions_polygon, "HREndDate", "!HR_HREndda!", "PYTHON_9.3", "")
        arcpy.CalculateField_management(Hazard_Reductions_polygon, "TotalNoofDevices", "!HR_TotalNo!", "PYTHON_9.3", "")
 
        arcpy.AlterField_management(Hazard_Reductions_polygon,"HR_Provinc", "Province", "Province", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_Distric", "District", "District", "TEXT", "254", "NULLABLE", "false")       
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_Sub_Dis", "SubDistrict", "Sub-District", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_City_Co", "CityorCommunity", "City/Community", "TEXT", "254", "NULLABLE", "false")    
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_Org_Com", "Partner", "Partner", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_HazardR", "HazardReductionID", "HazardID", "TEXT", "254", "NULLABLE", "false")
        #arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_TypeofH", "TypeofHazardReduction", "Hazard Reduction type", "TEXT", "254", "NULLABLE", "false")    
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_Areasiz", "Areasize", "Hazard Area Size", "DOUBLE", "8", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_Calcula", "CalculatedArea", "CalculatedArea", "DOUBLE", "8", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_latitud", "Latitude", "Latitude", "DOUBLE", "12", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_longitu", "Longitude", "Longitude", "DOUBLE", "12", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_polygon, "HR_MGRS", "MGRS", "MGRS", "TEXT", "254", "NULLABLE", "false")


        print "Updating Hazard polygons table..."
     
        # Ading new required fields
        arcpy.AddField_management(Hazards_polygon, "StatusChangeDate", "DATE", "", "", "", "Status Change Date", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(Hazards_polygon, "TotalDevicesFound", "LONG", "8", "", "", "# of devices found", "NULLABLE", "NON_REQUIRED", "")
           
        #        

        arcpy.CalculateField_management(Hazards_polygon, "StatusChangeDate", "!HZ_StatusC!", "PYTHON_9.3", "")
        arcpy.CalculateField_management(Hazards_polygon, "StatusChangeDate", "!HZ_StatusC!", "PYTHON_9.3", "")
        arcpy.CalculateField_management(Hazards_polygon, "TotalDevicesFound", "!HZ_TonalNo!", "PYTHON_9.3", "")   

        # Updating the names of fields
        arcpy.AlterField_management(Hazards_polygon, "HZ_Pointty", "PoinType", "Point Type", "TEXT", "254", "NULLABLE", "false") 
        arcpy.AlterField_management(Hazards_polygon, "HZ_Provinc", "Province", "Province", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazards_polygon, "HZ_Distric", "District", "District", "TEXT", "254", "NULLABLE", "false")       
        arcpy.AlterField_management(Hazards_polygon, "HZ_Sub_Dis", "SubDistrict", "Sub-District", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazards_polygon, "HZ_City_Co", "CityorCommunity", "City/Community", "TEXT", "254", "NULLABLE", "false")    
        arcpy.AlterField_management(Hazards_polygon, "HZ_Org_Com", "Partner", "Partner", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazards_polygon, "HZ_Hazardl", "HazardReductionID", "HazardID", "TEXT", "254", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_polygon, "HZ_HazardA", "Areasize", "Hazard Area Size", "DOUBLE", "8", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_polygon, "HZ_HazardC", "CalculatedSize", "Calculated Area", "DOUBLE", "8", "NULLABLE", "false") 
        arcpy.AlterField_management(Hazards_polygon, "HZ_TypeofH", "Type_of_Hazardous_Area", "Type of Hazardous Area", "TEXT", "254", "NULLABLE", "false")
        #arcpy.AlterField_management(Hazards_polygon, "HZ_Typeo_1", "TypeofHazard", "Type of Hazard", "TEXT", "254", "NULLABLE", "false")       
        arcpy.AlterField_management(Hazards_polygon, "HZ_Statu_1", "StatusChangeReason", "Status Change Reason", "TEXT", "254", "NULLABLE", "false")            
        arcpy.AlterField_management(Hazards_polygon, "HZ_latitud", "Latitude", "Latitude", "DOUBLE", "12", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_polygon, "HZ_longitu", "Longitude", "Longitude", "DOUBLE", "12", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_polygon, "HZ_MGRS", "MGRS", "MGRS", "TEXT", "254", "NULLABLE", "false")


        print "Updating Hazard Reduction points table..."

        # Add new required fields

        arcpy.AddField_management(Hazard_Reductions_point, "CalculatedArea", "DOUBLE", "8", "", "", "Calculated Area", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(Hazard_Reductions_point, "HazardArea", "DOUBLE", "8", "", "", "Hazard Area", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(Hazard_Reductions_point, "TotalDevicesFound", "LONG", "8", "", "", "# of devices found", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(Hazard_Reductions_point, "HRStartDate", "DATE", "", "", "", "HR Start Date", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddField_management(Hazard_Reductions_point, "HREndDate", "DATE", "", "", "", "HR End Date", "NULLABLE", "NON_REQUIRED", "")
        

        # Update the new fileds with the required values

        arcpy.CalculateField_management(Hazard_Reductions_point, "CalculatedArea", "!HR_Calcula!", "PYTHON_9.3", "")
        arcpy.CalculateField_management(Hazard_Reductions_point, "HazardArea", "!HR_Areasiz!", "PYTHON_9.3", "")
        arcpy.CalculateField_management(Hazard_Reductions_point, "TotalDevicesFound", "!HR_TotalNo!", "PYTHON_9.3", "")
        arcpy.CalculateField_management(Hazard_Reductions_point, "HRStartDate", "!HR_HRStart!", "PYTHON_9.3", "" )
        arcpy.CalculateField_management(Hazard_Reductions_point, "HREndDate", "!HR_HREndda!", "PYTHON_9.3", "" )

        # Update rest of the names

        arcpy.AlterField_management(Hazard_Reductions_point,"Hazard_Red", "Hazard_GUID", "Hazard GUID", "TEXT", "40", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_point, "Hazard_R_1", "SubType", "Subtype", "TEXT", "40", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_Provinc", "Province", "Province", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_Distric", "District", "District", "TEXT", "254", "NULLABLE", "false")       
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_Sub_Dis", "SubDistrict", "Sub-District", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_City_Co", "CityorCommunity", "City/Community", "TEXT", "254", "NULLABLE", "false")    
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_Org_Com", "Partner", "Partner", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_HazardR", "HazardReductionID", "HazardID", "TEXT", "254", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_TypeofH", "TypeofHazardReduction", "Hazard Reduction type", "TEXT", "254", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_longitu", "Longitude", "Longitude", "DOUBLE", "12", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_latitud", "Latitude", "Latitude", "DOUBLE", "12", "NULLABLE", "false")
        arcpy.AlterField_management(Hazard_Reductions_point, "HR_MGRS", "MGRS", "MGRS", "TEXT", "254", "NULLABLE", "false")


        print "Updating Hazard points tables..."

        # Adding other required fields
        
        #arcpy.AddField_management(Hazards_polygon, "StatusChangeDate", "DATE", "", "", "", "Status Change Date", "NULLABLE", "NON_REQUIRED", "")
        #arcpy.AddField_management(Hazards_polygon, "TotalDevicesFound", "LONG", "8", "", "", "# of devices found", "NULLABLE", "NON_REQUIRED", "")
        

        # Updating the new fileds with the requited values

        #arcpy.CalculateField_management(Hazards_polygon, "StatusChangeDate", "!HZ_StatusC!", "PYTHON_9.3", "")
        #arcpy.CalculateField_management(Hazards_polygon, "TotalDevicesFound", "!HZ_TonalNo!", "PYTHON_9.3", "")        
   
        arcpy.AlterField_management(Hazards_point, "HZ_Provinc", "Province", "Province", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazards_point, "HZ_Distric", "District", "District", "TEXT", "254", "NULLABLE", "false")       
        arcpy.AlterField_management(Hazards_point, "HZ_Sub_Dis", "SubDistrict", "Sub-District", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazards_point, "HZ_City_Co", "CityorCommunity", "City/Community", "TEXT", "254", "NULLABLE", "false")    
        arcpy.AlterField_management(Hazards_point, "HZ_Org_Com", "Partner", "Partner", "TEXT", "254", "NULLABLE", "false")        
        arcpy.AlterField_management(Hazards_point, "HZ_Hazardl", "HazardReductionID", "HazardID", "TEXT", "254", "NULLABLE", "false")      
        arcpy.AlterField_management(Hazards_point, "HZ_TypeofH", "TypeofHazardousArea", "Type of Hazardous area", "TEXT", "254", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_point, "HZ_Typeo_1", "TypeofHazard", "Type of Hazard", "TEXT", "254", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_point, "HZ_Statu_1", "StatusChangeReason", "Status Change Reason", "TEXT", "254", "NULLABLE", "false")         
        arcpy.AlterField_management(Hazards_point, "HZ_latitud", "Latitude", "Latitude", "DOUBLE", "12", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_point, "HZ_longitu", "Longitude", "Longitude", "DOUBLE", "12", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_point, "HZ_MGRS", "MGRS", "MGRS", "TEXT", "254", "NULLABLE", "false")
        arcpy.AlterField_management(Hazards_point, "HZ_Pointty", "PointType", "Point Type", "TEXT", "254", "NULLABLE", "false")

        print ""
        print "Tables update completed successfully"
        print ""

        print "Cleaning tables....."

        arcpy.DeleteField_management(Hazard_Reductions_polygon, ["HR_MGRS_Y","HR_TotalNo","HR_TypeofH","HR_HRStart","HR_TotalDe","HR_HREndda","HR_MGRS_X","HR_Hazredu","HR_OID"])
        arcpy.DeleteField_management(Hazards_polygon, ["HZ_Typeo_1","TypeofHazard","HZ_hazard_","HZ_MGRS_Y","HZ_MGRS_X","HZ_Hazar_1","HZ_Status","HZ_OID","HZ_TonalNo","HZ_StatusC"])
        arcpy.DeleteField_management(Hazard_Reductions_point, ["HR_TotalNo","HR_latitud","HR_Hazredu","HR_MGRS_Y","HR_MGRS_X","HR_OID","Hazard_R_3","Hazard_R_2","HR_TotalDe","HR_Calcula","HR_Areasiz","HR_HREndda","HR_HRStart"])
        arcpy.DeleteField_management(Hazards_point, ["HZ_TypeofH","HZ_HazardA","HZ_HazardC","HZ_Status","HZ_StatusC","HZ_TonalNo","HZ_OID","HZ_Hazar_1","HZ_MGRS_X","HZ_MGRS_Y","HZ_hazard_"])



        Hazard_point_status=['Status']
        
        
        
        #Hazards_polygon = "/ForPortal/04_GEODB/IMSMA_Server_Data.gdb/Hazards_polygon"
        with arcpy.da.UpdateCursor(Hazards_point,Hazard_point_status)as Cursor:
            for row in Cursor:
                if (row[0]=="Active"):
                    row[0]="Open"
                elif (row[0]=="Expired"):
                    row[0]="Closed"
                Cursor.updateRow(row)

        Hazard_polygon_status=['Status']
        with arcpy.da.UpdateCursor(Hazards_polygon, Hazard_polygon_status)as Cursor:
            for row in Cursor:
                if (row[0]=="Active"):
                    row[0]="Open"
                elif (row[0]=="Expired"):
                    row[0]="Closed"
                Cursor.updateRow(row)

        
        HR_Polygon_type=['Type']
        with arcpy.da.UpdateCursor(Hazard_Reductions_polygon, HR_Polygon_type)as Cursor:
            for row in Cursor:
                if (row[0]=="NonTechSurvey"):
                    row[0]="Non-Technical Survey"
                elif (row[0]=="CompletionReport"):
                    row[0]="Completion Report"
                Cursor.updateRow(row)

        
        HR_Point_type=['TypeofHazardReduction']
        with arcpy.da.UpdateCursor(Hazard_Reductions_point, HR_Point_type)as Cursor:
            for row in Cursor:
                if (row[0]=="NonTechSurvey"):
                    row[0]="Non-Technical Survey"
                elif (row[0]=="CompletionReport"):
                    row[0]="Completion Report"
                Cursor.updateRow(row)
        


        print ""
        print "Tables cleaning completed successfully"
        print ""
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        print "END OF PROCESS"
        print "+++++++++++++++++++++++++++++++++++++++++++++++++"
        print ""

    except Exception as err:
        print (err.args[0])

else:
    print "IMSMA.gdb is misssing in the current workspace"
    print "Please make sure the file is present in the folder 00_RawIMSMA"




