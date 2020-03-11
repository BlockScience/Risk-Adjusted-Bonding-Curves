# Impact Bonds Ecosystem

Roles as outlined in this document represent roles in the broader ecosystem. These roles may further have relations to specific steps in the life cycle and in some cases specific on chain mechanisms. Roles are distinct from entities which may in some cases occupy multiple roles.

## Roles

#### Role 1
An **InvestmentAgent** role is characterized by the ability to buy and redeem bond tokens to compose a bond portfolio. The investment agent has a private valuation of a given project, which they employ to make buy/sell decisions and ultimately their manage portfolio’s risk to return ratio.

An InvestmentAgent may employ two modes of investing:
1. Invest working capital into the project
2. Give up collateral for providing liquidity to the bonding curve trading pool. 
###### **InvestmentAgent** Mechanism Action Space:
1. Bond-to-mint
2. Burn-to-withdraw
3. Attestation - Claim Submission

#### Role 2
A **ServiceAgent** role is characterized by issuing impact claims, submitting disputes, receiving impact and bond tokens, and the ability to stake a performance deposit. 

The ServiceAgent receives a portion of bond tokens from the ProjectOwner's project founder share during the project initialization phase. 

###### **ServiceAgent** Mechanism Action Space:
1. Attestation - Claim Submission

#### Role 3
A **VerificationAgent** role is characterized by providing project verification services, evaluating claims and responding to disputes for service agents, and the ability to stake a performance deposit.

VerificationAgents are explicitly excluded from participating in *Bond-to-Mint*, *Burn-to-Withdraw*, and holding tokens due reasons detailed in Restriction 1.

###### **VerificationAgent** Mechanism Action Space:
1. Attestation - Claim Submission

#### Role 4
An **Arbitrator** role is characterized by providing artibitration services, evaluating disputes, and the ability to stake a performance deposit.
###### **Arbitrator** Mechanism Action Space:
1. Attestation - Claim Resolution, Dispute Evaluation

#### Role 5
An **Auditor** role is characterized by providing auditing services, auditing claims, auditing financial transactions, and submitting disputes.
###### **Auditor** Mechanism Action Space:
1. Attestation - Claim Auditing

#### Role 6
A **BondIssuer** role is characterized by the ability to issue bonds, receive impact tokens and bond tokens, distribute tokens to the bond’s stakeholders, change bond parameters or terminate bond life, and submit disputes. 
######  **BondIssuer** Mechanism Action Space:
1. Attestation - Dispute Submission

#### Role 7
An **Administrator** role is characterized by performing bond or project administration, reporting on bond or project performance against milestones, evaluating claims, and the ability to change bond or project parameters or terminate bond or project life.

Administrators are explicitly excluded from participating in *Bond-to-Mint*, *Burn-to-Withdraw*, and holding tokens due reasons detailed in Restriction 1.

###### **BondIssuer** Mechanism Action Space:
1. Attestation - Claim Evaluation

#### Role 8
A **ProjectOwner** role is characterized by the ability to create projects, receive bond and impact tokens, distribute tokens to project stakeholders, change project parameters or terminate project life, and submit disputes.  

ProjectOwners can purchase the first tranche of bond tokens during project initialization a at an entry price close to 0. They then distribute these tokens to various project stakeholders to incentivize them to participate in roles in the project.

###### **ProjectOwner** Mechanism Action Space:
1. Attestation - Dispute Submission

#### Role 9
An **OutcomesPayer** role is characterized by the ability to make final payments to bond token holders such as InvestmentAgents and ProjectOwners, and submit disputes. 

###### **OutcomesPayer** Mechanism Action Space:
1. Attestation - Dispute Submission
