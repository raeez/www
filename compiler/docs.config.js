/**
 * Document Configuration
 *
 * Each document has:
 * - id: Google Doc ID
 * - slug: Output filename (without .html)
 * - title: Display title
 * - subtitle: Italic subtitle
 * - meta: Date, version, collaborators, links
 * - filterPatterns: Strings to remove from doc content (already in header)
 */

module.exports = [
  {
    id: '1RW1DNRaVieee3NvW4BUf1m6pYGr0jcPo9HHlnZdrLqM',
    slug: 'smart-assets',
    title: 'Smart Assets',
    subtitle: 'Embedding Compliance, Identity, and Operational Intelligence Directly into Assets',
    meta: 'August 2025 — Version 0.3',
    description: 'Smart Assets are a fundamental reimagining of how financial assets exist, behave, and interact in the global economy.',
    filterPatterns: [
      'SMART ASSETS',
      'RAEEZ LORGAT',
      'SATURDAY AUGUST',
      'VERSION 0.3'
    ]
  },
  {
    id: '170dFcQSTIIXgQYSaiL8BJYL8Az_Cj4llPrvU9OjB1DI',
    slug: 'momentum-monograph',
    title: 'Momentum',
    subtitle: 'Incubating Ecosystems: A New Model for Capital Formation Through Jurisdictional Decentralization',
    meta: 'v0.35 — October 2025',
    metaLink: {
      text: 'View on Google Docs',
      url: 'https://docs.google.com/document/d/170dFcQSTIIXgQYSaiL8BJYL8Az_Cj4llPrvU9OjB1DI'
    },
    description: 'Momentum exists to originate, incubate, and scale programmable institutions into trillion-dollar market outcomes.',
    filterPatterns: [
      'MOMENTUM',
      'INCUBATING ECOSYSTEMS',
      'V0.35',
      'OCTOBER',
      'NEW MODEL FOR CAPITAL FORMATION',
      'NOTE TO READER'
    ]
  },
  {
    id: '1oTfyWyjEgBjWSw30W4BLQa029pMGJ7ciFDUzn4fUjj4',
    slug: 'sez-in-a-box',
    title: 'Special Economic Zones in a Box',
    subtitle: 'From Proof of Scale to Proof of Network',
    meta: 'Momentum — 2025',
    metaLink: {
      text: 'View on Google Docs',
      url: 'https://docs.google.com/document/d/1oTfyWyjEgBjWSw30W4BLQa029pMGJ7ciFDUzn4fUjj4'
    },
    description: 'A comprehensive framework for deploying turnkey Special Economic Zone infrastructure.',
    filterPatterns: [
      'SPECIAL ECONOMIC ZONES IN A BOX',
      'SEZ IN A BOX',
      'TURNKEY',
      'MOMENTUM CAPITAL'
    ]
  },
  {
    id: '18c076KBHJZLo-HZSI8rZM5l5xgzPJ_J1HHMHzafMg2Y',
    slug: 'sez-stack',
    title: 'The Momentum Open Source SEZ Stack',
    subtitle: 'A Technical Specification for Programmable Jurisdictional Infrastructure',
    meta: 'Version 0.4.0 — December 2025',
    metaLink: {
      text: 'View on Google Docs',
      url: 'https://docs.google.com/document/d/18c076KBHJZLo-HZSI8rZM5l5xgzPJ_J1HHMHzafMg2Y'
    },
    description: 'The complete open-source stack for building and operating Special Economic Zones.',
    filterPatterns: [
      'MOMENTUM OPEN SOURCE SEZ STACK',
      'THE MOMENTUM OPEN SOURCE SEZ STACK',
      'THE MOMENTUM OPEN SOURCE SPECIAL ECONOMIC ZONE STACK',
      'DECEMBER 2025',
      'RAEEZ LORGAT',
      'TECHNICAL SPECIFICATION',
      'PROGRAMMABLE JURISDICTIONAL',
      'VERSION',
      'TABLE OF CONTENTS'
    ]
  },
  {
    id: '1nNZcgk4zH0-aKP_Sea5dqrS56nzRsYxNBUvqOuAHX5Y',
    slug: 'competitive-topologies',
    title: 'Competitive Topologies & The Monopoly Problem',
    subtitle: 'Why Democratic Institutions Need Competition',
    meta: 'A Response to Eric Schmidt and Andrew Sorota\'s',
    metaLink: {
      text: '"This Is No Way to Rule a Country"',
      url: 'https://www.nytimes.com/2025/11/11/opinion/ai-democracy-government-authoritarianism.html'
    },
    description: 'Why Democratic Institutions Need Competition. A Response to Eric Schmidt and Andrew Sorota.',
    filterPatterns: [
      'COMPETITIVE TOPOLOGIES',
      'WHY DEMOCRATIC INSTITUTIONS',
      'RESPONSE TO ERIC SCHMIDT',
      'RAEEZ LORGAT, MANAGING PARTNER'
    ]
  },
  {
    id: '1G4qUdBcrrabR50oqOvCk2uqI7mWh371ykvx92bILPL4',
    slug: 'smart-buildings',
    title: 'Smart Buildings',
    subtitle: 'The Programmable Built Environment Operating System',
    meta: 'Momentum × Jan Bunge × Broad Group — October 2025',
    metaLink: {
      text: 'View on Google Docs',
      url: 'https://docs.google.com/document/d/1G4qUdBcrrabR50oqOvCk2uqI7mWh371ykvx92bILPL4'
    },
    description: 'A strategic specification for buildings as autonomous economic entities.',
    filterPatterns: [
      'SMART BUILDINGS',
      'OCTOBER 28, 2025',
      'PROGRAMMABLE BUILT ENVIRONMENT',
      'OPERATING SYSTEM',
      'JAN BUNGE',
      'BROAD GROUP',
      'CONFIDENTIAL',
      'STRATEGIC SPECIFICATION'
    ]
  },
  {
    id: '1c5iKhtAs03-KnmoRyF45xjePOszGIeMRUe642dpWTEQ',
    slug: 'moxie',
    title: 'Moxie IP Operating System',
    subtitle: 'Programmable Loyalty and Rewards for Large-Distribution Brands',
    meta: 'April 2025 — WIP v0.4',
    metaLink: {
      text: 'View on Google Docs',
      url: 'https://docs.google.com/document/d/1c5iKhtAs03-KnmoRyF45xjePOszGIeMRUe642dpWTEQ'
    },
    description: 'Recent advances in tokenomic incentive coordination technology enable experience-based monetization of IP.',
    filterPatterns: [
      'MOXIE IP',
      'IPOS',
      'PROGRAMMABLE LOYALTY',
      'RAEEZ LORGAT, APRIL 2025',
      'WIP V0.4'
    ]
  },
  {
    id: '12TriV64rqMidmlzEXU5HdvbhpX_Fu4bNq5UUo7-125I',
    slug: 'archai',
    title: 'Archai Protocol Whitepaper',
    subtitle: 'Programmable Ownership for Land, Housing, and Community Infrastructure',
    meta: 'Version 0.2 — June 2025',
    metaLink: {
      text: 'View on Google Docs',
      url: 'https://docs.google.com/document/d/12TriV64rqMidmlzEXU5HdvbhpX_Fu4bNq5UUo7-125I'
    },
    description: 'The protocol layer that turns land and buildings into programmable, arbitration-enabled, on-chain/off-chain hybrid institutions.',
    filterPatterns: [
      'ARCHAI PROTOCOL WHITEPAPER',
      'PROGRAMMABLE OWNERSHIP FOR LAND',
      'VERSION 0.2',
      'DISCLAIMER',
      'THIS DOCUMENT IS FOR RESEARCH'
    ]
  },
  {
    id: '1eGnq8WpcdjS5TbD4U87v4HaN5YBgSwjKvXwerrXMIFY',
    slug: 'licc',
    title: 'The Laboratory for Incentivization, Coordination and Cooperation',
    subtitle: 'A Research Institute for Coordination Science',
    meta: 'July 2025',
    metaLink: {
      text: 'View on Google Docs',
      url: 'https://docs.google.com/document/d/1eGnq8WpcdjS5TbD4U87v4HaN5YBgSwjKvXwerrXMIFY'
    },
    description: 'LICC is a private research institute dedicated to Coordination Science.',
    filterPatterns: [
      'LABORATORY FOR INCENTIVIZATION',
      'COORDINATION AND COOPERATION',
      'LICC',
      'RESEARCH INSTITUTE FOR COORDINATION SCIENCE',
      'RAEEZ LORGAT, MANAGING PARTNER'
    ]
  },
  {
    id: '1c4luYj4edBCkVnW47JojjDK_3m8a20wX-2fPztIAF8Q',
    slug: 'prefabricated-construction',
    title: 'Prefabricated Construction Methodologies',
    subtitle: 'A Dual-Track Industrialized Response for the UAE and Wider Middle East',
    meta: '王臻品 (Lilith Wang) & Raeez Lorgat — Momentum',
    description: 'This paper proposes a dual-track, industrialized response combining Precast Concrete and Modular Integrated BOX technologies.',
    filterPatterns: [
      'PREFABRICATED CONSTRUCTION METHODOLOGIES',
      'LILITH WANG',
      '王臻品',
      'RAEEZ LORGAT',
      'MOMENTUM CAPITAL'
    ]
  }
];
