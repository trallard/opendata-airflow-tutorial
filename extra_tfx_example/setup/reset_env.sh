# Use this to completely nuke the pypi libraries that TFX requires
# and start with a 'clean' environment.  This will uninstall TF/TFX
# libraries and airflow libraries.
#
# It will not delete the Airflow install itself.  You'll want to delete
# ~/airflow on your own.
#


GREEN=$(tput setaf 2)
NORMAL=$(tput sgr0)

printf "${GREEN}Resetting TFX workshop${NORMAL}\n\n"

pip uninstall tensorflow
pip uninstall tfx
pip uninstall tensorflow-model-analysis
pip uninstall tensorflow-data-validation
pip uninstall tensorflow-metadata
pip uninstall tensorflow-transform
pip uninstall apache-airflow

printf "\n\n${GREEN}TFX workshop has been reset${NORMAL}\n"
printf "${GREEN}Remember to delete ~/airflow${NORMAL}\n"

