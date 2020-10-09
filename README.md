# Alpha Bonds: Risk-Adjusted Bonding Curves
## Ethical FinTech for Social Impact
<br>

This research project explores the formalized design of cryptoeconomic mechanisms to be used in a novel impact bond, called **Alpha Bonds**. This tool **composes bonding curve + prediction market functionality to improve risk assessment** for funding outcome-based social impact projects.

The outcome of this initiative is a digital twin cadCAD model, which can inform the implementation of this new impact bond primitive as part of the Cosmos SDK. We believe it will provide great value within the Sustainability Hub and beyond.


## Implementation Partners
---

This project is a collaboration of mutual interest between the Interchain Foundation, the ixo Foundation, and BlockScience. 

Motivations:
* **Interchain Foundation:** funding robust tooling primitives for the Cosmos SDK
* **ixo Foundation:** seeking to build novel impact funding tools to improve existing options for real world impact
* **BlockScience:** expanding an open source library of high leverage components using rigorous design & modeling processes and tools

![logos](https://i.imgur.com/9Xc0R63.jpg)

<br>

# Project Breakdown

This project is being carried out in 3 phases: 
* **Phase 1. Engineering Requirements Gathering** [*complete*]
* **Phase 2. Formalized Specification** [*complete*]
* **Phase 3. Analysis & Testing** [*in progress*]

Each phase is broken out into a series of deliverables as listed below, which are collated into a stakeholder report at the completion of each phase.

## Phase 1 Deliverables:  Requirements Gathering
* **1.1 [Problem Statement and Methodology](Paper/0_ProblemStatementandMethodology.md)** - Understand what problem we are trying to solve and what methodology we intend to utilize in order to solve it

* **1.2 [Ecosystem Roles](Paper/1_EcosystemRoles.md)** - Identify all of the various roles users can take in the ecosystem

* **1.3 [Bond Lifecycle Phases](Paper/2_BondLifecyclePhases.md)** - Identify each phase in the bond lifecycle

* **1.4 [Engineering Requirements](Paper/3_EngineeringRequirements.ipynb)** - Define formal mathematical definitions and requirements for the ecosystem

## Phase 2 Deliverables: Specification
* **2.1 [Math Specification](Math_Specification)** - Mathematical documentation of the model including system and component specifications as well as behavioural models of agents
* **2.2 [cadCAD Model Source Code](src)** - Source code of the model built in cadCAD
* **2.3 [Simulation Notebook and Explanatory Results](main.ipynb)** - Representative simulation notebook validating that the model meets core system properties
* **2.4 [Component Validation Tests](tests)** - Other supporting validation tests (varying granularity, agent beliefs, etc.)
* **2.5 [Preliminary (WIP) Modular SDK Specification Mapping](https://hackmd.io/nV1Dkx_BS12mNKEjL1wMJg?view)** - Template framework for documenting and implementing an SDK module using the BlockScience Systems Engineering modeling specification.
    - [Risk Prediction Module](https://hackmd.io/pBdH1OedQLuvhQU0ezTttA?view)
* **2.6 [Preliminary (WIP) Phase 3 Test Plan](https://docs.google.com/spreadsheets/d/1xdiogvWU_NP2PGOTVK6V2rl642u56y26nMKQznGaO1o/edit#gid=0)** - Initial planning around experiments to be performed in Phase 3


<br>
<br>

# More Project Information

## Summary of Work
- Use Case Research - Interviewing and gathering requirements from the impact investment space ~*complete*
- Converting business requirements and user stories into formal functional requirements for the bond mechanism ~*complete*
- Preliminary Algorithm Design - Mathematical Derivations ~*complete*
- Initial Implementation of cadCAD model ~*complete*
- Design Iterations based on computational experiments ~*active*
- Recommendations for Proper use: conditions for using the design and parameter guidelines ~*active*
- Support partner during implementation ~*active*

<br>


## Scope of Research Initiative
Our goal is to gather requirements, formally specify, document, design, and test an Impact Bond Mechanism to fund outcome driven projects. The Bonds life cycle will account for the (i) pre-conditions and execution of bond initialization, (ii) a set of mechanisms available to participants for continuous funding and attestation regarding project status, and (iii) a close-out plus reconcilation mechanism that accounts for a final verdict on the success of the project, as well as the post-conditions for the system, e.g. impact tokens representing the participation level in a successful project. This design is for a parameterized class of bond mechanisms which may be configured to fit a wide range of circumstances.  

<br>

## Methods and Tools
System Requirements and Functional Requirements will be mapped to formally frame the inherently human challenge into a bounded dynamic Mechanism Design problem. The framework for Discrete Event Games as described in [Economic Games as Estimators](https://epub.wu.ac.at/7433/1/zargham_paruch_shorish.pdf) will be applied. The Impact Bonds will be more advanced variations of Bonding Curves, see [From Curved Bonding to Configuration Spaces](https://epub.wu.ac.at/7385/1/zargham_shorish_paruch.pdf). While initial designs will be analytical in nature, the computer aided design process is iterative. The [cadCAD](https://github.com/cadCAD-org/cadCAD) modeling software will be applied to develop a computational model of the mechanisms by following [cadCAD best practices](https://github.com/cadCAD-org/cadCAD/tree/master/documentation). The model will be used for failure mode analysis, sensitivity analysis and other design validation procedures prior to implementation.

<br>

## Why Model Systems in cadCAD?

In cyber-physical systems like international power grids, global flight networks, or socioeconomic community ecosystems, engineers model **simulated replicas of their system**, called **digital twins**. These models help to manage the complexity of systems that have trillions of data points and are constantly in flux. These simulations channel the information into pathways that allow humans to understand what is going on in their ecosystem at a high level, so they can intervene where and as appropriate. (Like hitting a breaker switch when a fault is cleared in a power system).

![img](https://i.imgur.com/kb4Tnh6.jpg)

Digital twins can be considered like a flight simulator, which can be used to run your system through a billion different "tests", varying one parameter at a time, to see what effects may throw your system out of balance. As engineers with public safety in mind, we must understand the tipping points of our systems, and ensure mechanisms are in place to push the system back towards balance if and when they enter their boundary conditions of safety.

<br>


## What is cadCAD?
cadCAD (complex adaptive dynamics Computer-Aided Design) is a python based modeling framework for research, validation, and Computer Aided Design of complex systems. Given a model of a complex system, cadCAD can simulate the impact that a set of actions might have on it. This helps users make informed, rigorously tested decisions on how best to modify or interact with the system in order to achieve their goals. cadCAD supports different system modeling approaches and can be easily integrated with common empirical data science workflows. Monte Carlo methods, A/B testing and parameter sweeping features are natively supported and optimized for.

cadCAD links for more information:
* https://community.cadcad.org/t/introduction-to-cadcad/15
* https://community.cadcad.org/t/putting-cadcad-in-context/19
* https://github.com/cadCAD-org/demos

<br> 

## Model Reproducibility
In order to reperform this code, we recommend the researcher use the following link https://www.anaconda.com/products/individual to download Python 3.7. To install the specific version of cadCAD this repository was built with, run the following code:
pip install cadCAD==0.4.23

Then run cd InterchainFoundation to enter the repository. Finally, run jupyter notebook to open a notebook server to run the various notebooks in this repository.

Check out the [cadCAD forum](https://community.cadcad.org/t/python-newbies-setup-for-cadcad/101) for more information about installing and using cadCAD.

<br>