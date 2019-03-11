#Commnands to run each time I make changes. I have added here so I only have to run this file and it will do the rest.
git add .
git commit -m'New publication'
git push origin dev
pelican content -s publishconf.py
ghp-import output -b master
git push origin master 
