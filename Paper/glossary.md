# Glossary 

1. Token Economy <br/>
    Bonding Curves are continuous liquidity mechanisms which are used in market design for cryptographically-supported token economies. Academic literature increasingly refers to bonding curves as "configuration spaces" as Bonding Curves are part of a larger theory of scalar functions that remain invariant under legal changes in state.
    
2. Impact Bond <br/>
    A social impact bond is a type of bond where repayment to investors is contingent on the bond's success in achieving certain pre-specified social impact objectives.

3. Bonding Curve <br/>
    Bonding Curves are continuous liquidity mechanisms which are used in market design for cryptographically-supported token economies. Academic literature increasingly refers to bonding curves as "configuration spaces" as Bonding Curves are part of a larger theory of scalar functions that remain invariant under legal changes in state.

4. Alpha <br/>
    The **alpha** signal ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%5Cin%20%5B0%2C1%5D) at time ![img](https://latex.codecogs.com/svg.latex?t) is an estimate of the likelihood of success of the bond, represented normalized such that ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%3D%200) indicates that the project is estimated to fail, and ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%3D%201) indicates the highest likelhood of success.
    
5. Economic engineering <br/>
	The professional discipline around the design, modelling, analysis, implementation and steering of economic systems, rooted in and drawing from the well-established scientific body of knowledge of System Theory, Control Systems Engineering, Operations Research, Mathematics, and several other relevant fields.

6. State Space <br/>
    Set of all possible configurations of a system. It is a useful abstraction for reasoning about the behavior of a given system and is widely used in the fields of artificial intelligence and game theory. May be interpreted as that collection of variables which serve to define the system at any point in time.

7. Action space <br/>
    The set $U(X_a; x)$ represents the set of feasible actions, given agent a’s local state space $X_a$, and the global state $x$.

8. Configuration space <br/>
    Reachable state space. Subset of a system's (global) state space, representing all achievable states under the designed mechanisms. Any global properties true for all points in the configuration space are true for all possible sequences of actions on the part of agents. A Manifold characterized by the enforced conservation of one or more desired global properties. Resulting induced state space after introducing internally consistent restrictions to the global state spac. Serves the role of enforcing desirable macro-economic properties, while retaining sufficient degrees of freedom for the agents at the micro level to act according to their own private preferences.

9. Markov chain <br/>
    A Markov chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. In continuous-time, it is known as a Markov process. Markov processes are the basis for general stochastic simulation methods known as Markov chain Monte Carlo

10. Portfolio
    Similar to an investment portfolio, a bond consists of multiple bonds picked by an investor, based on their preferences, evaluated on their risk/return ratio.
    
11. Bond-to-mint <br/>
    The **bond-to-mint** mechanism mints impact tokens in exchange of bond tokens through an agent’s action ![img](https://latex.codecogs.com/svg.latex?u_%7Ba%2C%20t%7D). The agent’s action represents a transaction to transfer ![img](https://latex.codecogs.com/svg.latex?%5CDelta%20R_t%20%3A%3D%20r_%7Ba%2Ct%7D%20-%20r_%7Ba%2C%20t&plus;1%7D%20%5Cgeq%200) quantity of bond tokens into the bonding curve system. 

12. Burn-to-withdraw <br/>
    The **burn-to-withdraw** mechanism removes impact tokens to redeem bond tokens through an agent’s action ![img](https://latex.codecogs.com/svg.latex?u_%7Ba%2C%20t%7D). The agent’s action represents a transaction to remove ![img](https://latex.codecogs.com/svg.latex?%5CDelta%20S_t%20%3A%3D%20s_%7Ba%2C%20t%7D%20-%20s_%7Ba%2C%20t&plus;1%7D%20%5Cleq%200) quantity of impact tokens from the bonding curve system. 

13. Attestation <br/>
    The **attestation** mechanism involves the lifecylce of claims. Claims undergo the stages of submission, evaluation, and resolution. During resolution, if a claim does not reflect the state of the bonding curve, a dispute is issued against it to regain the bonding curve state.
    
14. Pre-initialization phase <br/>
    During the pre-initialization phase, the bond is set up with an associated wallet and repository, bond parameters are initialized for best-fit to the project, the receipients of project funds are set, and all bond participants are identified with digital IDs, public keys, and credentials. The bond also acquires non-bond investment such as resources, materials, and equipment. 

15. Initialization phase <br/>
    During the Initialization Phase, bond funds are raised, conditions for project launch are specified including ProjectTime, ClaimsSubmitted and Alpha thresholds, and the bond Alpha is initialized to 0.5.

16. Execution phase <br/>
    The execution phase is the phase where active bond trading occurs.

17. Dispute pause phase
    In the Dispute Pause Phase, disputes issued against the bond will undergo external resolution. During this state, all system activity except those directly involved in dispute resolution is paused.

18. Settlement Consideration Pause Phase <br/>
    In this phase, the bond is evaluated against the Settlement Conditions for success or failure. Similar to the Dispute Pause Phase, all system activity other than settlement consideration activity is paused during this phase. A detailed view of the Settlement process is shown [here](artifacts/SettlementConsiderationPhase.png).

19. Settlement phase <br/>
    During the Settlement Phase, Bond Tokens are converted into a compatible form and are distributed to the participants in the bond.

20. Impact token <br/>
    Impact tokens are the the supply or community tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), the local state of agent ![img](https://latex.codecogs.com/svg.latex?a) comprises of the individual holding of Impact Tokens, ![img](https://latex.codecogs.com/svg.latex?s_%7Ba%2Ct%7D).

21. Bond token <br/>
    Bond Tokens are the bond's reserve currency tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), each agent ![img](https://latex.codecogs.com/svg.latex?a) possess their holding of Bond Tokens, denoted by ![img](https://latex.codecogs.com/svg.latex?r_%7Ba%2Ct%7D%3E0).

22. Operational requirement 1 <br/>
    Trader Agents can call the Bond Action and the Burn Action. 

23. Operational requirement 2 <br/>
    An agent which is able to execute the *Bond-to-Mint* or *Burn-to-Withdraw* mechanisms - such as Trader Agents - must not be involved in the Claim Evaluation, Claim Auditing, and Claim Resolution stages of the *Attestation* mechanism. 

24. Operational requirement 3 <br/>
    Claim & Dispute Issuers call the SubmitClaim Action or SubmitDispute Action

25. Operational Requirment 4 <br/>
    Claim & Dispute Issuers are explicity excluded from having the ability to call EvaluateClaim Action, AuditClaim Action, or ResolveClaim Action.

26. Operational requirement 5 <br/>
    Evaluators can call the EvaluateClaim Action, AuditClaim Action, or ResolveClaim Action to process Claims, or the EvaluateDispute Action or ResolveDispute Action to process Disputes

27. Operational Requirement 6 <br/>
    Agents involved in the Claim Evaluation, Claim Auditing, and Claim Resolution stages of the *Attestation* mechanism, such as Claim & Dispute Evaluators, are explictly excluded from holding or trading bond tokens as it results in a conflict of interest. 
    
28. ProjectTime threshold <br/>
    The **ProjectTime** state variable ![img](https://latex.codecogs.com/svg.latex?p%20%5Cin%20%5Cmathbb%7BZ%7D_%7B&plus;&plus;%7D) describes the duration for which the project has been in the Execution phase.<br/> 

    The **ProjectTime threshold** ![img](https://latex.codecogs.com/svg.latex?p_%7Blim%7D) describes the maximum allowable duration for a project's Execution phase. 

29. ClaimsSubmitted threshold <br/>
    The **ClaimsSubmitted** state variable ![img](https://latex.codecogs.com/svg.latex?c%20%5Cin%20%5Cmathbb%7BZ%7D_%7B&plus;%7D) describes the number of claims submitted towards the project during its Execution phase. <br/>

    The **ClaimsSubmitted threshold** ![img](https://latex.codecogs.com/svg.latex?c_%7Blim%7D) describes the minimum number of claims required to be collected during the project's Execution phase. 

30. Alpha threshold <br/>
    The **Alpha** state variable ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%5Cin%20%5B0%2C1%5D) is an estimate of the probability of project success, as evaluated by the Alpha Oracle. It is represented normalized such that ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D%200) indicates that the project is estimated to fail, and ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D%201) indicates the highest likelhood of success. <br/>

    The initial value of Alpha is 0.5, as a default. <br/>

    The **Alpha threshold** is ![img](https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D) describes the minimum alpha value required for the settlement to be successful. ![img](https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D) is set to a positive finite integer during project initialization.

31. Reserve Funds <br/>
    The **reserve** ![img](https://latex.codecogs.com/svg.latex?R_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D). at time ![img](https://latex.codecogs.com/svg.latex?t) is the total quantity of bond tokens bonded to the bonding curve contract. <br/>

    Bond Tokens are reserve currency tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), each agent ![img](https://latex.codecogs.com/svg.latex?a) possess their holding of Bond Tokens, denoted by ![img](https://latex.codecogs.com/svg.latex?r_%7Ba%2Ct%7D%3E0).

32. Supply Tokens <br/>
    The **supply** ![img](https://latex.codecogs.com/svg.latex?S_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D) at time ![img](https://latex.codecogs.com/svg.latex?t) is the total quantity of impact tokens issued by the bonding curve contract. <br/>

    Impact tokens are community tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), the local state of agent ![img](https://latex.codecogs.com/svg.latex?a) comprises of the individual holding of Impact Tokens, ![img](https://latex.codecogs.com/svg.latex?s_%7Ba%2Ct%7D).
    
33. Project Success Attestation Supply Tokens <br/>
    Supply or Impact Tokens that are bonded to attest that the project will succeed.
    
50. Project Failure Attestation Supply Tokens <br/>
    Supply or Impact Tokens that are bonded to attest that the project will fail.
    
34. Reserve Ratio <br/>
    The Reserve Ratio $\rho \in [0, 1]$ is determined by the curvature of the bonding curve $\kappa$, and is given by $$ \rho = 1/\kappa$$

35. Price <br/>
    The **price** signal ![img](https://latex.codecogs.com/svg.latex?P_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D) at time ![img](https://latex.codecogs.com/svg.latex?t) is an estimate of the value of the bond token, in units of ![img](https://latex.codecogs.com/svg.latex?R) per units of ![img](https://latex.codecogs.com/svg.latex?S).

36. Impact Payers Commitment <br/>
    Outcome Payer's commitment of a set amount of tokens that they will pay out during the Settlement Phase conditioned on one or many state variables, typically ![img](https://latex.codecogs.com/gif.latex?$\Omega$). The outcome payers' commitment $C\in\mathbb{R}_+$ is set during the Initialization Phase. The bond terms set during Initialization outline all $(C, \Omega)$ pairs, and remain constant through the following phases. $C$ is known to all agents after the Initialization phase. 

37. Initialization Conditions <br/>
    Criteria specified at the Initialization Phase which need to be met for the state to transition into the Execution phase. In the bonding curve use case, the initialization conditions are also referred to as launch conditions.

38. Settlement Conditions <br/>
    Conditions that need to be achieved by the bond during the Executuion Phase for a bond to be considered successful.

39. Conservation function <br/>
    The bonding curve **conservation function** describes a conserved quantity, which is a functional relationship between the reserve and supply tokens. <br/>
    
    This conservation function imposed over the bonding curve ensures that the price of the token reflects the amount invested into projects in the platform, thus preventing imbalances through incentive design.
