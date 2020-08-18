# InterchainFoundation
Public Repo for Collaboration between Interchain Foundation and BlockScience

# Research Project Scope
Document, Design, and Test an Impact Bond Mechanism to fund outcome driven projects. The Bonds life cycle will account for the (i) pre-conditions and execution of bond initialization, (ii) a set of mechanisms available to participants for continuous funding and attestation regarding project status, and (iii) a close-out plus reconcilation mechanism that accounts for a final verdict on the success of the project, as well as the post-conditions for the system, e.g. impact tokens representing the participation level in a successful project. This design is for a parameterized class of bond mechanisms which may be configured to fit a wide range of circumstances.  

# Methods and Tools
System Requirements and Functional Requirements will be mapped to formally frame the inherently human challenge into a bounded dynamic Mechanism Design problem. The framework for Discrete Event Games as described in [Economic Games as Estimators](https://epub.wu.ac.at/7433/1/zargham_paruch_shorish.pdf) will be applied. The Impact Bonds will be more advanced variations of Bonding Curves, see [From Curved Bonding to Configuration Spaces](https://epub.wu.ac.at/7385/1/zargham_shorish_paruch.pdf). While initial designs will be analytical in nature, the computer aided design process is iterative. The [cadCAD](https://github.com/cadCAD-org/cadCAD) modeling software will be applied to develop a computational model of the mechanisms by following [cadCAD best practices](https://github.com/cadCAD-org/cadCAD/tree/master/documentation). The model will be used for failure mode analysis, sensitivity analysis and other design validation procedures prior to implementation.

# Summary of Work
- Use Case Research - Interviewing and gathering requirements from the impact investment space ~*complete*
- Converting business requirements and user stories into formal functional requirements for the bond mechanism ~*complete*
- Preliminary Algorithm Design - Mathematical Derivations ~*complete*
- Initial Implementation of cadCAD model ~*complete*
- Design Iterations based on computational experiments ~*active*
- Recommendations for Proper use: conditions for using the design and parameter guidelines ~*active*
- Support partner during implementation ~*active*

# Implementation Partner
BlockScience is further collaborating with ixo, to implement the impact bond primitive as part of the Cosmos SDK. We believe it will provide great value within the Sustainability Hub and beyond.

# Phase 1 Deliverables
- [Problem Statement and Methodology](Paper/0_ProblemStatementandMethodology.md) - Understand what problem we are trying to solve and what methodology we intend to utilize in order to solve it
- [Ecosystem Roles](Paper/1_EcosystemRoles.md) - Identify all of the various roles users can take in the ecosystem
- [Bond Lifecycle Phases](Paper/2_BondLifecyclePhases.md) - Identify each phase in the bond lifecycle
- [Engineering Requirements](Paper/3_EngineeringRequirements.ipynb) - Define formal mathematical definitions and requirements for the ecosystem

# Phase 2 Deliverables
- [Math Specification](Math_Specification) - Mathematical documentation of the model including system and component specifications as well as behavioural models of agents
- [cadCAD Model Source Code](src) - Source code of the model built in cadCAD
- [Simulation Notebook and Explanatory Results](main.ipynb) - Representative simulation notebook validating that the model meets core system properties
- [Component Validation Tests](tests) - Other supporting validation tests (varying granularity, agent beliefs, etc.)
- [Preliminary (WIP) Modular SDK Specification Mapping](https://hackmd.io/nV1Dkx_BS12mNKEjL1wMJg?view) - Template framework for documenting and implementing an SDK module using the BlockScience Systems Engineering modeling specification.
    - [Risk Prediction Module](https://hackmd.io/pBdH1OedQLuvhQU0ezTttA?view)
- [Preliminary (WIP) Phase 3 Test Plan](https://docs.google.com/spreadsheets/d/1xdiogvWU_NP2PGOTVK6V2rl642u56y26nMKQznGaO1o/edit#gid=0) - Initial planning around experiments to be performed in Phase 3
