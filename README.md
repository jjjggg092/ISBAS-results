# ISBAS results
### Description
 plot_ts.py The script `plot_ts.py` allows to read all the files result of executing the ISBAS  method from   [this reposotory](https://github.com/ericlindsey/isbas "ISBAS code") and create a plot with the time series displacement of a specific location.

### Files

- **baseline_table.dat:** file with information about the acquisition dates of the images.
- **rate_mm_yr.grd:** NetCDF 4 file with all the data calculated to obtain the mean displacement between 2015 and 2020.
- **rate_mm_yr.kml:** Google Earth file to visualize the results obtained.
- **rate_mm_yr.png:** Supplement of the *rate_mm_yr.kml* to see the results.

### Requiriments
##### Software

- [Python 3](https://www.python.org/downloads/)
- [The Generic Mapping Tools (GMT)](https://www.generic-mapping-tools.org/download/)

##### Python libraries

- Numpy
- Matplotlib


### Usage

```bash
python3 plot_ts.py (disp_file.txt) (latitude) (longitude)
```
where:

- **disp_file.txt:** A file with all the locations of the grd files with the information about displacements.
- **latitude:** The latitude reference in decimal degrees.
- **longitude:** The longitude reference in decimal degrees.

Example:
```bash
python3 plot_ts.py files.txt 0.0352876437857 -78.4276493471
```
[![](https://raw.githubusercontent.com/jjjggg092/ISBAS-results/main/example.png)]() 
