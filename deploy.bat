del /q /f /s output
pelican content -s publishconf.py
ghp-import -m "Generate Pelican site" -b master output
git push origin master