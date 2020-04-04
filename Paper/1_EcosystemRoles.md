# Ecosystem Roles

Defining all of the possible roles one can take in an ecosystem is a crucial first step in understanding the overall requirements of the system. Roles as outlined in this document represent roles of agents in the broader impact bond ecosystem. General descriptions of the roles are provided in order to provide the full context of the overall role in the ecosystem, however the Mechanism Action Space is only intended to define the specific system mechanisms available within the bonding curve implementation (i.e. once it is launched until it is closed). Roles are distinct from *entities* which may, in some cases, occupy multiple roles. 

Note that in the context of a generalized design pattern, ecosystem roles and their respective rights are unique to the use case and must always be determined prior to launch in the pre-initialization phase (lifecycle phases described in the next chapter). For our purposes here, we will define roles in the impact bond ecoysystem and we will take the case of a development impact project improving the quality of primary school education in India to provide real-world examples for each role.

## Roles

### Role 1: Investment Agent
**Investment Agents** are individuals, institutions, or funding mechanisms that commit capital to a bond in return for financial and non-financial returns on the capital. Investors tend to seek returns that are above the market average (Alpha) and are rewarded for their investments if a project funded by the bond is successful in achieving its targets. Investors must therefore analyse the financial risks associated with the bond, as well as the operational risks associated with the projects which are funded by the bond.

An **InvestmentAgent** role is characterized by the ability to buy and redeem bond tokens<a href="glossary.md#note21" id="note21ref"><sup>21</sup></a> to compose a portfolio<a href="glossary.md#note10" id="note10ref"><sup>10</sup></a>  of bonds. The Investment Agent has a private valuation of a given project, which they employ to make buy and sell decisions and ultimately  manage their portfolio’s risk to return ratio.

#### **InvestmentAgent** Mechanism Action Space:
1. Bond-to-mint<a href="glossary.md#note11" id="note11ref"><sup>11</sup></a> 
2. Burn-to-withdraw<a href="glossary.md#note12" id="note12ref"><sup>12</sup></a> 
3. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a> 

#### Example:
A high net worth investor willing to take on the risk of investment for the social benefit to childhood education in India, as well as the potential above market average return.

### Role 2: Service Agent
**Service Agents** can be organisations, individuals, or machines that provide goods and services to the project, in order to make progress towards achieving the predetermined outcomes. 

A **ServiceAgent** role is characterized by issuing claims and submitting disputes. 

ServiceAgents are compensated in fee payments for providing goods and services.

#### **ServiceAgent** Mechanism Action Space:
1. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a> 

#### Example:
Chimple - a non-profit education technology provider that will aim to utilize their technology to improve childhood learning in India. 

### Role 3: Verification Agent
**Verification Agents** evaluate the claims made by Service Agents, to opinionate on the probability of a claim being both factually true and positively correlated with an outcome state. In this process, a Verification Agent may further enrich the claims data with additional information, such as statistical predictions, data transformations, and external data. The result of the claim evaluation is cryptographically verified with the Verification Agent's digital identity credentials and signature. 

A **VerificationAgent** role is characterized by providing project verification services, evaluating claims and responding to disputes for Service Agents.

VerificationAgents are explicitly excluded from participating in the *Bond-to-Mint* and *Burn-to-Withdraw* mechanisms, as well as holding tokens due to reasons detailed in Operational Requirement 1 and 2.<a href="glossary.md#note22" id="note22ref"><sup>22,23</sup></a>

#### **VerificationAgent** Mechanism Action Space:
1. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a> 

#### Example:
Gray Matters India - an independent evaluator that will measure growth in learning outcomes of school-going children in India.

### Role 4: Arbitrator
**Arbitrators** are independent agents employed to facilitate dispute resolution when disputes are raised by any of the participants in a project or bond. The Arbitrator evaluates disputes between counterparties and recommends resolutions.

An **Arbitrator** role is characterized by providing arbitration services evaluating disputes.

#### **Arbitrator** Mechanism Action Space:
1. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a>

#### Example:
Jur - a blockchain-based ecosystem for creating smart legal contracts and providing a platform for conflict resolution. This platform will be used to resolve disputes online, with agreed upon arbitrators that have expertise in particular topics. 

