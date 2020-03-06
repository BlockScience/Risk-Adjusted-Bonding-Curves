# Impact Bonds Bonding Curve Engineering Requirements 

## Assumptions
#### Assumption 1
The Bond Alpha Oracle is assumed to be pre-trained at system start. 

## Roles
[comment]: # Link to Chapter 1: Impact Bonds Ecosystem 

## Agents

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
#### Operational Requirement 9
OutcomesPayers are disincentivized from holding bond tokens.

Since an OutcomesPayer makes the final decision evaluating if the bond or project terms satisfy the conditions for payout to InvestmentAgents and ProjectOwners, holding bond tokens presents a conflict of interest.
