# Economic Engineering of Risk Adjusted Impact Bonds

### Impact bonds
A social impact bond is a type of bond where repayment to investors is contingent on the bond's success in achieving certain pre-specified social impact objectives. 

### Bonding curves
A bonding curve is a mechanism for distribution of blockchain tokens, in which tokens are automatically issued using buy and sell functions. 
The impact bond bonding curve is parametrically adjusted to mitigate risk, thereby adapting to external events. 

### Problem: Static bonding curves
Current token bonding curve implementations act as automated market makers for initial and ongoing investment. However, they generally are static, with fixed *a priori* assumptions about the interaction between the token economy and its external factors. 
<br/><br/> 
Since these bonding curve implementations are static, they cannot incorpoate external risk factors during live execution. This results in pricing and supply anomalies, such as tokens being misallocated on both buy-side and sell-side, with loss in risk correlation. 
<br/><br/> 
Ultimately, risk remains poorly mitigated, and investors do not receive a fair return on investment.
Systems with compound economic mechanisms (e.g. staking deposits also being used as debt collateral) contain interdependencies that produce non-linear effects. In the case of static bonding curves, risk accumulates in a non-linear fashion which can lead to systemic collapse.

### Solution: Risk Adjusted Bonding Curve for Impact Bonds
The goal of this project is to provide a generalized reusable economic design pattern for outcome dependent funding. 
To maintain practicality, we have anchored it in a motivating use case of alpha-Bonds in the ixo ecosystem. 
alpha-Bonds are currently being implemented for high-profile development projects for improving the quality of primary school education in India. 
<br/><br/> 
The system consists of several impact investors who invest in impact bonds containing social good projects and receive a return contingent on the project's degree of success. 
A bonding curve issues and burns tokens according to the investor's buy and sell decisions. The token price is governed by the bonding curve which is influenced by aggregated investor decisions. Since the system employs a risk-adjusted bonding curve, there exists a parameter alpha which predicts the bond's likelihood of success based on internal and external inputs. Alpha changes as the bond participants issue claims or disputes towards the bond or its constituent projects.
<br/><br/> 
The bonding curve thus acts as an estimator of market price and the bond's likelihood of success, alpha.

In the following paper, we demonstrate our entire economic engineering process from discovery and formulating business and engineering requirements to arriving at a suitable mathematical model to be input into a simulation. 

### Methodology
Systems Engineering is a process that integrates the technical effort within a managed project to transform an operational need, or user's requirement, into a description of systems performance parameters and systems configuration. When implemented early in the design process, systems engineering ensures that the total system is efficient, cost-effective, operable, reliable, and maintainable. In addition to a fully integrated engineering effort and an established definition of system operating parameters, the customer also gains these benefits:

The design is conducted on a total system basis which incorporates other requirements.
A means is provided for evaluating changes which affect the overall system performance.
A framework of coherent system requirements exists that will be used as performance, design, and test criteria, further, these criteria serve as source data for specifications, tests, contract work statements, and documentation.
A means of documenting technical decisions made during the course of the program is available to managers.

#### Design Phase 1 Requirements
A collaborative effort of the business and technical teams, through facilitated discussions, is necessary in order to define and analyze the ecosystem scope, program plan, role taxonomies, program phasing requirements, and system requirements. Requirements analysis will address customer expectations, project and enterprise constraints, external constraints, operational scenarios, measures of effectiveness/suitability; and will extend to system boundaries, interfaces, utilization environments, life cycle process outputs, functional requirements, performance requirements, modes of operation, and human factors. At the conclusion of this phase, all requirements business and systems­ must be clear, concise, correct, and complete in order to create a strong foundation for subsequent design phases.

The culmination of this first phase of design effort produced the following deliverables:
1. [Ecosystem Scope](1_Ecosystem.md)
1. [Finite State Machine](2_FiniteStateMachine.md)
1. [System Requirements](3_EngineeringRequirements.md)

#### Design Phase 2­ System Design
The system model will incorporate system requirement aspects, including stakeholder goals, purposes, and success conditions for the system. Specification will incorporate black box behavior and characteristics, specifically what the system has to do to meet the requirements, the transformations of inputs to outputs (functional/activity models), and state/mode­based behavioral differences (state models). The structure of the model will include the parts that exhibit the behavior and the component hierarchy, elements, and stores. The properties of the model are the performance, physical characteristics, and governing rules that constrain the structure and behavior. The interconnections of the model are the way the structural elements arrange and communicate to achieve the required behavior under the given constraints. Component level mathematical specifications precisely characterizing the systems mechanisms, allowed action spaces for users of all roles, and any explicit reachable subspace proofs will be provided.

#### Design Phase 3 Validation
Simulation techniques may involve discrete differential equations, Monte Carlo methods and Markov chains to provide the numerical experiments necessary to validate the design. This process involves developing a custom battery of system level tests which correspond to system requirements, through an implementation of deterministic and stochastic processes. User behavior models will be derived strategies including but not limited to rational best response irrational antagonism, and random actions.

Continue reading Chapter 1: [Ecosystem Scope](1_Ecosystem.md)
