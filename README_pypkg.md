[![CI - main](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/main.yaml/badge.svg)](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/main.yaml)
[![CI - docs](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/deploy-docs.yaml/badge.svg?branch=main)](https://github.com/nfdi4cat/pid4cat-model/actions/workflows/deploy-docs.yaml)
[![PyPI - Version](https://img.shields.io/pypi/v/pid4cat)](https://pypi.org/project/pid4cat)
[![DOI](https://zenodo.org/badge/598213054.svg)](https://zenodo.org/badge/latestdoi/598213054)

# Python package for pid4cat persistent identifiers

The package helps to interface the **pid4cat service**, a service offered by NFDI4Cat for metadata rich, universal persistent identifiers.
pid4cat builds upon the handle-system (as DOIs do). pid4cat adds a **custom API** to a handle server and provides a **LinkML model for  PID-related metadata**.
The metadata are stored in the handle records.

This Python package includes an equivalent Python (pydantic) model of the LinkML-based datamodel for the metadata of pid4cat identifiers.
It moreover includes some helpers to make simplify using the pid4cat identifiers.

## Documentation

- [pid4cat Python package](https://nfdi4cat.github.io/pid4cat-model/latest/tools/) metadata schema documentation

## Contributors

See main [README](https://github.com/nfdi4cat/pid4cat-model/blob/main/README.md).

## License

The pid4cat Python package is distributed under the MIT license.

## Acknowledgement

This project started as an in-kind contribution of [Leibniz-Institut für Katalyse e.V.](https://www.catalysis.de) (Rostock, Germany) to the NFDI4Cat project.

After 2024-03-27 this work has been funded by the German Research Foundation (DFG) through the project "[NFDI4Cat](https://www.nfdi4cat.org) - NFDI for Catalysis-Related Sciences" (DFG project no. [441926934](https://gepris.dfg.de/gepris/projekt/441926934)), within the National Research Data Infrastructure ([NFDI](https://www.nfdi.de)) programme of the Joint Science Conference (GWK).
