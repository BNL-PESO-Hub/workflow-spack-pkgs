# CI Recipes for Workflow Tools Built with Spack

Use provided GitHub Actions workflow recipes (`.github/workflows/*.yml`) to build and run CI pipelines for workflow tools. They all use the same `spack-base.yml` workflow template, with different parameters for each tool.

## Supported Workflow Tools

### PSI/J: Portable Submission Interface for Jobs

Spack recipe: https://packages.spack.io/package.html?name=py-psij-python  
PyPI: https://pypi.org/project/psij-python/  
Documentation: https://exaworks.org/psij-python/

**Description:** PSI/J is a portable job submission and execution API for HPC and distributed computing platforms. It provides a simple and flexible interface for defining, submitting, monitoring, and managing jobs across diverse resource managers and execution backends without requiring application modifications.

---

## Legacy Tools/Packages

### RADICAL-Pilot
[![spack-radical-pilot](https://github.com/BNL-PESO-Hub/workflow-spack-pkgs/actions/workflows/spack-radical-pilot.yml/badge.svg)](https://github.com/BNL-PESO-Hub/workflow-spack-pkgs/actions/workflows/spack-radical-pilot.yml)

Spack recipe: https://packages.spack.io/package.html?name=py-radical-pilot  
PyPI: https://pypi.org/project/radical.pilot/  
Documentation: https://radicalpilot.readthedocs.io

**Description:** RADICAL-Pilot is a distributed runtime system and pilot-job framework for executing heterogeneous workloads and large-scale applications on HPC platforms. It decouples resource acquisition from task execution and enables scalable orchestration and execution of heterogeneous tasks across diverse resource managers and execution backends.

