step 1: create environment
conda create -p venv python==3.9

step 2: Activate the environment
conda Activate venv/

step 3: create a github repo

step 4: initialize git by using following command
git init

step 5: add readme file
git add readme.md

step 6: commit
git commit -m "first commit" 

step 7: create main branch
git branch -M main
git branch

step 8: add origin
git remote add origin https://github.com/rohit-gupta99939/ml_project.git

step 9: push into git
git push -u origin main

step 10: go to github wesite and create gitignore file and select python as template

step 11: git pull to pull git ignore file.
git pull origin main

step 12: create requriment.txt file.
run folloing command to install requirments
pip install -r requirment.txt

step 13: create setup.py folder
write setup() function inside it.

step 14: create src folder and create __init__.py file
run python python setup.py install

step 15: save everithing git
git add.
git push origin main

step 16: create template.py file
run python template.py

step 17: write code inside src/mlproject/logging.py and exception.py and app.py
run 
python app.py

step 18: git hub add .
git commit -m "logging and exception code writen"
git push origin main


