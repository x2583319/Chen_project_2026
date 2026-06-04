# BrainHack School 2026 — Project Management Module

This document summarizes my answers for the BrainHack School Project Management module and documents the project-management structure added to my BrainHack School project repository.

## 1. License choices

### 1.1 Code license

If I want to share code as widely as possible while still receiving credit, I would choose the **MIT License**.

The MIT License is permissive: it allows others to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, as long as the copyright notice and permission notice are included. This fits the goal of making scientific code reusable while preserving attribution.

### 1.2 Data license

If I want to share data, receive credit, allow modifications, but prohibit commercial use, I would choose **CC BY-NC 4.0**.

This license allows others to share and adapt the material, but requires attribution and does not allow commercial use. This fits the stated goal because reuse and modification are allowed, but commercial use is restricted.

## 2. FAIR public dataset example

I chose the **Music Genre fMRI Dataset** on OpenNeuro, dataset ID `ds003720`.

This dataset includes fMRI data from five participants listening to music stimuli from ten genres. It is relevant to my BrainHack School project because my project explores genre-related brain responses and possible genre decoding from fMRI data.

### Findable

The dataset is findable because it is deposited in OpenNeuro with a dataset identifier (`ds003720`) and versioned releases. It also has a related Data in Brief data descriptor article, which makes it easier for researchers to discover and cite.

### Accessible

The data are accessible through OpenNeuro. The related paper also states that raw brain data are available through OpenNeuro, while behavioral data, presentation scripts, and stimuli preprocessing scripts are available through OSF.

### Interoperable

The brain data are organized using BIDS, which is a community standard for organizing neuroimaging data. This makes the dataset easier to inspect, preprocess, and reuse with standard neuroimaging tools.

### Reusable

The dataset is reusable because it includes raw fMRI data, anatomical MRI data, behavioral data, and supporting scripts. The data descriptor explains the experimental design and data structure, including the training/test split and repeated test stimuli.

Overall, I would consider this dataset reasonably FAIR. Its strongest FAIR features are accessibility through OpenNeuro, organization in BIDS format, and the availability of documentation through the data descriptor paper. One possible limitation is that users still need to carefully inspect the metadata and scripts before reanalysis, especially because music-stimulus licensing and preprocessing details may affect how the dataset can be reused.

## 3. Open-science neuroimaging paper / project example

I chose:

**Nakai, T., Koide-Majima, N., & Nishimoto, S. “Music genre neuroimaging dataset.” Data in Brief.**

### Code available?

Partially yes. The related OSF project provides behavioral data, presentation software scripts, and stimuli preprocessing scripts. These are useful for understanding how the experiment was implemented and how stimuli were prepared.

### Documentation for data analysis available?

Yes. The Data in Brief article documents the dataset, participants, task design, scanning procedure, and data organization. The BIDS organization also provides machine-readable metadata that supports analysis documentation.

### Data available?

Yes. Raw brain data are available through OpenNeuro, and behavioral/supporting files are available through OSF.

### Standards followed

The main standard followed is **BIDS** for neuroimaging data organization. The use of OpenNeuro and OSF also supports open-science practices by separating large neuroimaging files from supporting behavioral and script files while keeping both publicly accessible.

## 4. Project template added to repository

For the practical project-management component, I organized my BrainHack School project repository with a clear project structure, an environment file, a license, a `.gitignore`, and placeholder `.gitkeep` files so that empty directories can be tracked by Git.

The goal is to make the project easier to clone, inspect, and continue developing.
