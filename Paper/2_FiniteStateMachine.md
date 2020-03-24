# Phases in Bond Lifecycle
<div align="center">
	<img width="900" height="744" src="img/phases.png" alt="bondlifecyclephases">
	<br>
</div>

`//TODO: Add white background to image. Currently it's transparent and can't be seed outside of a website w a white background`

## Phase 0: Pre-initialization 
During the pre-initialization phase, the bond is set up with an associated wallet and repository, bond parameters are initialized for best-fit to the project, the Fund Recipient role is set, and all Bond Participants are identified with decentralized IDs, public keys, and credentials. The bond also acquires non-bond investment such as resources, materials, and equipment. 	`//TODO: Add link to definition of "Fund Recipient"  and "Bond Participant" roles. Give a concrete example to explain what this bond is and who might be interacting with it.`

### Transitions into Pre-initialization Phase
Since this is the first state of the bond lifecycle, there are no inward transitions. 	`//TODO: What ia an "inward transition"?`

### Inputs
1. Amount raised in Non-Bond Funds 
2. Wallet Address
3. Repository Account 	`//TODO: What is this?`
4. Bond Curve Parameter

### Next State Outputs
1. Amount secured in Non-Bond Funds

### Transitions out of Pre-initialization Phase
A Funding Secured Event will move the system from the Pre-initialization Phase into the Initialization Phase. `//TODO: link to "Funding Secured Event"`

## Phase 1: Initialization
During the Initialization phase, bond funds are raised, launch conditions are specified including ProjectTime, ClaimsSubmitted and Alpha thresholds, and the bond Alpha is initialized to 0.5. `//TODO: What are "bond funds"? Can you give specifc example for this as well wrt a specific project and specific participants? What are "ClaimsSubmitted" and "Alpha thresholds" at this point, who would come up with them and what are their justifications?` 

### Transitions into Initialization Phase
A Funding Secured Event will move the system from the Pre-initialization Phase into the Initialization Phase. `//TODO: link to "Funding Secured Event"`

### Inputs
1. Amount required in Bond Funds 
2. ProjectTime 
3. ClaimsSubmitted 
4. Alpha 

### Next State Outputs
1. Amount raised in Bond Funds 
2. ProjectTime threshold
3. ClaimsSubmitted threshold
4. Alpha threshold

### Transitions out of Initilization Phase
If Funding Threshold = Go, the system will move from the Initialization Phase to the Execution Phase. `//TODO: What is Funding Threshold and how does it equal "Go" or "No-Go". If these are state update functions please introduce the proper context to let the reader know that we are looking at pseudo code and not a protocol for running an organization.`

Else if Funding Threshold = No-Go, the system will move from the Initialization Phase to the Settlement Phase.

## Phase 2: Execution
The execution phase is the phase where active bond trading is occurring.

### Transitions into Execution Phase
1. Initialization Threshold Triggering Event from Initialization Phase
2. Dispute Resolution Return Event to Execution from Dispute Pause Phase
3. A Not Complete Event from the Settlement Consideration Pause Phase

### Inputs
1. Reserve Funds to be Deposited
1. Supply Tokens to be Burned
1. Project Success Attestation Supply Tokens
1. Project Failure Attestation Supply Tokens
1. Dispute Claim
1. Settlement Consideration Claim

### Next State Outputs
1. Amount of Supply Tokens Minted
2. Amount of Reserve Funds Withdrawn
2. Amount of Funds to Project
2. Price Update
3. Alpha Update
1. Reserve Ratio Update
1. Project Attestion Token Ratio

### Transitions out of Execution Phase
1. A Dispute Triggering Event will move from the Execution Phase into the Dispute Pause Phase
2. A Propose Completion Event will move from the Execution Phase into the Settlement Consideration Pause Phase

### Initial State
Once the threshold is met during the Initialization Phase, an output set of initial conditions determine the initial state of the Execution Phase. All values are at time 0:
1. Time to Complete Execution
2. Reserve Funds raised
3. Supply of Tokens Minted
4. Alpha
5. Project Operating Funds
6. Impact Payers Commitment
7. Reserve Ratio
8. Price
9. Maximum Reserve Ratio
10. Minimum Reserve Ratio
11. Fund Fee

## Phase 3: Dispute Pause
In the Dispute Pause Phase, disputes issued against the bond will undergo external resolution. During this state, all system activity except those directly involved in dispute resolution is paused.

### Transitions into Dispute Pause Phase
A Dispute Triggering event moves the system from the Execution Phase to the Dispute Pause Phase.

### Inputs
1. Dispute Issued 
2. Funding Threshold
3. Dispute Resolution External Resolution

### Next State Outputs
1. Dispute Issued 
2. Dispute Verdict

### Transitions out of Dispute Pause Phase
If Dispute Verdict = return to Execution, the system will move from the Dispute Pause Phase back to the Execution Phase.

Else if Dispute Verdict = resolved to completion, the system will move from the Dispute Pause Phase back to the Settlement Consideration Pause Phase.

## Phase 4: Settlement Consideration Pause 
In this phase, the bond is evaluated against the Settlement Conditions for success or failure. Similar to the Dispute Pause Phase, all system activity other than settlement consideration activity is paused during this phase. A detailed view of the Settlement process is shown [here](artifacts/SettlementConsiderationPhase.png).

### Transitions into Settlement Consideration Pause Phase
1. A Propose Completion Event moves the system from the Execution Phase to the Settlement Consideration Pause Phase.
2. If Dispute Verdict = resolved to completion, the system moves from the Dispute Pause Phase back to the Settlement Consideration Phase Phase.

### Inputs
1. Settlement Claim
2. Dispute Verdict
3. Settlement Consideration External Resolution

### Next State Outputs
1. Settlement Verdict

### Transitions out of Settlement Consideration Pause Phase
A Completion event moves the system from the Settlement Consideration Pause Phase to the Settlement Phase

## Phase 5: Settlement
During the settlement phase, bond tokens are converted into a compatible form and are distributed to the participants in the bond.

### Transitions into Settlement Phase
A Completion event moves the system from the Settlement Consideration Pause Phase to the Settlement Phase

### Inputs
1. Bond to Token Conversion
2. Payments to be redeeemed
3. Outcomes Payees
4. Outcomes Payments

### Next State Outputs
1. Fee Distribution
2. Impact Token Distribution
3. Outcomes Payment Distribution

### Transitions out of Settlement Consideration Pause Phase
This is the last phase of the system, thus there are no outward state transitions. 

Continue reading Chapter 3: [System Requirements](3_EngineeringRequirements.md)
