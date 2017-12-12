# WebMapapplication
Web map using folium, python
This repo used python and folium to create Web map for school data.
Data was obtained from https://data.cese.nsw.gov.au

File Structure
1. Input file: "Collections.csv", this is the data file obtained from https://data.cese.nsw.gov.au. This has data for all NSW public schools.
2. convert.py --- extracts required fields from collection.csv and generate out.csv file.
3. webmap.py --- Generate map based on out.csv file. Layer control is added to map based on type of school(selctive, non-selective, partially-selective).
