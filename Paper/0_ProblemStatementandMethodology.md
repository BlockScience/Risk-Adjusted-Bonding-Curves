# Problem Statement and Methodology

### Background Info: Bonding Curves
Token bonding curves are continuous liquidity mechanisms which are used in market design for cryptographically-supported token economies whereby tokens are automatically issued using buy and sell functions. 

### Problem: Static Bonding Curves are Insufficient
Current token bonding curve implementations act as automated market makers for initial and ongoing investment. However, they generally are static, with fixed *a priori* assumptions about the interaction between the token economy <a href="https://github.com/BlockScience/InterchainFoundation/blob/shruti-definitions/Paper/glossary.md#note1ref" id="note1ref"><sup>1</sup></a> and its external factors. 
<br/><br/> 
Since these bonding curve implementations are static, they cannot incorporate external risk factors during live execution. This results in pricing and supply anomalies, such as tokens being misallocated on both buy-side and sell-side, with loss in risk correlation. 
<br/><br/> 
Ultimately, risk remains poorly mitigated, and investors do not receive a fair return on investment.
Systems with compound economic mechanisms (e.g. staking deposits also being used as debt collateral) contain interdependencies that produce non-linear effects. In the case of static bonding curves, risk accumulates in a non-linear fashion which can lead to systemic collapse.

### Solution: Risk adjusted bonding curves 
The goal here is to design a bonding curve implementation that will dynamically adapt to changing risks over time. If a mapping is made between 1) how external events affect the risk distribution, and 2) how the resulting risk distribution affects the token bonding curve, then a parametric class of token bonding curves can be created that adapts its underlying parameters to external events.

### Use case:
In this project we aim to provide a generalized reusable economic design pattern for a risk adjusted bonding curve. However, in order to maintain practicality, we have chosen to anchor the design in a motivating use case: tokenized social impact bonds in the ixo ecosystem. 

A social impact bond is a type of bond where repayment to investors is contingent on the bond's success in achieving certain pre-specified social impact objectives. Impact bonds therefore transfer the operational risks of a development intervention to capital investors. In return, these investors receive financial returns as compensation for the risks, so long as the bond achieves the predetermined outcomes. Traditional impact bonds typically have set terms for duration, coupon value, and performance triggers. Additionally, bonds are only issued after the full capital has been secured. Traditional impact bonds require a conviction that the operational risks will be kept within acceptable limits. These risks result in underwriting costs based on assumptions that may or may not hold true.

ixo is intending to overcome many of the flaws with traditional impact bonds by designing an adaptive impact financing mechanism called an alpha-bond, which will utilize a risk adjusted bonding curve. 

The bonding curve will issue and burn tokens according to the investor's buy and sell decisions. The token price will be governed by the bonding curve which is influenced by aggregated investor decisions. Since the system will employ a risk adjusted bonding curve, there exists a parameter, alpha, which will predict the bond's likelihood of success based on internal and external inputs. Alpha will change as the bond participants issue claims, demonstrating progress towards the impact objectives, or disputes, disputing those claims. The bonding curve thus will act as an estimator of market price and the bond's likelihood of success.

alpha-Bonds are currently being implemented for high-profile development projects for improving the quality of primary school education in India. 

### Methodology
In the following paper, we demonstrate our entire economic engineering process from discovery and formulating business and engineering requirements to arriving at a suitable mathematical model to be input into a simulation. 

Systems Engineering is a process that integrates the technical effort within a managed project to transform an operational need, or user's requirement, into a description of systems performance parameters and systems configuration. When implemented early in the design process, systems engineering ensures that the total system is efficient, cost-effective, operable, reliable, and maintainable. In addition to a fully integrated engineering effort and an established definition of system operating parameters, the customer also gains these benefits:

The design is conducted on a total system basis which incorporates other requirements.
A means is provided for evaluating changes which affect the overall system performance.
A framework of coherent system requirements exists that will be used as performance, design, and test criteria, further, these criteria serve as source data for specifications, tests, contract work statements, and documentation.
A means of documenting technical decisions made during the course of the program is available to managers.

#### Design Phase 1: Requirements
A collaborative effort of the business and technical teams, through facilitated discussions, is necessary in order to define and analyze the ecosystem scope, program plan, role taxonomies, program phasing requirements, and system requirements. Requirements analysis will address customer expectations, project and enterprise constraints, external constraints, operational scenarios, measures of effectiveness/suitability; and will extend to system boundaries<a href="glossary.md#note49" id="note49ref"><sup>49</sup></a>, interfaces, utilization environments, life cycle process outputs, functional requirements, performance requirements, modes of operation, and human factors. At the conclusion of this phase, all requirements - business requirements, system requirements<a href="glossary.md#note46" id="note46ref"><sup>46</sup></a>, operational requirements<a href="glossary.md#note48" id="note48ref"><sup>48</sup></a>, and functional requirements<a href="glossary.md#note47" id="note47ref"><sup>47</sup></a> - must be clear, concise, correct, and complete in order to create a strong foundation for subsequent design phases. 

The culmination of this first phase of design effort produced the following deliverables:
1. [Ecosystem Roles](1_EcosystemRoles.md)
1. [Bond Lifecycle Phases](2_BondLifecyclePhases.md)
1. [Engineering Requirements](3_EngineeringRequirements.md)

#### Design Phase 2: System Design
The system model will incorporate system requirement aspects, including stakeholder goals, purposes, and success conditions for the system. Specification will incorporate black box behavior and characteristics, specifically what the system has to do to meet the requirements, the transformations of inputs to outputs (functional/activity models), and state/mode­based behavioral differences (state models). The structure of the model will include the parts that exhibit the behavior and the component hierarchy, elements, and stores. The properties of the model are the performance, physical characteristics, and governing rules that constrain the structure and behavior. The interconnections of the model are the way the structural elements arrange and communicate to achieve the required behavior under the given constraints. Component level mathematical specifications precisely characterizing the systems mechanisms, allowed action spaces for users of all roles, and any explicit reachable subspace proofs will be provided.

#### Design Phase 3: Validation
Simulation techniques may involve discrete differential equations, Monte Carlo methods and Markov chains to provide the numerical experiments necessary to validate the design. This process involves developing a custom battery of system level tests which correspond to system requirements, through an implementation of deterministic and stochastic processes. User behavior models will be derived strategies including but not limited to rational best response irrational antagonism, and random actions.

Continue reading Chapter 1: [Ecosystem Roles](1_EcosystemRoles.md)
