# Two Harnesses and a Limit

People who build AI agents call the machinery around a model "the harness". The model predicts text. The harness turns those predictions into action: it supplies context, exposes tools, checks permissions on every action, and records what happened. The word comes from horses, where a harness couples an animal’s strength to a load and determines where it can pull.

An agent harness works on the actor in two ways: alignment tries to make it behave well, and permission checks bound what it may try. Both are useful, but both place the guarantee inside the actor. Each actor needs its own safeguards, and more capable actors are harder to constrain. A permission check illustrates the problem: forbidding a behavior requires anticipating it, and a stronger model can find a move its designer missed.

Other engineering disciplines address this problem by constraining the system in which an actor works. A circuit breaker cuts the power when a fault occurs, whatever caused it. In the 1800s, railway engineers built interlocking lever frames that physically prevented signalmen from setting two colliding routes at once. Safety depended on the arrangement of the levers rather than the signalman’s care. In both examples, breaking the invariant requires the mechanism itself to fail.

Call an actor’s safeguards a permission harness, and these constraints on its environment a world harness. A world harness checks a proposed change without predicting the tactic that produced it. A brilliant adversary and a careless actor face the same check. Provided that check is sound for its invariant, greater sophistication in the actor does not weaken it. Every actor that enters the system inherits the constraint, including actors that do not yet exist.

Security researchers made this argument decades ago, including in debates over capability systems and access-control lists. Lessig’s "code is law" made the broader point that software architecture can constrain behavior more reliably than rules. AI gives the argument urgency wherever an actor’s capability grows faster than we can revise the predictions on which its permission checks depend.

For AI, a world harness would have to operate through institutions: accounts, contracts, companies, licenses, and payments. These are where an agent’s actions become binding. Institutional safeguards have mostly worked after the fact. Double-entry bookkeeping does not prevent a fraudulent entry. It makes certain inconsistencies detectable afterward. Audits search for damage that has already happened.

A software ledger, however, can refuse an unbalanced entry before it posts. That shifts the check to the moment of action. Carry the shift through the institution, and its rules execute as software that checks each change as it happens. [A programmable institution](https://research.momentum.inc/papers/programmable-institutions.html) applies these constraints where agent actions become binding.

I have an interest in this argument: I spend my days building such institutions. Readers should discount accordingly. I think the argument survives that discount because its hardest requirement came from outside and applies to the builder.

Institutional checks cover actions involving money, property, and law, where agents can cause the most durable damage. These are the domains of most activity we police by audit. They cannot cover everything an AI could do wrong. Both harnesses therefore have a role. Permission checks can stop a bad action at its source, quickly and cheaply. Institutional checks must handle actions that get past them.

The operator poses the hardest problem. Whoever runs a check can change it. If one company can quietly alter the constraints, it concentrates the risk from a thousand unpredictable agents in one predictable operator. A government that adopted such a system would delegate control of its institutions to the operator. The design must answer that objection.

I know this requirement from experience. Governments ask whether the system will constrain us. It must bind its builder through the same mechanism that binds everyone else.

The operator’s changes pass through the same checks, with no administrative bypass. A rule change is itself checked and recorded, proposed openly, effective from a stated date, and never retroactive. [Each jurisdiction runs its own check under its own law.](https://research.momentum.inc/papers/sovereign-jurisdiction-network.html) The receiving jurisdiction verifies a change again when it crosses a border. The design goal is to prevent any participant, including the software’s author, from altering the rules without detection.

This connects safety to sovereignty. Safety requires the system to refuse illegal changes regardless of the actor’s capability. Sovereignty requires a network whose operator cannot quietly alter the constraints. Governments call that neutrality. An operator bypass defeats both requirements. It puts the strongest actor back under a permission harness, where the guarantee depends on that actor’s behavior.

A world harness guarantees that actions within its coverage follow the rules as written. This limits both where the guarantee applies and what it can achieve.

Coverage is the first limit. An actor can persuade a human or use a system with no checks. Protection grows only as the checked environment grows, which makes ease of use part of the safety problem. That environment must offer the fastest, easiest way to start a company, move money, or prove identity.

If people and agents choose the path with least friction, the legal path must be the easy path. Coverage then grows with each actor that chooses it. Safety can reach scale through convenience.

Even complete coverage would leave the choice of rules to people. A world harness enforces the law as written. Where the law requires judgment, a person makes that judgment, and the system records who decided and under what authority. Perfect enforcement of a bad law still gives bad law. A harness directs strength and turns it into work. Choosing what work it should do remains a human responsibility.
