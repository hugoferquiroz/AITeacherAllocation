# AITeacherAllocation
This repository create an AI to evaluate teacher allocation in peruvian public schools.

# Problem Definition

The numbers of classroom is determined in meets between by workers of ministry of education and workers of regional district schools.

In these meet the allocation of the classroom is based by the resolution [RMV 307-2019](https://cdn.www.gob.pe/uploads/document/file/436535/RVM_N__307-2019-MINEDU.pdf). This resolution assig classroom by:


|                  |  Teacher workforce | Urban | Rural |   |
|------------------|--------------------|-------|-------|---|
| kindergarten     |                    |       |       |   |
|                  |                    |       |       |   |
| Primary school   |                    |       |       |   |
| Secondary school |                    |       |       |   |


|               |          Grouping             ||         Grouping 2         ||  Not Grouped    |
| First Header  | Second Header | Third Header   | Forth Header | Fifth Header | Sixth Header    |
| ------------- | :-----------: | -------------: | :----------: | :----------: | --------------- |
| Tall Cell     |          *Long Cell*          ||         *Long Long Cell*                    |||
| ^^            |   **Bold**    | 1. first item  | *Italic*     | 3. third item | + first point  |\
| ^^            |               | 1. second item |              | 1. forth item | + second point |

| New section   |     More      |         Data   | ... - -- --- |||
| And more      | With an escaped \|          || "Try 'quotes' in quotes "         |||
[Compicated table]



The allocation given by theses l but is not necesary strick because there area flexibilite rules


This project aims to determine which factor determine the number of classroom in schools. We show:
- The contribution to each factor for the numbers of classroom.
- Which features are more important in determining the classroom.

The main goal of this project is



# Use of Case
_"Predict the number of classroom in the schools to determine the teacher allocation and budget"_


# Scope of the project
For now, the scope of the project is for kindergarten and primary schools managed by the Ministry of Education.



# Steps to replicate
1. **Download the data:** Please clic [here](https://1drv.ms/u/s!AodhAFTTDqU00U8a53GPrtoVbxtH?e=cvotnC) to download the data. If you need a password contact with the administrators. Then, copy the data and paste en in the file 'Raw Data' and run the srcipt "0 Construccion de la base.py" in the Scripts file.

2. **Descriptive stats** This step is optional but if you want to know more about the data set please run the script "Descriptive stats"



# Requirements
- Python 3 or more
- RAM: 6 GB  



# Libraries
- Pandas
- Numpy
- Sklearn
- Path
