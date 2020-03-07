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

<!--[comment]: # (Some tests or simualtions may call for a finer timestep granularity, in which case 1 timestep = 1 transaction. At this granularity, only one agent action can be performed at a single timestep.) -->

#### Definition 3
The **agent-level state** represents all agent states at a given time $t$. The agent state is a vector $\hat{x}_{a,t}$ making the agent state space <img src="https://render.githubusercontent.com/render/math?math=\hat{X}_{a} \in R^k"> such that $\forall a, \forall t, \hat{x}_{a,t} \in \hat{X}_a$. Since the agent's state transition reflects an agent action, the agent-level state summarizes the flow of information in the system indexed by time. The agent-level state is given by

$$     (\hat{x}_{1,t}, \hat{x}_{2,t}, \ldots, \hat{x}_{n,t})\in\prod_{a=1}^n\hat{X}_a \subseteq \mathbb{R}^{nk}.
$$

<!-- <img src="https://render.githubusercontent.com/render/math?math=(\hat{x}_{1,t}, \hat{x}_{2,t}, \ldots, \hat{x}_{n,t})\in\prod_{a=1}^n\hat{X}_a \subseteq \mathbb{R}^{nk}"> -->

<!-- <img src="https://latex.codecogs.com/svg.latex?\Large&space;" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" /> -->

