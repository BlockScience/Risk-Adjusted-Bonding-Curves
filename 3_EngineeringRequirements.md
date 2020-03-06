# Engineering Requirements

## Assumptions
#### Assumption 1
The Bond Alpha Oracle is assumed to be pre-trained at system start. 

## Roles
<!--- Link to Chapter 1: Impact Bonds Ecosystem -->

## Agents

#### Definition 1
Let A be the set of all possible addresses that interact within the system. At any timestep, the set of addresses that exist is $A \subset \lambda$

The address $a \subset \lambda$ is called an **agent** when referring to an address which takes an action. Agent decisions and actions take place over time $t \in Z^{v\geq 0}$ such that at any timestep $t$, an agent can perform an array of agent actions represented as an ordered list of transactions. 


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

## System State Variables 

#### Definition 2
The **timestep** or period $t$ defined for the system is one block. A block contains an ordered list of transactions, also referred to as agent actions $u_t$. Therefore, in each timestep, an agent $a$ can perform multiple actions chosen from the set of all legal actions $U$.

[comment]: # (Some tests or simualtions may call for a finer timestep granularity, in which case 1 timestep = 1 transaction. At this granularity, only one agent action can be performed at a single timestep.) 

#### Definition 3
The **agent-level state** represents all agent states at a given time $t$. The agent state is a vector $\hat{x}_{a,t}$ making the agent state space $ \hat{X}_{a} \in R^k $ such that $\forall a, \forall t, \hat{x}_{a,t} \in \hat{X}_a$. Since the agent's state transition reflects an agent action, the agent-level state summarizes the flow of information in the system indexed by time. The agent-level state is given by

$$     (\hat{x}_{1,t}, \hat{x}_{2,t}, \ldots, \hat{x}_{n,t})\in\prod_{a=1}^n\hat{X}_a \subseteq \mathbb{R}^{nk}.
$$

#### Definition 4
The **system state** is the network’s internal state composed of a finite number of elements, denoted by $\bar{x}_t$. The system-level state depends on the information arrival process summarized by time $t$. The system-level state space is a set $\bar{X} \in R^m$, such that $\forall t$, $\bar{x}_t \in \bar{X}$ where $m$ is the number of finite elements. The system state $x_t$ is the state of all agents and the system-level state, and is given by

$$
x_t := (\hat{x}_{1,t}, \hat{x}_{2,t}, \ldots, \hat{x}_{n,t}, \bar{x}_t) \in X := \prod_{a=1}^n\hat{X}_a \times \bar{X} \subseteq \mathbb{R}^{nk} \times \mathbb{R}^m.
$$

#### Definition 5
The **reserve** $R_t \in \mathbb{R}_{++}$ at time $t$ is the total quantity of bond tokens bonded to the bonding curve contract.

Bond Tokens are reserve currency tokens. At time $t$, each agent $a$ possess their holding of Bond Tokens, denoted by $r_{a,t}>0$

#### Definition 6
The **supply** $S_t \in \mathbb{R}_{++}$ at time $t$ is the total quantity of impact tokens issued by the bonding curve contract.

Impact tokens are community tokens. At time $t$, the local state of agent $a$ comprises of the individual holding of Impact Tokens, $s_{a,t}$.

#### Definition 7
The **price** signal $P_t \in \mathbb{R}_{++}$ at time $t$ is an estimate of the value of the bond token, in units of $R$ per units of $S$.

#### Definition 8
The **bond alpha** signal at time $t$ is an estimate of the likelihood of success of the bond, represented normalized such that $\alpha = 0$ indicates that the project is estimated to fail, and $\alpha = 1$ indicates the highest likelhood of success.
