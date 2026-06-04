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

For the FAIR dataset exercise, I chose **OpenNeuro ds000102**, an event-related Flanker task fMRI dataset.

This dataset is **not my finalized BrainHack School 2026 project dataset**. In my project pitch, I noted that I had not yet chosen the public dataset that I would use to run or demonstrate my QC workflow. Therefore, I am using ds000102 here only as a public dataset example for the Project Management module, and as a possible candidate for later workflow testing.

I chose this example because my BrainHack School 2026 project focuses on reproducible task-fMRI metadata and QC workflows. A public task-fMRI dataset is useful for thinking about project organization, metadata checking, events files, and reproducibility.

### Findable

The dataset is findable because it is deposited on OpenNeuro with a dataset identifier, `ds000102`. This makes it easier for researchers to locate, reference, and reuse.

### Accessible

The dataset is accessible through OpenNeuro. Because it is publicly hosted, researchers can access it without needing access to a private lab server.

### Interoperable

The dataset is organized in a way that supports standard neuroimaging workflows. This is important for my project because QC scripts depend on predictable file structures, metadata files, and task/event information.

### Reusable

The dataset is reusable because it contains public task-fMRI data that can be inspected, downloaded, and used for workflow testing or tutorial-style analysis. However, reuse still requires careful quality control. Public availability does not mean that every subject, run, or file is analysis-ready.

Overall, I would consider this dataset reasonably FAIR. It is findable through OpenNeuro, accessible as a public dataset, organized in a way that supports interoperability, and reusable for task-fMRI workflow testing. For my BrainHack School 2026 project, its role is only as a FAIR example and possible future external validation dataset, not as a finalized project dataset.

## 3. Open-science neuroimaging paper / project example

For an open-science neuroimaging project example, I chose **OpenNeuro / OpenfMRI-style public neuroimaging data sharing**, using public task-fMRI datasets as an example.

### Code available?

The amount of code available depends on the specific dataset. Some datasets include scripts or links to external repositories, while others mainly provide raw or minimally processed data. This shows why clear project management is important: code, dependencies, and expected directory structure should be documented when possible.

### Documentation for data analysis available?

Yes, public neuroimaging datasets usually include metadata files, task information, and dataset descriptions. However, the completeness of documentation can vary. This is why README files, environment files, and reproducible project organization are important.

### Data available?

Yes. The data are publicly available through OpenNeuro.

### Standards followed

The key standard is **BIDS**, the Brain Imaging Data Structure. BIDS helps make neuroimaging datasets easier to inspect, validate, preprocess, and reuse. For my project, this is especially relevant because I am interested in building tools that check task-fMRI metadata and event-level information.

## 4. Project template added to repository

For the practical project-management component, I organized my BrainHack School project repository with a clear project structure, an environment file, a license, a `.gitignore`, and placeholder `.gitkeep` files so that empty directories can be tracked by Git.

The goal is to make the project easier to clone, inspect, and continue developing.
