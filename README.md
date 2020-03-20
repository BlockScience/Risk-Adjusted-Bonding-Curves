# InterchainFoundation
Public Repo for Collaboration between Interchain Foundation and BlockScience

# Research Project Scope
Document, Design, and Test an Impact Bond Mechanism to fund outcome driven projects. The Bonds life cycle will account for the (i) pre-conditions and execution of bond initialization, (ii) a set of mechanisms available to participants for continuous funding and attestation regarding project status, and (iii) a close-out plus reconcilation mechanism that accounts for a final verdict on the success of the project, as well as the post-conditions for the system, e.g. impact tokens representing the participation level in a successful project. This design is for a parameterized class of bond mechanisms which may be configured to fit a wide range of circumstances.

Begin by reading the [Problem Statement and Methodology](Paper/0_Summary.md).

# Methods and Tools
System Requirements and Functional Requirements will be mapped to formally frame the inherently human challenge into a bounded dynamic Mechanism Design problem. The Framework for Discrete Event Games as described in [Economic Games as Estimators](https://epub.wu.ac.at/7433/1/zargham_paruch_shorish.pdf) will be applied. The Impact Bonds will be more advanced variations of Bonding Curves, see [From Curved Bonding to Configuration Spaces](https://epub.wu.ac.at/7385/1/zargham_shorish_paruch.pdf). While initial designs will be analytical in nature, the computer aided design process is iterative. The [cadCAD](https://github.com/BlockScience/cadCAD/tree/master/cadCAD) modeling software will be applied to develop a computational model of the mechanisms. The model will be used for failure mode analysis, sensitivity analysis and other design validation procedures prior to implementation.

# Summary of Work
- Use Case Research - Interviewing and gathering requirements from the impact investment space ~*active*
- Converting business requirements and user stories into formal functional requirements for the bond mechanism ~*active*
- Preliminary Algorithm Design - Mathematical Derivations
- Initial Implementation of cadCAD model
- Design Iterations based on computational experiments
- Recommendations for Proper use: conditions for using the design, and parameter guidelines
- Support partner during implementation 

# Implementation Partner
BlockScience is further collaborating with IXO, to implement the impact bond primitive as part of the Cosmos SDK. We believe it will provide great value within the Sustainability Hub and beyond.
