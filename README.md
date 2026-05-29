# CI Recipes for Workflow Tools Built with Spack

Use provided GitHub Actions workflow recipes (`.github/workflows/*.yml`) to build and run CI pipelines for workflow tools. They all use the same `spack-base.yml` workflow template, with different parameters for each tool.

## Supported Workflow Tools

| Tool | CI Status | Spack |
| :--- | :--- | :--- |
| [PSI/J: Portable Submission Interface for Jobs](#psij-portable-submission-interface-for-jobs) | [![spack-psij](https://github.com/BNL-PESO-Hub/workflow-spack-pkgs/actions/workflows/spack-psij.yml/badge.svg)](https://github.com/BNL-PESO-Hub/workflow-spack-pkgs/actions/workflows/spack-psij.yml) | [![spack](https://img.shields.io/spack/v/py-psij-python)](https://packages.spack.io/package.html?name=py-psij-python) |

### PSI/J: Portable Submission Interface for Jobs

Spack recipe: https://packages.spack.io/package.html?name=py-psij-python  
PyPI: https://pypi.org/project/psij-python/  
Documentation: https://exaworks.org/psij-python/

**Description:** PSI/J is a portable job submission and execution API for HPC and distributed computing platforms. It provides a simple and flexible interface for defining, submitting, monitoring, and managing jobs across diverse resource managers and execution backends without requiring application modifications.

---

## Legacy Tools/Packages

| Tool | CI Status | Spack |
| :--- | :--- | :--- |
| [RADICAL-Pilot](#radical-pilot) | [![spack-radical-pilot](https://github.com/BNL-PESO-Hub/workflow-spack-pkgs/actions/workflows/spack-radical-pilot.yml/badge.svg)](https://github.com/BNL-PESO-Hub/workflow-spack-pkgs/actions/workflows/spack-radical-pilot.yml) | [![spack](https://img.shields.io/spack/v/py-radical-pilot)](https://packages.spack.io/package.html?name=py-radical-pilot) |
| [RADICAL-EnTK](#radical-entk) | [![spack-radical-entk](https://github.com/BNL-PESO-Hub/workflow-spack-pkgs/actions/workflows/spack-radical-entk.yml/badge.svg)](https://github.com/BNL-PESO-Hub/workflow-spack-pkgs/actions/workflows/spack-radical-entk.yml) | [![spack](https://img.shields.io/spack/v/py-radical-entk)](https://packages.spack.io/package.html?name=py-radical-entk) |

### RADICAL-Pilot

Spack recipe: https://packages.spack.io/package.html?name=py-radical-pilot  
PyPI: https://pypi.org/project/radical.pilot/  
Documentation: https://radicalpilot.readthedocs.io

**Description:** RADICAL-Pilot is a distributed runtime system and pilot-job framework for executing heterogeneous workloads and large-scale applications on HPC platforms. It decouples resource acquisition from task execution and enables scalable orchestration and execution of heterogeneous tasks across diverse resource managers and execution backends.

### RADICAL-EnTK

Spack recipe: https://packages.spack.io/package.html?name=py-radical-entk  
PyPI: https://pypi.org/project/radical.entk/  
Documentation: https://radicalentk.readthedocs.io

**Description:** RADICAL-EnTK (Ensemble Toolkit) is a Python framework for developing and executing large-scale ensemble-based workflows on high-performance computing (HPC) systems. It provides high-level abstractions—pipelines, stages, and tasks—that allow users to describe application logic independently of resource management and execution details. EnTK uses RADICAL-Pilot as its runtime system, which handles resource acquisition, scheduling, and task execution on heterogeneous HPC platforms. This separation enables users to focus on workflow structure while delegating execution management to the underlying runtime.


