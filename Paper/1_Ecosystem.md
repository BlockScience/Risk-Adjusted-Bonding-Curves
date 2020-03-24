# Impact Bonds Ecosystem

Roles as outlined in this document represent roles in the broader ecosystem. These roles may further have relations to specific steps in the life cycle and in some cases specific on chain mechanisms. Roles are distinct from entities which may, in some cases, occupy multiple roles.

## Roles

### Role 1
**Investment Agents** are individuals, institutions or funding mechanisms that commit capital to a bond in return for financial and non-financial returns on the capital. Investors tend to seek returns that are above the market average (Alpha) and are rewarded for their investments if a project funded by the bond is successful in achieving targets. Investors must therefore analyse the financial risks associated with the bond, as well as the operational risks associated with the project which is funded by the bond.

An **InvestmentAgent** role is characterized by the ability to buy and redeem bond tokens to compose a bond portfolio. The investment agent has a private valuation of a given project, which they employ to make buy and sell decisions and ultimately their managed portfolio’s risk to return ratio.

An **InvestmentAgent** may employ two modes of investing:
1. Invest working capital into the project `//TODO: Add description/example of what this mode includes`
2. Give up collateral for providing liquidity to the bonding curve trading pool. `//TODO: Add description/example of what this mode includes`
#### **InvestmentAgent** Mechanism Action Space:
1. Bond-to-mint `//TODO: Add description/example of what this action does`
2. Burn-to-withdraw `//TODO: Add description/example of what this action does`
3. Attestation - Claim Submission `//TODO: Add description/example of what this action does`

### Role 2
**Service Agents** can be organisations, individuals or machines that provide goods and services to the project, to produce a change in state for Beneficiaries.  `//TODO: Provide concrete example, define or link to "Beneficiaries"`

A **ServiceAgent** role is characterized by issuing impact claims, submitting disputes, receiving impact and bond tokens, and the ability to stake a performance deposit.  `//TODO: define impact claim, define performance deposit`

The ServiceAgent receives a portion of bond tokens from the ProjectOwner's project founder share during the project initialization phase. `//TODO: Explain why this happens. Link to definition of "ProjectOwner" and "initialization phase"`

#### **ServiceAgent** Mechanism Action Space:
1. Attestation - Claim Submission

### Role 3
**Verification agents** evaluate the claims made by Service Agents, to opinionate on the probability of a claim being both factually true and positively correlated with an outcome state. In this process, a Verification Agent may further enrich the claims data with additional information, such as statistical predictions, data transformations and external data. The result of the evaluation is cryptographically verified with the digital identity credentials and signature of the verification agent. This process may issue an Impact Token.

A **VerificationAgent** role is characterized by providing project verification services, evaluating claims and responding to disputes for service agents, and the ability to stake a performance deposit. `//TODO: link to definition of performance deposit`

VerificationAgents are explicitly excluded from participating in the *Bond-to-Mint* and *Burn-to-Withdraw* mechanisms, as well as holding tokens due to reasons detailed in Restriction 1. `//TODO: link to definitions of "bond-to-mint" and "burn-to-withdraw" plus link to "Restriction 1"`

#### **VerificationAgent** Mechanism Action Space:
1. Attestation - Claim Submission

### Role 4
**Arbitrators** are independent agents employed to facilitate dispute resolution when disputes are raised by any of the participants in a project or bond. The Arbitrator evaluates claims made by counterparties and recommends resolutions.

An **Arbitrator** role is characterized by providing artibitration services, evaluating disputes, and the ability to stake a performance deposit. `//TODO: Link to definition of "performance deposit"`
#### **Arbitrator** Mechanism Action Space:
1. Attestation - Claim Resolution, Dispute Evaluation

### Role 5
**Auditors** are independent agents who may be employed by any of the participating agents in a Project or a Bond to audit transactions and claims, using the available transaction records and data. Audits may be required as part of a Bond Settlement process. Auditors may provide inputs to dispute-resolution mechanisms. `//TODO: Add definition or link to "Bond Settlement". Add link to "dispute-resolution mechanisms"`