### Role 5: Auditor
**Auditors** are independent agents who may be employed by any of the participating agents in a project or a bond to audit transactions and claims, using available transaction records and data. Audits may be required as part of a bond's Settlement<a href="glossary.md#note19" id="note19ref"><sup>19</sup></a> process. Auditors may provide inputs to dispute resolution mechanisms.

An **Auditor** role is characterized by providing auditing services, auditing claims, auditing financial transactions, and submitting disputes.

#### **Auditor** Mechanism Action Space:
1. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a>

#### Example:
KPMG - one of the "big four" accounting organizations.

### Role 6: Bond Issuer
The **Bond Issuer** raises capital for a project through an impact bond debt instrument. They are responsible for ensuring regulatory compliance and for establishing the legal constructs of the fund. The Bond Issuer is liable to investors for the capital raised and liable to Project Owners for making payments for goods and services to be delivered through the project.  The Bond Issuer authorises agents to participate in the bond and interact with the bond mechanisms within the scopes of capabilities allowed by their respective roles. 

A **BondIssuer** role is characterized by the ability to issue bonds, receive bond tokens, distribute bond tokens to the bond’s stakeholders, change bond parameters or terminate bond life, and submit disputes. 

####  **BondIssuer** Mechanism Action Space:
1. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a>

#### Example:
UBS Optimus Foundation - a foundation linked to a global wealth manager staffed with philanthropy experts.

### Role 7: Project Administrator
**Project Administrator** can be assigned by the Project Owner to act on their behalf and run the project. In this role the Project Administrator is also responsible for the approval of milestones and settlements of payments. A **Bond Administrator** on the other hand is equivalent to the traditional finance role of a fund administrator. This agent may be one or more entities or persons, or a system like a governance DAO. The role is assigned by the Bond Issuer. The Bond Administrator is responsible for authorizing projects for funding, fund disbursements and facilitating settlements. They facilitate the governance of the bond. 

These two roles can be generalized under the **Administrator** role which is characterized by performing bond or project administration, reporting on bond or project performance against milestones, evaluating claims, and the ability to change bond or project parameters or terminate bond or project life.

Administrators are explicitly excluded from participating in the *Bond-to-Mint* mechanism, *Burn-to-Withdraw* mechanism, and holding tokens due to reasons detailed in Operational Requirement 1.<a href="glossary.md#note22" id="note22ref"><sup>22</sup></a>  

#### **Adminstrator** Mechanism Action Space:
1. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a>

#### Example:
Dalberg Capital - an experienced advisor on impact investing. 

### Role 8: Project Owner
The **Project Owner** is the founder and controller of the overall project. This stakeholder initiates the project and defines its parameters. Once a project's parameters have been set up, the Project Owner deploys the project on an impact bond blockchain network, using their cryptographic keys to instantiate the project by signing a message payload that records the genesis of the project in a blockchain record.

A **ProjectOwner** role is characterized by the ability to create projects, receive bond tokens, distribute tokens to project stakeholders, change project parameters or terminate project life, and submit disputes.  

ProjectOwners can purchase the first tranche of bond tokens prior to launch of the bond at an entry price close to 0. They then can distribute these tokens to various project stakeholders to incentivize them to participate in roles in the project in order to secure the required resources and funding to launch.

#### **ProjectOwner** Mechanism Action Space:
1. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a>

#### Example:
Quality Education India - the creator of the development impact bond.

### Role 9: Outcomes Payer
The **Outcomes Payer** purchases the outcomes of a Project for a promised future value. In other words, the Outcomes payer commits to providing predetermined payment(s) if the project meets predetermined outcome(s). 

An **OutcomesPayer** role is characterized by the ability to make final payments to bond token holders, and submit disputes. 

#### **OutcomesPayer** Mechanism Action Space:
1. Attestation<a href="glossary.md#note13" id="note13ref"><sup>13</sup></a>

#### Example:
Michael and Susan Dell Foundation - a non-profit foundation dedicated to transforming the lives of children living in urban poverty through improving their education, health, and family economic stability. Note that Government Agencies may also typically fulfill this role.

Continue reading Chapter 2: [Bond Lifecycle Phases](2_BondLifecyclePhases.md)
