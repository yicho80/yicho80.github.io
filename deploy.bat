del /q /f output
pelican content
ghp-import -m "Generate Pelican site" -b master output
git push origin master