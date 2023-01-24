rd build /Q /S
rd dist /Q /S
rd pywxwork.egg-info /Q /S

python setup.py sdist build
twine upload dist/*


rd build /Q /S
rd dist /Q /S
rd pywxwork.egg-info /Q /S

clear
