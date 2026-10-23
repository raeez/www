from pathlib import Path
p=Path('archai.html');s=p.read_text();changes=[
('Land ownership carries financial rights and obligations concerning:','Land ownership also determines:'),
('These rights must be explicit and take priority.','The design must make these enforceable rights explicit from the outset.'),
('The model below retains that relationship and specifies time, risk, and contribution limits:','The model below adds explicit terms for time, risk, and contribution:'),
('Mass automatically forms and maintains these entities. It encodes their governance, ownership tables, identity checks, and consent workflows.','Mass provides software to form and maintain these entities automatically. It encodes their governance, ownership tables, identity checks, and consent workflows.'),
('Together, these systems make legal rights, building operations, and compliance programmable.','Together, these systems support the legal rights, operating records, and compliance checks that programmable property institutions require.'),
('Each Archai project is a ','Each Archai project implements these requirements through a '),
('The economics must explain ','The contracts must specify '),
('why participants lock capital','what participants receive for locking capital'),
('Most tokenized real estate fails to provide liquidity and exit while constraining rentier speculation.','Returns alone do not resolve exit: most tokenized real estate fails to provide liquidity while constraining rentier speculation.'),
('The initial proposal describes governance as “stake-based, resident-weighted, trustee-checked.” The roles and constraints below make this enforceable.','The initial proposal describes governance as “stake-based, resident-weighted, trustee-checked.” The roles below assign control over local rules, capital, and compliance, subject to constitutional limits.'),
('These records let governance act on the building’s operations, finances, and risks.','These records connect governance decisions to the building’s operations, finances, and risks.'),
('The initial proposal names modular templates: Cayman foundation, Swiss Verein, and Panama company. These form part of the following design:','The initial proposal names templates such as a Cayman foundation, Swiss Verein, and Panama company. Jurisdiction modules organize these legal choices:'),
('Primary risks:','The legal and governance controls must address the following risks:'),
('The initial proposal uses insurance and the protocol token to underwrite network risk:','The initial proposal assigns insurance and the protocol token a role in network underwriting:'),
('The design separates vault assets from the network token:','Vault assets carry rights in individual projects. The network token serves protocol governance and underwriting, with distinct legal conditions:'),
('Each phase has explicit deliverables:','The roadmap starts with one vault, then adds portability, shared underwriting, jurisdiction modules, and resident and operator tools:'),
]
for a,b in changes:
 if s.count(a)!=1:raise SystemExit((s.count(a),a))
 s=s.replace(a,b)
p.write_text(s)
with Path('archai-change-ledger.txt').open('a') as f:
 f.write('\nHOLISTIC PASS AND CLAIM REVIEW CORRECTIONS\n')
 for i,(a,b) in enumerate(changes,1):f.write(f'{i:03} [1]\nOLD: {a}\nNEW: {b}\n\n')
with Path('RESUME-STATE.md').open('a') as f:f.write('''\nArchai: full baseline diagnosis and 84 initial edits complete; first full reread, independent review underway. Holistic contract read and forwarded to both children. Dependency/recurrence map appended before 16 further composition/correction edits. Source/markup invariants passed except intentional six br removals; numerical tokens differ only twelve 0.1 and one 0.2 document-process labels, approved by parent under external-documents policy. Formula blocks unchanged. Browser visual inspection blocked by explicit URL security policy; do not bypass or claim rendering. Next: final whole reread, claim review, static link/source checks and parent handoff.\n''')
print('Applied holistic changes and correction pass')
