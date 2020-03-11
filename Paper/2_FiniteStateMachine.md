# Phases in Bond Lifecycle
<div align="center">
	<img width="900" height="744" src="img/phases.png" alt="bondlifecyclephases">
	<br>
</div>

## Phase 0: Pre-initialization 

## Phase 1: Initialization

## Phase 2: Execution
The execution phase is the phase where active bond trading is occurring.


### Transitions into Execution Phase
1. Initialization Threshold Triggering Event from Initialization Phase
1. Dispute Resolution Return Event to Execution from Dispute Pause Phase
1. A Not Complete Event from the Settlement Consideration Pause Phase



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
1. A Propose Completion Event will move from the Execution Phase into the Settlement Consideration Pause Phase

### Initial State
Once the threshold is met during the Initialization Phase, an output set of initial conditions determine the initial state of the Execution Phase. All values are at time 0:
1. Time to Complete Execution
1. Reserve Funds raised
1. Supply of Tokens Minted
1. Alpha
1. Project Operating Funds
1. Impact Payers Commitment
1. Reserve Ratio
1. Price
1. Maximum Reserve Ratio
1. Minimum Reserve Ratio
1. Fund Fee

## Phase 3: Dispute Pause

## Phase 4: Settlement Consideration Pause 

## Phase 5: Settlement

