# Risk-Adjusted Bonding Curves: An R&D Initiative


This research project explores the design of cryptoeconomic mechanisms **composing functionality from bonding curves + prediction markets**, the first formalized instance of a dynamic bonding curve.  This risk-adjusted bonding curve will be used to provide dynamic risk assessment for funding outcome-based social impact projects as part of a novel impact finance tool - **Alpha Bonds**.

The outcome of this initiative is a digital twin cadCAD model, which can inform the implementation of this new dynamic bonding curve functionality as part of the Cosmos SDK. We believe it will provide great value within the Sustainability Hub and beyond, into the first use case of dynamic bonding curves for social impact.


## Implementation Partners
---

This project is a collaboration of mutual interest between the [Interchain Foundation](https://interchain.io/), the [ixo Foundation](https://ixo.foundation/), and [BlockScience](https://block.science/). 

Motivations:
* **Interchain Foundation:** funding robust tooling primitives for the Cosmos SDK
* **ixo Foundation:** building novel impact funding tools to improve financing options for real world impact
* **BlockScience:** expanding an open source library of modeled cryptoeconomic components using rigorous design processes and tools

![logos](https://i.imgur.com/9Xc0R63.jpg)

<br>

# **Background Info: Bonding Curves**

Token bonding curves are continuous liquidity mechanisms which are used in market design for cryptographically-supported token economies whereby tokens are automatically issued using buy and sell functions. Read more about [bonding curves at a high level](https://yos.io/2018/11/10/bonding-curves/), jump into a [technical deep-dive](https://medium.com/commonsstack/deep-dive-augmented-bonding-curves-b5ca4fad4436) or dig into their [mathematical formalization](https://epub.wu.ac.at/7381/1/zargham_shorish_paruch.pdf).
<br>

![img](https://i.imgur.com/Q0IJGXM.png)
<br>
## **Problem: Static Bonding Curves are Insufficient**
Current token bonding curve implementations act as automated market makers for continuous investment. However, they generally are static, with fixed *a priori* assumptions about the interaction between the token economy <a href="https://github.com/BlockScience/InterchainFoundation/blob/shruti-definitions/Paper/glossary.md#note1ref" id="note1ref"><sup>1</sup></a> and its external factors. 
<br/><br/> 
Since these bonding curve implementations are static, they **cannot incorporate external risk factors** during live execution. This results in pricing and supply anomalies, such as tokens being misallocated on both buy-side and sell-side, with loss in risk correlation. 
<br/><br/> 
Systems with compound economic mechanisms (e.g. staking deposits also being used as debt collateral) contain interdependencies that produce non-linear effects. In the case of static bonding curves, **risk accumulates in a non-linear fashion which can lead to systemic collapse**.
<br><br>

## **Solution: Dynamic Bonding Curves**
The goal of this R&D initiative is to design a bonding curve implementation that will dynamically adapt to changing risks over time, with a  parameter $alpha$ that is determined by the prediction mechanism. This prediction mechanism formally maps how external events affect the risk distribution, and thus how the resulting risk distribution affects the shape of the bonding curve, while preserving invariants. This **'Risk-Adjusted Bonding Curve'** is one instance of a new class of token bonding curves that can adapt their underlying parameters to external events - **Dynamic Bonding Curves**. 

In the next section, we will look at these new types of bonding curves more closely.

<br><br>

# Risk-Adjusted Bonding Curves: A Deeper Look

Risk-Adjusted Bonding Curves (RABCs) are composed of four mechanisms: two bonding curve mechanisms (bond-to-mint & burn-to-withdraw), and two prediction mechanisms (attest-positive  & attest-negative) to predict project success & failure.  The invariant properties of these mechanisms can be seen below, and their in-depth mathematical derivation can be found in the [invariant derivation notebook](Math_Specification/2_Invariants.ipynb) produced in Phase 2.


![img](https://i.imgur.com/I7nWzOW.png)


![img](https://i.imgur.com/FYTsahB.png)

As mentioned in the slides above, agents may choose to participate in just the bonding curve, or the bonding curve and the prediction market. Tokens minted through the bonding curve can be burned back to the curve to reclaim collateral, but note that once tokens are attested towards project success or failure, they cannot be unattested and burned or re-cast. However, an agent may attest both positively and negatively with subsequent actions, denoting a change of agent sentiment towards a project's chances of success.

The diagram below demonstrates how the alpha coefficient is updated through agent attestations in the prediction mechanism.

![img](https://i.imgur.com/AnxLa0x.png)

The prediction market avoids the Keynesian Beauty Contest problem (also called "vote memeing", or voting with the crowd) through the **'Heavy Underdog' property**, which is the same reason you might bet on a severely outmatched team in the playoffs if you think they are going to win - because the payout is worth it to vote accurately according to your belief. With a bonding curve as your bookie, the odds are updated with each transaction - **making these tools essentially [estimators](https://epub.wu.ac.at/7433/1/zargham_paruch_shorish.pdf) of collective sentiment**, a powerful new tool in the Token Engineering toolkit.
<br><br>

![img](https://i.imgur.com/G0io8OV.png)

Alpha can be considered a probability of project success, ranging from 0-100%. This parameter is set according to a dynamic average consensus of all prediction market participants, and serves as a "wisdom of the crowd" measure to surface an estimation of project risk to funders & decision makers. 

Varying alpha impacts the shape of the bonding curve and thus the price of the token, as well as the reserve ratio. This is explained in mathematical detail in the [System Specification notebook](Math_Specification/1_System_Specification.ipynb).  In this model, a lower alpha denotes lower confidence in project success, which increases the collateralization of the bonding curve to reduce risk for participants.

<br>

# Use case: Alpha Bonds
## **Dynamic Bonding Curves for Effective Social  Impact**
<br>

**The Challenge:**
* Traditional Social & Development Impact Bonds lack transparency of the risk involved in a given project. This deters investors, increases the costs of borrowing funds, and raises the barrier to successful impact interventions. 

**The Opportunity:**
* Alpha Bonds dynamically price impact bonds according to a risk coefficient that adjusts to information via a built-in prediction mechanism. This increases transparency of risk to decision makers and investors, and aligns participant incentives towards project success. 

<br>

In this project we aim to provide a generalized reusable economic design pattern for a risk-adjusted bonding curve. However, in order to maintain practicality, we have anchored the design in a motivating use case: tokenized social impact bonds in the ixo ecosystem - **Alpha Bonds**. 

![img](https://i.imgur.com/YS3g0tS.png)

A social impact bond is a type of bond where repayment to investors is contingent on the bond's success in achieving certain pre-specified social impact objectives. Impact bonds therefore transfer the operational risks of a development intervention to capital investors. In return, these investors receive financial returns as compensation for the risks, so long as the bond achieves the predetermined outcomes. Traditional impact bonds typically have set terms for duration, coupon value, and performance triggers. Additionally, bonds are only issued after the full capital has been secured. Traditional impact bonds require a belief that the operational risks will be kept within acceptable limits. These risks result in underwriting costs based on assumptions that may or may not hold true.

ixo is intending to overcome many of the flaws with traditional impact bonds by designing an adaptive impact financing mechanism called an alpha-bond, which will utilize a risk-adjusted bonding curve. 

The bonding curve will issue and burn tokens according to the investor's buy and sell decisions. The token price will be governed by the bonding curve which is influenced by aggregated investor decisions. Since the system will employ a risk adjusted bonding curve, there exists a parameter, alpha, which will predict the bond's likelihood of success based on internal and external inputs. Alpha will change as the bond participants attest positively or negatively in the prediction mechanism. The bonding curve thus will act as an estimator of market price and the bond's likelihood of success.

Alpha Bonds are currently being implemented for high-profile development projects for improving the quality of primary school education in India. 

![img](https://i.imgur.com/p0RDwAY.png)


<br><br>
## The Benefits of Alpha Bonds

* **For impact projects:** Align participant incentives through collaborative investment & shared benefits
* **For funding bodies & decision makers:** Access real-time risk probability inherent in a given impact project
* **For communities:** Empower local investment in local challenges through standardized, unitized impact financing tools

The benefits of alpha bonds are manyfold. Impact initiatives can use alpha bonds to **align participant incentives and simultaneously earn continuous funding** by allowing communities and beneficiaries to purchase tokens from the bonding curve, thus co-investing in the success of the project. Meanwhile, funding groups or decision makers further afield are provided with a **real-time risk signal** through the prediction mechanism. 

Further benefits of alpha bonds lie in **reducing barriers to funding impact projects**, and also in reducing their necessary scale. Through replicable processes and tools (such as this digital twin model), outcomes-based impact projects can be unitized and operate on much smaller scales, avoiding the difficulties of "too big to fail" projects and their overhead.


<br>

## Alpha Bond Specification

Read more about the [lifecycle stages of an Alpha Bond](Paper/2_BondLifecyclePhases.md) and [what agent roles are involved](Paper/1_EcosystemRoles.md) in our Phase 1 documentation. This [article on risk-adjusted bonding curves](https://medium.com/ixo-blog/risk-adjusted-token-bonding-curves-eb4fffc86bf0) also provides some high-level context for this new impact bond tool, and our [Engineering Requirements notebook](Paper/3_EngineeringRequirements.ipynb) dives into technical detail. 

<br>






## Alpha Bond Settlement & Payout

When a project comes to a close (in either success or failure), the alpha bond resolves to its settlement phase. Payouts from the alpha bond system vary depending on project completion. For a full mathematical derivation of payouts, see the [System Specification notebook](Math_Specification/1_System_Specification.ipynb). A TL;DR is below.

<br>

### 🎉Case 1: Project Success🎉

When a project is completed successfully, the Outcomes Payer provides a lump sum of $C$ dollars to the bonding curve reserve.

The reserve is then split up and paid out according to the proportion of bonding curve tokens that have not been entered into the prediction mechanism ($s_{free}$) and tokens cast towards predicting project success ($s_1$) as a fraction of total token supply ($S$).

**In short, all participants split the pot of outcomes payment and bonding curve reserve proportionally to their token holdings.**

<br>

### 💣Case 2: Project Failure💣

When a project fails, the Outcomes Payer provides no additional funding.

The reserve is then split up and paid out according to the proportion of bonding curve tokens that have not been entered into the prediction mechanism ($s_{free}$) and tokens cast towards predicting project failure ($s_0$) as a fraction of total token supply ($S$).

**In short, all participants split the bonding curve reserve (without outcome payment) proportionally to their token holdings.**

<br>

Note that the lump sum ($C$) offered by the **Outcomes Payer** on project completion provides **incentive for participants to collude towards project success**.

Full mathematical derivations of settlement conditions can be found in the [System Specification notebook](Math_Specification/1_System_Specification.ipynb) produced in Phase 2 of this research initiative.
<br><br>



## Alpha Bond Simulation 

Dive into the Phase 2 [Alpha Bond Simulation Notebook](main.ipynb) and take a deeper look at how tests were carried out to ensure alpha and price converge, as well as to confirm that agent payouts are commensurate with the accuracy of their predictions.
<br><br>

## Alpha Bond Testing & Analysis

Read more about the rigorous testing & analysis carried out in Phase 3. [Simulations and experiments for the ixo pilot of Alpha Bonds](https://github.com/BlockScience/InterchainFoundation/blob/master/IXO_Chimple_Pilot_Revised.ipynb) may be of interest readers interested in social impact bond development. Testing of the [synthesis of public & private $alpha$ signal](https://github.com/BlockScience/InterchainFoundation/blob/master/private_alpha_synthesis_v2.ipynb) was also carried out. [Parametric tests](https://github.com/BlockScience/InterchainFoundation/tree/phase_3_kappa/parametric_tests) were run on multiple system parameters, including the [bonding curve exponent ($\kappa$)](https://github.com/BlockScience/InterchainFoundation/blob/master/parametric_tests/kappa_test.ipynb), the [proportion of funds allocated to project funding vs reserve of the bonding curve ($\theta$)](https://github.com/BlockScience/InterchainFoundation/blob/master/parametric_tests/parametric_test_theta.ipynb), [outcome payments ($C$)](https://github.com/BlockScience/InterchainFoundation/blob/phase_3_kappa/parametric_tests/parametric_test_outcome_payment.ipynb), and more.


<br><br>

# Detailed Research Project Breakdown

This project was carried out in 3 phases: 
* **Phase 1. Engineering Requirements Gathering** 
* **Phase 2. Formalized Specification**
* **Phase 3. Analysis & Testing**

Each phase is broken out into a series of deliverables as listed below, which are collated into a stakeholder report at the completion of each phase.

## Phase 1 Deliverables:  Requirements Gathering
*In Phase 1, we focused on gathering requirements around the ixo use-case including all of the roles and lifecycle phases in ixo alpha bonds. This allowed us to understand the overall needs, the participants, and application of our eventual design to that particular use-case. We then took a step back and determined what specific design we needed to focus on in Phase 2 and ensure that it would be a generalized design. The goal we kept in mind was to provide a useful primitive that could, with some customization be utilized by ixo, but also could be applied to any number of other use-cases in the cosmos ecosystem.*

* **1.0 [Problem Statement and Methodology](Paper/0_ProblemStatementandMethodology.md)** - Understand what problem we are trying to solve and what methodology we intend to utilize in order to solve it

* **1.1 [Ecosystem Roles](Paper/1_EcosystemRoles.md)** - Identify all of the various roles users can take in the ecosystem

* **1.2 [Alpha Bond Lifecycle Phases](Paper/2_BondLifecyclePhases.md)** - Identify the phases and state transitions in the bond lifecycle

* **1.3 [Engineering Requirements](Paper/3_EngineeringRequirements.ipynb)** - The **key deliverable notebook in this phase**. Define formal mathematical definitions and requirements for the alpha bond ecosystem.

<br>

## Phase 2 Deliverables: System Specification
*In Phase 2 we zoomed in on the focus of the design work: the bonding curve itself and the risk-adjusting component, the prediction module. In this Phase our design specifications leave behind the ixo use-case specific details (out of scope for the design) and instead focus specifically on the math related to the primitive design of a risk-adjusted bonding curve. Of particular note, the claims mechanism which is of relevance to the ixo-specific implementation is replaced with the attestation mechanism, introduced as a formal part of the prediction module.*

* **2.1 [Math Specification](Math_Specification)** - Mathematical documentation of the model including system and component specifications as well as behavioural models of agents
* **2.2 [cadCAD Model Source Code](src)** - Source code of the model built in cadCAD
* **2.3 [Component Validation Tests](tests)** - Other supporting validation tests (varying granularity, agent beliefs, etc.)
* **2.4 [Main Simulation Notebook and Explanatory Results](main.ipynb)** - Representative simulation notebook validating that the model meets core system properties

* **2.5 [Preliminary Modular SDK Specification Mapping](https://hackmd.io/nV1Dkx_BS12mNKEjL1wMJg?view)** - Template framework for documenting and implementing an SDK module using the BlockScience Systems Engineering modeling specification.
    - [Risk Prediction Module](https://hackmd.io/pBdH1OedQLuvhQU0ezTttA?view)
* **2.6 [Preliminary Phase 3 Test Plan](https://docs.google.com/spreadsheets/d/1xdiogvWU_NP2PGOTVK6V2rl642u56y26nMKQznGaO1o/edit#gid=0)** - Initial planning around experiments to be performed in Phase 3

<br>

## Phase 3 Deliverables: Analysis & Testing
*In Phase 3 we performed validation testing for the bonding curve design and created parametric testing notebooks to allow for exploration and modification of key parameters in the system. In addition, we brought back into view the ixo use-case to ensure that the design primitive could be utilized to meet the needs of ixo alpha bonds. One key customization was that with the prediction market module in ixo’s pilot education use-case, it did not seem feasible or likely at this point for impact investors to participate in making attestations with their bond tokens. So, instead of using agent attestations to create a prediction market to update alpha, we instead allowed for the alpha signal to be directly “plugged in” from an external source. ixo plans to update their alpha based on real test scores from the education pilot in order to demonstrate progress (recall the Claim mechanism from Phase 1). This was a perfect example of how the design primitive created, could be customized for the particular use-case.*

* **3.1 [cadCAD Model Files](https://github.com/BlockScience/InterchainFoundation/tree/master/src/sim)** - These files compose the cadCAD simulation. Download this if you want to run and play with the simulations locally. 

* **3.2 [Alpha Belief Synthesis](https://github.com/BlockScience/InterchainFoundation/blob/master/private_alpha_synthesis_v2.ipynb)** - This notebook provides a battery of tests that examine the synthesis of private & public alpha belief. 

* **3.3 [Parametric Testing Notebooks](https://github.com/BlockScience/InterchainFoundation/tree/master/parametric_tests)** - Explore Risk-Adjusted Bonding Curves for yourself by modifying key aspects of the system. 

* **3.4 [ixo Pilot Analysis](https://github.com/BlockScience/Risk-Adjusted-Bonding-Curves/blob/master/Pilot/Chimple_Pilot.ipynb)** - This notebook provides a simulation for the ixo pilot implementation of Alpha Bonds.

<br>
<br>

# More Research Project Information

## Scope of Research Initiative
Our goal is to gather requirements, formally specify, document, design, and test an Impact Bond Mechanism to fund outcome driven projects. The Bonds life cycle will account for the (i) pre-conditions and execution of bond initialization, (ii) a set of mechanisms available to participants for continuous funding and attestation regarding project status, and (iii) a close-out plus reconcilation mechanism that accounts for a final verdict on the success of the project, as well as the post-conditions for the system, e.g. impact tokens representing the participation level in a successful project. This design is for a parameterized class of bond mechanisms which may be configured to fit a wide range of circumstances.  In this instance, the digital twin model underlies a Cosmos SDK Implemnentation, upon which ixo is building an instance of an alpha bond risk-adjusted bonding curve, as shown below.

![img](https://i.imgur.com/hFBOUSQ.png)
<br>

## Methods and Tools
System Requirements and Functional Requirements will be mapped to formally frame the inherently human challenge into a bounded dynamic Mechanism Design problem. The framework for Discrete Event Games as described in [Economic Games as Estimators](https://epub.wu.ac.at/7433/1/zargham_paruch_shorish.pdf) will be applied. The Impact Bonds will be more advanced variations of Bonding Curves, see [From Curved Bonding to Configuration Spaces](https://epub.wu.ac.at/7385/1/zargham_shorish_paruch.pdf). While initial designs will be analytical in nature, the computer aided design process is iterative. The [cadCAD](https://github.com/cadCAD-org/cadCAD) modeling software will be applied to develop a computational model of the mechanisms by following [cadCAD best practices](https://github.com/cadCAD-org/cadCAD/tree/master/documentation). The model will be used for failure mode analysis, sensitivity analysis and other design validation procedures prior to implementation.

<br>

## Why Model Systems in cadCAD?

In cyber-physical systems like international power grids, global flight networks, or socioeconomic community ecosystems, engineers model **simulated replicas of their system**, called **digital twins**. These models help to manage the complexity of systems that have trillions of data points and are constantly in flux. These simulations channel the information into pathways that allow humans to understand what is going on in their ecosystem at a high level, so they can intervene where and as appropriate. (Like hitting a breaker switch when a fault is cleared in a power system).

![img](https://i.imgur.com/vREp8ts.png)

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
```
pip install cadCAD==0.4.23
```

Then enter the repository.
```
cd Risk-Adjusted-Bonding-Curves
``` 
Finally, open a jupyter notebook server to run the various notebooks in this repository.
```
jupyter notebook
```

Check out the [cadCAD forum](https://community.cadcad.org/t/python-newbies-setup-for-cadcad/101) for more information about installing and using cadCAD.


## Read More 
Read the blog post [Alpha Bonds: Risk-adjusted Bonding Curves for Financing Impact](https://medium.com/block-science/alpha-bonds-risk-adjusted-bonding-curves-for-financing-impact-5be949fbc5a0) 

## About BlockScience
BlockScience® is a complex systems engineering, R&D, and analytics firm. Our goal is to combine academic-grade research with advanced mathematical and computational engineering to design safe and resilient socio-technical systems. We provide engineering, design, and analytics services to a wide range of clients, including for-profit, non-profit, academic, and government organizations, and contribute to open-source research and software development.

## Follow & Subscribe
[🐦Twitter](https://twitter.com/block_science) | [📚 Medium](https://medium.com/block-science) | [👻Blog](https://blockscience.ghost.io/) | [🎥 YouTube](https://www.youtube.com/c/BlockScience) | [👥 Linkedin](https://www.linkedin.com/company/blockscience/)

## Contact

The above model was designed to be configurable and customizable for multiple use cases. If you are interested in using the model, supporting further development or have any other questions, reach out to us at **info@block.science**.

<br>

![img](https://i.imgur.com/ypZlPg9.png)
