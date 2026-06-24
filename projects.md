---
layout: page
title: Projects
permalink: /projects/
---

## [Mechanism-informed enzymatic reaction rules](/assets/other/2026_pate_mechanism_informed_rules_jcim.pdf)

![Project visualization](/assets/imgs/projects/mechinformed_key_figure.svg)

<span style="display: inline-block; background-color: #22c55e; color: white; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;">Research</span>

**Overview:**
In the very first conversation I had with my PhD advisor, Linda, I was captivated by a problem she described: how to best summarize known biochemistry, the collection of chemical reactions known to be catalyzed by enzymes. I'd been reading [David MacKay's book on information theory](https://www.inference.org.uk/mackay/itila/book.html) and I recognized this as a compression problem. The trick would be to abstract only the important features of known reactions in order to predict new ones that could lead to the synthesis of target molecules of interest. My excitement carried me through three years of fits and starts, coming to grips with the complexities and contingencies of biochemistry, learning my own version of [the Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), and eventually arriving at a solution which leverages a [wonderful mechanistic dataset](https://www.ebi.ac.uk/thornton-srv/m-csa/) and just a pinch of machine learning. A data-driven approach unlocked a level of performance we would not have otherwise reached, but not until we first stewed in the data, pushing past the loudest features toward the more subtle details that really mattered. For anyone interested, the enzymatic reaction rules which came out of this project are available [here](https://github.com/stefanpate/coarse-grain-rxns).

---

## [Biological computer-aided synthesis planning (BioCASP)](https://github.com/stefanpate/bottle)

<video controls muted loop playsinline width="100%" style="max-width: 800px; display: block; margin: 0 auto;">
  <source src="/assets/imgs/projects/260525_annotated_pathway_viewer_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

<span style="display: inline-block; background-color: #a855f7; color: white; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;">Resource</span>

**Overview:**
This is a CASP data pipeline specific to enzymatically catalyzed reactions. The main processing steps are:

1. **Reaction network expansion:** iterative application of reaction rules in either the forward or retrosynthetic direction
2. **Pathfinding & analysis:** searches for paths from feedstocks to targets in the reaction network, then retrieves similar known reactions, & calculates Gibbs free energies
3. **Interative path viewer:** allows users to sort, filter, and evaluate paths, leave feedback and save high-priority paths, as well as access and download enzyme information

I have and continue to use the [pipeline](https://github.com/stefanpate/bottle) and [viewer](https://biocasp.up.railway.app) to predict paths toward monomers of interest in my capacity as a researcher in the Department of Energy's [BOTTLE Consortium](https://www.bottle.org), but these tools may be used for any BioCASP campaign.

---

## [Reaction center Graph Neural Network (RC-GNN)](/assets/other/2026_pate_development_reaction_centered_encoders_jcim.pdf)

![Project visualization](/assets/imgs/projects/rcgnn_key_figure.svg)

<span style="display: inline-block; background-color: #22c55e; color: white; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;">Research</span>

**Overview:**
At the time we began this project, we believed enzyme function prediction to be needlessly constrained by proxy. Several efforts had focused on predicting Enzyme Commission number or matching an enzyme with its substrate only. We and others have since shown that one can successfully match enzymes with full, balanced reactions by jointly embedding them into vector space. The enzyme encoder makes use of a protein language model, [ESM](https://github.com/facebookresearch/esm). The reaction encoder uses a Graph Neural Network implemented by [Chemprop](https://github.com/chemprop/chemprop). Reaction graphs are peculiar in that they can consist of unconnected subgraphs which nonetheless have important physical interactions amongst each other and with enzyme residues. We developed several simple solutions to this issue involving graph augmentation around the reaction center. Additionally we benchmark our model designs to a condensed graph of reactions scheme and several other models in literature.

---

## [Ergochemics](https://github.com/stefanpate/ergochemics)

![Project visualization](/assets/imgs/projects/ergochemics_logo.png){: width="300px" .center}

<span style="display: inline-block; background-color: #a855f7; color: white; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;">Resource</span>

**Overview:**
Ergochemics (ergonomics + cheminformatics) is a collection of [RDKit](https://www.rdkit.org/) functionality that I found myself using again and again across projects. I find packaging them up in this way to be very convenient and I hope you do too. There are several modules:

| Module | Description |
|--------|-------------|
| `ergochemics.draw` | Convenient drawing functions for molecules and reactions. |
| `ergochemics.mapping` | For mapping reaction rules to reactions, generating atom-mapped reactions, and extracting reaction centers. |
| `ergochemics.standardize` | Customizable molecule and reaction standardization techniques. |
| `ergochemics.similarity` | Featurization and similarity for molecules and reactions. |

Basic usage is explained in a pair of example notebooks in the repository linked above. The package is also pip installable:

```
pip install ergochemics
```

---

## [Enzymatic reaction data](https://github.com/stefanpate/enz-rxn-data)

![Project visualization](/assets/imgs/projects/enz_rxn_logo.png){: width="500px" .center}

<span style="display: inline-block; background-color: #a855f7; color: white; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;">Resource</span>

**Overview:**
This repository contains code to pull high-quality enzymatic reaction data from several sources. [Rhea](https://www.rhea-db.org/) and [UniProt](https://www.uniprot.org/) jointly index reactions and their protein catalysts. Their annotations are organized, transparent, and highly useful. The code here merely merges the two into a convenient set of tables. In addition to overall reactions, we've found mechanistic level data - elementary reaction steps - very useful for our work in computer-aided synthesis planning. The repository additionally pulls this data from the [Mechanism and Catalytic Site Atlas](https://www.ebi.ac.uk/thornton-srv/m-csa/). It does focus on substrates moreso than active site residues but can be modified to pull residues as well.

---

## [Deciding what to eat](https://www.pnas.org/doi/10.1073/pnas.2513479122)

![Project visualization](/assets/imgs/projects/putida_ferulate_glucose.jpg)

<span style="display: inline-block; background-color: #22c55e; color: white; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;">Research</span>

**Overview:**
This study characterizes in exquisite detail how two different nutrients are metabolized by soil bacteria *Pseudomonas putida*. *Putida* become popular among bio-engineers, especially metabolic engineers, due to it's wide ranging palate, which gives flexibility in the choice of feedstock. The team at the Aristilde Lab show how mass flows around the network of chemical reactions comprising the microbe's metabolism. Collaborators at the Waldbauer Lab measured the abundances of the enzymes catalyzing all these reactions. Others at the Guss and Nikel labs painstakingly prepared gene knockouts and measured enzyme kinetics to help sharpen our hypotheses on metabolic function. 

**My Role:**
Under the expert guidance of Niall Mangan, I formulated a simple model with the intention of making quantitative a hypothesis that Ludmilla Aristilde had about the control point of the metabolic network in the face of changing nutrient abundance. In experiments, *Putida* would cease to grow after glucose was removed, and ferulate added to the media (or vice versa). This quiet period is often referred to as the lag phase of growth. We hypothesized that during this period the abundances of one or a few key enzymes were changing to prepare metabolism to process the new nutrient. Notwithstanding the cutting-edge technology available to th group, there remained several unmeasured parameters including absolute protein concentrations and kinetic parameters. We therefore took the approach of sweeping parameter space with our numerical simulations and mapping out for which values of our unknown parameters our hypothesis should hold.

---

## [Neuromodulating between contexts](https://www.biorxiv.org/content/10.1101/2021.05.31.446462v3.full)

![Neuromodulation Project Overview](/assets/imgs/projects/neuromod_key_figure.png)

<span style="display: inline-block; background-color: #22c55e; color: white; padding: 4px 12px; border-radius: 6px; font-weight: bold; font-size: 14px;">Research</span>

**Overview:**
Before transformers, it was uncommon for a neural network to be good at multiple tasks. Rather, each trained network was like a savant. In contrast, real brains can perform many different tasks. The work of Eve Marder and colleagues pushed the field of neuroscience past its "wiring diagram" phase by showing that the particular way a neural circuit was wired up was insufficient to predict its behavior. Variations in the local concentrations of molecules known as neuromodulators could shift the circuit's behavior between modes. In this work, we conducted experiments with an abstract model of neuromodulation, *in silico*. By broadcasting a signal to the learned synaptic weight matrix of an RNN, i.e., scaling a group of synaptic strengths, we could shift the RNN between behaviors.

**My Role:**
This was my first project in computational neuroscience. Under the compassionate mentorship of Ben Tsuda, I learned basic skills in training neural networks, using TensorFlow, and so on. I pitched in by running some experiments that sought to push our abstract model of neuromodulation as far as we could in terms of number of unique behavior modes, how many (or how few) synaptic weights we had to scale, etc. Inspired by work from the lab of David Sussillo, I sought an explanation for the RNN behavior - and shifts between behavioral modes - in terms of fixed points. I found that there were not always (even approximate) fixed points, which turned out to be a good lesson in it's own way. The output space had many fewer dimensions than the hidden layer space of our RNNs, so there were many ways the neural activity vector could wander around while the output was none the wiser.

---