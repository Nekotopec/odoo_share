# There is custom module for odoo that allows to share files.
### A user who has admin rights can upload files to server. Every user can get access 
### to any file by link and download it.

## Start service

1. Clone this repository   
`git clone git@github.com:Nekotopec/odoo_share.git`   
2. Change current directory to odoo_share   
`cd odoo_share/`   
3. Start docker-compose   
`docker-compose up --build -d`   
It will set up server on http://localhost:8069.  
4. Create database and admin user account following the instructions.      
5. Install nekotopec_share app in standard app's menu.  

After the installation you will get two new menu items "OdooShare_nekotopec" and 
"OdooShare_nekotopec_view_files". Use the first menu item for uploading new 
files to database. Use the second menu item to view the list of uploaded files.