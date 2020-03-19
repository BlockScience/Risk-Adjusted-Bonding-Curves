# Economic Engineering of Risk Adjusted Impact Bonds

### Impact bonds
A social impact bond is a type of bond where repayment to investors is contingent on the bond's success in achieving certain pre-specified social impact objectives. 

### Bonding curves
A bonding curve is a mechanism for distribution of blockchain tokens, in which tokens are automatically issued using buy and sell functions. 
The impact bond bonding curve is parametrically adjusted to mitigate risk, thereby adapting to external events. 

### Problem: Static bonding curves
Current token bonding curve implementations act as automated market makers for initial and ongoing investment. However, they generally are static, with fixed *a priori* assumptions about the interaction between the token economy and its external factors. 
<br/><br/> 
Since these bonding curve implementations are static, they cannot incorpoate external risk factors during live execution. This results in pricing and supply anomalies, such as tokens being misallocated on both buy-side and sell-side, with loss in risk correlation. 
<br/><br/> 
Ultimately, risk remains poorly mitigated, and investors do not receive a fair return on investment.
Systems with compound economic mechanisms (e.g. staking deposits also being used as debt collateral) contain interdependencies that produce non-linear effects. In the case of static bonding curves, risk accumulates in a non-linear fashion which can lead to systemic collapse.

### Solution: Risk Adjusted Bonding Curve for Impact Bonds
The goal of this project is to provide a generalized reusable economic design pattern for outcome dependent funding. 
To maintain practicality, we have anchored it in a motivating use case of alpha-Bonds in the ixo ecosystem. 
alpha-Bonds are currently being implemented for high-profile development projects for improving the quality of primary school education in India. 
<br/><br/> 
The system consists of several impact investors who invest in impact bonds containing social good projects and receive a return contingent on the project's degree of success. 
A bonding curve issues and burns tokens according to the investor's buy and sell decisions. The token price is governed by the bonding curve which is influenced by aggregated investor decisions. Since the system employs a risk-adjusted bonding curve, there exists a parameter alpha which predicts the bond's likelihood of success based on internal and external inputs. Alpha changes as the bond participants in the issue claims or disputes towards the bond or its constituent projects.
<br/><br/> 
The bonding curve thus acts as an estimator of market price and the bond's likelihood of success, alpha.

In the following paper, we demonstrate our entire economic engineering process from discovery and formulating business and engineering requirements to arriving at a suitable mathematical model to be input into a simulation. 
