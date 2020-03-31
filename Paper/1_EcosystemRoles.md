# Ecosystem Roles

Defining all of the possible roles one can take in an ecosystem is a crucial first step in understanding the overall requirements of the system. Roles as outlined in this document represent roles of agents in the broader impact bond ecosystem. These roles may further have relations to specific steps in the lifecycle of the bond and in some cases, specific on-chain mechanisms. Roles are distinct from *entities* which may, in some cases, occupy multiple roles.

## Roles

### Role 1: Investment Agent
**Investment Agents** are individuals, institutions, or funding mechanisms that commit capital to a bond in return for financial and non-financial returns on the capital. Investors tend to seek returns that are above the market average (Alpha) and are rewarded for their investments if a project funded by the bond is successful in achieving its targets. Investors must therefore analyse the financial risks associated with the bond, as well as the operational risks associated with the projects which are funded by the bond.

An **InvestmentAgent** role is characterized by the ability to buy and redeem bond tokens<a href="glossary.md#note21" id="note21ref"><sup>21</sup></a> to compose a portfolio<a href="glossary.md#note10" id="note10ref"><sup>10</sup></a>  of bonds. The Investment Agent has a private valuation of a given project, which they employ to make buy and sell decisions and ultimately  manage their portfolio’s risk to return ratio.

An **InvestmentAgent** may employ two modes of investing:
1. Invest working capital into the project
2. Give up collateral for providing liquidity to the bonding curve trading pool

#### **InvestmentAgent** Mechanism Action Space:
1. Bond-to-mint<a href="glossary.md#note11" id="note11ref"><sup>11</sup></a> 
2. Burn-to-withdraw<a href="glossary.md#note12" id="note12ref"><sup>12</sup></a> 
3. Attestation - Claim Submission<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a> 

### Role 2
**Service Agents** can be organisations, individuals, or machines that provide goods and services to the project, to produce a change in state for the project's beneficiaries.  

A **ServiceAgent** role is characterized by issuing claims, submitting disputes, receiving impact and bond tokens, and the ability to stake a performance deposit.

The ServiceAgent receives a portion of bond tokens from the ProjectOwner's founder's share during the project's initialization phase.<a href="glossary.md#note15" id="note15ref"><sup>15</sup></a> 

#### **ServiceAgent** Mechanism Action Space:
1. Attestation - Claim Submission

### Role 3
**Verification Agents** evaluate the claims made by Service Agents, to opinionate on the probability of a claim being both factually true and positively correlated with an outcome state. In this process, a Verification Agent may further enrich the claims data with additional information, such as statistical predictions, data transformations, and external data. The result of the claim evaluation is cryptographically verified, with the Verification Agent's digital identity credentials and signature. This process may issue an impact token.<a href="glossary.md#note20" id="note20ref"><sup>20</sup></a>

A **VerificationAgent** role is characterized by providing project verification services, evaluating claims and esponding to disputes for Service Agents, and the ability to stake a performance deposit.

VerificationAgents are explicitly excluded from participating in the *Bond-to-Mint* and *Burn-to-Withdraw* mechanisms, as well as holding tokens due to reasons detailed in Operational Requirement 1 and 2.<a href="glossary.md#note22" id="note22ref"><sup>22,23</sup></a>

#### **VerificationAgent** Mechanism Action Space:
1. Attestation - Claim Submission

### Role 4
**Arbitrators** are independent agents employed to facilitate dispute resolution when disputes are raised by any of the participants in a project or bond. The Arbitrator evaluates claims made by counterparties and recommends resolutions.

An **Arbitrator** role is characterized by providing artibitration services, evaluating disputes, and the ability to stake a performance deposit.

#### **Arbitrator** Mechanism Action Space:
1. Attestation - Claim Resolution, Dispute Evaluation

### Role 5
**Auditors** are independent agents who may be employed by any of the participating agents in a project or a bond to audit transactions and claims, using available transaction records and data. Audits may be required as part of a bond's Settlement<a href="glossary.md#note19" id="note19ref"><sup>19</sup></a> process. Auditors may provide inputs to dispute resolution mechanisms.

An **Auditor** role is characterized by providing auditing services, auditing claims, auditing financial transactions, and submitting disputes.

#### **Auditor** Mechanism Action Space:
1. Attestation - Claim Auditing

#
## Role 6
The **Bond Issuer** raises capital for a project through an impact bond debt instrument. They are responsible for ensuring regulatory compliance and for establishing the legal constructs of the fund. The Bond Issuer is liable to investors for the capital raised and liable to project owners for making payments for goods and services to be delivered through the project.  The Bond Issuer authorises agents to participate in the bond and interact with the bond mechanisms within the scopes of capabilities allowed by their respective roles. Note that a Bond Issuer should be a positively identified legal entity and/or person.

A **BondIssuer** role is characterized by the ability to issue bonds, receive impact tokens and bond tokens, distribute tokens to the bond’s stakeholders, change bond parameters or terminate bond life, and submit disputes. 

####  **BondIssuer** Mechanism Action Space:
1. Attestation - Dispute Submission

### Role 7
**Project Administrator** can be assigned by the Project Owner to act on their behalf and run the project. In this role the Project Administrator is also responsible for the approval of milestones and settlements of payments. A **Bond Administrator** on the other hand is equivalent to the traditional finance role of a fund administrator. This agent may be one or more entities or persons, or a system like a governance DAO. The role is assigned by the Bond Issuer. The Bond Administrator is responsible for authorizing projects for funding, fund disbursements and facilitating settlements. They facilitate the governance of the bond. 

These two roles can be generalized under the **Administrator** role which is characterized by performing bond or project administration, reporting on bond or project performance against milestones, evaluating claims, and the ability to change bond or project parameters or terminate bond or project life.

Administrators are explicitly excluded from participating in the Bond-to-Mint mechanism, Burn-to-Withdraw mechanism, and holding tokens due to reasons detailed in Operational Requirement 1.<a href="glossary.md#note22" id="note22ref"><sup>22</sup></a>  

#### **Adminstrator** Mechanism Action Space:
1. Attestation - Claim Evaluation

### Role 8
The **Project Owner** is the initiator and controller of a project on an impact bond blockchain network. This stakeholder creates the project and defines its parameters. Once a project's parameters have been set up, the Project Owner deploys the project on an impact bond blockchain network, using their cryptographic keys to instantiate the project by signing a message payload that records the genesis of the project in a blockchain record.

A **ProjectOwner** role is characterized by the ability to create projects, receive bond and impact tokens, distribute tokens to project stakeholders, change project parameters or terminate project life, and submit disputes.  

ProjectOwners can purchase the first tranche of bond tokens during project initialization at an entry price close to 0. They then distribute these tokens to various project stakeholders to incentivize them to participate in roles in the project.

#### **ProjectOwner** Mechanism Action Space:
1. Attestation - Dispute Submission

### Role 9
The **Outcomes Payer** purchases the outcomes of a Project for a promised future value. This purchase is made typically from Investment Agents who provide the working capital for outcomes to be delivered. Payments are usually conditioned on the project achieving predetermined performance milestones.

An **OutcomesPayer** role is characterized by the ability to make final payments to bond token holders such as InvestmentAgents and ProjectOwners, and submit disputes. 

#### **OutcomesPayer** Mechanism Action Space:
1. Attestation - Dispute Submission

Continue reading Chapter 2: [Bond Lifecycle Phases](2_BondLifecyclePhases.md)
