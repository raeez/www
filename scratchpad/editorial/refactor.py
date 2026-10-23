from pathlib import Path
import re,json
p=Path(__file__).resolve().parents[2]/'content/reader-papers'
changes={
 'title-remedies-and-institutional-change':[
 ("The buyer can acquire the existing right without acquiring an unencumbered right or another five grams.","The buyer acquires the existing encumbered right, with no additional five-gram allocation."),
 ("Similar problems arise when delivery is disputed, an award remains unpaid, or a successor institution takes over unfinished work.","The same preservation problem arises with disputed delivery, an unpaid award, or a successor institution taking over unfinished work."),
 ("The transaction changes the holder. It leaves the same metal, debt, security interest, and priority in place.","The transaction changes the holder while retaining the same metal, debt, security interest, and priority."),
 ("A new holder's name cannot turn missing metal into present metal.",""),
 ("The answer requires more than a balance. It requires the exact right, its physical support, the authority for changing it, and everything already done toward performance.","A balance alone is insufficient. The record must identify the exact right, its physical support, the authority for changing it, and all performance to date."),
 ("The first depends on effective property arrangements and actual custody. The second depends on an obligor's performance.","Ownership depends on effective property arrangements and actual custody, while the promise depends on an obligor's performance."),
 ("The construction identifies each physical lot and its quantity. Different descriptions of the same lot cannot create additional capacity. It assigns non-overlapping quantity portions to holdings.","The construction identifies each physical lot and its quantity, then assigns non-overlapping quantity portions to holdings. Different descriptions of the same lot cannot create additional capacity."),
 ("A holding has one of three bases, and the register shows which on the face of the balance.","The register states which of three bases applies to each holding, directly on the balance."),
 ("title is an undivided share of one identified bulk in one vault whose bar list is published; it is the form that lets a holder of less than a bar own metal.","title is an undivided share of one identified bulk in one vault, with a published bar list. It lets a holder own less than a bar."),
 ("Only then is each buyer's share reduced in proportion, as the Sale of Goods Act 1979, section 20A, provides.","Any remaining loss reduces each buyer's share in proportion, as the Sale of Goods Act 1979, section 20A, provides."),
 ("One unit then trades for the whole pool, so liquidity does not split by bar list.","One unit trades for the whole pool, keeping liquidity together across its bar list."),
 ("Money needs comparable care.","Payment records must also preserve quantity."),
 ("Cash available for a new payment is separate: the institution may already have spent money received earlier.","Cash available for a new payment is a separate quantity because the institution may already have spent money received earlier."),
 ("Reconciliation compares five records, not four:","Reconciliation compares five records:"),
 ("For metal the register is the custodian's record of each pool. For securities and fund units it is the transfer agent's.","For metal, the register is the custodian's record of each pool. For securities and fund units, it is the transfer agent's."),
 ("Where the ledger is only a projection of the register, a transfer reads", "Where the ledger is only a projection of the register, a transfer reads"),
 ("until the register posts it, and legal effect follows the register.","until the register posts it. Legal effect follows the register."),
 ("Even aggregate equality can mislead.","Equal aggregate quantities can conceal different legal states."),
 ("Unfinished instructions are part of this decision.","Admission must also account for unfinished instructions."),
 ("Completion requires a reservation, a stable guard admitting the transaction, and weak fairness, meaning continuously enabled work eventually receives service.","Completion requires a reservation, a stable guard admitting the transaction, and weak fairness. Weak fairness means continuously enabled work eventually receives service."),
 ("Forty conforming kilograms are delivered and accepted. They earn 400 units.","Delivery and acceptance of forty conforming kilograms earn 400 units."),
 ("The acceptance cannot rest on a weight report alone. It must bind the relevant quantity, measurement, assay where required, title and delivery conditions, receiving decision, and current authority.","Acceptance requires more than a weight report. It must bind the relevant quantity, measurement, assay where required, title and delivery conditions, receiving decision, and current authority."),
 ("Serializing allocation means competing uses are decided in one order against the same current state.","The allocation authority decides competing uses in one order against the same current state."),
 ("Correction presents a different problem from initial acceptance.","A correction must also account for earlier acceptance and payment."),
 ("The stay changes present permission to act. It does not undo the voluntary payment or the earlier custody release merely by entering the record.","Entering the stay in the record changes present permission to act. It does not undo the voluntary payment or the earlier custody release."),
 ("This design does not declare every historical conclusion immutable.","Historical legal conclusions remain subject to revision."),
 ("The theorem's preservation statement is deliberately narrower than", "The theorem therefore does not assert"),
 ("The theorem checks how their determinations are used. It proves none of those predicates true.","The theorem checks how their determinations are used, without proving those predicates true."),
 ("The institution's remuneration rule addresses a different incentive.","The remuneration rule addresses the decision maker's financial incentives."),
 ("A successor inherits an 85-unit obligation, but has no capacity for an additional independent 85-unit command. The existing command already occupies it.","A successor inherits an 85-unit obligation. The existing command occupies its capacity, leaving none for an additional independent 85-unit command."),
 ("including effects already made but not yet reflected at the accounting cutoff.","including effects that have occurred but are not yet reflected at the accounting cutoff."),
 ("The successor needs more than a document archive and current balance.","A document archive and current balance are insufficient for the successor to resume work."),
 ("Useful completion needs additional service assumptions.","Completion requires additional service assumptions."),
 ("The constructions therefore preserve obligations through change without promising that change will resolve them.","Preserving obligations through change leaves their completion subject to these service assumptions."),
 ("These are specific remaining duties or obstructions. Removing them from the successor's record would conceal the work that still needs an authorized actor.","These remaining duties or obstructions identify work for an authorized actor. Removing them from the successor's record would conceal that work."),
 ],
 'when-institutional-programs-work-together':[
 ("Institutional composition asks for one executable strategy that meets every condition and preserves the requested outcome.","Institutional composition requires one executable strategy that meets every condition and preserves the requested outcome."),
 ("A buyer has 120 units and needs an asset delivered. The first supplier charges 100.","A buyer has 120 units and needs delivery of an asset priced at 100 by the first supplier."),
 ("Its ordinary route pays the first supplier immediately. If delivery fails, that payment remains unavailable throughout the required period.","Under the ordinary route, the buyer pays the first supplier immediately. If delivery fails, that payment remains unavailable throughout the required period."),
 ("The buyer then needs another 120 for replacement delivery. The failure branch therefore requires initial funding of 220. The primary success branch requires 100.","Replacement delivery then needs another 120, so the failure branch requires initial funding of 220. The primary success branch requires 100."),
 ("The conditional route reserves 100 in escrow. Delivery releases that amount to the first supplier.","The conditional route reserves 100 in escrow for release to the first supplier upon delivery."),
 ("This case identifies the composition problem. The supplier, escrow provider, and standby supplier must support the same acquisition under compatible conditions.","Composition requires the supplier, escrow provider, and standby supplier to support the same acquisition under compatible conditions."),
 ("An institutional program records the permitted actions and their consequences through this shared request.","An institutional program records the actions permitted for this shared request and their consequences."),
 ("These conditions give different problems.","Each condition defines a different problem."),
 ("An application transmission and an authoritative registration have different results. A provider's acceptance and its completed payment have different results.","Transmitting an application differs from registering it authoritatively, just as accepting a payment instruction differs from completing payment."),
 ("The designer selects a supplier or a conditional payment route. It must then cover every outcome that the chosen contract admits.","The designer selects a supplier or a conditional payment route, then must cover every outcome that the chosen contract admits."),
 ("Selecting a favorable future result inside an optimization would remove the very risk the strategy must handle.","Selecting a favorable future result within the optimization would exclude risks the strategy must handle."),
 ("Two changes can make the example feasible. An authorized observation can distinguish the worlds. Alternatively, an authorized and funded common action can succeed in both.","An authorized observation that distinguishes the worlds can make the example feasible. So can an authorized and funded common action that succeeds in both."),
 ("The institution must acquire the evidence or capability that makes the selected change real.","The institution must acquire the evidence or capability needed for its selected change."),
 ("A finite relation is a table of permitted combinations. One table can constrain route and authority. Another can constrain route, capital, and supplier. A third can constrain the observation plan.","A finite relation is a table of permitted combinations. Separate tables can constrain route and authority, route with capital and supplier, and the observation plan."),
 ("A surviving root row then extends to a full assignment through retained matches. The connectedness condition ensures that choices agree across branches.","The connectedness condition ensures that choices agree across branches."),
 ("Conversely, the retained matches extend a surviving root through the whole tree.","Conversely, retained matches extend a surviving root row to a full assignment through the whole tree."),
 ("The size of those groups affects the work required.","Larger groups require more computational work."),
 ("Finiteness makes this process stop. These maximal cells cover the admissible relation.","The process stops because the relation is finite. Its maximal cells cover the admissible relation."),
 ("They can differ, and some retain little useful choice. Maximality therefore specifies permitted extension within a fixed model.","Maximal cells can differ, and some retain little useful choice. Maximality specifies how far menus can extend within a fixed model."),
 ("The capacity example also admits an exact count.","The capacity example gives an exact count of independent-choice cells."),
 ("With capacity 100 and no additional capacity, preserving every original allocation requires 101 independent-choice cells.","With the original capacity of 100, preserving every original allocation requires 101 independent-choice cells."),
 ("This counts menus after compatible selection.","This count concerns menus after compatible selection."),
 ("Each plan retains duties created by every acquisition, including evidence the plan later leaves unused.","Each plan retains the duties created by every acquisition, including acquisitions of evidence that it later leaves unused."),
 ("Buying 240 bundles and 120 additional observations of the third quantity costs the same amount. Its counts are $(240,240,360)$.","Buying 240 bundles and 120 additional observations of the third quantity gives counts $(240,240,360)$ for the same cost."),
 ("These results help formulate a joint institutional request. An evidence purchase can serve several requirements and create duties that affect another operation.","An evidence purchase can serve several requirements and create duties that affect another operation in a joint institutional request."),
 ("These are different parts of institutional state. Both can constrain a future admission.","Continuation state and retained knowledge are distinct parts of institutional state that can both constrain a future admission."),
 ("The probability of public output histories requires a different test.","Comparing probabilities of public output histories requires a different test."),
 ("Financial continuation has the same need for complete state.","Financial continuation also requires complete state."),
 ("Randomness has an implementation boundary too.","Random selectors also face implementation limits."),
 ("Each output then owns an integer number of equally likely bit strings, which proves the denominator restriction.","Each output then corresponds to an integer number of equally likely bit strings, which proves the denominator restriction."),
 ("The implementation must preserve modeled transitions and make the progress the model requires.","The implementation must preserve modeled transitions and meet the model's progress requirements."),
 ("Under a nonincreasing total rank and a productive decrease within each fixed transition interval, the group completes within interval length times initial rank.","The total rank must never increase and must decrease productively within each fixed transition interval. The group then completes within interval length times initial rank."),
 ],
}
log=[]
for stem,pairs in changes.items():
 for ext in ('.md','.tex'):
  f=p/(stem+ext); text=f.read_text()
  for old,new in pairs:
   if old==new:continue
   pattern=r'\s+'.join(re.escape(x) for x in old.split())
   matches=list(re.finditer(pattern,text))
   if len(matches)!=1:raise RuntimeError((str(f),old,len(matches)))
   text=re.sub(pattern,lambda m:new,text,count=1)
   log.append({'file':f.name,'old':old,'new':new})
  text=text.replace('  \n','\n')
  f.write_text(text)
(Path(__file__).parent/'changes.json').write_text(json.dumps(log,indent=2))
print('Applied',len(log),'paired source replacements.')
