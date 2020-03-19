# Engineering Requirements

## Assumptions
#### Assumption 1
The Bond Alpha Oracle is assumed to be pre-trained at system start. 

## Roles
<!--- Link to Chapter 1: Impact Bonds Ecosystem -->

## Agents

#### Definition 1
Let A be the set of all possible addresses that interact within the system. At any timestep, the set of addresses that exist is ![img](https://latex.codecogs.com/svg.latex?A%20%5Csubset%20%5Clambda)

The address ![img](https://latex.codecogs.com/svg.latex?a%20%5Csubset%20%5Clambda) is called an **agent** when referring to an address which takes an action. Agent decisions and actions take place over time ![img](https://latex.codecogs.com/svg.latex?t%20%5Cin%20Z%5E%7Bv%5Cgeq%200%7D) such that at any timestep ![img](https://latex.codecogs.com/svg.latex?t), an agent can perform an array of agent actions represented as an ordered list of transactions. 


### Agent Class 1: Trader Agents
- Trader Agents can execute the *Bond-to-Mint* and *Burn-to-Withdraw* mechanisms.

 - Constitutes of roles:
1. InvestmentAgent
 
##### Operational Requirement 1
Trader Agents can call the Bond Action and the Burn Action. 
##### Operational Requirement 2
An agent which is able to execute the *Bond-to-Mint* or *Burn-to-Withdraw* mechanisms - such as Trader Agents - must not be involved in the Claim Evaluation, Claim Auditing, and Claim Resolution stages of the *Attestation* mechanism. 

### Agent Class 2: Claim & Dispute Issuers
- Claim & Dispute Issuers can execute the Claim Submission and Dispute Submission functions of the *Attestations* mechanism.

- Constitutes of roles:
1. InvestmentAgent
2. ServiceAgent
3. BondIssuer
4. ProjectOwner
5. OutcomesPayer
 
##### Operational Requirement 3
Claim & Dispute Issuers call the SubmitClaim Action or SubmitDispute Action
##### Operational Requirment 4
Claim & Dispute Issuers are explicity excluded from having the ability to call EvaluateClaim Action, AuditClaim Action, or ResolveClaim Action. 
 
### Agent Class 3: Evaluators
 - Claim Evaluators can execute the Claim Evaluation, Claim Auditing, and Claim Resolution functions of the *Attestations* mechanism.

- Constitutes of roles:
1. VerificationAgent
2. Administrator
3. Auditor
4. Arbitrator
 
##### Operational Requirement 5
Evaluators can call the EvaluateClaim Action, AuditClaim Action, or ResolveClaim Action to process Claims, or the EvaluateDispute Action or ResolveDispute Action to process Disputes
##### Operational Requirement 6
Agents involved in the Claim Evaluation, Claim Auditing, and Claim Resolution stages of the *Attestation* mechanism, such as Claim & Dispute Evaluators, are explictly excluded from holding or trading bond tokens as it results in a conflict of interest. 

### Agent Class 4: Outcomes Payers
- Outcomes Payers evaluate the state of the project through the CompleteBond Action and  disburse the final payout to Bond token holders through the SettleBond Action, all according to the project terms.

- Constitutes of roles:
1. OutcomesPayers
 
##### Operational Requirement 7
OutcomesPayers can perform the CompleteBond Action and SettleBond Action. 
##### Operational Requirement 8
OutcomesPayers are explicitly excluded from the ability to execute the EvaluateClaim Action, AuditClaim Action, ResolveClaim Action, EvaluateDispute Action and ResolveDispute Action.
##### Operational Requirement 9
OutcomesPayers are disincentivized from holding bond tokens.

Since an OutcomesPayer makes the final decision evaluating if the bond or project terms satisfy the conditions for payout to InvestmentAgents and ProjectOwners, holding bond tokens presents a conflict of interest.

## System Boundary
The system under consideration is at the bond system level. The level above the bond system consists of the bond portfolio, which is comprised of multiple bonds. The level below the bond system is the project system, where each bond can be a composition of many projects. 

Since a bond comes into existence upon the Bond Initialization phase, and this phase corresponds with the Bond Alpha Initialization phase in the Alpha Oracle Lifecycle, the temporal system boundary starts at the Bond Initialization and Bond Alpha Initialization phase. 

![](https://i.imgur.com/qYIDv36.png)

## System Requirements

#### System Requirement 1 
The state of all Claims issued in a bond must reflect the state of the bonding curve. If the bonding curve state is not respected, disputes will be issued against the claims to regain the bonding curve state. 

<!-- [comment]: # (The Dispute mechanism acts as a fail-safe, therefore making the protocol more resilient. Other fail-safes tbd) --> 

#### System Requirement 2 
The economic incentive layer of the system, which contains all the bonding curve mechanisms, must incentivize behaviour that achieves system goals. 

#### System Requirement 3
All agent roles have restrictions over their action space, which are defined in the role's corresponding operational requirement. 

## System State Variables 

#### Definition 2
The **timestep** or period ![img](https://latex.codecogs.com/svg.latex?t) defined for the system is one block. A block contains an ordered list of transactions, also referred to as agent actions ![img](https://latex.codecogs.com/svg.latex?u_t). Therefore, in each timestep, an agent ![img](https://latex.codecogs.com/svg.latex?a) can perform multiple actions chosen from the set of all legal actions ![img](https://latex.codecogs.com/svg.latex?U).

<!--[comment]: # (Some tests or simualtions may call for a finer timestep granularity, in which case 1 timestep = 1 transaction. At this granularity, only one agent action can be performed at a single timestep.) -->

#### Definition 3
The **agent-level state** represents all agent states at a given time ![img](https://latex.codecogs.com/svg.latex?t). The agent state is a vector ![img](https://latex.codecogs.com/svg.latex?%5Chat%7Bx%7D_%7Ba%2Ct%7D) making the agent state space <img src="https://render.githubusercontent.com/render/math?math=\hat{X}_{a} \in R^k"> such that ![img](https://latex.codecogs.com/svg.latex?%5Cforall%20a%2C%20%5Cforall%20t%2C%20%5Chat%7Bx%7D_%7Ba%2Ct%7D%20%5Cin%20%5Chat%7BX%7D_a). Since the agent's state transition reflects an agent action, the agent-level state summarizes the flow of information in the system indexed by time. The agent-level state is given by <br/>

<!-- <img src="https://render.githubusercontent.com/render/math?math=(\hat{x}_{1,t}, \hat{x}_{2,t}, \ldots, \hat{x}_{n,t})\in\prod_{a=1}^n\hat{X}_a \subseteq \mathbb{R}^{nk}"> -->

<!-- <img src="https://latex.codecogs.com/svg.latex?\Large&space;" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" /> -->

<p align="center">
 <img src="http://latex.codecogs.com/svg.latex?%28%5Chat%7Bx%7D_%7B1%2Ct%7D%2C+%5Chat%7Bx%7D_%7B2%2Ct%7D%2C+%5Cldots%2C+%5Chat%7Bx%7D_%7Bn%2Ct%7D%29%5Cin%5Cprod_%7Ba%3D1%7D%5En%5Chat%7BX%7D_a+%5Csubseteq+%5Cmathbb%7BR%7D%5E%7Bnk%7D">
</p>

#### Definition 4
The **system state** is the network’s internal state composed of a finite number of elements, denoted by ![img](https://latex.codecogs.com/svg.latex?%5Cbar%7Bx%7D_t). The system-level state depends on the information arrival process summarized by time ![img](https://latex.codecogs.com/svg.latex?t). The system-level state space is a set ![img](https://latex.codecogs.com/svg.latex?%5Cbar%7BX%7D%20%5Cin%20R%5Em), such that ![img](https://latex.codecogs.com/svg.latex?%5Cforall%20t), ![img](https://latex.codecogs.com/svg.latex?%5Cbar%7Bx%7D_t%20%5Cin%20%5Cbar%7BX%7D) where ![img](https://latex.codecogs.com/svg.latex?m) is the number of finite elements. The system state ![img](https://latex.codecogs.com/svg.latex?x_t) is the state of all agents and the system-level state, and is given by <br/>

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?x_t%20%3A%3D%20%28%5Chat%7Bx%7D_%7B1%2Ct%7D%2C%20%5Chat%7Bx%7D_%7B2%2Ct%7D%2C%20%5Cldots%2C%20%5Chat%7Bx%7D_%7Bn%2Ct%7D%2C%20%5Cbar%7Bx%7D_t%29%20%5Cin%20X%20%3A%3D%20%5Cprod_%7Ba%3D1%7D%5En%5Chat%7BX%7D_a%20%5Ctimes%20%5Cbar%7BX%7D%20%5Csubseteq%20%5Cmathbb%7BR%7D%5E%7Bnk%7D%20%5Ctimes%20%5Cmathbb%7BR%7D%5Em">
</p>

#### Definition 5
The **reserve** ![img](https://latex.codecogs.com/svg.latex?R_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D). at time ![img](https://latex.codecogs.com/svg.latex?t) is the total quantity of bond tokens bonded to the bonding curve contract.

Bond Tokens are reserve currency tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), each agent ![img](https://latex.codecogs.com/svg.latex?a) possess their holding of Bond Tokens, denoted by ![img](https://latex.codecogs.com/svg.latex?r_%7Ba%2Ct%7D%3E0).

#### Definition 6
The **supply** ![img](https://latex.codecogs.com/svg.latex?S_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D) at time ![img](https://latex.codecogs.com/svg.latex?t) is the total quantity of impact tokens issued by the bonding curve contract.

Impact tokens are community tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), the local state of agent ![img](https://latex.codecogs.com/svg.latex?a) comprises of the individual holding of Impact Tokens, ![img](https://latex.codecogs.com/svg.latex?s_%7Ba%2Ct%7D).

#### Definition 7
The **price** signal ![img](https://latex.codecogs.com/svg.latex?P_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D) at time ![img](https://latex.codecogs.com/svg.latex?t) is an estimate of the value of the bond token, in units of ![img](https://latex.codecogs.com/svg.latex?R) per units of ![img](https://latex.codecogs.com/svg.latex?S).

#### Definition 8
The **bond alpha** signal ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%5Cin%20%5B0%2C1%5D) at time ![img](https://latex.codecogs.com/svg.latex?t) is an estimate of the likelihood of success of the bond, represented normalized such that ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%3D%200) indicates that the project is estimated to fail, and ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%3D%201) indicates the highest likelhood of success.

#### Definition 9
The **Alpha** state variable ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%5Cin%20%5B0%2C1%5D) is an estimate of the probability of project success, as evaluated by the Alpha Oracle. It is represented normalized such that ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D%200) indicates that the project is estimated to fail, and ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D%201) indicates the highest likelhood of success.

The initial value of Alpha is 0.5, as a default.

#### Defintion 10
The **ProjectTime** state variable ![img](https://latex.codecogs.com/svg.latex?p%20%5Cin%20%5Cmathbb%7BZ%7D_%7B&plus;&plus;%7D) describes the duration for which the project has been in the Execution phase. 

#### Defintion 11
The **ClaimsSubmitted** state variable ![img](https://latex.codecogs.com/svg.latex?c%20%5Cin%20%5Cmathbb%7BZ%7D_%7B&plus;%7D) describes the number of claims submitted towards the project during its Execution phase.

## Initialization Conditions
The ProjectTime, Alpha, ClaimsSubmitted state variables need to meet a pre-specified criteria for the state to transition into the Execution phase. In the bonding curve use case, the initialization conditions are also referred to as launch conditions.

#### Definition 12
The **ProjectTime threshold** ![img](https://latex.codecogs.com/svg.latex?p_%7Blim%7D) describes the maximum allowable duration for a project's Execution phase. 

At initialization, ![img](https://latex.codecogs.com/svg.latex?p_%7Blim%7D) is set to a strictly positive finite integer 

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?p_%7Blim%7D%20%5Cin%20%5Cmathbb%7BZ%7D_%7B&plus;&plus;%7D%24%24%20%24%24p%20%5Coverset%7Bset%7D%7B%3D%7D%200">
</p>

#### Definition 13
The **ClaimsSubmitted threshold** ![img](https://latex.codecogs.com/svg.latex?c_%7Blim%7D) describes the minimum number of claims required to be collected during the project's Execution phase. 

At initialization, ![img](https://latex.codecogs.com/svg.latex?c_%7Blim%7D) is set to a positive finite integer 

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?c_%7Blim%7D%20%5Cin%20%5Cmathbb%7BZ%7D_%7B&plus;%7D%24%24%20%24%24c%20%5Coverset%7Bset%7D%7B%3D%7D%200">
</p>

#### Definition 14
The **Alpha threshold** is ![img](https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D) describes the minimum alpha value required for the settlement to be successful. ![img](https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D) is set to a positive finite integer during project initialization.

At initialization, ![img](https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D) is set to a real value between 0 and 1 

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D%20%5Cin%20%5B0%2C1%5D">
 <br/> 
 <img src="https://latex.codecogs.com/svg.latex?%5Calpha%20%5Coverset%7Bset%7D%7B%3D%7D%200.5">
</p>
 

## Settlement Conditions

#### Condition 1
For successful settlement, the project must complete execution before the duration specified by the ProjectTime threshold. If the project does not reach Settlement Phase before ![img](https://latex.codecogs.com/svg.latex?p_%7Blim%7D), the project fails settlement and is terminated. 

For successful settlement, 
<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?p%20%5Coverset%7B%21%7D%7B%5Cgeq%7D%20p_%7Blim%7D">
</p>

#### Condition 2
For successful settlement, the project must collect as many or more claims than the amount specified by the ClaimsSubmitted threshold ![img](https://latex.codecogs.com/svg.latex?c_%7Blim%7D) Failing to meet this criteria results in the failure of settlement and project termination.

For successful settlement, 
<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?c%20%5Coverset%7B%21%7D%7B%5Cgeq%7D%20c_%7Blim%7D">
</p>

#### Condition 3
For successful settlement, the project's Alpha must be evaluated to be greater than or equal to ![img](https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D) set at initialization. Failing to meet this criteria results in the failure of settlement and project termination.

For successful settlement, 
<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?%5Calpha%20%5Coverset%7B%21%7D%7B%5Cgeq%7D%20%5Calpha_%7Blim%7D">
</p>

## Mechanisms 

#### Definition 15
The set of **mechanisms** is ![img](https://latex.codecogs.com/svg.latex?F) such that any ![img](https://latex.codecogs.com/svg.latex?f%20%5Cin%20F) is an operator 

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?f%20%3A%20%5Cmathcal%7BX%7D%20%5Ctimes%20U%20%5Cto%20%5Cmathcal%7BX%7D">
</p>

where ![img](https://latex.codecogs.com/svg.latex?%5Cmathcal%7BX%7D) is the space of all possible states ![img](https://latex.codecogs.com/svg.latex?X), and ![img](https://latex.codecogs.com/svg.latex?U) is the space of all legal actions associated with the mechanism ![img](https://latex.codecogs.com/svg.latex?f).

#### Functional Requirement 1
The bonding curve mechanism should be robust enough to account for large or catastropic risks that occur at either extemes of the curve. 

[comment]: # (Define a cut off point for asymptotic portion of the curve)

#### Mechanism 1 
The **bond-to-mint** mechanism mints impact tokens in exchange of bond tokens through an agent’s action ![img](https://latex.codecogs.com/svg.latex?u_%7Ba%2C%20t%7D). The agent’s action represents a transaction to transfer ![img](https://latex.codecogs.com/svg.latex?%5CDelta%20R_t%20%3A%3D%20r_%7Ba%2Ct%7D%20-%20r_%7Ba%2C%20t&plus;1%7D%20%5Cgeq%200) quantity of bond tokens into the bonding curve system. Quantity ![img](https://latex.codecogs.com/svg.latex?%5CDelta%20R_t) of bond tokens are transferred into the bonding curve, resulting in

System state, ![img](https://latex.codecogs.com/svg.latex?x_%7Bt&plus;1%7D)

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?R_%7Bt&plus;1%7D%20%3D%20R_%7Bt%7D%20&plus;%20%5CDelta%20R_t">
 <br/> 
 <img src="https://latex.codecogs.com/svg.latex?S_%7Bt&plus;1%7D%20%3D">
 <br/> 
 <img src="https://latex.codecogs.com/svg.latex?P_%7Bt&plus;1%7D%20%3D">
 <br/> 
 <img src="https://latex.codecogs.com/svg.latex?%5Calpha_%7Bt&plus;1%7D%20%3D">
</p>

Agent-level state, ![img](https://latex.codecogs.com/svg.latex?%5Chat%20x_%7Bt&plus;1%7D)

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?r_%7Ba%2C%20t&plus;1%7D%20%3D%20r_t%20-%20%5CDelta%20R_t">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?s_%7Ba%2C%20t&plus;1%7D%20%3D">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?p_%7Ba%2C%20t&plus;1%7D%20%3D">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?%5Calpha_%7Ba%2C%20t&plus;1%7D%20%3D">
</p>

#### Functional Requirement 2
Upon the execution the Bond Action, Bond tokens are added to the bonding curve. 

#### Mechanism 2 
The **burn-to-withdraw** mechanism removes impact tokens to redeem bond tokens through an agent’s action ![img](https://latex.codecogs.com/svg.latex?u_%7Ba%2C%20t%7D). The agent’s action represents a transaction to remove ![img](https://latex.codecogs.com/svg.latex?%5CDelta%20S_t%20%3A%3D%20s_%7Ba%2C%20t%7D%20-%20s_%7Ba%2C%20t&plus;1%7D%20%5Cleq%200) quantity of impact tokens from the bonding curve system. Quantity ![img](https://latex.codecogs.com/svg.latex?%5CDelta%20S_t) of impact tokens are removed from the bonding curve, resulting in:

System state, ![img](https://latex.codecogs.com/svg.latex?x_%7Bt&plus;1%7D)

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?R_%7Bt&plus;1%7D%20%3D">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?S_%7Bt&plus;1%7D%20%3D%20S_t%20&plus;%20%5CDelta%20S_t">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?P_%7Bt&plus;1%7D%20%3D">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?%5Calpha_%7Bt&plus;1%7D%20%3D">
</p>

Agent-level state, ![img](https://latex.codecogs.com/svg.latex?%5Chat%20x_%7Bt&plus;1%7D)

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?r_%7Ba%2C%20t&plus;1%7D%20%3D">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?s_%7Ba%2C%20t&plus;1%7D%20%3D%20s_%7Ba%2Ct%7D%20&plus;%20%5CDelta%20S_t">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?p_%7Ba%2C%20t&plus;1%7D%20%3D">
 <br/>
 <img src="https://latex.codecogs.com/svg.latex?%5Calpha_%7Ba%2C%20t&plus;1%7D%20%3D">
</p>

#### Functional Requirement 3
Upon the execution of the Burn Action, Impact tokens are removed from the bonding curve.

#### Mechanism 3
The **attestation** mechanism involves the lifecylce of claims. Claims undergo the stages of submission, evaluation, and resolution. During resolution, if a claim does not reflect the state of the bonding curve, a dispute is issued against it to regain the bonding curve state.

![](https://i.imgur.com/vamnLGV.png)

#### Functional Requirement 4
A lack of trading activity on the bonding curve does not indicate a degradation of the Bond Alpha, Project Alpha,  or the bonding curve itself. 

<!-- [comment]: # (Sustainability: Consider temporal effects on investor sentiment, i.e passage of time correlates with decaying excitement about project, thus lesser activity. However, sunk cost bias simultaneously is in contention with this.) -->
    
#### Definition 16
The bonding curve **conservation function** describes a conserved quantity, which is a functional relationship between the reserve and supply tokens, and is given by 

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?V%28R_t%2CS_t%29%20%3A%3D%20%5Cfrac%7BS_t%5E%5Ckappa%7D%7BR_t%7D%20%5Cequiv%20V_0%2C">
</p>

where 

<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?V_0%20%3D%20V%28R_0%2CS_0%29%20%3A%3D%20%5Cfrac%7BS_0%5E%5Ckappa%7D%7BR_0%7D">
</p>

is a constant defined by initial supply ![img](https://latex.codecogs.com/svg.latex?S_0) and initial reserve ![img](https://latex.codecogs.com/svg.latex?R_0). Parameter ![img](https://latex.codecogs.com/svg.latex?%5Ckappa) is the curvature of the bonding curve.

This conservation function imposed over the bonding curve ensures that the price of the token reflects the amount invested into projects in the platform, thus preventing imbalances through incentive design.