![img](http://latex.codecogs.com/svg.latex?%28%5Chat%7Bx%7D_%7B1%2Ct%7D%2C+%5Chat%7Bx%7D_%7B2%2Ct%7D%2C+%5Cldots%2C+%5Chat%7Bx%7D_%7Bn%2Ct%7D%29%5Cin%5Cprod_%7Ba%3D1%7D%5En%5Chat%7BX%7D_a+%5Csubseteq+%5Cmathbb%7BR%7D%5E%7Bnk%7D)

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
The **bond alpha** signal $\alpha_b \in [0,1]$ at time $t$ is an estimate of the likelihood of success of the bond, represented normalized such that $\alpha_b = 0$ indicates that the project is estimated to fail, and $\alpha_b = 1$ indicates the highest likelhood of success.

#### Definition 9
The **Alpha** state variable $\alpha \in [0,1]$ is an estimate of the probability of project success, as evaluated by the Alpha Oracle. It is represented normalized such that $\alpha = 0$ indicates that the project is estimated to fail, and $\alpha = 1$ indicates the highest likelhood of success.

The initial value of Alpha is 0.5, as a default.

#### Defintion 10
The **ProjectTime** state variable $p \in \mathbb{Z}_{++}$ describes the duration for which the project has been in the Execution phase. 

#### Defintion 11
The **ClaimsSubmitted** state variable $c \in \mathbb{Z}_{+}$ describes the number of claims submitted towards the project during its Execution phase.

## Initialization Conditions
The ProjectTime, Alpha, ClaimsSubmitted state variables need to meet a pre-specified criteria for the state to transition into the Execution phase. In the bonding curve use case, the initialization conditions are also referred to as launch conditions.

#### Definition 12
The **ProjectTime threshold** $p_{lim}$ describes the maximum allowable duration for a project's Execution phase. 

At initialization, $p_{lim}$ is set to a strictly positive finite integer $$p_{lim} \in \mathbb{Z}_{++}$$ $$p \overset{set}{=} 0$$

#### Definition 13
The **ClaimsSubmitted threshold** $c_{lim}$ describes the minimum number of claims required to be collected during the project's Execution phase. 

At initialization, $c_{lim}$ is set to a positive finite integer $$c_{lim} \in \mathbb{Z}_{+}$$ $$c \overset{set}{=} 0$$

#### Definition 14
The **Alpha threshold** is $\alpha_{lim}$ describes the minimum alpha value required for the settlement to be successful. $c_{lim}$ is set to a positive finite integer during project initialization.

At initialization, $\alpha_{lim}$ is set to a real value between 0 and 1 $$\alpha_{lim} \in [0,1]$$ $$\alpha \overset{set}{=} 0.5$$

## Settlement Conditions

#### Condition 1
For successful settlement, the project must complete execution before the duration specified by the ProjectTime threshold. If the project does not reach Settlement Phase before $p_{lim}$, the project fails settlement and is terminated. 

For successful settlement, $$p \overset{!}{\geq} p_{lim}$$

#### Condition 2
For successful settlement, the project must collect as many or more claims than the amount specified by the ClaimsSubmitted threshold $c_{lim}$. Failing to meet this criteria results in the failure of settlement and project termination.

For successful settlement, $$c \overset{!}{\geq} c_{lim}$$

#### Condition 3
For successful settlement, the project's Alpha must be evaluated to be greater than or equal to $\alpha_{lim}$ set at initialization. Failing to meet this criteria results in the failure of settlement and project termination.

For successful settlement, $$\alpha \overset{!}{\geq} \alpha_{lim}$$

## Mechanisms 

#### Definition 9
The set of **mechanisms** is $F$ such that any $f \in F$ is an operator $$f : \mathcal{X} \times U \to \mathcal{X}$$
where $\mathcal{X}$ is the space of all possible states $X$, and $U$ is the space of all legal actions associated with the mechanism $f$.

#### Functional Requirement 1
The bonding curve mechanism should be robust enough to account for large or catastropic risks that occur at either extemes of the curve. 

[comment]: # (Define a cut off point for asymptotic portion of the curve)

#### Mechanism 1 
The **bond-to-mint** mechanism mints impact tokens in exchange of bond tokens through an agent’s action $u_{a, t}$ . The agent’s action represents a transaction to transfer $\Delta R_t := r_{a,t} - r_{a, t+1} \geq 0$ quantity of bond tokens into the bonding curve system. Quantity $\Delta R_t$ of bond tokens are transferred into the bonding curve, resulting in

System state, $x_{t+1}$

$$R_{t+1} = R_{t} + \Delta R_t$$

$$S_{t+1} = $$

$$ P_{t+1} = $$

$$\alpha_{t+1} = $$

Agent-level state, $\hat x_{t+1}$

$$r_{a, t+1} = r_t - \Delta R_t$$

$$s_{a, t+1} =$$

$$p_{a, t+1} =$$

$$\alpha_{a, t+1} =$$

#### Functional Requirement 2
Upon the execution the Bond Action, Bond tokens are added to the bonding curve. 

#### Mechanism 2 
The **burn-to-withdraw** mechanism removes impact tokens to redeem bond tokens through an agent’s action $u_{a, t}$ . The agent’s action represents a transaction to remove $\Delta S_t := s_{a, t
} - s_{a, t+1} \leq 0$ quantity of impact tokens from the bonding curve system. Quantity $\Delta S_t$ of impact tokens are removed from the bonding curve, resulting in:

System state, $x_{t+1}$

$$R_{t+1} = $$

$$S_{t+1} = S_t + \Delta S_t$$

$$ P_{t+1} = $$

$$\alpha_{t+1} = $$

Agent-level state, $\hat x_{t+1}$

$$r_{a, t+1} = $$

$$s_{a, t+1} = s_{a,t} + \Delta S_t$$

$$p_{a, t+1} = $$

$$\alpha_{a, t+1} = $$

#### Functional Requirement 3
Upon the execution of the Burn Action, Impact tokens are removed from the bonding curve.

#### Mechanism 3
The **attestation** mechanism involves the lifecylce of claims. Claims undergo the stages of submission, evaluation, and resolution. During resolution, if a claim does not reflect the state of the bonding curve, a dispute is issued against it to regain the bonding curve state.

![](https://i.imgur.com/vamnLGV.png)

#### Functional Requirement 4
A lack of trading activity on the bonding curve does not indicate a degradation of the Bond Alpha, Project Alpha,  or the bonding curve itself. 

<!-- [comment]: # (Sustainability: Consider temporal effects on investor sentiment, i.e passage of time correlates with decaying excitement about project, thus lesser activity. However, sunk cost bias simultaneously is in contention with this.) -->
    
#### Definition 10
The bonding curve **conservation function** describes a conserved quantity, which is a functional relationship between the reserve and supply tokens, and is given by 

$$V(R_t,S_t)  := \frac{S_t^\kappa}{R_t} \equiv V_0,$$

where $V_0 = V(R_0,S_0) := \frac{S_0^\kappa}{R_0}$ is a constant defined by initial supply $S_0$ and initial reserve $R_0$. Parameter $\kappa$ is the curvature of the bonding curve.

This conservation function imposed over the bonding curve ensures that the price of the token reflects the amount invested into projects in the platform, thus preventing imbalances through incentive design.


