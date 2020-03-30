# Glossary 

<a id="note1" href="#note1ref">1</a> **Token Economy** <br/>
<p> Token economies are data-driven, multiscale, adaptive, and dynamic peer-to-peer economic systems enabled by a blockchain.These systems use cryptographic tokens as information carriers, allowing for economic activities to emerge on top of a shared distributed ledger technology (DLT) enabled infrastructure such as blockchain. DLT creates the conditions for a digital economic game with enforced state-space restrictions, by providing a tamper-proof universal state layer. </p>
    
<a id="note2" href="#note2ref">2</a> **Impact Bond** <br/>
<p> A social impact bond is a type of bond where repayment to investors is contingent on the bond's success in achieving certain pre-specified social impact objectives. </p>

<a id="note3" href="#note3ref">3</a> **Bonding Curve** <br/>
<p> Bonding Curves are continuous liquidity mechanisms which are used in market design for cryptographically-supported token economies. Academic literature increasingly refers to bonding curves as "configuration spaces" as Bonding Curves are part of a larger theory of scalar functions that remain invariant under legal changes in state. </p>

<a id="note4" href="#note4ref">4</a>  **Alpha** <br/> <br/>
The **alpha** signal ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%5Cin%20%5B0%2C1%5D) at time ![img](https://latex.codecogs.com/svg.latex?t) is an estimate of the likelihood of success of the bond, represented normalized such that ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%3D%200) indicates that the project is estimated to fail, and ![img](https://latex.codecogs.com/svg.latex?%5Calpha_b%20%3D%201) indicates the highest likelhood of success.
    
<a id="note5" href="#note5ref">5</a>  **Economic engineering** <br/>
<p>	The professional discipline around the design, modelling, analysis, implementation and steering of economic systems, rooted in and drawing from the well-established scientific body of knowledge of System Theory, Control Systems Engineering, Operations Research, Mathematics, and several other relevant fields. </p>

<a id="note6" href="#note6ref">6</a> **State Space** <br/>
<p>   Set of all possible configurations of a system. It is a useful abstraction for reasoning about the behavior of a given system and is widely used in the fields of artificial intelligence and game theory. May be interpreted as that collection of variables which serve to define the system at any point in time. </p>

<a id="note7" href="#note7ref">7</a> **Action space** <br/> <br/>
    The set ![img](https://latex.codecogs.com/svg.latex?U%28X_a%3B%20x%29) represents the set of feasible actions, given agent a’s local state space ![img](https://latex.codecogs.com/svg.latex?X_a), and the global state ![img](https://latex.codecogs.com/svg.latex?X).

<a id="note8" href="#note8ref">8</a> **Configuration space** <br/>
<p> Reachable state space.The configuration space describes the *allowable* state and action space available to agents acting within a system, given its conservation laws. It is a subset of a system's (global) state space, representing all achievable states under the designed mechanisms. Any global properties that are true for all points in the configuration space are true for all possible sequences of actions on the part of agents. It is a manifold characterized by the enforced conservation of one or more desired global properties. The configuration space serves the role of enforcing desirable macro-economic properties, while retaining sufficient degrees of freedom for the agents at the micro level to act according to their own private preferences. </p>

<a id="note9" href="#note9ref">9</a> **Markov chain** <br/>
 <p> A Markov chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. In continuous-time, it is known as a Markov process. Markov processes are the basis for general stochastic simulation methods known as Markov chain Monte Carlo. </p>

<a id="note10" href="#note10ref">10</a> **Portfolio** <br/>
<p>   Similar to an investment portfolio, a bond consists of multiple bonds picked by an investor, based on their preferences, evaluated on their risk/return ratio.  </p>
    
<a id="note11" href="#note11ref">11</a> **Bond-to-mint** <br/><br/>
    The bond-to-mint mechanism mints impact tokens in exchange of bond tokens through an agent’s action ![img](https://latex.codecogs.com/svg.latex?u_%7Ba%2C%20t%7D). The agent’s action represents a transaction to transfer ![img](https://latex.codecogs.com/svg.latex?%5CDelta%20R_t%20%3A%3D%20r_%7Ba%2Ct%7D%20-%20r_%7Ba%2C%20t&plus;1%7D%20%5Cgeq%200) quantity of bond tokens into the bonding curve system. 

<a id="note12" href="#note12ref">12</a> **Burn-to-withdraw** <br/><br/>
    The burn-to-withdraw mechanism removes impact tokens to redeem bond tokens through an agent’s action ![img](https://latex.codecogs.com/svg.latex?u_%7Ba%2C%20t%7D). The agent’s action represents a transaction to remove ![img](https://latex.codecogs.com/svg.latex?%5CDelta%20S_t%20%3A%3D%20s_%7Ba%2C%20t%7D%20-%20s_%7Ba%2C%20t&plus;1%7D%20%5Cleq%200) quantity of impact tokens from the bonding curve system. 

<a id="note13" href="#note13ref">13</a> **Attestation** <br/><br/>
    The **attestation** mechanism involves the lifecylce of claims. Claims undergo the stages of submission, evaluation, and resolution. During resolution, if a claim does not reflect the state of the bonding curve, a dispute is issued against it to regain the bonding curve state.
    
<a id="note14" href="#note14ref">14</a> **Pre-initialization Phase** <br/>
<p> During the pre-initialization phase, the bond is set up with an associated wallet and repository, bond parameters are initialized for best-fit to the project, the receipients of project funds are set, and all bond participants are identified with digital IDs, public keys, and credentials. The bond also acquires non-bond investment such as resources, materials, and equipment. </p>
    
<a id="note15" href="#note15ref">15</a> **Initialization Phase** <br/>
<p>     During the Initialization Phase, bond funds are raised, conditions for project launch are specified including ProjectTime, ClaimsSubmitted and Alpha thresholds, and the bond Alpha is initialized to 0.5. </p>

<a id="note16" href="#note16ref">16</a> **Execution Phase** <br/>
<p>     The execution phase is the phase where active bond trading occurs. </p>

<a id="note17" href="#note17ref">17</a> **Dispute Pause Phase** <br/>
<p>     In the Dispute Pause Phase, disputes issued against the bond will undergo external resolution. During this state, all system activity except those directly involved in dispute resolution is paused. </p>

<a id="note18" href="#note18ref">18</a> **Settlement Consideration Pause Phase** <br/><br/>
  In this phase, the bond is evaluated against the Settlement Conditions for success or failure. Similar to the Dispute Pause Phase, all system activity other than settlement consideration activity is paused during this phase. A detailed view of the Settlement process is shown [here](artifacts/SettlementConsiderationPhase.png). 

<a id="note19" href="#note19ref">19</a> **Settlement Phase** <br/>
<p>     During the Settlement Phase, Bond Tokens are converted into a compatible form and are distributed to the participants in the bond. </p>

<a id="note20" href="#note20ref">20</a> **Impact Token** <br/><br/>
    Impact tokens are the the supply or community tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), the local state of agent ![img](https://latex.codecogs.com/svg.latex?a) comprises of the individual holding of Impact Tokens, ![img](https://latex.codecogs.com/svg.latex?s_%7Ba%2Ct%7D).

<a id="note21" href="#note21ref">21</a> **Bond Token** <br/><br/>
    Bond Tokens are the bond's reserve currency tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), each agent ![img](https://latex.codecogs.com/svg.latex?a) possess their holding of Bond Tokens, denoted by ![img](https://latex.codecogs.com/svg.latex?r_%7Ba%2Ct%7D%3E0).

<a id="note22" href="#note22ref">22</a> **Operational requirement 1** <br/>
 <p>   Trader Agents can call the Bond Action and the Burn Action. </p>

<a id="note23" href="#note23ref">23</a> **Operational requirement 2** <br/>
<p>    An agent which is able to execute the *Bond-to-Mint* or *Burn-to-Withdraw* mechanisms - such as Trader Agents - must not be involved in the Claim Evaluation, Claim Auditing, and Claim Resolution stages of the *Attestation* mechanism. </p>

<a id="note24" href="#note24ref">24</a> **Operational requirement 3** <br/>
<p>    Claim & Dispute Issuers call the SubmitClaim Action or SubmitDispute Action. </p>

<a id="note25" href="#note25ref">25</a> **Operational requirment 4** <br/>
<p>    Claim & Dispute Issuers are explicity excluded from having the ability to call EvaluateClaim Action, AuditClaim Action, or ResolveClaim Action. </p>

<a id="note26" href="#note26ref">26</a> **Operational requirement 5** <br/>
<p>    Evaluators can call the EvaluateClaim Action, AuditClaim Action, or ResolveClaim Action to process Claims, or the EvaluateDispute Action or ResolveDispute Action to process Disputes. </p>

<a id="note27" href="#note27ref">27</a> **Operational requirement 6** <br/>
<p>    Agents involved in the Claim Evaluation, Claim Auditing, and Claim Resolution stages of the *Attestation* mechanism, such as Claim & Dispute Evaluators, are explictly excluded from holding or trading bond tokens as it results in a conflict of interest. </p>
    
<a id="note28" href="#note28ref">28</a> **ProjectTime** <br/><br/>
    The ProjectTime state variable ![img](https://latex.codecogs.com/svg.latex?p%20%5Cin%20%5Cmathbb%7BZ%7D_%7B&plus;&plus;%7D) describes the duration for which the project has been in the Execution phase.

<a id="note29" href="#note29ref">29</a> **ProjectTime threshold** <br/><br/>
    The ProjectTime threshold ![img](https://latex.codecogs.com/svg.latex?p_%7Blim%7D) describes the maximum allowable duration for a project's Execution phase. 

<a id="note30" href="#note30ref">30</a> **ClaimsSubmitted** <br/><br/>
    The ClaimsSubmitted state variable ![img](https://latex.codecogs.com/svg.latex?c%20%5Cin%20%5Cmathbb%7BZ%7D_%7B&plus;%7D) describes the number of claims submitted towards the project during its Execution phase.

<a id="note31" href="#note31ref">31</a> **ClaimsSubmitted threshold** <br/>  
    The ClaimsSubmitted threshold ![img](https://latex.codecogs.com/svg.latex?c_%7Blim%7D) describes the minimum number of claims required to be collected during the project's Execution phase. 

<a id="note32" href="#note32ref">32</a> **Alpha (state variable)** <br/><br/>
    The Alpha state variable ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%5Cin%20%5B0%2C1%5D) is an estimate of the probability of project success, as evaluated by the Alpha Oracle. It is represented normalized such that ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D%200) indicates that the project is estimated to fail, and ![img](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D%201) indicates the highest likelhood of success. <br/>

   The initial value of Alpha is 0.5, as a default. 

<a id="note33" href="#note33ref">33</a> **Alpha threshold** <br/><br/> 
    The Alpha threshold is ![img](https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D) describes the minimum alpha value required for the settlement to be successful. ![img](https://latex.codecogs.com/svg.latex?%5Calpha_%7Blim%7D) is set to a positive finite integer during project initialization.

<a id="note34" href="#note34ref">34</a> **Reserve Funds** <br/><br/>
    The reserve ![img](https://latex.codecogs.com/svg.latex?R_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D). at time ![img](https://latex.codecogs.com/svg.latex?t) is the total quantity of bond tokens bonded to the bonding curve contract. <br/>

   Bond Tokens are reserve currency tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), each agent ![img](https://latex.codecogs.com/svg.latex?a) possess their holding of Bond Tokens, denoted by ![img](https://latex.codecogs.com/svg.latex?r_%7Ba%2Ct%7D%3E0).

<a id="note35" href="#note35ref">35</a> **Supply Tokens** <br/><br/>
    The supply ![img](https://latex.codecogs.com/svg.latex?S_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D) at time ![img](https://latex.codecogs.com/svg.latex?t) is the total quantity of impact tokens issued by the bonding curve contract. <br/>

   Impact tokens are community tokens. At time ![img](https://latex.codecogs.com/svg.latex?t), the local state of agent ![img](https://latex.codecogs.com/svg.latex?a) comprises of the individual holding of Impact Tokens, ![img](https://latex.codecogs.com/svg.latex?s_%7Ba%2Ct%7D).
    
<a id="note36" href="#note36ref">36</a> **Project Success Attestation Supply Tokens** <br/>
<p>    Supply or Impact Tokens that are bonded to attest that the project will succeed. </p>
    
<a id="note37" href="#note37ref">37</a> **Project Failure Attestation Supply Tokens** <br/>
<p>     Supply or Impact Tokens that are bonded to attest that the project will fail. </p>
    
<a id="note38" href="#note38ref">38</a> **Reserve Ratio** <br/><br/>
    The Reserve Ratio ![img](https://latex.codecogs.com/svg.latex?\rho&space;\in&space;[0,&space;1]) is determined by the curvature of the bonding curve ![img](https://latex.codecogs.com/svg.latex?$\kappa$), and is given by ![img](https://latex.codecogs.com/svg.latex?$$&space;\rho&space;=&space;1/\kappa$$)

<a id="note39" href="#note39ref">39</a> **Price** <br/><br/>
    The price signal ![img](https://latex.codecogs.com/svg.latex?P_t%20%5Cin%20%5Cmathbb%7BR%7D_%7B&plus;&plus;%7D) at time ![img](https://latex.codecogs.com/svg.latex?t) is an estimate of the value of the bond token, in units of ![img](https://latex.codecogs.com/svg.latex?R) per units of ![img](https://latex.codecogs.com/svg.latex?S).

<a id="note40" href="#note40ref">40</a> **Impact Payers Commitment** <br/><br/>
    Outcome Payer's commitment of a set amount of tokens that they will pay out during the Settlement Phase conditioned on one or many state variables, typically ![img](https://latex.codecogs.com/svg.latex?$\Omega$). The outcome payers' commitment  ![img](https://latex.codecogs.com/svg.latex?$C\in\mathbb{R}_&plus;$) is set during the Initialization Phase. The bond terms set during Initialization outline all $(C, \Omega)$ pairs, and remain constant through the following phases. ![img](https://latex.codecogs.com/svg.latex?$C$) is known to all agents after the Initialization phase. 

<a id="note41" href="#note41ref">41</a> **Initialization Conditions** <br/>
<p>     Criteria specified at the Initialization Phase which need to be met for the state to transition into the Execution phase. In the bonding curve use case, the initialization conditions are also referred to as launch conditions. </p>

<a id="note42" href="#note42ref">42</a> **Settlement Conditions** <br/>
<p>     Conditions that need to be achieved by the bond during the Executuion Phase for a bond to be considered successful. </p>

<a id="note43" href="#note43ref">43</a> **Conservation function** <br/>
<p>     The bonding curve conservation function describes a conserved quantity, which is a functional relationship between the reserve and supply tokens. <br/>
    
   This conservation function imposed over the bonding curve ensures that the price of the token reflects the amount invested into projects in the platform, thus preventing imbalances through incentive design. </p>
