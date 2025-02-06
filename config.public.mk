# config.public.mk

# This file is public in git. No sensitive info allowed.
# These variables are sourced in justfile and/or Makefile..

###### schema definition variables, used by justfile/Makefile

# Note: 
# - just works fine with quoted variables of dot-env files like this one
# - make does not support standard dot-env files. If you use make remove the quotes.
#   see also https://github.com/linkml/linkml-project-cookiecutter/issues/106
LINKML_SCHEMA_NAME="pid4cat_model"
LINKML_SCHEMA_AUTHOR="David Linke <david.linke@catalysis.de>"
LINKML_SCHEMA_DESCRIPTION="LinkML model for handle-based PIDs for resources in catalysis (pid4cat)"
LINKML_SCHEMA_SOURCE_PATH="src/pid4cat_model/schema/pid4cat_model.yaml"
LINKML_SCHEMA_GOOGLE_SHEET_MODULE="personinfo_enums"
LINKML_SCHEMA_GOOGLE_SHEET_ID=""
LINKML_SCHEMA_GOOGLE_SHEET_TABS="personinfo enums"
LINKML_USE_SCHEMASHEETS=No

###### linkml generator variables, used by justfile/Makefile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS=

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile rdfs)
LINKML_GENERATORS_OWL_ARGS=

## pass args to trigger experimental java/typescript generation
LINKML_GENERATORS_JAVA_ARGS=
LINKML_GENERATORS_TYPESCRIPT_ARGS=