An **Auditor** role is characterized by providing auditing services, auditing claims, auditing financial transactions, and submitting disputes.
#### **Auditor** Mechanism Action Space:
1. Attestation - Claim Auditing

#
## Role 6
The **Bond Issuer** raises capital for a project through an impact bond debt instrument. They are responsible for ensuring regulatory compliance and for establishing the legal constructs of the fund. The Bond issuer is liable to investors for the capital raised and liable to project owners for making payments for goods and services to be delivered through the project.  The Bond Issuer authorises agents to participate in the bond and interact with the bond mechanisms within the scopes of capabilities given as rights to their respective roles. Note that a Bond issuer should be a positively identified legal entity and/or person. `//TODO: What does "potitively identified" mean?`

A **BondIssuer** role is characterized by the ability to issue bonds, receive impact tokens and bond tokens, distribute tokens to the bond’s stakeholders, change bond parameters or terminate bond life, and submit disputes.  `//TODO: Add links to definitions of "bond token" and "impact token"`
####  **BondIssuer** Mechanism Action Space:
1. Attestation - Dispute Submission
`//TODO: Aren't there a lot of other actions listed above that should be included here?`

### Role 7
**Project Administrator** can be assigned by the Project Owner to act on its behalf and run the project. In this role the Project Admin is also responsible for the approval of milestones and settlements of payments. A **Bond Administrator** on the other hand is equivalent to the traditional finance role of a Fund Administrator. This agent may be one or more entities or persons, or a mechanism such as a governance DAO. The role is assigned by the Bond Issuer. The Bond Admin is responsible for authorizing projects for funding, fund disbursements and facilitating settlements. They facilitate the governance of the bond. 

These two roles can be generalized under the **Administrator** role which is characterized by performing bond or project administration, reporting on bond or project performance against milestones, evaluating claims, and the ability to change bond or project parameters or terminate bond or project life.

Administrators are explicitly excluded from participating in *Bond-to-Mint*, *Burn-to-Withdraw*, and holding tokens due to reasons detailed in Restriction 1. `//TODO: Add links to "bond-to-mint", "burn-to-withdraw", "Restriction 1". `

#### **BondAdministrator** Mechanism Action Space:
1. Attestation - Claim Evaluation

### Role 8
The **Project Owner** is the initiator and controller of a project on an impact bond blockchain network. This stakeholder creates the project and defines its parameters. Once a project's parameters have been set up, the Project Owner deploys the project on an impact bond blockchain network, using their cryptographic keys to instantiate the project by signing a message payload that records the genesis of the project in a blockchain record.

A **ProjectOwner** role is characterized by the ability to create projects, receive bond and impact tokens, distribute tokens to project stakeholders, change project parameters or terminate project life, and submit disputes.  

ProjectOwners can purchase the first tranche of bond tokens during project initialization at an entry price close to 0. They then distribute these tokens to various project stakeholders to incentivize them to participate in roles in the project.

#### **ProjectOwner** Mechanism Action Space:
1. Attestation - Dispute Submission
`//TODO: Weren't there way more actions just listed for a project owner to be able to perform?`

### Role 9
The **Outcomes Payer** purchases the outcomes of a Project for a promised future value. This purchase is made typically from Bond Investors who provide the working capital for outcomes to be delivered. Payments are usually conditioned on the project achieving predetermined performance milestones. `//TODO: Add description of who typically fills this role in the world of impact bonds. Specific examples would be helpful thoughout this whole document.`

An **OutcomesPayer** role is characterized by the ability to make final payments to bond token holders such as InvestmentAgents and ProjectOwners, and submit disputes. 

#### **OutcomesPayer** Mechanism Action Space:
1. Attestation - Dispute Submission
`//TODO: Don't they also buy the outcome? does that mean they buy impact tokens? does that mean they buy bond tokens?`

Continue reading Chapter 2: [Finite Sate Machine](2_FiniteStateMachine.md)
